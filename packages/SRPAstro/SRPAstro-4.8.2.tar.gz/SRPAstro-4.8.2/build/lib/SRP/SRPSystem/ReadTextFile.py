""" Utility functions and classes for SRP

Context : SRP
Module  : System.py
Version : 1.0.0
Author  : Stefano Covino
Date    : 19/05/2021
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks :

History : (19/05/2021) First version.

"""


import os, os.path


def ReadTextFile(filename):
    try:
        with open(filename) as f:
            lst=[line.strip() for line in f]
        return lst
    except FileNotFoundError:
        return None

