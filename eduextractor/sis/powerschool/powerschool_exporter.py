from eduextractor.config import secrets

import mechanize 
from urlparse import urlparse
class PowerSchoolFrontend():
    """A class, representing a interface to the Powerschool frontend
    which most teachers/students/admins have access to. 
    """
    SECRETS = secrets['powerschool']['frontend']
    username = SECRETS['username']
    password = SECRETS['password']
    url = SECRETS['url']
    o = urlparse(url) 
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
    
    
    # Cookie Jar
    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)


    # Browser options
    br.set_handle_equiv(True)
    br.set_handle_gzip(True)
    br.set_handle_redirect(True)
    br.set_handle_referer(True)
    br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    def login(self):
        self.br.open('http://' + self.o.netloc)

class PowerSchoolAdmin():
    """A class, representing an interface to the backend of a powerschool
    installation. This backend typically has few users, but allows us to 
    upload html pages that expose ts_sql (the custom variant of SQL that 
    powerschool uses and allows HTML injection of.)
    """


if __name__ == '__main__':
    psf = PowerSchoolFrontend()
    psf.login()
#notes on flow    
# powerschool login 
# ask for the specific table

# download table

# normalize names


