import pandas as pd
from ...config import _load_secrets
import sqlalchemy
import os
from tqdm import tqdm


class IlluminateSQLInterface:
    """A class representing a SQL interface to 
    Illuminate 
    """
    def __init__(self, secrets=None):
        if secrets is None:
            secrets = _load_secrets()
        try:
            SECRETS = secrets['illuminate']
            self.username = SECRETS['username']
            self.password = SECRETS['password']
            self.host = SECRETS['host']
            self.dbname = SECRETS['dbname']
        except KeyError:
            print("Please check the configuration of your config file")

        engine = sqlalchemy.create_engine('postgres://' + self.username + 
                                          ':' + self.password + 
                                          '@' + self.host + ':' +
                                          self.port + '/' + 
                                          self.dbname)
        self.conn = engine.connect()
    
    def query_to_df(query):
        """executes query, converts to pd.dataframe"""
        df = pd.read_sql(query, conn)
        return df

    def _list_queries(file_dir='./sql'):
        return os.listdir(file_dir)

    def download_files():
        files = self._list_queries()
        for file_name in tqdm(files): 
            with open('./sql/' + file_name, 'r') as filebuf:
                data = filebuf.read()
                df = query_to_df(data)
                file_name = file_name.replace('.sql','.csv')
                df.to_csv('/tmp/' + file_name)

if __name__ == '__main__':
    IlluminateSQLInterface.download_files()
    
