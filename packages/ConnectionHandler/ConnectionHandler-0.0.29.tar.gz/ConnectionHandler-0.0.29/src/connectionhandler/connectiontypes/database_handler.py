from .postgres_handler import Postgres_Handler as pg_handler

class Database_Handler:
    def __init__(self, db_type, user_name, password, host, database, port):
        self.db_type = db_type
        self.__build_connection(user_name, password, host,database, port)

    def __build_connection(self, user_name, password, host, database, port):
        self.handler = pg_handler(user_name, password, host, database, port)
    
    def search_records(self, columns, keywords):
        return self.handler.search_for_records(columns, keywords)
    
    def insert_record(self, **keywords):
        return self.handler.insert_row(**keywords)
    
    def update_record(self, keywords):
        return self.handler.update_record(keywords)
    