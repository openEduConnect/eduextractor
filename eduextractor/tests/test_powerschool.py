import nose
import unittest.TestCase
from eduextractor.sis.powerschool import PowerSchoolFrontend

class test_powerschool_frontend(unittest.TestCase):
    def setUp():
        psa = PowerSchoolFrontend()
