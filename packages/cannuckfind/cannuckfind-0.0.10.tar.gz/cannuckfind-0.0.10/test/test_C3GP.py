print(40*'*')
print('testing location \n')
import sys,math
import unittest



sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2023CannuckFind/cannuckfind/src')
from cannuckfind import geolocation



class test_CanC3GP(unittest.TestCase):
    """
    Test GeoGraphy C3 country identication
    """     
    # Test Canada   
    def test_isCanC3GP(self):
        print('*** 19 test C3GP')
        from cannuckfind import geolocation
        testisCanC3GP = geolocation.isC3GP()
        testisCanC3GP.loadrawGP("Toronto, Canada")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == True ) 
        testisCanC3GP.loadrawGP("Ottawa, Canada")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == True ) 
        testisCanC3GP.loadrawGP("Paris, France")
        junkval = testisCanC3GP.isCanC3GP()
        self.assertTrue(junkval == False ) 

    def test_isUSC3GP(self):
        from cannuckfind import geolocation
        print('*** 34 in test_C3GP')
        testisCanC3GP = geolocation.isC3GP()
        print('*** 36 in test_C3GP')
        testisCanC3GP.loadrawGP("New York, United States")
        print('*** 83 in test_location',testisCanC3GP.rawtext)
        print('***84 in  test_location test_isUSC3GP = ',testisCanC3GP.isUSC3GP())
        junkval = testisCanC3GP.isUSC3GP()
        print('***86 in test_location junkval =',junkval)
        self.assertTrue(junkval == True )
        
    def test_isOthGP(self):
        from cannuckfind import geolocation
        testisCanC3GP = geolocation.isC3GP()
        testisCanC3GP.loadrawGP("Paris, France")
        print(testisCanC3GP.isOthC3GP())
        junkval = testisCanC3GP.isOthC3GP()
        print(junkval)
        self.assertTrue(junkval == True )           


print('*** test cannuckfind geolocation complete')
print(40*'*')       


if __name__ == '__main__':
    unittest.main()



print(40*'*')


