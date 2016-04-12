from __future__ import print_function
import requests
import pandas as pd
from zipfile import ZipFile
from io import StringIO
from eduextractor.config import secrets

NWEA_USERNAME = secrets['nwea_map']['username']
NWEA_PASSWORD = secrets['nwea_map']['secret']

def load_map_files():
    """
    Hits the NWEA automated reporting API and downloads the comprehensive data file.
    Returns: writes 'map.csv' to /tmp

    """
    # send a GET request to the API endpoint
    print('Connecting to NWEA...')
    cdf_url = "https://api.mapnwea.org/services/reporting/dex"
    r = requests.get(cdf_url, auth=(NWEA_USERNAME, NWEA_PASSWORD))

    print(r.reason)

    # if the request is successful..
    df_list = []
    print(r.status_code)
    if r.status_code == 200:
        print('Downloading CDF...')

        # convert the response content into a zipfile
        z = ZipFile(StringIO(r.content))
        zfiles = z.namelist()

        for i, f in enumerate(zfiles):
            print('Extracting', f)

            # open/extract file from zip
            cdf = z.open(f)

            # read into dataframe
            df = pd.read_csv(cdf)
            df_list.append(df)

        whole_df = pd.concat(df_list)
        whole_df.to_csv('/tmp/map.csv')

if __name__ == '__main__':
    load_map_files()
