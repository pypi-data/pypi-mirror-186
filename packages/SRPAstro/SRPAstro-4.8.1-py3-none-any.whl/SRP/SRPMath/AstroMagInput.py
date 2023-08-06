""" Utility functions and classes for SRP

Context : SRP
Module  : Math.py
Version : 1.0.1
Author  : Stefano Covino
Date    : 31/05/2011
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : 

History : (11/08/2010) First version.
        : (31/05/2021) Beter management of warnings.
"""


import ephem
import math
import warnings


from . import MathConstants




class AstroMagInput:
    def __init__ (self, mag, emag):
        #
        warnings.filterwarnings('error', category=UserWarning, append=True)
        #
        try:
            self.Mag = float(mag)
        except (ValueError, UserWarning):
            self.Mag = MathConstants.BADMAG
        try:
            self.eMag = float(emag)
        except (ValueError, UserWarning):
            self.eMag = MathConstants.BADMAG 
        #
        warnings.resetwarnings()
        
        
    def __str__ (self):
        msg = "%10.3f %9.3f" % (self.Mag, self.eMag)
        return msg