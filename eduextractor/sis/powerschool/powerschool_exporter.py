from eduextractor.config import secrets
from eduextractor.browser import Driver

from selenium.common.exceptions import NoSuchElementException
from urlparse import urlparse
import requests

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
    SECRETS = secrets['powerschool']['admin']
    username = SECRETS['username']
    password = SECRETS['password']
    postfix = SECRETS['postfix']
    url = secrets['powerschool']['frontend']['url']
    dr = Driver().driver
    o = urlparse (url + postfix)
    def login(self):
        """Runs the login flow
        """
        self.dr.get(self.url + self.postfix)
        #find the username, pw fields
        try:
            fuser = self.dr.find_element_by_id('j_username')
            fpw = self.dr.find_element_by_id('j_password')
            # send the keys
            fuser.send_keys(self.username)
            fpw.send_keys(self.password)
            # Click the button! 
            button = self.dr.find_element_by_id('loginsubmit')
            button.click()
        except NoSuchElementException: 
            # If no login element, then person is already logged in
            return  
    def _go_to_custom_pages(self):
        self.dr.get(self.url + self.postfix + '/custompages/index.action')
    def _add_eduextractor_folder(self):
        all_cookies = self.dr.get_cookies()
        ## Convert cookies into request format
        cookies = {}  
        for s_cookie in all_cookies:
            cookies[s_cookie["name"]]=s_cookie["value"]
        
        payload = {'newAssetName': 'eduextractor', 'newAssetPath': 'admin',
                'newAssetType': 'folder'}
        r = requests.post(self.o.scheme + '://' +
                self.o.netloc + '/powerschool-sys-mgmt/custompages/createAsset.action'
                ,cookies=cookies,
                data = payload)
        return r
    
        
if __name__ == '__main__':
    psa = PowerSchoolAdmin()
    psa.login()
    psa._go_to_custom_pages()
    psa._add_eduextractor_folder()
# ask for the specific table

# download table

# normalize names


