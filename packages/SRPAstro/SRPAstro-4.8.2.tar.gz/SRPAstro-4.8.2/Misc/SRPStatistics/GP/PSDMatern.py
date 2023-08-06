""" Utility functions and classes for SRP

Context : SRP
Module  : GP
Version : 1.0.0
Author  : Stefano Covino
Date    : 29/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : From C. E. Rasmussen & C. K. I. Williams, Gaussian Processes
            for Machine Learning, the MIT Press, 2006

History : (29/01/2020) First version.

"""


import numpy as np
import scipy.special as ss


def PSDMatern (s,L,nu,D=1):
    expfct = nu + D/2
    fnum = 2**D * np.pi**(D/2)*ss.gamma(expfct)*(2*nu)**nu
    fdem = ss.gamma(nu)*L**(2*nu)
    tterm = ((2*nu)/L**2 + 4*np.pi**2*s**2)**-(nu+D/2)
    #
    return fnum * tterm / fdem
