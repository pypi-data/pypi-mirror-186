print(40*'*')
print('testing location geocasual \n')
import sys
import unittest

sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2023CannuckFind/cannuckfind/src')
print(sys.path)
import cannuckfind


class Testgeocasual(unittest.TestCase):
    """
    Test geocasual
    """
    def test_geocasual(self):
        from cannuckfind import geocasual
        testloc = geocasual.geocasual()
        print("Start GeoCasual test in cannuckfind")
        print(dir(testloc))
        print(40*'=')

    def test_GeoCasual(self):
        print(40*'=')
        from cannuckfind import geocasual
        
        print("Start GeoCasual test in cannuckfind")
        testcasual = geocasual.geocasual()
        print(dir(testcasual))
        self.assertTrue(testcasual.isjoke('Nowhere'))
        self.assertTrue(testcasual.isjoke('Miles away'))
        self.assertTrue(testcasual.isCan("amiskwacîwâskahikan"))
        self.assertTrue(testcasual.isUS('NYC'))

        
    def test_Docs(self):
        # test examples used in documentation
        print(40*'=')
        from cannuckfind import geocasual
        testcasual = geocasual.geocasual()
 
        
        isjoke = testcasual.isjoke("everywhere")
        print(isjoke)
 
print('*** test geocasual complete')
print('*** only two tests should appear as there are not asserts in the first test')
print(40*'*')       

if __name__ == '__main__':
    unittest.main()




