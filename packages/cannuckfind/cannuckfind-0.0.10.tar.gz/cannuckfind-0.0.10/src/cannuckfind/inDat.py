# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:01:21 2022

@author: HEHenson
"""

import sys
import os
import pandas as pd
import csv

import geolocation
from geolocation import unknownC


class inDat(unknownC):
    def __init__(self, thefile=geolocation.unknownC().UNKNOWN):
        """
        Creates object to import external data
        :param exfile: path to external file
        """
        print('*** 20 thefile=',thefile)
        self.exFile = None    #: path to external file
        self.inDat = geolocation.unknownC().UNKNOWN     #: open file object
        self.SAMPSIZE = 100   #: load random sample size
        self.SEED = 1                       #: Default Seed for Random Sample
        self.sampdat = geolocation.unknownC().UNKNOWN   #: open file object
        if f"{thefile}" != geolocation.unknownC().UNKNOWN:
            self.exFile = f"{thefile}"
        print('*** 30 ',f"{thefile}")
        self.datProg  = pd.Series([-1,0,1,2,3]) #: stage of data analysis
        self.loadrawfile(thefile = f"{self.exFile}")
       
    def loadrawfile(self, thefile = geolocation.unknownC().UNKNOWN):
        """ load file extracted from raw source
        """
        print('*** 33',thefile)
        if (os.path.isfile(thefile)):
            self.inDat = pd.read_csv(f"{thefile}",sep='\t',quotechar="'")
            return True
        print('*** 40 will return false in loadrawfile')
        return False
        
    def inDatinfo(self):
        """ convience function to give quick look at the data
            return 1 if rawfile read in 2 if there is a sample of it
            -1 and something is wrong
        """
        print('*** 48 in indat.py top of info')
        self.datProg = 1
        if self.inDat is not None :
            print(self.inDat.describe())
            print('*** in 50')
        else:
            print('inDat not yet read in')
            self.datProg = 0
            return self.datProg
        if self.sampdat != geolocation.unknownC().UNKNOWN:
            print('*** 56')
            print(self.sampdat)
            print(self.sampdat.describe())
            self.datProg = 2
            return self.datProg
        else:
            print('sampdat not created')
            self.datProg
            return 
        # something is wrong
        self.datProg = -1
        return self.datProg
        
    def loadrandomsample(self,smpsize = unknownC().UNKNOWN):
        # assume rawfile has been read in
        if smpsize == geolocation.unknownC().UNKNOWN:
             smpsize = self.SAMPSIZE
        self.sampdat = self.inDat.sample(smpsize,random_state = self.SEED)
        self.sampdat = self.sampdat.loc[:,["description","screen_name","user_location","text"]]
        outfilestr = "../CovidTwitDat_V2" + "RawTrain" + str(smpsize)
        self.sampdat.to_csv(outfilestr,sep='\t')
        return self.sampdat
    
    def __del__(self):
        # note pandas file should be closed automatically
        pass
    


    
