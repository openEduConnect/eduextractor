from config import secrets

from mechanize import Browser
from zipfile import ZipFile

BASE_URL = secrets['nwea_map']['url']
LOGIN_URL = BASE_URL + '/admin'
USERNAME = secrets['nwea_map']['username']
SECRET = secrets['nwea_map']['secret']
UNZIPPED_DEST = secrets['nwea_map']['dest']

# flow control
def main():
    ## create a browser object
    ## NWEA has a pretty aggressive robots.txt
    ## here's what we'll do about that: ignore it
    br = Browser()
    #br.set_handle_redirect(False)    
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

    ## open the login page, form is called loginForm
    br.open(LOGIN_URL)
    br.select_form(name="loginForm")    
    br['username'] = USERNAME
    br['password'] = SECRET    
    response = br.submit()  ## submit and store response
    print 'credentials successful, logged in'
    #print response.read()

    #once logged in, navigate to reports page
    br.open(BASE_URL + '/report/home/map')

    #CDF file looks like "https://kippteamschools-admin.mapnwea.org/report/download/cdf/7492"
    #get the matching cdf and build the full url
    cdf_string = '/report/download/cdf/[0-9]+'
    file_target = br.find_link(url_regex=cdf_string)
    file_loc =  BASE_URL + file_target.url
    print 'cdf is located at %s' % (file_loc)

    #retrieve will get file at the location and save to a temp directory
    cdf_zipped = br.retrieve(file_loc)[0]
    print 'temp file is located at %s' % cdf_zipped

    sourceZip = ZipFile(cdf_zipped, 'r')
    print
    print 'beginning unzip'
    for name in sourceZip.namelist():
        print 'extracted %s...' % (name)
        sourceZip.extract(name, UNZIPPED_DEST)
    sourceZip.close()

if __name__ == '__main__':
    main()
