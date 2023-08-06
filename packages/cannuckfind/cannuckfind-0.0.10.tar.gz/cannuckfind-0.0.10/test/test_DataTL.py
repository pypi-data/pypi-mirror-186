print(40*'*')
print('testing location \n')
import sys
import os
import unittest
import pandas as pd

sys.path.append('/media/henskyconsulting/easystore/Hensky/Projects/2023CannuckFind/cannuckfind/src/cannuckfind')

import geolocation
from geolocation import unknownC
import inDat

# will import this dataset 
# this is an 8 row dataset intended for expository purposes
# it will be resused in other documents

utestDat = '../src'

print(os.listdir(utestDat))

testPth = './ex8.csv'
testCsv = pd.read_csv(f'{testPth}', sep='\t', quotechar='"')
print(testCsv.describe())






class TestinDat(unittest.TestCase):
    """
    Test inDat
    """
    def test_loadrsamp1(self):
        import inDat
        # Test with invalid name
        testloc1 = inDat.inDat("Idonotexist")
        self.assertTrue(testloc1.exFile == "Idonotexist")
        self.assertTrue(testloc1.inDat == geolocation.unknownC().UNKNOWN)
    def test_loadrsamp2(self):
        print('*** 39 in test')
        print(testCsv.describe())
        testloc2 = inDat.inDat('ex8.csv')
        print('*** 42 in test')
        print(testloc2.inDat)
        self.assertTrue(testloc2.inDat.shape[0] == 8)
        self.assertTrue(testloc2.inDat.shape[1] == 16)
        print('*** 47 in test')
        # expecting 1 as one data set has been read in at this point
        junk = testloc2.inDatinfo()
        print('***50 in test',junk)
    def test_rsamp3(self):
        testL1 = inDat.inDat('ex8.csv')
        self.assertTrue(testL1.inDat.shape[0] == 8)
        self.assertTrue(testL1.inDat.shape[1] == 16)
        testS1 = testL1.loadrandomsample(smpsize = 4)
        self.assertTrue(testS1.shape[0] == 4)
        self.assertTrue(testS1.shape[1] == 4)
        
  


        
print('*** test DataTL location complete')
print('*** ')
print(40*'*')       


if __name__ == '__main__':
    unittest.main()



print(40*'*')


