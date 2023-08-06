""" Utility functions and classes for SRP

Context : SRP
Module  : Stats.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 03/02/2020
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : FourierPeriodogram

History : (03/02/2020) First version.

"""

import numpy as np


def ACF(x):
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    #assert N.allclose(r, N.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(np.arange(n, 0, -1)))
    return result
