import unittest
from eduextractor.sis.powerschool import PowerSchoolFrontend, PowerSchoolAdmin


class test_powerschool_frontend(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.ps = PowerSchoolFrontend()

    def testLogin(self):
        """
        Test if we can login
        """
        self.ps.login()
        self.assertEqual(self.ps.dr.title, u'Start Page')


class test_powerschool_admin(unittest.TestCase):
    
    @classmethod
    def setUp(self):
        self.ps = PowerSchoolAdmin()

    def testLogin(self):
        self.ps.login()
        self.assertEqual(self.ps.dr.title, 
                         u'Powerschool System Management')
