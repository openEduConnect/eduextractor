from eduextractor.config import secrets
from eduextractor.browser import Driver
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from urlparse import urlparse
import requests


class PowerSchoolFrontend():
    """A class, representing a interface to the Powerschool frontend
    which most teachers/students/admins have access to. 
    """
    try:
        SECRETS = secrets['powerschool']['frontend']
        username = SECRETS['username']
        password = SECRETS['password']
        url = SECRETS['url']
        postfix = SECRETS['postfix']
    except KeyError:
        print "Please check the configuration of your config file"
    dr = Driver().driver

    def login(self):
        """Go login to the Pearson site, in a browser window
        """
        self.dr.get(self.url + self.postfix)
        # Username and Password Fields
        
        try:
            us_field = self.dr.find_element_by_id('fieldUsername')
            pw_field = self.dr.find_element_by_id('fieldPassword')
        except NoSuchElementException:
            print "already logged in"
            return
        # send the text
        us_field.send_keys(self.username)
        pw_field.send_keys(self.password)
        # Submit button
        button = self.dr.find_element_by_id('btnEnter')
        button.click()
    
    def _download_html_table(self, page_name):
        """
        Gets the HTML table from teh page
        and returns pd.DataFrame
        """
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        self.dr.get(self.url + self.postfix + "/eduextractor/" + page_name)
        try:
            elem = WebDriverWait(self.dr, 150).until(
                    EC.presence_of_element_located((By.ID,'eduextractor_t'))
                    )
        except selenium.exceptions.TimeOutException:
            raise "Timeout Problem"
        return pd.read_html(self.dr.page_source)


class PowerSchoolAdmin():
    """A class, representing an interface to the backend of a powerschool
    installation. This backend typically has few users, but allows us to 
    upload html pages that expose ts_sql (the custom variant of SQL that 
    powerschool uses and allows HTML injection of.)
    """
    try:
        SECRETS = secrets['powerschool']['admin']
        username = SECRETS['username']
        password = SECRETS['password']
        postfix = SECRETS['postfix']
        url = secrets['powerschool']['frontend']['url']
    except KeyError:
        print "Please check the configuration of your config file"
    dr = Driver().driver
    o = urlparse(url + postfix)

    def login(self):
        """Runs the login flow
        """
        self.dr.get(self.url + self.postfix)
        # find the username, pw fields
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
        """Adds the custom folder /admin/eduextractor
        """
        cookies = self._convert_cookies()
        payload = {'newAssetName': 'eduextractor', 'newAssetPath': 'admin',
                   'newAssetType': 'folder'}
        r = requests.post(self.o.scheme + '://' +
                          self.o.netloc + 
                          """/powerschool-sys-mgmt/custompages/createAsset.action""", 
                          cookies=cookies,
                          data=payload)
        return r

    def _create_html_page(self, page_name):
        """Creates an HTML file on powerschool 
        under /admin/eduextractor.  
        
        usage: psa._upload_html('test.html')
        """
        cookies = self._convert_cookies()
        payload = {'newAssetName': page_name,
                   'newAssetPath': '/admin/eduextractor',
                   'newAssetType': 'file'}
        r = requests.post(self.o.scheme + '://' + 
                          self.o.netloc + """/powerschool-sys-mgmt/custompages/createAsset.action""",
                          cookies=cookies,
                          data=payload)
        return r

    def _publish_custom_page(self, page_name, content):
        """uploads a html file to the given location
        """
        print page_name
        cookies = self._convert_cookies()
        payload = {'customContent': content,
                   'keyPath': "admin_eduextractor." +
                   page_name.replace('.html', ''),
                   'customContentId': self._get_custom_content_id(page_name),
                   'customContentPath': "/admin/eduextractor/" + page_name}
        r = requests.post(self.o.scheme + '://' + self.o.netloc
                          + """/powerschool-sys-mgmt/custompages/publishCustomPageContent.action""",
                          cookies=cookies,
                          data=payload)
        return r

    def _convert_cookies(self):
        """Converts the cookies from Selenium to 
        request format. 
        """
        all_cookies = self.dr.get_cookies()
        # Convert cookies into request format
        cookies = {}  
        for s_cookie in all_cookies:
            cookies[s_cookie["name"]] = s_cookie["value"]
        return cookies

    def _get_custom_content_id(self, page_name):
        """give a page that exists in in /admin/eduextractor
        finds the PowerSchool Custom Content id. 
        """
        r = requests.get(self.o.scheme + "://" + self.o.netloc + 
                         """/powerschool-sys-mgmt/custompages/builtintext.action?LoadFolderInfo=false&path=/admin/eduextractor/""" + 
                         page_name, 
                         cookies=self._convert_cookies())
        id = r.json()['activeCustomContentId']
        return id
