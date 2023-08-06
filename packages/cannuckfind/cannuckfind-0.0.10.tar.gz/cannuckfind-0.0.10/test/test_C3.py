print(40*'*')
print('testing location \n')
import sys
import unittest

sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2023CannuckFind/cannuckfind/src')

from cannuckfind import C3
from cannuckfind import geolocation
from geograpy import get_geoPlace_context


class TestC3(unittest.TestCase):
    """
    Test C3
    """
    def test_C3(self):
        from cannuckfind import C3
        testloc = C3.C3()
        print("Start C3 test in canuckfind")
        print(dir(testloc))
        self.assertEqual(testloc.CAN ,11)
        self.assertTrue(testloc.isCan('Canada'))
        self.assertTrue(testloc.isUS('NYC'))
        self.assertFalse(testloc.isCan('NYC'))

    def test_C3geograpy(self):
        from cannuckfind import C3
        import geograpy
        print("Start C3geograpy test in canuckfind")
        testgeograpy = C3.C3(useGEOGRPY = True)
        self.assertTrue(testgeograpy.isCan('Toronto'))
        self.assertTrue(testgeograpy.isCan('Kingston'))
        self.assertTrue(testgeograpy.isCan('Montreal'))
        self.assertTrue(testgeograpy.isCan('Halifax'))
        self.assertTrue(testgeograpy.isCan('Calgary'))
        self.assertTrue(testgeograpy.isCan('Ottawa'))
        self.assertTrue(testgeograpy.isCan('Montreal'))
        self.assertFalse(testgeograpy.isCan('Lisbon'))
        self.assertFalse(testgeograpy.isUS('Lisbon'))
        self.assertEqual(testgeograpy.getC3('Lisbon'),13)
        
    def test_C3NoGeograpy(self):
        from cannuckfind import C3
        import geograpy
        
        testgeograpy = C3.C3(useGEOGRPY = False)
        self.assertFalse(testgeograpy.isCan('Toronto'))

 
    
    def test_C3NL(self):
        from cannuckfind import C3
        import geograpy
        testgeograpy = C3.C3(useGEOGRPY = True)
        self.assertTrue(testgeograpy.isCan('I am Canadian living in Toronto'))
        self.assertFalse(testgeograpy.isCan('I am Canadian!'))     
        
    def test_Docs(self):
        # test examples used in documentation
        from cannuckfind import C3
        import geograpy
        testlocation = C3.C3(useGEOGRPY = True)
        isCan = testlocation.isCan("Winnipeg")
        print(isCan)
        self.assertTrue(isCan)
    
        
print('*** test cannuckfind location complete')
print('*** only two tests should appear as there are not asserts in the first test')
print(40*'*')       


if __name__ == '__main__':
    unittest.main()



print(40*'*')


