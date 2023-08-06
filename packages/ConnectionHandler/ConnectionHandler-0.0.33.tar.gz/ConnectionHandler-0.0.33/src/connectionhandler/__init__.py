from .get_handler import get_handler

def create_handler(db_type, username, password, host, database, port="5432"):
    return get_handler(db_type, username, password, host, database, port)