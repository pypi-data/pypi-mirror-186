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


def MaternKernel (A,r,L,nu):
    fi = (2**(1-nu))/ss.gamma(nu)
    sem = np.sqrt(2*nu)*r/L
    se = sem**nu
    te = ss.kv(nu,sem)
    return A*fi*se*te
