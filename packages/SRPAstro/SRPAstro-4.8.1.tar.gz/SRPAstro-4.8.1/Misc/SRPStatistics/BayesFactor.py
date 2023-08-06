""" Utility functions and classes for SRP

Context : SRP
Module  : Stats.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 04/10/2019
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : BayesFactor(e1,ee1,e2,ee2)
            e1,e2 are the computed evidence, ee1 and ee2 the errors.
          The function return the a dictorionary with e Bayes factor and the
          associated probabilities with error.
        
Remarks : 

History : (04/10/2019) First version.

"""


import numpy as np
from SRP.SRPStatistics.ScoreatPercentile import ScoreatPercentile
from SRP.SRPStatistics.GenGaussSet import GenGaussSet

def BayesFactor (p1, ep1, p2, ep2):
    p1set = GenGaussSet(p1,ep1,10000)
    p2set = GenGaussSet(p2,ep2,10000)
    #p1l = np.exp(p1)
    #ep1l = p1l*ep1
    #p2l = np.exp(p2)
    #ep2l = p2l*ep2
    #
    lnbf = p2-p1
    elnbf = np.sqrt(ep1**2+ep2**2)
    #
    bf = np.exp(p2-p1)
    #ebf = bf*np.sqrt(ep1**2 + ep2**2)
    bfset = np.exp(p2set-p1set)
    ebf = ScoreatPercentile(bfset)[3]
    #
    #bfl = p2l/p1l
    #ebfl = bfl*np.sqrt((ep1l/p1l)**2+(ep2l/p2l)**2)
    #
    #pl = p2l/(p1l+p2l)
    #sl = p1l+p2l
    #esl = np.sqrt(ep1l**2+ep2l**2)
    #epl = pl*np.sqrt((ep2l/p2l)**2 + (esl/sl)**2)
    #
    p = 1./(1+np.exp(p1-p2))
    #ep = (np.exp(p1-p2)*p**2)*np.sqrt(ep1**2+ep2**2)
    pset = 1./(1+np.exp(p1set-p2set))
    ep = ScoreatPercentile(pset)[3]
    return {"BF": bf, "eBF": ebf, "p":p, "ep":ep, "lnBF":lnbf, "elnBF":elnbf}

