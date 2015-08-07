import requests
import pandas as pd
from zipfile import ZipFile
from StringIO import StringIO
from nweaconfig import NWEA_USERNAME, NWEA_PASSWORD

## import database configuration from parent directory
## config contains SQLalchemy engine and a few DB functions
import sys
sys.path.append('../config')
import databaseconfig

## send a GET request to the API endpoint
print 'Connecting to NWEA...'
cdf_url = 'https://api.mapnwea.org/services/reporting/dex'
r = requests.get(cdf_url, auth=(NWEA_USERNAME,NWEA_PASSWORD))

print r.reason
## if the request is successful...
if r.status_code == 200:
    print 'Downloading CDF...'
    ## convert the response content into a zipfile
    z = ZipFile(StringIO(r.content))
    zfiles = z.namelist()

    ## create database engine and open a connection
    print 'Connecting to database...'
    engine = databaseconfig.DB_ENGINE
    conn = engine.connect()

    for i, f in enumerate(zfiles):    
        print 'Extracting', f
        ## open/extract file from zip
        cdf = z.open(f)
        ## read into dataframe
        df = pd.read_csv(cdf)        
        ## define the table name        
        tablename = 'AUTOLOAD$NWEA_' + f.strip('.csv')            
        ## load it!
        if len(df) > 0:
            print 'Loading %s records into database...' % (len(df))
            ## truncate
            databaseconfig.truncate_table(conn, tablename)
            ## "append" to the truncated destination table         
            df.to_sql(tablename, engine, if_exists='append', index_label='BINI_ID')
            
    conn.close()

print 'Done!'
