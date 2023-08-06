""" Utility functions and classes for SRP

Context : SRP
Module  : Math
Version : 2.0.1
Author  : Stefano Covino
Date    : 12/11/2021
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks :

History : (20/09/2012) First version.
        : (30/07/2020) Alternative version for [0,180] interval.
        : (12/11/2021) Both versions available.
"""

import numpy as np


def PhaseAngle (ang, mina=0.0, maxa=360.0):
    while ang < mina or ang >= maxa:
        if ang < mina:
            ang = ang + (maxa-mina)
        else:
            ang = ang - (maxa-mina)
    return ang



def phaseang (ang):
    x = np.cos(ang)
    y = np.sin(ang)
    return np.arctan(y/x)

