import unittest
from eduextractor.sis.powerschool import PowerSchoolFrontend, PowerSchoolAdmin


class test_powerschool_frontend(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        ps = PowerSchoolFrontend()

    def testLogin(self):
        """
        Test if we can login
        """
        self.ps.login() 
        assert self.assertEqual(self.ps.dr.title,u'Start Page')


class test_powerschool_admin(unittest.TestCase):

    def setUp():
        ps = PowerSchoolAdmin()


