""" Utility functions and classes for SRP

Context : SRP
Module  : Photometry
Version : 1.0.0
Author  : Stefano Covino
Date    : 17/01/2023
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : 
    
History : (17/02/2023) First version.

"""

import numpy as np

def AirMass (ang):
    return 1./np.cos(np.radians(ang))

def InvAirMass (am):
    return np.degrees(np.arccos(1./am))
