""" Utility functions and classes for SRP

Context : SRP
Module  : GP
Version : 1.0.0
Author  : Stefano Covino
Date    : 30/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : From C. E. Rasmussen & C. K. I. Williams, Gaussian Processes
            for Machine Learning, the MIT Press, 2006

History : (30/01/2020) First version.

"""


import numpy as np


def ExpSineKernel(r,A,G,P):
    return A*np.exp(-G*(np.sin(np.pi*r/P))**2)
