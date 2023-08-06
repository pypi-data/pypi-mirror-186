""" Utility functions and classes for SRP

Context : SRP
Module  : Catalogue.py
Version : 2.0.0
Author  : Stefano Covino
Date    : 28/05/2021
E-mail  : stefano.covino@brera.inaf.it
URL:    : http://www.merate.mi.astro.it/utenti/covino

Usage   : to be imported

Remarks : 

History : (26/07/2013) First version.
        : (23/07/2015) python3 comparison.
        : (28/05/2021) Porting to Vizier query
"""

import os
from SRP.SRPMath.AstroMagInput import AstroMagInput
from SRP.SRPMath.AstroCoordInput import AstroCoordInput
from astropy.coordinates import SkyCoord
from astropy.coordinates import search_around_sky
from astropy import units as u
from astroquery.vizier import Vizier
from astroquery.vizier import Conf
import warnings



class APASS:
    Conf.row_limit = -1
    #
    class CatEntries:
        def __init__ (self,ra,dec,b,eb,v,ev,g,eg,r,er,i,ei):
            self.Id = 'APASS'
            self.RA = float(ra)
            self.DEC = float(dec)
            inpmag = AstroMagInput (b,eb)
            self.B = inpmag.Mag
            self.eB = inpmag.eMag
            inpmag = AstroMagInput (v,ev)
            self.V = inpmag.Mag
            self.eV = inpmag.eMag
            inpmag = AstroMagInput (g,eg)
            self.g = inpmag.Mag
            self.eg = inpmag.eMag
            inpmag = AstroMagInput (r,er)
            self.r = inpmag.Mag
            self.er = inpmag.eMag
            inpmag = AstroMagInput (i,ei)
            self.i = inpmag.Mag
            self.ei = inpmag.eMag
            
        def __str__ (self):
            msg = "%20s\t%15.6f\t%15.6f\t" % (self.Id, self.RA, self.DEC)
            msg = msg + "%10.3f\t%9.3f\t" % (self.B, self.eB)
            msg = msg + "%10.3f\t%9.3f\t" % (self.V, self.eV)
            msg = msg + "%10.3f\t%9.3f\t" % (self.g, self.eg)
            msg = msg + "%10.3f\t%9.3f\t" % (self.r, self.er)
            msg = msg + "%10.3f\t%9.3f\t" % (self.i, self.ei)
            return msg
            

        def __lt__ (self, other):
            return self.V < other.V


    
    def __init__ (self, ra, dec, radius=1.0/60., epoch=2000.0):
        inpcoord = AstroCoordInput(ra,dec,inp_equinox=epoch)
        self.RA = inpcoord.RA
        self.DEC = inpcoord.DEC
        self.Epoch = 2000.0
        self.Radius = radius/60.
        self.ListEntries = []
        
        
    def GetData(self):
        crd = SkyCoord(ra=self.RA*u.degree, dec=self.DEC*u.degree)
        warnings.filterwarnings('ignore', category=UserWarning, append=True)
        try:
            restab = Vizier.query_region(crd, radius=self.Radius*u.degree, catalog=["II/336"])
        except:
            restab = []
        warnings.resetwarnings()
        #
        if len(restab) > 0:
            data = restab[0]
            for ii in data:
                ra = ii['RAJ2000']
                dec = ii['DEJ2000']
                coord = AstroCoordInput(ra,dec)
                b = ii['Bmag']
                eb = ii['e_Bmag']
                v = ii['Vmag']
                ev = ii['e_Vmag']
                g = ii['g_mag']
                eg = ii['e_g_mag']
                r = ii['r_mag']
                er = ii['e_r_mag']
                i = ii['i_mag']
                ei = ii['e_i_mag']
                newinp = self.CatEntries(coord.RA,coord.DEC,b,eb,v,ev,g,eg,r,er,i,ei)
                self.ListEntries.append(newinp)
            return len(self.ListEntries)
        else:
            return None

    def __str__(self):
        msg = ''
        for i in self.ListEntries:
            msg = msg + str(i) + os.linesep
        return msg



    def Skycat(self, outname='SRP.cat'):
        msg = ''
        msg = msg + "long_name: SRP catalog for file %s\n" % (outname)
        msg = msg + "short_name: %s\n" % (outname)
        msg = msg + "url: ./%s\n" % (outname)
        msg = msg + "symbol: {} {circle blue} 4\n"
        msg = msg + "id_col: 0\n"
        msg = msg + "ra_col: 1\n"
        msg = msg + "dec_col: 2\n"
        msg = msg + "Id\tRA\tDEC\tB\teB\tV\teV\tg\teg\tr\ter\ti\tei\n"
        msg = msg + "---------\n"
        msg = msg + str(self)
        msg = msg + "EOD\n"
        return msg

        
        
    def sort(self):
        self.ListEntries.sort()
        
        
