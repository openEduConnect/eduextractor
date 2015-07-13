import eduextractor
import unittest


class test_browser(unittest.TestCase):
    """
    Are we using a firefox browser. 
    """
    def test_browser(self):
        d = eduextractor.browser.Driver()
        self.assertEquals(str(type(d.driver)),
                          'selenium.webdriver.firefox.webdriver.WebDriver')

