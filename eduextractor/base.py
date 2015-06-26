from config import secrets
import pandas as pd
from sqlalchemy import create_engine

class RemoteSource():
    """A remote source of data, 
    the fundamental abstraction of the project.
    """
    def __init__(self,name):
        self.name = name

class TestSource(RemoteSource):
    """A subclass representing test score data
    """
    def __init__(self):
        pass
class MAPSource(TestSource):
    """The Source for NWEA Map test scores
    """
    def __init(self):
        pass

def _create_connection_string():
    dialect = secrets['sql']['dialect'] 
    username = secrets['sql']['username']  
    password = secrets['sql']['password']
    host = secrets['sql']['host'] 
    port = secrets['sql']['port']
    dbname = secrets['sql']['dbname']
    conn_str = dialect + "://" + username + ":" + password + "@" + host + ":" + str(port) + "/" + dbname
    return conn_str

def _make_connection_to_sql_db():
    return create_engine(_create_connection_string())

def toSQL(file,table):
    """Converts a CSV file into a SQL table. 
    Should be a flag or something.

    Arguments:
    file: path to CSV to load into a table
    table: SQL table to load into 
    """
    df = pd.read_csv(file)
    df.to_sql(table,conn=_make_connection_to_sql_db())
