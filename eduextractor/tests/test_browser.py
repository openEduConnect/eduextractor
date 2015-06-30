import nose
import eduextractor
import eduextractor.browser
def test_browser():
    d = eduextractor.browser.Driver()
    assert type(d.driver) == 'selenium.webdriver.firefox.webdriver.WebDriver'
