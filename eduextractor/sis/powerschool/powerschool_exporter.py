import pandas as pd
from ...config import _load_secrets
import sqlalchemy

class PowerSchoolSQLInferface: 
    """A class, representing a interface to the Powerschool frontend
    which most teachers/students/admins have access to.
    """
    def __init__(self, secrets=None):
        if secrets is None:
            secrets = _load_secrets()
        try:
            SECRETS = secrets['powerschool']
            self.username = SECRETS['username']
            self.password = SECRETS['password']
            self.host = SECRETS['host']
            self.dbname = SECRETS['dbname']
        except KeyError:
            print("Please check the configuration of your config file")

        engine = sqlalchemy.create_engine('oracle://' + self.username + 
                                          ':' + self.password + 
                                          '@' + self.host + ':' +
                                          self.port + '/' + 
                                          self.dbname)
        self.conn = engine.connect()
    
    def query_to_df(query):
        """executes query, converts to pd.dataframe"""
        df = pd.read_sql(query, conn)
        return df
