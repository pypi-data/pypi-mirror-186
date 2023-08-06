from .sql_handler import Sql_Handler
import psycopg2
import json

class Postgres_Handler(Sql_Handler):
    #Initializer that takes the values for connection
    def __init__(self, user_name, password, host, port, database):
        self.user_name = user_name
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        
    #Methods from inherited abstract class
    def define_columns(self, columns):
        super().define_columns(columns)
    
    def set_table_name(self, table_name):
        return super().set_table_name(table_name)
        
    def set_keywords(self, keywords): 
        return super().set_keywords(keywords)
   
    # Used internally create to run query
    def __run_query(self, query, values):
        #Sets the message to 'No records found' and status -1
        status = 0
        results = 'No records found'
        
        #Creates cursor to iterate through rows
        with psycopg2.connect(user=self.user_name, password=self.password, host=self.host, dbname=self.database) as conn:
            with conn.cursor() as cursor:
        
                try:
                    cursor.execute(query, values)
                    results = cursor.fetchall()

                    status = 1
                    conn.commit()
                    
                    if results.count == 0:
                        results = 'No records found'
                        
                except Exception as ex:
                    status = -1
                    results = f"{ex}"
            
        return (status, results)
    
    #Method to close the connection    
    def Close(self):
            try:
                self.conn.close() 
            except Exception as ex:
                return f'Error: {ex}'
        
    #Select all rows 
    def search_for_records(self):
        payload = {}
    
        query_value_list = self.__build_search_query()       

        #Runs the query and returns the results
        results = self.__run_query(query_value_list[0], query_value_list[1])
        payload = self.__format_search_results(results)
    
        return payload

    def __build_search_query(self):
        where_string = ''
        values_dict = {}
        
        #Start of query string
        query = f"SELECT * FROM %(table_name)s"
        values_dict['table_name'] = self.table_name
        
        #Keys for the StartDate and EndDate
        start_date_key = "SearchStartDate"
        end_date_key = "SearchEndDate"

        if len(self.keywords) != 0:
            #Iterates through the keywords to build search string
            for key, item in self.keywords.items():
                if where_string != '':
                    where_string += ' AND '
                
                if key == start_date_key:
                    where_string += f'"DocumentDate" >= %({key})s'
                    values_dict[key] = item
                elif key == end_date_key:
                    where_string += f'"DocumentDate" <= %({key})s'
                    values_dict[key] = item
                else:
                    where_string += f'"{key}" ILIKE %({key})s'
                    values_dict[key] = f'{item}'
                    
            if where_string != '':
                query = f"{query} WHERE {where_string}"
                
        return [query, values_dict]
        
    
    def __format_search_results(self, results):
        formatted_rows = []
        records = ''
        error = ''
        
        status_code = 200
        internal_status = results[0]
        data = results[1]  
        
        if internal_status != -1:
            row_count = len(data)
            
            if row_count > 0:
                for row in data:
                    formatted_row = {}
                    
                    for index, item in enumerate(row):
                        formatted_row[self.columns[f"{index}"]] = f'{item}'
                    
                    formatted_rows.append(formatted_row)

            records = {
                'count': row_count,
                'records': formatted_rows
            }
        else:
            error = data
            
        return {
            'statusCode': status_code,
            'headers': {
                'Content-Type': "application/json",
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            },
            "body": json.dumps({
                'results': records,
                'error' : f'{error}'
            })
        } 
        
        
    #This needs to be looked at, likely there are only certain fields that will be passed and the rest will be created either in lambda or S3/postgresql
    def insert_row(self, **kwargs):
        #Key to get table_name argument
        table_name_key = 'table_name'
        
        #Values dictioniary for sql parameters
        values_dict = {}
        
        #Empty strings for column names and column values to be added
        column_names_string = ''
        column_values_string = ''
        
        #checks for the table name in args
        if table_name_key not in kwargs:
            assert("Error: table_name required as argument")
        table_name = kwargs[table_name_key]
        
        #Begining of the SQL query
        query_start = 'INSERT INTO %(table_name)s'
        values_dict[table_name_key] = table_name
        
        #Iterates through the arguments adds the key to the column_name, and the value to the column_value
        for key, value in kwargs.items():
            column_names_string += f'{key}s'
            column_values_string += f"%({key})s,"
            values_dict[key] = value
            
        column_names = column_names_string[:-1]
        column_values = column_values_string[:-1]
        
        #Builds the final SQL query for updating values
        query = f'{query_start}({column_names}) VALUES({column_values})'
        
        #Runs the command
        results = self.__run_query(query, values_dict)
        return self.__format_insert_results(results)
        
    def __format_insert_results(self, results):
        internal_status = results[0]
        message = results[1]  if internal_status != -1 else ''
        error = results[1] if internal_status == -1  else ''
        status_code = 200 if internal_status != -1 else 400
                
        return {
            'statusCode': status_code,
            'headers': {
                'Content-Type': "application/json",
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET',
            },
            "body": json.dumps({
                'results': f'{message}',
                'error' : f'{error}'
            })
        } 
        
    #Method to update a SQL row
    def update_row(self, **kwargs):
        id_key = 'id'
        other_search_key = 'oldName'
        
        query_string = 'UPDATE "MetaData" SET'
        for key in kwargs:
            if key == id_key or key not in self.metadata_column_map: continue
            
            column_name = self.metadata_column_map[key]
            section = f' "{column_name}" = \'{kwargs[key]}\','
            query_string += section
            
        query_string = query_string[:-1]
        
        if id_key in kwargs:
            id_val = kwargs['id']
            query_string += f' WHERE "ID"=\'{id_val}\''
        else:
            search_val = kwargs[other_search_key]
            query_string += f' WHERE "FileName"=\'{search_val}\''
        
        results = self.__run_query(query_string)
        return results
    
    #Delete command, will use policy or agent number to delete
    #todo - This may requrie removing items from S3 not sure yet how that will work
    def deleteRow(self, number, status):
        #Primary column to find row that should be removed
        primary_column = f'{status.lower().title()}Number'
        
        #Builds query to run 
        query_string = f'DELETE FROM "MetaData" WHERE "{primary_column}"=\'{number}\''
        
        #Runs the query and handles the success or error.
        results = self.__run_query(query_string)
        return results
