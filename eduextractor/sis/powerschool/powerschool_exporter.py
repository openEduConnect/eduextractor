from eduextractor.config import secrets
from eduextractor.browser import Driver

from urlparse import urlparse
class PowerSchoolFrontend():
    """A class, representing a interface to the Powerschool frontend
    which most teachers/students/admins have access to. 
    """
    SECRETS = secrets['powerschool']['frontend']
    username = SECRETS['username']
    password = SECRETS['password']
    url = SECRETS['url']
    postfix = SECRETS['postfix']
    dr = Driver().driver
    def login(self):
        """Go login to the Pearson site, in a browser window
        """
        self.dr.get(self.url + self.postfix)
        ## Username and Password Fields
        field = self.dr.find_element_by_id('fieldPassword')
        ## send the text with semicolon
        field.send_keys(self.username + ';' + self.password)
        ## Submit button
        button = self.dr.find_element_by_id('btnEnter')
        button.click()

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


