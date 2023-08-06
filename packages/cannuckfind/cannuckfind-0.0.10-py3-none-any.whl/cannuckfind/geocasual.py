# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:01:21 2022

@author: HEHenson
"""
import sys
# from enum import Enum


# informal GeoNames

class geocasual:
    '''
    Comments about location known not to be accurate
    '''
    def __init__(self):
        pass
    def isjoke(self,rawLoc):
        if "Nowhere" in rawLoc:
            return True
        if "Everywhere" in rawLoc:
            return True
        if "Politics" in rawLoc:
            return True
        if "Knowledge" in rawLoc:
            return True
        if "Goblinarium" in rawLoc:
            return True
        if "Global" in rawLoc:
            return True
        # may be worthwhile going back to web addresses later
        if "https" in rawLoc:
            return True
        if "Miles away" in rawLoc:
            return True
        if "Sweateronbackwards" in rawLoc:
            return True
        if "plague" in rawLoc:
            return True
        if "Past2Future" in rawLoc:
            return True
        return False
    def isCan(self,rawLoc):
    # Aboriginal
        if "amiskwacîwâskahikan" in rawLoc:
            return True
        if "PERTH, ON" in rawLoc:
            return True
        if "Brossard" in rawLoc:
            return True
    def isUS(self,rawLoc):
        if "NYC" in rawLoc:
            return True
        if "USA" in rawLoc:
            return True
        if "Washington" in rawLoc:
            return True
        if "Maine" in rawLoc:
            return True
        if "seattle" in rawLoc:
            return True
        if "Singleville AR" in rawLoc:
            return True
        if "Santa Barbara, CA" in rawLoc:
            return True
        if "HoCo CA" in rawLoc:
            return True
        if "greensburg, pa" in rawLoc:
            return True
        if "Orange County, CA" in rawLoc:
            return True        
        return False
    def isNonUS_Can(self,rawLoc):
        if self.isAustralia(rawLoc):
            return True
        if self.isUK(rawLoc):
            return True
        if self.isDEU(rawLoc):
            return True
        return False
    def isAustralia(self,rawLoc):
        if "Australia" in rawLoc:
            return True
        if "Wurundjeri" in rawLoc:
            return True
        return False
    def isUK(self,rawLoc):
        if "Gweriniaeth" in rawLoc:
            return True
        if "London England" in rawLoc:
            return True
        if "Worcestershire UK" in rawLoc:
            return True
        return False
    def isDEU(self,rawLoc):
        if " DEU " in rawLoc:
            return True
        if "NRW" in rawLoc:
            return True
        if "Niederrhein" in rawLoc:
            return True
        return False
    def isFJT(self, rawLoc):
        if " FJT " in rawLoc:
            return True
        return False

