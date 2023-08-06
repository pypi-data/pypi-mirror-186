""" Utility functions and classes for SRP

Context : SRP
Module  : Plot
Version : 1.0.0
Author  : Stefano Covino
Date    : 12/08/2020
E-mail  : stefano.covino@inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : SetPlotPars(...)
        : px: subplot (e.g. px = p.add_subplot(111))

Remarks :

History : (12/08/2020) First version.

"""

import matplotlib.pyplot as plt


def SetPlotPars (px,xlbl="",ylbl="",titlbl="",linwidth=2,tickxfonsiz=24,tickyfonsiz=24,xlblfonsiz=30,ylblfonsiz=30,titlblfonsiz=35):
    #
    # Lines
    [i.set_linewidth(linwidth) for i in px.spines.values()]
    #
    # Ticks
    plt.tick_params(axis='both', which='major', labelsize='xx-large')
    plt.tick_params(axis='both', which='minor', labelsize='x-large')
    #
    for tickx,ticky in zip(px.xaxis.get_major_ticks(),px.yaxis.get_major_ticks()):
        tickx.label.set_fontsize(tickxfonsiz) 
        ticky.label.set_fontsize(tickyfonsiz)
    #
    # Labels
    plt.xlabel(xlbl,fontsize=xlblfonsiz)
    plt.ylabel(ylbl,fontsize=ylblfonsiz)
    plt.title(titlbl,fontsize=titlblfonsiz)
#



