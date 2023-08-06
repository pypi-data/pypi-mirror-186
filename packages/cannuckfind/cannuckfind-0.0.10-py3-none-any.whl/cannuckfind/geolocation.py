# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:01:21 2022

@author: HEHenson
"""

#from enum import Enum

# should be moved into some sort of universal toolbox

class unknownC(object):

    '''
    Expands on the concept of unknown variables to categorical variables
    '''
    def __init__(self):
        
        self.UNKNOWN = int(101)  #: uninitialized
        self.PRIV = int(102)     #: unknown to be private
        self.NA = int(103)       #: known to unavailable
        self.NL = int(104)       #: invalid
        self.JK = int(105)       #: Joke
        self.MX = int(106)       #: maximum number of records
        
class isC3(unknownC):
    """
    Object that stores explanatory variables for ML analysis
    """
    def __init__(self):
        
        import geonamescache
        # C3iscan
        super(isC3,self).__init__()
        iscanC3 = self.UNKNOWN
        isusC3 = self.UNKNOWN
        isothC3 = self.UNKNOWN
        # geocasual
        iscanGeoCasual = self.UNKNOWN
        iscanSpaCy = self.UNKNOWN
        iscanGeoGrapy = self.UNKNOWN
        # load up a list of country names
        self.gc = geonamescache.GeonamesCache().get_countries()
        
        
class isC3SC(isC3,unknownC):
    """
    Object that uses SpaCy 
    """
    def __init__(self):
        """Constructor Method
        """
       
        import spacy
       
        super(isC3SC,self).__init__()
        self.__version__ = 'v0.0.09'
        # load up SpaCy nlp vocab for the web
        self.en = spacy.load('en_core_web_sm')
        self.iscanSC    = unknownC().UNKNOWN
        self.isusSC   = unknownC().UNKNOWN
        self.isoth3SC  = unknownC().UNKNOWN   
        self.rawtext = unknownC().UNKNOWN 
        self.rawtext_ents = unknownC().UNKNOWN
                 
    def loadSCraw(self,newtext=""):
        """
        Loads record for further analysis
       
        :param rawtext: A string of text of be analyzed
        """
        self.rawtext = newtext
        self.rawtext_ents = self.en(self.rawtext)
       
        # save a list of the entities identified
        self.entvect = []
        for ent in self.rawtext_ents.ents:
            # print(ent.text,ent.start_char,ent.end_char, ent.label_)
            if ent.label_ == 'GPE':
                self.entvect.append(ent.text)        
    def isCanC3SC(self):
        """
        See if raw text locates as Canada
       
        :returns: True if Canadian
        """
        if 'Canada' in self.entvect:
            self.iscanSC = True
        else:
            self.iscanSC = False
        return self.iscanSC
           
    def isUSC3SC(self):
        """
        See if raw text locates as United States
       
        :returns: True if US
        """
        if 'United States' in self.entvect:
            self.isusSC = True
        else:
            self.isusSC = False
        return self.isusSC
   
   
    def isOthC3SC(self):
        """
        See if raw text locates from rest of world
       
        :returns: True if rest of world
        """
        # need to ensure that the other the two are false
        if self.iscanSC == self.NA | self.isusSC == self.NA :
            return self.NA
        # if Canadian status is unknown set it
        if self.iscanSC == self.UNKNOWN:
            self.isCanC3SC()
        # if US status is unknown then set it
        if self.isusSC == self.UNKNOWN:
            self.isUSC3SC()
        # if neither are true
        if self.iscanSC == True | self.isusSC == True:
            self.isothSC = False
        else:
            self.isothSC = True
        return self.isothSC
   
class isC3GP(isC3,unknownC):
    """
    Object that uses geograpy 
    """
    def __init__(self):
       
        import geograpy
       
        super().__init__()
        self.__version__ = 'v0.0.09'
      
        self.iscanGP    = unknownC().UNKNOWN
        self.isusGP     = unknownC().UNKNOWN
        self.isoth3GP   = unknownC().UNKNOWN

       
    def loadrawGP(self,rawtext):
   
        """
        Loads record for further analysis
       
        :param rawtext: A string of text of be analyzed
        """
        from geograpy import get_geoPlace_context
       
        self.rawtext = rawtext
        # country should be the zero vector
        self.places = get_geoPlace_context(text=self.rawtext)
              
    def isCanC3GP(self):
        """
        returns boolean if Canada
        """
       
        if u'Canada' in self.places.countries[0]:
            self.iscanGP = True
        else:
            self.iscanGP = False
        return self.iscanGP
           
    def isUSC3GP(self):
        """ returns boolean if United States
        """
        if u'United States of America' == self.places.countries[0]:
            self.isusGP = True
        else:
            self.isusGP = False
        return self.isusGP
   
   
    def isOthC3GP(self):
        """ returns boolean if rest of world
        """
        # need to ensure that the other the two are false
        if self.iscanGP == self.NA | self.isusGP == self.NA :
            return self.NA
        # if Canadian status is unknown set it
        if self.iscanGP == self.UNKNOWN:
            self.isCanC3GP()
        # if US status is unknown then set it
        if self.isusGP == self.UNKNOWN:
            self.isUSC3GP() 
       # if neither are true
        if self.iscanGP == True | self.isusGP == True:
            self.isothGP = False
        else:
            self.isothGP = True
        return self.isothGP
   

 
 
 
 
