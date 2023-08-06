""" 

Context : SRP
Module  : Statistics
Version : 1.10.0
Author  : Stefano Covino
Date    : 29/01/2020
E-mail  : stefano.covino@brera.inaf.it
URL     : http://www.me.oa-brera.inaf.it/utenti/covino


Usage   : to be imported

Remarks :

History : (28/10/2010) First version.
        : (30/04/2011) ChiSqIncrement.
        : (19/02/2012) ScoreatPercentile.
        : (27/08/2012) Faster sigma clipping for frames.
        : (04/03/2013) MAD.
        : (04/04/2013) XCorr_1D.
        : (07/06/2013) FTest.
        : (22/12/2014) RebinData.
        : (08/11/2015) StDev.
        : (02/11/2016) FourierPeriodogram.
        : (04/10/2019) Bayes factor.
        : (29/01/2020) GP and FT library.
"""



__all__ = ['AsymmetricGaussianDistrib', 'AverIterSigmaClipp', 'AverSigmaClippFrame', 
           'AverSigmaClippFrameFast', 'BayesFactor', 'ChSqIncrement',
           'CoordDistanceMinimization', 'FT', 'FTest', 'GenFitPars',
           'GenGaussSet', 'GP', 'MAD', 'RebinData', 'ScoreatPercentile', 'StDev',
           'XCorr_1D', 'WeightedMean', 'WeightedMeanFrame']

