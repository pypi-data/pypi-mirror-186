""" Utility functions and classes for SRP

Context : SRP
Module  : Sky
Version : 1.0.0
Author  : Stefano Covino
Date    : 19/01/2023
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : 
    
History : (19/02/2023) First version.

"""

import AstroAtmosphere as AA

def AtmRefraction (l, z, site='CERRO_PARANAL'):
    return AA.quick_refraction(l, z, conditions=site)*3600
