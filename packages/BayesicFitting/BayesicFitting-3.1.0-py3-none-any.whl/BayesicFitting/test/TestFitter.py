# run with : python3 -m unittest TestFitter

import numpy as numpy
from numpy.testing import assert_array_almost_equal as assertAAE
from astropy import units
import unittest
import os

from BayesicFitting import *
from BayesicFitting import formatter as fmt

__author__ = "Do Kester"
__year__ = 2017
__license__ = "GPL3"
__version__ = "0.9"
__maintainer__ = "Do"
__status__ = "Development"

#  *
#  * This file is part of the BayesicFitting package.
#  *
#  * BayesicFitting is free software: you can redistribute it and/or modify
#  * it under the terms of the GNU Lesser General Public License as
#  * published by the Free Software Foundation, either version 3 of
#  * the License, or ( at your option ) any later version.
#  *
#  * BayesicFitting is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  * GNU Lesser General Public License for more details.
#  *
#  * The GPL3 license can be found at <http://www.gnu.org/licenses/>.
#  *
#  * A JAVA version of this code was part of the Herschel Common
#  * Science System (HCSS), also under GPL3.
#  *
#  *  2004 - 2014 Do Kester, SRON (Java code)
#  *    2016 - 2017 Do Kester

class TestFitter( unittest.TestCase ):
    """
    Test harness for Fitter class.

    Author:      Do Kester

    """
    aa = 5              #  average offset
    bb = 2              #  slope
    ss = 0.3            #  noise Normal distr.

    x = numpy.asarray( [ -1.0, -0.8, -0.6, -0.4, -0.2, 0.0, 0.2, 0.4, 0.6, 0.8, 1.0] )
    x += 2
    noise = numpy.asarray( [-0.000996, -0.046035,  0.013656,  0.418449,  0.0295155,  0.273705,
      -0.204794,  0.275843, -0.415945, -0.373516, -0.158084] )

    def eq( self, a, b, eps=1e-10 ) :
        if ( a + b ) != 0 :
            return abs( a - b ) / abs( a + b ) < eps
        else :
            return abs( a - b ) < eps

    def __init__( self, testname ):
        super( ).__init__( testname )
        self.doplot = ( "DOPLOT" in os.environ and os.environ["DOPLOT"] == "1" )

    #  **************************************************************
    def testStraightLineParameter( self ):
        """
        test slope fit

        1. Compare PolynomialModel(1) with chain of PowerModel(0) + PowerModel(1)

        2. Fix parameters in PolynomialModel

        """
        plot = self.doplot

        print( "\n   Fitter Test 1  \n" )
        model = PolynomialModel( 1 )
        fitter = Fitter( self.x, model )
        model0 = PowerModel( 0 )
        model1 = PowerModel( 1 )
        model0.addModel( model1 )
        altfit = Fitter( self.x, model0 )
        y = self.noise + self.aa + self.bb * self.x

        print( "Testing Straight Line fit" )

        self.assertTrue( model1.npchain == 2 )
        par = fitter.fit( y )
        alt = altfit.fit( y )

        plotFit( self.x, data=y, model=model, fitter=fitter, residuals=True, show=self.doplot )


        print( "offst = %f  alt = %f  truth = %f"%(par[0], alt[0], self.aa) )
        print( "slope = %f  alt = %f  truth = %f"%(par[1], alt[1], self.bb) )
        assertAAE( par, alt )

        chisq = fitter.chisq
        altch = altfit.chisq
        print( "chisq = %f  alt = %f"%( chisq, altch) )
        self.assertTrue( self.eq(chisq, altch) )

        std = fitter.standardDeviations
        ast = altfit.standardDeviations
        print( "stdev = %f  alt = %f"%(std[0], ast[0]) )
        print( "stdev = %f  alt = %f"%(std[1], ast[1]) )
        assertAAE( std, ast )

        par1 = altfit.fit( y, keep={0:par[0]} )

        plotFit( self.x, data=y, model=model0, fitter=altfit, residuals=False, 
            figsize=[12,7], xlim=[0,12], ylim=[-10,10], show=self.doplot )

        self.assertTrue( 2 == len( par1) )
        assertAAE( par1, par )
        self.assertTrue( model0.npchain == 2 )

        model1 = PolynomialModel( 2, fixed={2:0.0} )

        altfit = Fitter( self.x, model1 )

        par1 = altfit.fit( y )
        print( par, par1 )

        print( "x  ", self.x )
        print( "y  ", y )

        plotFit( self.x, data=y, model=model0, show=self.doplot )

        self.assertTrue( 2 == len( par1) )
        assertAAE( par, par )

        error1 = altfit.monteCarloError( )
        print( "error = ", error1 )

    #  **************************************************************
    def testNormalize( self ):
        """
        test normalized parameter, alternative for keepfixed.

        1.

        2.

        """
        plot = self.doplot

        print( "\n   Fitter Test 2 Normalize  \n" )
        model = PolynomialModel( 2 )

        sm = PowerModel( 1 )

        numpy.random.seed( 2345 )
        x = numpy.linspace( 0.0, 10.0, 101 )
        y = 1.0 + 0.5 * x - 0.2 * x * x +  numpy.random.randn( 101 ) * 0.1

        sm += model                     ## degenerate model par[0] == par[2]

        print( sm )

        fitter = Fitter( x, sm )

        self.assertTrue( sm.npchain == 4 )

        print( fmt( fitter.hessian ) )

        ppp = fitter.fit( y, plot=self.doplot )
        print( ppp )
#        self.assertRaises( numpy.linalg.linalg.LinAlgError, fitter.fit, y )

        fitter.normalize( [0.0, 0.0, 1.0, 0.0], 1.0 )       ## fix par[2] at 1.0

        print( fmt( fitter.hessian ) )
        print( fmt( fitter.covariance ) )

        par = fitter.fit( y, plot=self.doplot )

        print( "param = ", sm.parameters )
        assertAAE( par[2], 1.0 )
        assertAAE( par, [ -0.5, 1.0, 1.0, -0.2], 1 )

        chisq = fitter.chisq
        print( "chisq = %f"%( chisq) )

        std = fitter.standardDeviations
        print( "stdev = ", std )

#        assertAAE( std, ast )


    def test3( self ):

        p = [3.2, -0.1, 0.3, 1.1, 2.1]
        ss = 0.3

        ndata = 101
        x = numpy.linspace( -1, +1, ndata, dtype=float )
        y = ( x - p[1] ) / p[2]
        numpy.random.seed( 3456 )
        y = p[0] * numpy.exp( -y * y ) + ss * numpy.random.randn( ndata )
        y += ( p[3] + p[4] * x )
        p1 = p



        print( "++++++++++++++++++++++++++++++++++++++++++++++++++" )
        print( "Testing Linear Fitter with limits" )
        print( "++++++++++++++++++++++++++++++++++++++++++++++++++" )


        print( "   1. no limits and keep in fit " )
        modl1 = PolynomialModel( 4 )

        amfit = Fitter( x, modl1 )

        par0 = amfit.limitsFit( amfit.fit, y )
        print( "pars0   ", fmt( par0 ) )
        print( "stdv0   ", fmt( amfit.stdevs ) )
        print( "chisq0  ", amfit.chisq )

        par1 = amfit.limitsFit( amfit.fit, y, keep={0:3.3} )
        print( "pars1   ", fmt( par1 ) )
        print( "stdv1   ", fmt( amfit.stdevs ) )
        print( "chisq1  ", amfit.chisq )

        printclass( amfit )

        print( "   2. limits and keep in fit " )
        modl2 = PolynomialModel( 4 )
        modl2.setLimits( [-7.0], [7.0] )

        lmfit = Fitter( x, modl2 )

        par2 = lmfit.limitsFit( lmfit.fit, y )
        print( "pars2   ", fmt( par2 ) )
        print( "stdv2   ", fmt( lmfit.stdevs ) )
        print( "chisq2  ", lmfit.chisq )

        par3 = lmfit.limitsFit( lmfit.fit, y, keep={0:3.3} )
        print( "pars3   ", fmt( par3 ) )
        print( "stdv3   ", fmt( lmfit.stdevs ) )
        print( "chisq3  ", lmfit.chisq )

        printclass( lmfit )

        print( "   3. limits and keep in fitter and fit " )
        modl3 = PolynomialModel( 4 )
        modl3.setLimits( [-7.0], [7.0] )

        lmfit = Fitter( x, modl3, keep={4:5.0} )

        par4 = lmfit.limitsFit( lmfit.fit, y )
        print( "pars4   ", fmt( par4 ) )
        print( "stdv4   ", fmt( lmfit.stdevs ) )
        print( "chisq4  ", lmfit.chisq )

        par5 = lmfit.limitsFit( lmfit.fit, y, keep={0:3.3} )
        print( "pars5   ", fmt( par5 ) )
        print( "stdv5   ", fmt( lmfit.stdevs ) )
        print( "chisq5  ", lmfit.chisq )

        printclass( lmfit )

        if self.doplot :
            xx = numpy.linspace( -1, +1, 1001 )
            plt.plot( x, y, 'k+' )
            plt.plot( xx, modl1.result( xx ), 'k-' )

            plt.plot( xx, modl2.result( xx ), 'r-' )
            plt.show()



if __name__ == '__main__':
    unittest.main( )



