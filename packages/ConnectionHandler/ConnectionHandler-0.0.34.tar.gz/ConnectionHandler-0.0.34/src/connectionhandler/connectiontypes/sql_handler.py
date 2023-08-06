from abc import ABC, abstractmethod

class Sql_Handler(ABC):
    @abstractmethod
    def define_columns(self, columns):
        self.columns = columns
    
    @abstractmethod
    def set_table_name(self, table_name):
        self.table_name = table_name
        
    @abstractmethod
    def set_keywords(self, keywords):
        self.keywords = keywords