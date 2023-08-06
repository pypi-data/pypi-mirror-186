""" Utility functions and classes for SRP

Context : SRP
Module  : System.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 20/05/2021
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks :

History : (20/05/2021) First version.

"""


import os, os.path


def WriteTextFile(filename,msg,mode='w'):
    with open(filename,mode) as f:
        f.write(msg)

