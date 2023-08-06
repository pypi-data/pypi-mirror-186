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


def PSDSE (s,L,D=1):
    fn = (2*np.pi*L**2)**(D/2)
    return fn * np.exp(-2*(np.pi*L*s)**2)
