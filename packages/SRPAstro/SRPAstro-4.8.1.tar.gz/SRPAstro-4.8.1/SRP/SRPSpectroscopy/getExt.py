""" Utility functions and classes for SRP

Context : SRP
Module  : Spectroscopy.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 25/02/2022
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported
        : lambda in micron units

History : (25/02/2022) First version.
"""

from dust_extinction.averages import G03_SMCBar
from dust_extinction.averages import G03_LMCAvg
from dust_extinction.averages import GCC09_MWAvg
import astropy.units as u
from . import ExtConstants
import numpy as np


extsmc = G03_SMCBar()
extlmc = G03_LMCAvg()
extmw = GCC09_MWAvg()

def getExt (ebv,glxy,lmbd):
    if not glxy in (list(ExtConstants.ExtCurDict.keys())):
        return None
    else:
        if glxy == 'SMC':
            absr = extsmc.extinguish(lmbd*u.micron,Ebv=ebv)
        elif glxy == 'LMC':
            absr = extlmc.extinguish(lmbd*u.micron,Ebv=ebv)
        elif glxy == 'MW':
            absr = extmw.extinguish(lmbd*u.micron,Ebv=ebv)
    return -2.5*np.log10(absr)

