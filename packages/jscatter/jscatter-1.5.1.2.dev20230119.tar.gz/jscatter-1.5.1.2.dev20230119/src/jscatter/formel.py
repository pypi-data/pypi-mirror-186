# -*- coding: utf-8 -*-
# written by Ralf Biehl at the Forschungszentrum Jülich ,
# Jülich Center for Neutron Science 1 and Institute of Complex Systems 1
#    Jscatter is a program to read, analyse and plot data
#    Copyright (C) 2015-2021  Ralf Biehl
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

"""
Physical equations and useful formulas as quadrature of vector functions, parallel execution,
viscosity, compressibility of water, scatteringLengthDensityCalc or sedimentationProfile.
Use scipy.constants for physical constants.

- Each topic is not enough for a single module, so this is a collection.
- All scipy functions can be used. See http://docs.scipy.org/doc/scipy/reference/special.html.
- Statistical functions http://docs.scipy.org/doc/scipy/reference/stats.html.

Mass and scattering length of all elements in Elements are taken from :
 - Mass: http://www.chem.qmul.ac.uk/iupac/AtWt/
 - Neutron scattering length: http://www.ncnr.nist.gov/resources/n-lengths/list.html

Units converted to amu for mass and nm for scattering length.

"""

import functools
import inspect
import math
import os
import re
import pickle
import io
import numbers
import warnings
from collections import deque
import multiprocessing as mp
import itertools

import numpy as np
from numpy import linalg as la
import scipy
import scipy.constants as constants
import scipy.integrate
import scipy.signal
import scipy.optimize
import scipy.special as special
from scipy import stats
from scipy.special.orthogonal import roots_legendre

from .dataarray import dataArray as dA
from .dataarray import dataList as dL
from .libs import ml_internal
from .libs.cubature import cubature
from .libs.imagehash import imageHash
from . import parallel
from .parallel import *


from .data import Elements, vdwradii, felectron
from .data import aquasolventdensity as _aquasolventdensity
from .data import bufferDensityViscosity as _bufferDensityViscosity

_path_ = os.path.realpath(os.path.dirname(__file__))

#: Variable to allow printout for debugging as if debug:print('message')
debug = False

#: Antisymmetric Levi-Civita symbol
eijk = np.zeros((3, 3, 3))
eijk[0, 1, 2] = eijk[1, 2, 0] = eijk[2, 0, 1] = 1
eijk[0, 2, 1] = eijk[2, 1, 0] = eijk[1, 0, 2] = -1


def _getFuncCode(func):
    """
    Get code object of a function
    """
    try:
        return func.__code__
    except AttributeError:
        return None


# noinspection PyIncorrectDocstring
def memoize(**memkwargs):
    """
    A least-recently-used cache decorator to cache expensive function evaluations.

    Memoize caches results and retrieves from cache if same parameters are used again.
    This can speedup computation in a model if a part is computed with same parameters several times.
    During fits it may be faster to calc result for a list and take from cache.

    Parameters
    ----------
    function : function
        Function to evaluate as e.g. f(Q,a,b,c,d)
    memkwargs : dict
        Keyword args with substitute values to cache for later interpolation. Empty for normal caching of a function.
        E.g. memkwargs={'Q':np.r_[0:10:0.1],'t':np.r_[0:100:5]} caches with these values.
        The needed values can be interpolated from the returned result. See example below.
    maxsize : int, default 128
        maximum size of the cache. Last is dropped.

    Returns
    -------
    function
        cached function with new methods
         - last(i) to retrieve the ith evaluation result in cache (last is i=-1).
         - clear() to clear the cached results.
         - hitsmisses counts hits and misses.

    Notes
    -----
    Only keyword arguments for the memoized function are supported!!!!
    Only one attribute and X are supported for fitting as .interpolate works only for two cached attributes.



    Examples
    --------
    The example uses a model that computes like I(q,n,..)=F(q)*B(t,n,..).
    F(q) is cheap to calculate B(t,n,..) not. In the following its better to calc
    the function for a list of q , put it to cache and take in the fit from there.
    B is only calculated once inside of the function.

    Use it like this::

     import jscatter as js
     import numpy as np

     # define some data
     TT=js.loglist(0.01,80,30)
     QQ=np.r_[0.1:1.5:0.15]
     # in the data we have 'q' and 'X'
     data=js.dynamic.finiteZimm(t=TT,q=QQ,NN=124,pmax=100,tintern=10,l=0.38,Dcm=0.01,mu=0.5,viscosity=1.001,Temp=300)

     # makes a unique list of all X values    -> interpolation is exact for X
     # one may also use a smaller list of values and only interpolate
     tt=list(set(data.X.flatten));tt.sort()

     # define memoized function which will always use the here defined q and t
     # use correct values from data for q     -> interpolation is exact for q
     memfZ=js.formel.memoize(q=data.q,t=tt)(js.dynamic.finiteZimm)

     def fitfunc(Q,Ti,NN,tint,ll,D,mu,viscosity,Temp):
        # use the memoized function as usual (even if given t and q are used from above definition)
        res= memfZ(NN=NN,tintern=tint,l=ll,Dcm=D,pmax=40,mu=mu,viscosity=viscosity,Temp=Temp)
        # interpolate to the here needed q and t (which is X)
        resint=res.interpolate(q=Q,X=Ti,deg=2)[0]
        return resint

     # do the fit
     data.setlimit(tint=[0.5,40],D=[0,1])
     data.makeErrPlot(yscale='l')
     NN=20
     data.fit(model=fitfunc,
              freepar={'tint':10,'D':0.1,},
              fixpar={'NN':20,'ll':0.38/(NN/124.)**0.5,'mu':0.5,'viscosity':0.001,'Temp':300},
              mapNames={'Ti':'X','Q':'q'},)

    Second example

    Use memoize as a decorator (@ in front) acting on the following function.
    This is a shortcut for the above and works in the same way
    ::

     # define the function to memoize
     @js.formel.memoize(Q=np.r_[0:3:0.2],Time=np.r_[0:50:0.5,50:100:5])
     def fZ(Q,Time,NN,tintern,ll,Dcm,mu,viscosity,Temp):
         # finiteZimm accepts t and q as array and returns a dataList with different Q and same X=t
         res=js.dynamic.finiteZimm(t=Time,q=Q,NN=NN,pmax=20,tintern=tintern,
                               ll=ll,Dcm=Dcm,mu=mu,viscosity=viscosity,Temp=Temp)
         return res

     # define the fitfunc
     def fitfunc(Q,Ti,NN,tint,ll,D,mu,viscosity,Temp):
        #this is the cached result for the list of Q
        res= fZ(Time=Ti,Q=Q,NN=NN,tintern=tint,ll=ll,Dcm=D,mu=mu,viscosity=viscosity,Temp=Temp)
        # interpolate for the single Q value the cached result has again 'q'
        return res.interpolate(q=Q,X=Ti,deg=2)[0]

     # do the fit
     data.setlimit(tint=[0.5,40],D=[0,1])
     data.makeErrPlot(yscale='l')
     data.fit(model=fitfunc,
              freepar={'tint':6,'D':0.1,},
              fixpar={'NN':20,'ll':0.38/(20/124.)**0.5,'mu':0.5,'viscosity':0.001,'Temp':300},
              mapNames={'Ti':'X','Q':'q'})
     # the result depends on the interpolation;


    """
    cachesize = memkwargs.pop('maxsize', 128)

    def _memoize(function):
        function.hitsmisses = [0, 0]
        cache = function.cache = {}
        deck = function.deck = deque([], maxlen=cachesize)
        function.last = lambda i=-1: function.cache[function.deck[i]]

        def clear():
            while len(function.deck) > 0:
                del function.cache[function.deck.pop()]
            function.hitsmisses = [0, 0]

        function.clear = clear

        @functools.wraps(function)
        def _memoizer(*args, **kwargs):
            # make new
            nkwargs = dict(kwargs, **memkwargs)
            key = pickle.dumps(args, 1) + pickle.dumps(nkwargs, protocol=1)
            if key in cache:
                function.hitsmisses[0] += 1
                deck.remove(key)
                deck.append(key)
                return cache[key]
            else:
                function.hitsmisses[1] += 1
                cache[key] = function(*args, **nkwargs)
                if len(deck) >= cachesize:
                    del cache[deck.popleft()]
                deck.append(key)
                return cache[key]

        return _memoizer

    return _memoize


def rotationMatrix(vector, angle):
    """
    Create a rotation matrix corresponding to rotation around vector v by a specified angle.

    .. math::  R = vv^T + cos(a) (I - vv^T) + sin(a) skew(v)
    See Notes for scipy rotation matrix.

    Parameters
    ----------
    vector : array
        Rotation around a general  vector
    angle : float
        Angle in rad

    Returns
    -------
    array
        Rotation matrix

    Notes
    -----
    A convenient way to define more complex rotations is found in
    `scipy.spatial.transform.Rotation
    <https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html>`_ .
    E.g. by Euler angles and returned as rotation matrix ::

     from scipy.spatial.transform import Rotation as Rot
     R=Rot.from_euler('YZ',[90,10],1).as_matrix()

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Rotation_matrix#Rotation_matrix_from_axis_and_angle

    Examples
    --------
    Examples show how to use a  rotation matrix with vectors.
    ::

     import jscatter as js
     import numpy as np
     from matplotlib import pyplot
     R=js.formel.rotationMatrix([0,0,1],np.deg2rad(-90))
     v=[1,0,0]
     # rotated vector
     rv=np.dot(R,v)
     #
     # rotate Fibonacci Grid
     qfib=js.formel.fibonacciLatticePointsOnSphere(300,1)
     qfib=qfib[qfib[:,2]<np.pi/2,:]                       # select half sphere
     qfib[:,2]*=(30/90.)                                  # shrink to cone of 30°
     qfx=js.formel.rphitheta2xyz(qfib)                    # transform to cartesian
     v = [0,1,0]                                          # rotation vector
     R=js.formel.rotationMatrix(v,np.deg2rad(90))        # rotation matrix around v axis
     Rfx=np.einsum('ij,kj->ki',R,qfx)                     # do rotation
     fig = pyplot.figure()
     ax = fig.add_subplot(111, projection='3d')
     sc=ax.scatter(qfx[:,0], qfx[:,1], qfx[:,2], s=2, color='r')
     sc=ax.scatter(Rfx[:,0], Rfx[:,1], Rfx[:,2], s=2, color='b')
     ax.scatter(0,0,0, s=55, color='g',alpha=0.5)
     ax.quiver([0],[0],[0],*v,color=['g'])
     fig.axes[0].set_title('rotate red points to blue around vector (green)')
     pyplot.show(block=False)
     # fig.savefig(js.examples.imagepath+'/rotationMatrix.jpg')

    .. image:: ../../examples/images/rotationMatrix.jpg
     :align: center
     :height: 300px
     :alt: sq2gr



    """
    normd = np.linalg.norm(vector)
    assert normd != 0, 'vector norm should be >0.'

    d = np.array(vector, dtype=np.float64)
    d = d / normd
    eye = np.eye(3, dtype=np.float64)
    ddt = np.outer(d, d)
    skew = np.array([[0, -d[2], d[1]],
                     [d[2], 0, -d[0]],
                     [-d[1], d[0], 0]], dtype=np.float64)
    mtx = np.cos(angle) * eye + np.sin(angle) * skew + (1 -np.cos(angle)) * ddt
    return mtx


def xyz2rphitheta(XYZ, transpose=False):
    """
    Transformation cartesian coordinates [X,Y,Z] to spherical coordinates [r,phi,theta].

    Parameters
    ----------
    XYZ : array Nx3
        Coordinates with [x,y,z]  ( XYZ.shape[1]==3).
    transpose : bool
        Transpose XYZ before transformation.

    Returns
    -------
    array Nx3
        Coordinates with [r,phi,theta]
         - phi   : float   azimuth     -pi < phi < pi
         - theta : float   polar angle  0 < theta  < pi
         - r     : float   length

    Examples
    --------
    Single coordinates
    ::

     js.formel.xyz2rphitheta([1,0,0])

    Transform Fibonacci lattice on sphere to xyz coordinates
    ::

     rpc=js.formel.randomPointsInCube(10)
     js.formel.xyz2rphitheta(rpc)

    Tranformation 2D X,Y plane coordinates to r,phi coordinates (Z=0)
    ::

     rp=js.formel.xyz2rphitheta([data.X,data.Z,abs(data.X*0)],transpose=True) )[:,:2]

    """
    xyz = np.array(XYZ, ndmin=2)
    if transpose:
        xyz = xyz.T
    assert xyz.shape[1] == 3, 'XYZ second dimension should be 3. Transpose it?'
    rpt = np.empty(xyz.shape)
    rpt[:, 0] = la.norm(xyz, axis=1)
    rpt[:, 1] = np.arctan2(xyz[:, 1], xyz[:, 0])  # arctan2 is special function for this purpose
    rpt[:, 2] = np.arctan2(la.norm(xyz[:, :-1], axis=1), xyz[:, 2])
    return np.array(rpt.squeeze(), ndmin=np.ndim(XYZ))


def rphitheta2xyz(RPT, transpose=False):
    """
    Transformation  spherical coordinates [r,phi,theta]  to cartesian coordinates [x,y,z].

    Parameters
    ----------
    RPT : array Nx3
        Coordinates with [r,phi,theta]
         - r     : float   length
         - phi   : float   azimuth     -pi < phi < pi
         - theta : float   polar angle  0 < theta  < pi
    transpose : bool
        Transpose RPT before transformation.

    Returns
    -------
    array Nx3
        [x,y,z] coordinates

    """
    rpt = np.array(RPT, ndmin=2)
    if transpose:
        rpt = rpt.T
    assert rpt.shape[1] == 3, 'RPT second dimension should be 3. Transpose it?'
    xyz = np.zeros(rpt.shape)
    xyz[:, 0] = rpt[:, 0] * np.cos(rpt[:, 1]) * np.sin(rpt[:, 2])
    xyz[:, 1] = rpt[:, 0] * np.sin(rpt[:, 1]) * np.sin(rpt[:, 2])
    xyz[:, 2] = rpt[:, 0] * np.cos(rpt[:, 2])
    return np.array(xyz.squeeze(), ndmin=np.ndim(RPT))


def qEwaldSphere(q, wavelength=0.15406, typ=None, N=60):
    r"""
    Points on Ewald sphere with different distributions.

    :math:`q = \vec{k_s} -\vec{k_i} =4\pi/\lambda sin(\theta/2)` with
    :math:`\vec{k_i} =[0,0,1]` and :math:`|\vec{k_i}| =2\pi/\lambda`

    Use rotation matrix to rotate to specific orientations.

    Parameters
    ----------
    q : array,list
        Wavevectors units 1/nm
    wavelength : float
        Wavelength of radiation, default X-ray K_a.
    N : integer
        Number of points in intervals.
    typ : 'cart','ring','random' default='ring'
        Typ of q value distribution on Ewald sphere.
         - cart : Cartesian grid between -q_max,q_max with N points (odd to include zero).
         - ring : Given q values with N-points on rings of equal q.
         - random : N² random points on Ewald sphere between q_min and q_max.

    Returns
    -------
        array : 3xN [x,y,z] coordinates


    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     fig = js.mpl.figure(figsize=[8, 2.7],dpi=200)
     ax1 = fig.add_subplot(1, 4, 1, projection='3d')
     ax2 = fig.add_subplot(1, 4, 2, projection='3d')
     ax3 = fig.add_subplot(1, 4, 3, projection='3d')
     ax4 = fig.add_subplot(1, 4, 4, projection='3d')
     q0 = 2 * np.pi / 0.15406  # Ewald sphere radius |kin|

     q = np.r_[0.:2*q0:10j]
     qe = js.formel.qEwaldSphere(q)
     js.mpl.scatter3d(qe[0],qe[1],qe[2],ax=ax1,pointsize=1)
     ax1.set_title('equidistant q')

     q = 2*q0*np.sin(np.r_[0.:np.pi:10j]/2)
     qe = js.formel.qEwaldSphere(q)
     js.mpl.scatter3d(qe[0],qe[1],qe[2],ax=ax2,pointsize=1)
     ax2.set_title('equidistant angle')

     qe = js.formel.qEwaldSphere(q=[10],N=20,typ='cart')
     js.mpl.scatter3d(qe[0],qe[1],qe[2],ax=ax3,pointsize=1)
     ax3.set_title('cartesian grid')

     qe = js.formel.qEwaldSphere(q=[10,0.5*q0],N=60,typ='random')
     fig = js.mpl.scatter3d(qe[0],qe[1],qe[2],ax=ax4,pointsize=1)
     ax4.set_title('random min,max')
     #fig.savefig(js.examples.imagepath+'/qEwaldSphere.jpg')

    .. image:: ../../examples/images/qEwaldSphere.jpg
     :width: 90 %
     :align: center
     :alt: qEwaldSphere

    """
    q = np.array(q)  # scattering vector 4

    # Ewald Sphere radius
    q0 = 2 * np.pi / wavelength

    if typ == 'cart':
        # cartesian grid in x.y
        x = y = np.r_[-q.max():q.max():1j * N]
        xx, yy = np.meshgrid(x, y, indexing='ij')
        qx = xx.flatten()
        qy = yy.flatten()
        qz = (q0 ** 2 - qx ** 2 - qy ** 2) ** 0.5 - q0
        if np.all(np.isfinite(qz)):
            return np.stack([qx.flatten(), qy.flatten(), qz.flatten()])
        else:
            raise ValueError('q.max() range to large for this wavelength.')

    elif typ == 'random':
        mi = 2 * np.arcsin(q.min() / 2/ q0)
        ma = 2 * np.arcsin(q.max() / 2/ q0)
        ringarea = (1 - np.cos(ma))/2 - (1 - np.cos(mi))/2
        # increase number by 1/ringarea
        rps = rphitheta2xyz(randomPointsOnSphere(int(N ** 2 / ringarea), q0)).T - np.r_[0, 0, q0][:, None]
        qrps = la.norm(rps, axis=0)
        return rps[:, (q.min() < qrps) & (qrps < q.max())]

    else:
        # q to angle
        theta = 2 * np.arcsin(q / 2/ q0)
        phi = np.r_[0:np.pi * 2:1j * (N+1)][:-1]
        # q = ks - ki
        # assume ki=[0,0,1], theta is scattering angle, phi azimuth
        qx = q0 * np.sin(theta) * np.cos(phi)[:, None]
        qy = q0 * np.sin(theta) * np.sin(phi)[:, None]
        qz = q0 * (np.cos(theta) - np.ones_like(phi)[:, None])

        return np.stack([qx.flatten(), qy.flatten(), qz.flatten()])


def loglist(mini=0.1, maxi=5, number=100):
    """
    Log like sequence between mini and maxi.

    Parameters
    ----------
    mini,maxi : float, default 0.1, 5
        Start and endpoint.
    number : int, default 100
        Number of points in sequence.

    Returns
    -------
    ndarray

    """
    ll = np.r_[np.log((mini if mini != 0. else 1e-6)):
               np.log((maxi if maxi != 0 else 1.)):
               (number if number != 0 else 10) * 1j]

    return np.exp(ll)


def smooth(data, windowlen=7, window='flat'):
    """
    Smooth data by convolution with window function or fft/ifft.

    Smoothing based on position ignoring information on .X.

    Parameters
    ----------
    data : array, dataArray
        Data to smooth.
        If is dataArray the .Y is smoothed and returned.
    windowlen : int, default = 7
        The length/size of the smoothing window; should be an odd integer.
        Smaller 3 returns unchanged data.
        For 'fourier' the high frequency cutoff is 2*size_data/windowlen.
    window :  'hanning', 'hamming', 'bartlett', 'blackman','gaussian','fourier' default ='flat'
        Type of window/smoothing.
         - 'flat' will produce a moving average smoothing.
         - 'gaussian' normalized Gaussian window with sigma=windowlen/7.
         - 'fourier' cuts high frequencies above cutoff frequency between rfft and irfft.


    Returns
    -------
    array (only the smoothed array)

    Notes
    -----
    'hanning', 'hamming', 'bartlett', 'blackman','gaussian', 'flat' :
     These methods convolve a scaled window function with the signal.
     The signal is prepared by introducing reflected copies of the signal (with the window size)
     at both ends so that transient parts are minimized in the beginning and end part of the output signal.
     Adapted from SciPy/Cookbook.

     See  numpy.hanning, numpy.hamming, numpy.bartlett, numpy.blackman, numpy.convolve, scipy.signal.gaussian

    fourier :
     The real valued signal is mirrored at left side, Fourier transformed, the high frequencies are cut
     and the signal is back transformed.
     This is the simplest form as a hard cutoff frequency is used (ideal low pass filter)
     and may be improved using a specific window function in frequency domain.
     ::

      rft = np.fft.rfft(np.r_[data[::-1],data])
      rft[int(2*len(data)/windowlen):] = 0
      smoothed = np.fft.irfft(rft)

    Examples
    --------
    Usage:
    ::

     import jscatter as js
     import numpy as np
     t=np.r_[-5:5:0.01]
     data=np.sin(t)+np.random.randn(len(t))*0.1
     y=js.formel.smooth(data)  # 1d array
     #
     # smooth dataArray and replace .Y values.
     data2=js.dA(np.vstack([t,data]))
     data2.Y=js.formel.smooth(data2, windowlen=40, window='gaussian')

    Comparison of some filters:
    ::

     import jscatter as js
     import numpy as np
     t=np.r_[-5:5:0.01]
     data=js.dA(np.vstack([t,np.sin(t)+np.random.randn(len(t))*0.1]))
     p=js.grace()
     p.multi(4,2)
     windowlen=31
     for i,window in enumerate(['flat','gaussian','hanning','fourier']):
         p[2*i].plot(data,sy=[1,0.1,6],le='original + noise')
         p[2*i].plot(t,js.formel.smooth(data,windowlen,window),sy=[2,0.1,4],le='filtered')
         p[2*i].plot(t,np.sin(t),li=[1,0.5,1],sy=0,le='noiseless')
         p[2*i+1].plot(data,sy=[1,0.1,6],le='original noise')
         p[2*i+1].plot(t,js.formel.smooth(data,windowlen,window),sy=[2,0.1,4],le=window)
         p[2*i+1].plot(t,np.sin(t),li=[1,2,1],sy=0,le='noiseless')
         p[2*i+1].text(window,x=-2.8,y=-1.2)
         p[2*i+1].xaxis(min=-3,max=-1,)
         p[2*i+1].yaxis(min=-1.5,max=-0.2,ticklabel=[None,None,None,'opposite'])
         p[2*i].yaxis(label='y')
     p[0].legend(x=10,y=4.5)
     p[6].xaxis(label='x')
     p[7].xaxis(label='x')
     p[0].title(f'Comparison of smoothing windows')
     p[0].subtitle(f'with windowlen {windowlen}')
     #p.save(js.examples.imagepath+'/smooth.jpg')


    .. image:: ../../examples/images/smooth.jpg
     :align: center
     :height: 300px
     :alt: smooth


    """
    if hasattr(data, '_isdataArray'):
        data = data.Y

    if window in ['flat', 'hanning', 'hamming', 'bartlett', 'blackman', 'gaussian']:
        windowlen = int(np.ceil(windowlen / 2) * 2)

        if data.size < windowlen:
            raise ValueError("Input vector needs to be bigger than window size.")

        if windowlen < 3:
            return data
        s = np.r_[data[windowlen - 1:0:-1], data, data[-1:-windowlen:-1]]
        if window == 'flat':  # moving average
            w = np.ones(windowlen, 'd')
        elif window == 'gaussian':  # gaussian
            w = scipy.signal.gaussian(windowlen, std=windowlen / 7.)
        else:
            w = eval('np.' + window + '(windowlen)')

        y = np.convolve(w / w.sum(), s, mode='valid')
        res = y[int((windowlen / 2 - 1)):int(-(windowlen / 2))]
        return res
    elif window == 'fourier':
        # real fft; cut high frequencies; inverse fft
        rft = np.fft.rfft(np.r_[data[::-1], data])
        rft[int(2*len(data)/windowlen):] = 0
        smoothed = np.fft.irfft(rft)[data.size:]
        return smoothed
    else:
        raise ValueError("Window is on of 'flat', 'hanning', 'hamming', 'bartlett', 'blackman','gaussian'")


def box(x, edges=None, edgevalue=0, rtol=1e-05, atol=1e-08):
    """
    Box function.

    For equal edges and edge value > 0 the delta function is given.

    Parameters
    ----------
    x : array
    edges :  list of float, float, default=[0]
        Edges of the box.
        If only one number is given  the box goes from [-edge:edge]
    edgevalue : float, default=0
        Value to use if x==edge for both edges.
    rtol,atol : float
        The relative/absolute tolerance parameter for the edge detection.
        See numpy.isclose.

    Returns
    -------
    dataArray

    Notes
    -----
    Edges may be smoothed by convolution with a Gaussian.::

     import jscatter as js
     import numpy as np
     edge=2
     x=np.r_[-4*edge:4*edge:200j]
     f=js.formel.box(x,edges=edge)
     res=js.formel.convolve(f,js.formel.gauss(x,0,0.2))
     #
     p=js.mplot()
     p.Plot(f,li=1,le='box')
     p.Plot(res,li=2,le='smooth box')
     p.Legend()
     #p.savefig(js.examples.imagepath+'/box.jpg')

    .. image:: ../../examples/images/box.jpg
     :align: center
     :height: 300px
     :alt: smooth

    """
    if edges is None:
        edges = [0]
    edges = np.atleast_1d(edges)
    if edges.shape[0] < 2: edges = np.r_[-abs(edges[0]), abs(edges[0])]

    v = np.zeros_like(x)
    v[(x > edges[0]) & (x < edges[1])] = 1
    v[(np.isclose(x, edges[0], rtol, atol)) | (np.isclose(x, edges[1], rtol, atol))] = edgevalue
    box = dA(np.c_[x, v].T)
    box.setColumnIndex(iey=None)
    box.modelname = inspect.currentframe().f_code.co_name
    return box


def gauss(x, mean=1, sigma=1):
    r"""
    Normalized Gaussian function.

    .. math:: g(x)= \frac{1}{sigma\sqrt{2\pi}} e^{-0.5(\frac{x-mean}{sigma})^2}


    Parameters
    ----------
    x : float
        Values
    mean : float
        Mean value
    sigma : float
        1/e width.
        Negative values result in negative amplitude.

    Returns
    -------
    dataArray

    """
    x = np.atleast_1d(x)
    result = dA(np.c_[x, np.exp(-0.5 * (x - mean) ** 2 / sigma ** 2) / sigma / np.sqrt(2 * np.pi)].T)
    result.setColumnIndex(iey=None)
    result.mean = mean
    result.sigma = sigma
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def lorentz(x, mean=1, gamma=1):
    r"""
    Normalized Lorentz function

    .. math :: f(x) = \frac{gamma}{\pi((x-mean)^2+gamma^2)}

    Parameters
    ----------
    x : array
        X values
    gamma : float
        Half width half maximum
    mean : float
        Mean value

    Returns
    -------
    dataArray

    """
    x = np.atleast_1d(x)
    result = dA(np.c_[x, gamma / ((x - mean) ** 2 + gamma ** 2) / np.pi].T)
    result.setColumnIndex(iey=None)
    result.mean = mean
    result.gamma = gamma
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def _schulz(r, m, z):
    # not used anymore
    z1 = z + 1
    if np.all(z < 150):
        f = z1 ** z1 * (r / m) ** z / m / special.gamma(z1) * np.exp(-z1 * r / m)
    else:
        # using Stirling equation and exp(log(....))
        # f = (r / m) ** z / m / (2 * np.pi) ** 0.5 * z1 ** 0.5 * np.exp(z1 * (1 - r / m))
        f = np.exp(z * np.log(r / m) + z1 * (1 - r / m)) / m / (2 * np.pi) ** 0.5 * z1 ** 0.5

    return f


def schulzDistribution(r, mean, sigma):
    r"""
    Schulz (or Gamma) distribution for polymeric particles/chains.

    Distribution describing a polymerisation like radical polymerization:
     - constant number of chains growth till termination.
     - concentration of active centers constant.
     - start of chain growth not necessarily at the same time.
     - In polymer physics sometimes called Schulz-Zimm distribution. Same as Gamma distribution.

    Parameters
    ----------
    r : array
        Distribution variable such as relative molecular mass or degree of polymerization, number of monomers.
    mean : float
        Mean :math:`<r>`
    sigma : float
        Width as standard deviation :math:`s=\sqrt{<r^2>-<r>^2}` of the distribution.
        :math:`z = (<r>/s)^2 -1 < 600`

    Returns
    -------
    dataArray : Columns [x,p]
        - .z ==> z+1 = k is degree of coupling =  number of chain combined to dead chain in termination reaction
           z = (<r>/s)² -1

    Notes
    -----
    The Schulz distribution [1]_

    .. math:: h(r) = \frac{(z+1)^{z+1}r^z}{(mean^{z+1}\Gamma(z+1)}e^{-(z+1)\frac{r}{mean}}

    alternatively with :math:`a=<r>^2/s^2` and :math:`b=a/<r>`

    .. math:: h(r) = \frac{b^a r^(a-1)}{(\Gamma(a)}e^{-br}

    Normalized to :math:`\int h(r)dr=1`.



    Nth order average :math:`<r>^n = \frac{z+n}{z+1} <r>`
     - number average  :math:`<r>^1 =  <r>`
     - weight average  :math:`<r>^2 = \frac{z+2}{z+1} <r>`
     - z average       :math:`<r>^3 = \frac{z+3}{z+1} <r>`

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     N=np.r_[1:200]
     p=js.grace(1.4,1)
     p.multi(1,2)
     m=50
     for i,s in enumerate([10,20,40,50,75,100,150],1):
         SZ = js.formel.schulzDistribution(N,mean=m,sigma=s)
         p[0].plot(SZ.X/m,SZ.Y,sy=0,li=[1,3,i],le=f'sigma/mean={s/m:.1f}')
         p[1].plot(SZ.X/m,SZ.Y*SZ.X,sy=0,li=[1,3,i],le=f'sigma/mean={s/m:.1f}')
     p[0].xaxis(label='N/mean')
     p[0].yaxis(label='h(N)')
     p[0].subtitle('number distribution')
     p[1].xaxis(label='N/mean')
     p[1].yaxis(label='N h(N)')
     p[1].subtitle('mass distribution')
     p[1].legend(x=2,y=1.5)
     p[0].title('Schulz distribution')
     #p.save(js.examples.imagepath+'/schulzZimm.jpg')

    .. image:: ../../examples/images/schulzZimm.jpg
     :align: center
     :height: 300px
     :alt: schulzZimm

    References
    ----------
    .. [1]  Schulz, G. V. Z. Phys. Chem. 1939, 43, 25
    .. [2]  Theory of dynamic light scattering from polydisperse systems
            S. R. Aragón and R. Pecora
            The Journal of Chemical Physics, 64, 2395  (1976)

    """
    z = (mean / sigma) ** 2 - 1
    a=mean ** 2 / sigma ** 2
    scale=sigma ** 2 / mean
    result = dA(np.c_[r,  stats.gamma.pdf(r, a=a, scale=scale)].T)
    result.setColumnIndex(iey=None)
    result.columnname = 'x; p'
    result.mean = mean
    result.sigma = sigma
    result.z = z
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def lognorm(x, mean=1, sigma=1):
    r"""
    Lognormal distribution function.

    .. math:: f(x>0)= \frac{1}{\sqrt{2\pi}\sigma x }\,e^{ -\frac{(\ln(x)-\mu)^2}{2\sigma^2}}

    Parameters
    ----------
    x : array
        x values
    mean : float
        mean
    sigma : float
        sigma

    Returns
    -------
    dataArray

    """
    mu = math.log(mean ** 2 / (sigma + mean ** 2) ** 0.5)
    nu = (math.log(sigma / mean ** 2 + 1)) ** 0.5
    distrib = stats.lognorm(s=nu, scale=math.exp(mu))
    result = dA(np.c_[x, distrib.pdf(x)].T)
    result.setColumnIndex(iey=None)
    result.mean = mean
    result.sigma = sigma
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def voigt(x, center=0, fwhm=1, lg=1, asym=0, amplitude=1):
    r"""
    Voigt function for peak analysis (normalized).

    The Voigt function is a convolution of gaussian and lorenzian shape peaks for peak analysis.
    The Lorenzian shows a stronger contribution outside FWHM with a sharper peak.
    Asymmetry of the shape can be added by a sigmoidal change of the FWHM [2]_.

    Parameters
    ----------
    x : array
        Axis values.
    center : float
        Center of the distribution.
    fwhm : float
        Full width half maximum of the Voigt function.
    lg : float, default = 1
        Lorenzian/gaussian fraction of both FWHM, describes the contributions of gaussian and lorenzian shape.
         - lorenzian/gaussian >> 1  lorenzian,
         - lorenzian/gaussian ~  1  central part gaussian, outside lorenzian wings
         - lorenzian/gaussian << 1. gaussian
    asym : float, default=0
        Asymmetry factor in sigmoidal as :math:`fwhm_{asym} = 2*fwhm/(1+np.exp(asym*(x-center)))` .
        For a=0 the Voigt is symmetric.
    amplitude : float, default = 1
        amplitude

    Returns
    -------
    dataArray
         .center
         .sigma
         .gamma
         .fwhm
         .asymmetry
         .lorenzianOverGaussian (lg)

    Notes
    -----
    The Voigt function is a convolution of Gaussian and Lorentz functions

    .. math:: G(x;\sigma) = e^{-x^2/(2\sigma^2)}/(\sigma \sqrt{2\pi})\ and \
              L(x;\gamma) = \gamma/(\pi(x^2+\gamma^2))

    resulting in

    .. math:: V(x;\sigma,\gamma)=\frac{\operatorname{Re}[w(z)]}{\sigma\sqrt{2 \pi}}

    with :math:`z=(x+i\gamma)/(\sigma\sqrt{2})` and :math:`Re[w(z)]` is the real part of the Faddeeva function.

    :math:`\gamma` is the Lorentz fwhm width and :math:`fwhm=(2\sqrt{2\ln 2})\sigma` the Gaussian fwhm width.

    The FWHM in Lorentz and Gaussian dependent on the fwhm of the Voigt function is
    :math:`fwhm_{Gauss,Lorentz} \approx fwhm / (0.5346 lg + (0.2166 lg^2 + 1)^{1/2})` (accuracy 0.02%).


    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Voigt_profile
    .. [2] A simple asymmetric lineshape for fitting infrared absorption spectra
           Aaron L. Stancik, Eric B. Brauns
           Vibrational Spectroscopy 47 (2008) 66–69
    .. [3] Empirical fits to the Voigt line width: A brief review
           Olivero, J. J.; R. L. Longbothum
           Journal of Quantitative Spectroscopy and Radiative Transfer. 17, 233–236. doi:10.1016/0022-4073(77)90161-3

    """
    ln2 = math.log(2)
    # calc the fwhm in gauss and lorenz to get the final FWHM in the Voigt function with an accuracy of 0.02%
    # as given in Olivero, J. J.; R. L. Longbothum (February 1977).
    # Empirical fits to the Voigt line width: A brief review".
    # Journal of Quantitative Spectroscopy and Radiative Transfer. 17 (2): 233–236.
    # doi:10.1016/0022-4073(77)90161-3
    FWHM = fwhm / (0.5346 * lg + (0.2166 * lg ** 2 + 1) ** 0.5)

    def z(fwhm):
        return ((x - center) + 1j * lg * fwhm / 2.) / math.sqrt(2) / (fwhm / (2 * np.sqrt(2 * ln2)))

    # the sigmoidal fwhm for asymmetry
    def afwhm(fwhm, a):
        return 2 * fwhm / (1 + np.exp(a * (x - center)))

    # calc values with asymmetric FWHM
    val = amplitude / (afwhm(FWHM, asym) / (2 * np.sqrt(2 * ln2))) / math.sqrt(2 * np.pi) * \
          special.wofz(z(afwhm(FWHM, asym))).real

    result = dA(np.c_[x, val].T)
    result.setColumnIndex(iey=None)
    result.center = center
    result.sigma = (FWHM / (2 * np.sqrt(2 * ln2)))
    result.gamma = FWHM / 2.
    result.fwhm = fwhm
    result.asymmetry = asym
    result.lorenzianOverGaussian = lg
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def Ea(z, a, b=1):
    r"""
    Mittag-Leffler function for real z and real a,b with 0<a, b<0.

    Evaluation of the Mittag-Leffler (ML) function with 1 or 2 parameters by means of the OPC algorithm [1].
    The routine evaluates an approximation Et of the ML function E such that
    :math:`|E-Et|/(1+|E|) \approx 10^{-15}`

    Parameters
    ----------
    z : real array
        Values
    a : float, real positive
        Parameter alpha
    b : float, real positive, default=1
        Parameter beta

    Returns
    -------
    array

    Notes
    -----
     - Mittag Leffler function defined as

       .. math:: E(x,a,b)=\sum_{k=0}^{\inf} \frac{z^k}{\Gamma(b+ak)}

     - The code uses code from K.Hinsen at https://github.com/khinsen/mittag-leffler
       which is a Python port of
       `Matlab implementation <https://se.mathworks.com/matlabcentral/fileexchange/48154-the-mittag-leffler-function>`_
       of the generalized Mittag-Leffler function as described in [1]_.

     - The function cannot be simply calculated by using the above summation.
       This fails for a,b<0.7 because of various numerical problems.
       The above implementation of K.Hinsen is the best availible approximation in Python.

    Examples
    --------
    ::

     import numpy as np
     import jscatter as js
     from scipy import special
     x=np.r_[-10:10:0.1]
     # tests
     np.all(js.formel.Ea(x,1,1)-np.exp(x)<1e-10)
     z = np.linspace(0., 2., 50)
     np.allclose(js.formel.Ea(np.sqrt(z), 0.5), np.exp(z)*special.erfc(-np.sqrt(z)))
     z = np.linspace(-2., 2., 50)
     np.allclose(js.formel.Ea(z**2, 2.), np.cosh(z))


    References
    ----------
    .. [1] R. Garrappa, Numerical evaluation of two and three parameter Mittag-Leffler functions,
           SIAM Journal of Numerical Analysis, 2015, 53(3), 1350-1369

    """
    if a <= 0 or b <= 0:
        raise ValueError('a and b must be real and positive.')

    g = 1  # only use gamma=1
    log_epsilon = np.log(1.e-15)

    # definition through Laplace transform inversion
    # we use for this the code from K.Hinsen, see header in ml_internal
    _eaLPI = lambda z: np.vectorize(ml_internal.LTInversion, [np.float64])(1, z, a, b, g, log_epsilon)

    res = np.zeros_like(z, dtype=np.float64)
    eps = 1.e-15
    choose = np.abs(z) <= eps
    res[choose] = 1 / special.gamma(b)
    res[~choose] = _eaLPI(z[~choose])
    return res


def boseDistribution(w, temp):
    r"""
    Bose distribution for integer spin particles in non-condensed state (hw>0).

    .. math::

        n(w) &= \frac{1}{e^{hw/kT}-1} &\ hw>0

             &= 0                     &\: hw=0 \: This is not real just for convenience!

    Parameters
    ----------
    w : array
        Frequencies in units 1/ns
    temp : float
        Temperature in K

    Returns
    -------
    dataArray



    """
    h = constants.h
    k = constants.k
    bose = np.piecewise(w, [w == 0], [0, 1 / (np.exp(h * w[w != 0] * 1e9 / (k * temp)) - 1)])
    result = dA(np.c_[w, bose].T)
    result.setColumnIndex(iey=None)
    result.columnname = 'w; n'
    result.temperature = temp
    result.modelname = inspect.currentframe().f_code.co_name
    return result


########################################################################
# quadrature

class AccuracyWarning(Warning):
    pass


def _cached_roots_legendre(n):
    """
    Cache roots_legendre results to speed up calls of the fixed_quad function.
    """
    # scipy.integrate.quadrature
    if n in _cached_roots_legendre.cache:
        return _cached_roots_legendre.cache[n]

    _cached_roots_legendre.cache[n] = roots_legendre(n)
    return _cached_roots_legendre.cache[n]


_cached_roots_legendre.cache = dict()


# noinspection PyIncorrectDocstring
def parQuadratureFixedGauss(func, lowlimit, uplimit, parname, n=25, weights=None, **kwargs):
    """
    Vectorized definite integral using fixed-order Gaussian quadrature. Shortcut pQFG.

    Integrate func over parname from a to b using Gauss-Legendre quadrature [1]_ of order `n`.
    All columns are integrated.
    For func return values as dataArray the .X is recovered (unscaled) while for array
    also the X are integrated and weighted.

    Parameters
    ----------
    func : callable
        A Python function or method  returning a vector array of dimension 1.
        If func returns dataArray .Y is integrated.
    lowlimit : float
        Lower limit of integration.
    uplimit : float
        Upper limit of integration.
    parname : string
        Name of the integration variable which should be a scalar.
        After evaluation the corresponding attribute has the mean value with weights.
    weights : ndarray shape(2,N),default=None
        - Weights for integration along parname with a<weights[0]<b and weights[1] contains weight values.
        - Missing values are linear interpolated (faster). If None equal weights are used.
    kwargs : dict, optional
        Extra keyword arguments to pass to function, if any.
    n : int, optional
        Order of quadrature integration. Default is 15.
    ncpu : int,default=1, optional
        Use parallel processing for the function with ncpu parallel processes in the pool.
        Set this to 1 if the function is already fast enough or if the integrated function uses multiprocessing.
         - 0   -> all cpus are used
         - int>0      min (ncpu, mp.cpu_count)
         - int<0      ncpu not to use

    Returns
    -------
    array or dataArray


    Examples
    --------
    A simple polydispersity: integrate size distribution of equal weight. Normalisation by 4sig.

    We see that Rg and I0 at low Q also change because of polydispersity. Minima are smeared out.
    ::

     import jscatter as js
     q=js.loglist(0.01,5,500)
     p=js.grace()
     mean=5
     for sig in [0.01,0.1,0.3,0.4]:  # distribution width
         sp2=js.formel.pQFG(js.ff.sphere,mean-2*sig,mean+2*sig,'radius',q=q,radius=mean,n=200)
         p.plot(sp2.X, sp2.Y/(4*sig),sy=[-1,0.2,-1])
     p.yaxis(scale='l')

    Integrate Gaussian as test case.
    As we integrate over .X the final .X will be the first integration point .X, here the first Legendre knot.
    ::

     import jscatter as js
     import numpy as np
     import scipy
     # testcase: integrate over x of a function
     # area under normalized gaussian is 1
     js.formel.pQFG(js.formel.gauss,-10,10,'x',mean=0,sigma=1)

    Notes
    -----
    Reimplementation of scipy.integrate.quadrature.fixed_quad
    to work with vector output of the integrand function and weights.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Gaussian_quadrature

    """
    x, w = _cached_roots_legendre(n)
    x = np.real(x)
    if np.isinf(lowlimit) or np.isinf(uplimit):
        raise ValueError("Gaussian quadrature is only available for finite limits.")
    y = (uplimit - lowlimit) * (x + 1) / 2.0 + lowlimit
    if weights is not None:
        wy = np.interp(y, weights[0], weights[1])
        normfactor = np.trapz(weights[1], weights[0])
        parmean = np.trapz(weights[1] * weights[0], weights[0]) / normfactor
    else:
        wy = np.ones_like(y)
        normfactor = uplimit - lowlimit
        parmean = (uplimit + lowlimit) / 2
    # set default for ncpu to use only one process.
    if 'ncpu' not in kwargs:
        kwargs.update({'ncpu': 1, 'output': False})
    # calc the function values
    res = parallel.doForList(func, looplist=y, loopover=parname, **kwargs)
    # res = [func(**dict(kwargs, **{parname: yy})) for yy in y] # single cpu
    if isinstance(res[0], dA):
        res[0][:, :] = (uplimit - lowlimit) / 2.0 * np.sum(w * wy * np.atleast_2d(res).T, axis=-1).T
        res[0].X = res[1].X  # retrieve unweighted X values
        res[0].weightNormFactor = normfactor
        setattr(res[0], parname, parmean)
        return res[0]
    else:
        return (uplimit - lowlimit) / 2.0 * np.sum(w * wy * np.atleast_2d(res).T, axis=-1).T


pQFG = parQuadratureFixedGauss


def parQuadratureFixedGaussxD(func, lowlimit, uplimit, parnames, n=5,
                              weights0=None, weights1=None, weights2=None, **kwargs):
    r"""
    Vectorized fixed-order Gauss-Legendre quadrature in definite interval in 1,2,3 dimensions. Shortcut pQFGxD.

    Integrate func over parnames between limits using Gauss-Legendre quadrature [1]_ of order `n`.

    Parameters
    ----------
    func : callable
        Function to integrate.
        The return value should be 2 dimensional array with first dimension along integration variable
        and second along array to calculate. See examples.
    parnames : list of string, max len=3
        Name of the integration variables which should be scalar in the function.
    lowlimit : list of float
        Lower limits a of integration for parnames.
    uplimit : list of float
        Upper limits b of integration for parnames.
    weights0,weights1,weights3 : ndarray shape(2,N), default=None
        - Weights for integration along parname with a<weightsi[0]<b and weightsi[1] contains weight values.
        - Missing values are linear interpolated (faster).
        - None: equal weights are used.
    kwargs : dict, optional
        Extra keyword arguments to pass to function, if any.
    n : int, optional
        Order of quadrature integration for all parnames. Default is 5.


    Returns
    -------
    array

    Notes
    -----
    - To get a speedy integration the function should use numpy ufunctions which operate on numpy arrays with
      compiled code.

    Examples
    --------
    The following integrals in 1-3 dimensions over a normalised Gaussian give always 1
    which achieved with reasonable accuracy with n=15.

    The examples show different ways to return 2dim arrays with x,y,z in first dimension and vector q in second.
    `x[:,None]` adds a second dimension to array x.

    ::

     import jscatter as js
     import numpy as np
     q=np.r_[0.1:5.1:0.1]
     def gauss(x,mean,sigma):
        return np.exp(-0.5 * (x - mean) ** 2 / sigma ** 2) / sigma / np.sqrt(2 * np.pi)

     # 1dimensional
     def gauss1(q,x,mean=0,sigma=1):
         g=np.exp(-0.5 * (x[:,None] - mean) ** 2 / sigma ** 2) / sigma / np.sqrt(2 * np.pi)
         return g*q
     js.formel.pQFGxD(gauss1,0,100,parnames='x',mean=50,sigma=10,q=q,n=15)

     # 2 dimensional
     def gauss2(q,x,y=0,mean=0,sigma=1):
         g=gauss(x[:,None],mean,sigma)*gauss(y[:,None],mean,sigma)
         return g*q
     js.formel.pQFGxD(gauss2,[0,0],[100,100],parnames=['x','y'],mean=50,sigma=10,q=q,n=15)

     # 3 dimensional
     def gauss3(q,x,y=0,z=0,mean=0,sigma=1):
         g=gauss(x,mean,sigma)*gauss(y,mean,sigma)*gauss(z,mean,sigma)
         return g[:,None]*q
     js.formel.pQFGxD(gauss3,[0,0,0],[100,100,100],parnames=['x','y','z'],mean=50,sigma=10,q=q,n=15)


    Usage of weights allows weights for dimensions e.g. to realise a spherical average with weight
    :math:`sin(\theta)d\theta` in the integral
    :math:`P(q) = \int_0^{2\pi}\int_0^{\pi} f(q,\theta,\phi) sin(\theta) d\theta d\phi`.
    (Using the weight in the function is more accurate.)
    The weight needs to be normalised by unit sphere area :math:`4\pi`.
    ::

     import jscatter as js
     import numpy as np
     q=np.r_[0,0.1:5.1:0.1]
     def cuboid(q, phi, theta, a, b, c):
         pi2 = np.pi * 2
         fa = (np.sinc(q * a * np.sin(theta[:,None]) * np.cos(phi[:,None]) / pi2) *
               np.sinc(q * b * np.sin(theta[:,None]) * np.sin(phi[:,None]) / pi2) *
               np.sinc(q * c * np.cos(theta[:,None]) / pi2))
         return fa**2*(a*b*c)**2

     # generate weight for sin(theta) dtheta integration (better to integrate in cuboid function)
     # and normalise for unit sphere
     t = np.r_[0:np.pi:180j]
     wt = np.c_[t,np.sin(t)/np.pi/4].T

     Fq=js.formel.pQFGxD(cuboid,[0,0],[2*np.pi,np.pi],parnames=['phi','theta'],weights1=wt,q=q,n=15,a=1.9,b=2,c=2)

     # compare the result to the ff solution (which does the same with weights in the function).
     p=js.grace()
     p.plot(q,Fq)
     p.plot(js.ff.cuboid(q,1.9,2,2),li=1,sy=0)
     p.yaxis(scale='l')

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Gaussian_quadrature

    """
    v, w = _cached_roots_legendre(n)  # value and weights
    normfactor = []
    parmean = []

    if isinstance(parnames, str): parnames = [parnames]
    if isinstance(lowlimit, numbers.Number): lowlimit = [lowlimit]
    if isinstance(uplimit, numbers.Number): uplimit = [uplimit]
    if len(parnames) == 0 or len(parnames) > 3:
        raise AttributeError('Missing parnames or to many.')

    if len(parnames) > 0:
        if np.isinf(lowlimit[0]) or np.isinf(uplimit[0]):
            raise ValueError("Gaussian quadrature is only available for finite limits.")
        vol = (uplimit[0] - lowlimit[0]) / 2
        x = (uplimit[0] - lowlimit[0]) * (v + 1) / 2.0 + lowlimit[0]
        points = [[xx] for xx in x]
        if weights0 is not None:
            wx = np.interp(x, weights0[0], weights0[1])
            normfactor.append(np.trapz(weights0[1], weights0[0]))
            parmean.append(np.trapz(weights0[1] * weights0[0], weights0[0]) / normfactor[-1])
        else:
            wx = np.ones_like(x)
            normfactor.append(uplimit[0] - lowlimit[0])
            parmean.append((uplimit[0] + lowlimit[0]) / 2)
        weights = [w0[0]*w0[1] for w0 in zip(w, wx)]

    if len(parnames) > 1:
        vol = vol * (uplimit[1] - lowlimit[1]) / 2
        y = (uplimit[1] - lowlimit[1]) * (v + 1) / 2.0 + lowlimit[1]
        points = [[xx, yy] for xx in x for yy in y]
        if weights1 is not None:
            wy = np.interp(y, weights1[0], weights1[1])
            normfactor.append(np.trapz(weights1[1], weights1[0]))
            parmean.append(np.trapz(weights1[1] * weights1[0], weights1[0]) / normfactor[-1])
        else:
            wy = np.ones_like(y)
            normfactor.append( uplimit[1] - lowlimit[1])
            parmean.append( (uplimit[1] + lowlimit[1]) / 2)
        weights = [w0[0]*w0[1]*w1[0]*w1[1] for w0 in zip(w, wx) for w1 in zip(w, wy)]

    if len(parnames) > 2:
        vol = vol * (uplimit[2] - lowlimit[2]) / 2
        z = (uplimit[2] - lowlimit[2]) * (v + 1) / 2.0 + lowlimit[2]
        points = [[xx, yy, zz] for xx in x for yy in y for zz in z]
        if weights2 is not None:
            wz = np.interp(z, weights2[0], weights2[1])
            normfactor.append(np.trapz(weights2[1], weights2[0]))
            parmean.append(np.trapz(weights2[1] * weights2[0], weights2[0]) / normfactor[-1])
        else:
            wz = np.ones_like(z)
            normfactor.append(uplimit[2] - lowlimit[2])
            parmean.append((uplimit[2] + lowlimit[2]) / 2)
        weights = [w0[0]*w0[1]*w1[0]*w1[1]*w2[0]*w2[1] for w0 in zip(w, wx) for w1 in zip(w, wy) for w2 in zip(w, wz)]

    # calc values for all points
    res = func(**dict(kwargs, **dict(zip(parnames, np.array(points).T))))

    # do the integration by summing with weights
    return vol * np.sum(weights * np.atleast_2d(res).T, axis=-1)


pQFGxD = parQuadratureFixedGaussxD


# noinspection PyIncorrectDocstring
def parQuadratureAdaptiveGauss(func, lowlimit, uplimit, parname, weights=None, tol=1.e-8, rtol=1.e-8, maxiter=150,
                               miniter=8, **kwargs):
    """
    Vectorized definite integral using fixed-tolerance Gaussian quadrature. Shortcut pQAG.

    parQuadratureAdaptiveClenshawCurtis is more efficient.
    Adaptive integration of func from `a` to `b` using Gaussian quadrature adaptivly increasing number of points by 8.
    All columns are integrated. For func return values as dataArray the .X is recovered (unscaled) while for array
    also the X are integrated and weighted.

    Parameters
    ----------
    func : function
        A function or method to integrate returning an array or dataArray.
    lowlimit : float
        Lower limit of integration.
    uplimit : float
        Upper limit of integration.
    parname : string
        name of the integration variable which should be a scalar.
    weights : ndarray shape(2,N),default=None
        - Weights for integration along parname as a Gaussian with a<weights[0]<b and weights[1] contains weight values.
        - Missing values are linear interpolated (faster). If None equal weights are used.
    kwargs : dict, optional
        Extra keyword arguments to pass to function, if any.
    tol, rtol : float, optional
        Iteration stops when error between last two iterates is less than
        `tol` OR the relative change is less than `rtol`.
    maxiter : int, default 150, optional
        Maximum order of Gaussian quadrature.
    miniter : int, default 8, optional
        Minimum order of Gaussian quadrature.
    ncpu : int, default=1, optional
        Number of cpus in the pool.
        Set this to 1 if the integrated function uses multiprocessing to avoid errors.
         - 0   -> all cpus are used
         - int>0      min (ncpu, mp.cpu_count)
         - int<0      ncpu not to use

    Returns
    -------
    val : float
        Gaussian quadrature approximation (within tolerance) to integral for all vector elements.
    err : float
        Difference between last two estimates of the integral.

    Examples
    --------
    A simple polydispersity: integrate size distribution of equal weight. Normalisation by 4sig.

    We see that Rg and I0 at low Q also change because of polydispersity. Minima are smeared out.
    ::

     import jscatter as js
     q=js.loglist(0.01,5,500)
     p=js.grace()
     mean=5
     for sig in [0.01,0.1,0.3,0.4]:  # distribution width
         sp2=js.formel.pQAG(js.ff.sphere,mean-2*sig,mean+2*sig,'radius',q=q,radius=mean)
         p.plot(sp2.X, sp2.Y/(4*sig),sy=[-1,0.2,-1])
     p.yaxis(scale='l')

    Integrate Gaussian as test case.
    As we integrate over .X the final .X will be the first integration point .X, here the first Legendre knot.
    ::

     t=np.r_[1:100]
     gg=js.formel.gauss(t,50,10)
     js.formel.pQAG(js.formel.gauss,0,100,'x',mean=50,sigma=10)

    Notes
    -----
    Reimplementation of scipy.integrate.quadrature.quadrature to work with vector output of the integrand function.

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Gaussian_quadrature


    """
    val = np.inf
    err = np.inf
    maxiter = max(miniter + 1, maxiter)
    for n in np.arange(maxiter, miniter, -8)[::-1]:
        result = parQuadratureFixedGauss(func, lowlimit, uplimit, parname, n, weights, **kwargs)
        if isinstance(result, dA):
            newval = result.Y
        else:
            newval = result
        err = abs(newval - val)
        val = newval
        if np.all(err < tol) or np.all(err < rtol * abs(val)):
            break
    else:
        warnings.warn("maxiter (%d) exceeded in %s. Latest maximum abs. error %e and rel error = %e"
                      % (maxiter, _getFuncCode(func).co_name, err.flatten().max(), np.max(abs(err) / abs(val))),
                      AccuracyWarning)
    if isinstance(result, dA):
        result.IntegralErr_funktEval = err, n
    return result


pQAG = parQuadratureAdaptiveGauss


def _wrappedIntegrand(xarray, *args, **kwargs):
    func = kwargs.pop('func')
    parnames = kwargs.pop('parnames')
    test = kwargs.pop('_test_', False)
    kwargs.update({key: xarray[:, i] for i, key in enumerate(parnames)})

    result = func(*args, **kwargs)

    if test:
        return np.iscomplexobj(result), result.shape

    if np.iscomplexobj(result):
        # split complex to 2xfloat
        res = np.zeros((result.shape[0], 2*result.shape[1]))   # prepare for consecutive real,img parts in second dim
        # redistribute
        res[:, ::2] = result.real  # res2r[::2, :]
        res[:, 1::2] = result.imag  # res2r[1::2, :]
        return res
    else:
        return result


def parAdaptiveCubature(func, lowlimit, uplimit, parnames, fdim=None, adaptive='p',
                        abserr=1e-8, relerr=1e-3, *args, **kwargs):
    r"""
    Vectorized adaptive multidimensional integration (cubature). Shortcut pAC.

    We use the cubature module written by SG Johnson [2]_ for *h-adaptive* (recursively partitioning the
    integration domain into smaller subdomains) and *p-adaptive* (Clenshaw-Curtis quadrature,
    repeatedly doubling the degree of the quadrature rules).
    This function is a wrapper around the package cubature which can be used also directly.

    Parameters
    ----------
    func : function
        The function to integrate.
        The return array needs to be an 2-dim  array with the last dimension as vectorized return (=len(fdim))
        and first along the points of the *parnames* parameters to integrate.
        Use numpy functions for array functions to speedup computations. See example.
    parnames : list of string
        Parameter names of variables to integrate. Should be scalar.
    lowlimit : list of float
        Lower limits of the integration variables with same length as parnames.
    uplimit: list of float
        Upper limits of the integration variables with same length as parnames.
    fdim : int, None, optional
        Second dimension size of the func return array.
        If None, the function is evaluated with the uplimit values to determine the size.
        For complex valued function it is twice the complex array length.
    adaptive : 'h', 'p', default='p'
        Type of adaption algorithm.
         - 'h' Multidimensional h-adaptive integration by subdividing the integration interval into smaller intervals
            where the same rule is applied.
            The value and error in each interval is calculated from 7-point rule and difference to 5-point rule.
            For higher dimensions only the worst dimension is subdivided [3]_.
            This algorithm is best suited for a moderate number of dimensions (say, < 7), and is superseded for
            high-dimensional integrals by other methods (e.g. Monte Carlo variants or sparse grids).
         - 'p' Multidimensional p-adaptive integration by increasing the degree of the quadrature rule according to
            Clenshaw-Curtis quadrature
            (in each iteration the number of points is doubled and the previous values are reused).
            Clenshaw-Curtis has similar error compared to Gaussian quadrature even if the used error estimate is worse.
            This algorithm is often superior to h-adaptive integration for smooth integrands in a few (≤ 3) dimensions,
    abserr, relerr : float default = 1e-8, 1e-3
        Absolute and relative error to stop.
        The integration will terminate when either the relative OR the absolute error tolerances are met.
        abserr=0, which means that it is ignored.
        The real error is much smaller than this stop criterion.
    maxEval : int, default 0, optional
        Maximum number of function evaluations. 0 is infinite.
    norm : int, default=None, optional
        Norm to evaluate the error.
         - None: 0,1 automatically choosen for real or complex functions.
         - 0: individual for each integrand (real valued functions)
         - 1: paired error (L2 distance) for complex values as distance in complex plane.
         - Other values as mentioned in cubature documentation.
    args,kwargs : optional
        Additional arguments and keyword arguments passed to func.

    Returns
    -------
        arrays values , error

    Examples
    --------
    Integration of the sphere to get the sphere formfactor.
    In the first example the symmetry is used to return real valued amplitude.
    In the second the complex amplitude is used.
    Both can be compared to the analytic formfactor. Errors are much smaller than the abserr/relerr stop criterion.
    The stop seems to be related to the minimal point at q=2.8 as critical point.
    h-adaptive is for dim=3 less accurate and slower than p-adaptive.

    The integrands contain patterns of scheme ``q[:,None]*theta``
    (with later .T to transpose, alternative ``q*theta[:,None]``)
    to result in a 2-dim array with the last dimension as vectorized return.
    The first dimension goes along the points to evaluate as determined from the algorithm.
    ::

     import jscatter as js
     import numpy as np
     R=5
     q = np.r_[0.01:3:0.02]

     def sphere_real(r, theta, phi, b, q):
         res = b*np.cos(q[:,None]*r*np.cos(theta))*r**2*np.sin(theta)*2
         return res.T

     pn = ['r','theta','phi']
     fa_r,err = js.formel.pAC(sphere_real, [0,0,0], [R,np.pi/2,np.pi*2], pn, b=1, q=q)
     fa_rh,errh = js.formel.pAC(sphere_real, [0,0,0], [R,np.pi/2,np.pi*2], pn, b=1, q=q,adaptive='h')

     # As complex function
     def sphere_complex(r, theta, phi, b, q):
         fac = b * np.exp(1j * q[:, None] * r * np.cos(theta)) * r ** 2 * np.sin(theta)
         return fac.T

     fa_c, err = js.formel.pAC(sphere_complex, [0, 0, 0], [R, np.pi, np.pi * 2], pn, b=1, q=q)

     sp = js.ff.sphere(q, R)
     p = js.grace()
     p.multi(2,1,vgap=0)

     # integrals
     p[0].plot(q, fa_r ** 2, le='real integrand p-adaptive')
     p[0].plot(q, fa_rh ** 2, le='real integrand h-adaptive')
     p[0].plot(q, np.real(fa_c * np.conj(fa_c)),sy=[8,0.5,3], le='complex integrand')
     p[0].plot(q, sp.Y, li=1, sy=0, le='analytic')

     # errors
     p[1].plot(q,np.abs(fa_r**2 -sp.Y), le='real integrand')
     p[1].plot(q,np.abs(fa_rh**2 -sp.Y), le='real integrand h-adaptive')
     p[1].plot(q,np.abs(np.real(fa_c * np.conj(fa_c)) -sp.Y),sy=[8,0.5,3],le='complex p-adaptive')

     p[0].yaxis(scale='l',label='F(q)',ticklabel=['power',0])
     p[0].xaxis(ticklabel=0)
     p[0].legend(x=2,y=1e6)
     p[1].legend(x=2.1,y=5e-9,charsize=0.8)
     p[1].yaxis(scale='l',label=r'error', ticklabel=['power',0],min=1e-13,max=5e-6)
     p[1].xaxis(label=r'q / nm\S-1')
     p[1].text(r'error = abs(F(Q) - F(q)\sanalytic\N)',x=0.8,y=1e-9,charsize=1)
     p[0].title('Numerical quadrature sphere formfactor ')
     p[0].subtitle('stop criterion relerror=1e-3, real errors are smaller')
     #p.save(js.examples.imagepath+'/cubature.jpg')

    .. image:: ../../examples/images/cubature.jpg
     :width: 50 %
     :align: center
     :alt: sphere ff cubature

    Notes
    -----
    - The here used module jscatter.libs.cubature is an adaption of the Python interface of S.G.P. Castro [1]_
      (vers. 0.14.5) to access the C-module of S.G. Johnson [2]_ (vers. 1.0.3).
      Only the vectorized form is realized here. The advantage here are fewer dependencies during install.
      Check the original packages for detailed documentation or look in jscatter.libs.cubature
      how to use it for your own things.

    - Internal: For complex valued functions the complex has to be split in real and imaginary to pass to the
      integration and later the result has to be converted to complex again.
      This is done automatically dependent on the return value of the function.
      For the example the real valued function is about 9 times faster

    References
    ----------
    .. [1] https://github.com/saullocastro/cubature
    .. [2] https://github.com/stevengj/cubature
    .. [3] An adaptive algorithm for numeric integration over an N-dimensional rectangular region
           A. C. Genz and A. A. Malik,
           J. Comput. Appl. Math. 6 (4), 295–302 (1980).
    .. [4] https://en.wikipedia.org/wiki/Clenshaw-Curtis_quadrature

    """
    # default values
    norm = kwargs.pop('norm', None)
    maxEval = kwargs.pop('maxEval', 0)
    kwargs.update(func=func, parnames=parnames)

    # test for typ and shape of func result using the uplimit values
    iscomplex, resultshape = _wrappedIntegrand(np.r_[uplimit][None, :], _test_=True, *args, **kwargs)
    if norm is None:
        if iscomplex:
            norm = 1
        else:
            norm = 0
    if fdim is None:
        if iscomplex:
            fdim = 2*resultshape[1]
        else:
            fdim = resultshape[1]

    val, err = cubature(func=_wrappedIntegrand, ndim=len(parnames), fdim=fdim, vectorized=True,
                        abserr=abserr, relerr=relerr, norm=norm, maxEval=maxEval, adaptive=adaptive,
                        xmin=lowlimit, xmax=uplimit, args=args, kwargs=kwargs)

    if iscomplex:
        return val.view(complex), np.abs(err.view(complex))
    else:
        return val, err


pAC = parAdaptiveCubature


def _CCKnotsWeights(n):
    """
    Clenshaw Curtis quadrature nodes in interval x=[-1,1] and corresponding weights w
    uses cache dict to store calculated x,w

    Returns : knots x, weights w

    To calc integral : sum(w * f(x)) *(xmax-xmin)

    """

    if n < 2:
        # x,w central role
        return 0, 2

    elif n in _CCKnotsWeights.cache:
        return _CCKnotsWeights.cache[n]

    else:
        # assume n is even
        N = n + 1
        c = np.zeros((N, 2))
        k = np.r_[2.:n + 1:2]
        c[::2, 0] = 2 / np.hstack((1, 1 - k * k))
        c[1, 1] = -n
        v = np.vstack((c, np.flipud(c[1:n, :])))
        f = np.real(np.fft.ifft(v, axis=0))
        x = f[0:N, 1]
        w = np.hstack((f[0, 0], 2 * f[1:n, 0], f[n, 0]))
        _CCKnotsWeights.cache[n] = (x, w)

        return _CCKnotsWeights.cache[n]


_CCKnotsWeights.cache = dict()


def parQuadratureAdaptiveClenshawCurtis(func, lowlimit, uplimit, parnames,
                                        weights0=None, weights1=None, weights2=None, rtol=1.e-6, tol=1.e-12,
                                        maxiter=520, miniter=8, **kwargs):
    r"""
    Vectorized adaptive multidimensional Clenshaw-Curtis quadrature for 1-3 dimensions. Shortcut pQACC.

    Clenshaw-Curtis is superior to adaptive Gauss as for increased order the already calculated function
    values are reused. Convergence is similar to adaptive Gauss.
    In the cuboid example CC is about 3 times faster.

    Parameters
    ----------
    func : function
        A function or method to integrate.
        The return array needs to be a 2-dim array with the last dimension as vectorized return
        and first along the points of the *parnames* to integrate.
        Use numpy functions for array functions to speedup computations.
        See example.
    lowlimit : list of float
        Lower limits of integration.
    uplimit : list of float
        Upper limits of integration.
    parnames : list of strings
        Names of the integration variables which should be scalar.
    weights0,weights1,weights2 : ndarray shape(2,N),default=None
        - Weights for integration along parname as a e.g. Gaussian distribution
          with a<weights[0]<b and weights[1] contains weight values.
        - Missing values are linear interpolated (faster). If None equal weights are used.
    kwargs : dict, optional
        Extra keyword arguments to pass to function, if any.
    tol, rtol : float, optional
        Iteration stops when (average) error between last two iterates is less than
        `tol` OR the relative change is less than `rtol`.
    maxiter : int, default 520, optional
        Maximum order of quadrature.
        Remember that the array of function values is of size iter**dim .
    miniter : int, default 8, optional
        Minimum order of quadrature.

    Returns
    -------
        arrays values, error

    Notes
    -----
    - Convergence of Clenshaw Curtis is about the same as Gauss-Legendre [1]_,[2]_.
    - The iterative procedure reuses the previous calculated function values corresponding to F(n//2).
      Therefore eCC is faster
    - Error estimates are based on the difference between F(n) and F(n//2)
      which is on the order of other more sophisticated estimates [2]_.
    - Curse of dimension: The error for d-dim integrals is of order :math:`O(N^{-r/d})`
      if the 1-dim integration method is :math:`O(N^{-r})` with N as number of evaluation points in d-dim space.
      For Clenshaw-Curtis r is about 3 [2]_.
    - For higher dimensions used Monte-Carlo Methods (e.g. with pseudo random numbers).

    Examples
    --------
    The cuboid formfactor includes an orientational average over the unit sphere which is done by
    integration over angles phi and theta which are our scalar integration variables.
    The array of q values are our vector input as we want to integrate for all q.

    The integrand `cuboid` contains patterns of scheme ``q*theta[:,None]`` to result in a 2-dim array with the last
    dimension as vectorized return.
    The first dimension goes along the points to evaluate as determined from the algorithm.
    ::

     import jscatter as js
     import numpy as np

     pQACC = js.formel.pQACC  # shortcut
     pQFGxD = js.formel.pQFGxD

     def cuboid(q, phi, theta, a, b, c):
         # integrand
         # scattering for orientations phi, theta as 1 dim arrays from 2dim integration
         # q is array for vectorized integration in last dimension
         # basically scheme as q*theta[:,None] results in array output of correct shape
         pi2 = np.pi * 2
         fa = (np.sinc(q * a * np.sin(theta[:,None]) * np.cos(phi[:,None]) / pi2) *
               np.sinc(q * b * np.sin(theta[:,None]) * np.sin(phi[:,None]) / pi2) *
               np.sinc(q * c * np.cos(theta[:,None]) / pi2))
         # add volume, sin(theta) weight of integration, normalise for unit sphere
         return fa**2*(a*b*c)**2*np.sin(theta[:,None])/np.pi/4

     q=np.r_[0,0.1:11.1:0.1]
     NN=20
     a,b,c = 2,2,2

     # quadrature: use one quadrant and multiply later by 8
     FqCC,err = pQACC(cuboid,[0,0],[np.pi/2,np.pi/2],parnames=['phi','theta'],q=q,a=a,b=b,c=c)
     FqGL=js.formel.pQFGxD(cuboid,[0,0],[np.pi/2,np.pi/2],parnames=['phi','theta'],q=q,a=c,b=b,c=c,n=NN)

     p=js.grace()
     p.multi(2,1)
     p[0].title('Comparison adaptive Gauss and Clenshaw-Curtis integration',size=1.2)
     p[0].subtitle('Cuboid formfactor integrated over unit sphere')
     p[0].plot(q,FqCC*8,sy=1,le='CC')
     p[0].plot(q,FqGL*8,sy=0,li=[1,2,4],le='GL')
     p[1].plot(q,err,li=[1,2,2],sy=0,le='error estimate CC')
     p[1].plot(q,np.abs(FqCC*8-FqGL*8),li=[3,2,4],sy=0,le='difference')
     p[0].xaxis(label=r'', min=0, max=15,)
     p[1].xaxis(label=r'q / nm\S-1', min=0, max=15)
     p[0].yaxis(label='I(q)',scale='log',ticklabel='power')
     p[1].yaxis(label='I(q)', scale='log',ticklabel='power', min=1e-16, max=1e-6)
     p[1].legend(y=1e-12,x=8)
     p[0].legend(y=1,x=12)
     #p.save(js.examples.imagepath+'/Clenshaw-Curtis.jpg')

    .. image:: ../../examples/images/Clenshaw-Curtis.jpg
     :align: center
     :width: 50 %
     :alt: Clenshaw-Curtis



    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Clenshaw-Curtis_quadrature

    .. [2] Error estimation in the Clenshaw-Curtis quadrature formula
           H. O'Hara and Francis J. Smith
           The Computer Journal, 11, 213–219 (1968), https://doi.org/10.1093/comjnl/11.2.213

    .. [3] Monte Carlo theory, methods and examples, chapter 7 Other quadrature methods
           Art B. Owen, 2019
           https://statweb.stanford.edu/~owen/mc/


    """
    if isinstance(parnames, str): parnames = [parnames]
    if isinstance(lowlimit, numbers.Number): lowlimit = [lowlimit]
    if isinstance(uplimit, numbers.Number): uplimit = [uplimit]
    lenp = len(parnames)

    if np.any(np.isinf(lowlimit)) or np.any(np.isinf(uplimit)):
        raise ValueError("Clenshaw-Curtis quadrature is only available for finite limits.")

    miniter = miniter + miniter % 2  # make it even returning n+1 points
    maxiter = max(miniter + 1, maxiter)
    vol = np.prod([(u - l) / 2 for u, l in zip(uplimit, lowlimit)])

    def xw(n):
        v, w = _CCKnotsWeights(n)
        # get real xyz values from outside scope
        xyz = [(u - l) * (v + 1) / 2.0 + l for u, l, p in zip(uplimit, lowlimit, parnames)]
        # weightsi*w if present, same length as parnames
        wxyz = [np.interp(x, ww[0], ww[1]) * w if ww is not None else w
                for ww, x in zip([weights0, weights1, weights2], xyz)]
        # points and weights as ndim ndarray for easy indexing
        points = np.array(list(itertools.product(*xyz))).reshape(tuple([n + 1] * lenp + [-1]))
        weights = np.prod(list(itertools.product(*wxyz)), axis=1).reshape(tuple([n + 1] * lenp))
        return points, weights

    n = miniter
    fx = None
    while True:
        # calc points, weights for the result (n+1 points rule) and weightsh for error estimate (n//2+1 points rule)
        points, weights = xw(n)

        # calc values for all points reshape to matrix
        if fx is None:
            # first iteration
            pointslist = points.reshape((-1, lenp))
            fx = func(**dict(kwargs, **dict(zip(parnames, pointslist.T)))).reshape(tuple([n + 1] * lenp + [-1]))
            # we need the (n//2+1 points rule) to calc previous step result for error determination
            sel = (np.indices([n + 1] * lenp) % 2 == 0).prod(axis=0) == 1
            _, weightsh = xw(n // 2)
            prevresult = vol * np.sum(weightsh[..., None] * fx[sel].reshape((n // 2 + 1,) * lenp + (-1,)),
                                      axis=tuple(range(lenp)))
        else:
            prevvalues = fx.copy()
            prevresult = res.copy()  # save prevresult not to calc it twice
            fx = np.zeros((n + 1,) * lenp + (prevvalues.shape[-1],))
            # select (odd,odd) indices to assign previous step values
            sel = (np.indices([n + 1] * lenp) % 2 == 0).prod(axis=0) == 1
            fx[sel] = prevvalues.reshape((-1, prevvalues.shape[-1]))
            # calc new values and assign to missing
            pointslist = points[~sel]
            values = func(**dict(kwargs, **dict(zip(parnames, pointslist.T))))
            fx[~sel] = values

        # result
        res = vol * np.sum(weights[..., None] * fx, axis=tuple(range(lenp)))
        error = np.abs(res - prevresult)

        if (np.sum(error) < rtol * np.sum(np.abs(res))) or (np.sum(error) < tol) or (n > maxiter):
            break
        else:
            n = n * 2

    return res, error


pQACC = parQuadratureAdaptiveClenshawCurtis


def parQuadratureSimpson(funktion, lowlimit, uplimit, parname, weights=None, tol=1e-6, rtol=1e-6, dX=None, **kwargs):
    """
    Vectorized quadrature over one parameter with weights using the adaptive Simpson rule. Shortcut pQS.

    Integrate by adaptive Simpson integration for all .X values at once.
    Only .Y values are integrated and checked for tol criterion.
    Attributes and non .Y columns correspond to the weighted mean of parname.

    Parameters
    ----------
    funktion : function
        Function returning dataArray or array
    lowlimit,uplimit : float
        Interval borders to integrate
    parname : string
        Parname to integrate
    weights : ndarray shape(2,N),default=None
        - Weights for integration along parname as a Gaussian with a<weights[0]<b and weights[1] contains weight values.
        - Missing values are linear interpolated (faster). If None equal weights are used.
    tol,rtol : float, default=1e-6
        | Relative  error or absolute error to stop integration. Stop if one is full filled.
        | Tol is divided for each new interval that the sum of tol is kept.
        | .IntegralErr_funktEvaluations in dataArray contains error and number of points in interval.
    dX : float, default=None
        Minimal distance between integration points to determine a minimal step for integration variable.
    kwargs :
        Additional parameters to pass to funktion.
        If parname is in kwargs it is overwritten.

    Returns
    -------
    dataArray or array
        dataArrays have additional parameters as error and weights.

    Notes
    -----
    What is the meaning of tol in Simpson method?
    If the error in an interval exceeds tol, the algorithm subdivides the interval
    in two equal parts with each :math:`tol/2` and applies the method to each subinterval in a recursive manner.
    The condition in interval i is :math:`error=|f(ai,mi)+f(mi,bi)-f(ai,bi)|/15 < tol`.
    The recursion stops in an interval if the improvement is smaller than tol.
    Thus tol is the upper estimate for the total error.

    Here we use a absolute (tol) and relative (rtol) criterion:
    :math:`|f(ai,mi)+f(mi,bi)-f(ai,bi)|/15 < rtol*fnew`
    with  :math:`fnew= ( f(ai,mi)+f(mi,bi) + [f(ai,mi)+f(mi,bi)-f(ai,bi)]/15 )` as the next improved value
    As this is tested for all .X the **worst** case is better than tol, rtol.

    The algorithm is efficient as it memoizes function evaluation at each interval border and reuses the result.
    This reduces computing time by about a factor 3-4.

    Different distribution can be found in scipy.stats. But any distribution given explicitly can be used.
    E.g. triangular np.c_[[-1,0,1],[0,1,0]].T

    Examples
    --------
    Integrate Gaussian as test case.
    As we integrate over .X the final .X will be the first integration point .X, here the lowlimit.
    ::

     import jscatter as js
     import numpy as np
     import scipy
     # testcase: integrate over x of a function
     # area under normalized gaussian is 1
     js.formel.parQuadratureSimpson(js.formel.gauss,-10,10,'x',mean=0,sigma=1)

    Integrate a function over one parameter with a weighting function.
    If weight is 1 the result is a simple integration.
    Here the weight corresponds to a normal distribution and the result is a weighted average as implemented in
    parDistributedAverage using fixedGaussian quadrature.
    ::

     # normal distribtion of parameter D with width ds
     t=np.r_[0:150:0.5]
     D=0.3
     ds=0.1
     diff=js.dynamic.simpleDiffusion(t=t,q=0.5,D=D)
     distrib =scipy.stats.norm(loc=D,scale=ds)
     x=np.r_[D-5*ds:D+5*ds:30j]
     pdf=np.c_[x,distrib.pdf(x)].T
     diff_g=js.formel.parQuadratureSimpson(js.dynamic.simpleDiffusion,-3*ds+D,3*ds+D,parname='D',
                                              weights=pdf,tol=0.01,q=0.5,t=t)
     # compare it
     p=js.grace()
     p.plot(diff,le='monodisperse')
     p.plot(diff_g,le='polydisperse')
     p.xaxis(scale='l')
     p.legend()

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Adaptive_Simpson's_method


    """
    # We have to deal with return values as arrays and dataArrays
    if lowlimit == uplimit:
        # return function with parname=a ; to be consistent
        result = funktion(**dict(kwargs, **{parname: lowlimit}))
        if isinstance(result, dA):
            result.weightNormFactor = 1
        return result
    if lowlimit > uplimit:
        lowlimit, uplimit = uplimit, lowlimit

    def _memoize(f):
        """
        avoid multiple calculations of same values at borders in each interation
        saves factor 3-4 in time
        """
        f.memo = {}

        def _helper(x):
            if x not in f.memo:
                # this overwrites the kwargs[parname] with x
                Y = f(**dict(kwargs, **{parname: x}))
                if isinstance(Y, dA):  # calc the function value
                    f.memo[x] = Y.Y
                else:
                    f.memo[x] = Y
                if weights is not None:  # weight of value
                    f.memo[x] *= np.interp(x, weights[0], weights[1])
            return f.memo[x]

        return _helper

    stack = [[lowlimit, uplimit, tol]]
    if dX is None: dX = 2 * (uplimit - lowlimit)
    funkt = _memoize(funktion)
    Integral = 0
    Err = 0
    nn = 0
    # do adaptive integration
    while stack:  # is not empty
        [x1, x2, err] = stack.pop()
        m = (x1 + x2) / 2.
        I1 = (funkt(x1) + 4 * funkt(m) + funkt(x2)) * (x2 - x1) / 6.  # Simpson rule.
        mleft = (x1 + m) / 2.
        Ileft = (funkt(x1) + 4 * funkt(mleft) + funkt(m)) * (m - x1) / 6.  # Simpson rule.
        mright = (m + x2) / 2.
        Iright = (funkt(m) + 4 * funkt(mright) + funkt(x2)) * (x2 - m) / 6.  # Simpson rule.
        # does the new point improve better than interval err on relative scale
        if (np.all(np.abs(Ileft + Iright - I1) < 15 * rtol * (Ileft + Iright + (Ileft + Iright - I1) / 15.)) or
            np.all(np.abs((Ileft + Iright - I1)) < 15 * err)) and \
                (x2 - x1) < dX:
            # good enough in this interval
            Integral += (Ileft + Iright + (Ileft + Iright - I1) / 15.)
            Err += abs((Ileft + Iright - I1) / 15.)
            nn += 1
        else:
            # split interval to improve with new points
            stack.append([x1, m, err / 2])
            stack.append([m, x2, err / 2])
    # calc final result with normalized weights
    if weights is not None:
        normfactor = np.trapz(weights[1], weights[0])
        parmean = np.trapz(weights[1] * weights[0], weights[0]) / normfactor
    else:
        normfactor = uplimit - lowlimit
        parmean = (lowlimit + uplimit) / 2
    result = funktion(**dict(kwargs, **{parname: parmean}))
    if not isinstance(result, dA):
        return Integral
    result.Y = Integral
    result.IntegralErr_funktEvaluations = max(Err), nn
    result.weightNormFactor = normfactor
    return result


pQS = parQuadratureSimpson


def simpleQuadratureSimpson(funktion, lowlimit, uplimit, parname, weights=None, tol=1e-6, rtol=1e-6, **kwargs):
    """
    Integrate a scalar function over one of its parameters with weights using the adaptive Simpson rule.
    Shortcut sQS.

    Integrate by adaptive Simpson integration for scalar function.

    Parameters
    ----------
    funktion : function
        function to integrate
    lowlimit,uplimit : float
        interval to integrate
    parname : string
        parname to integrate
    weights : ndarray shape(2,N),default=None
        - Weights for integration along parname as a Gaussian with a<weights[0]<b and weights[1] contains weight values.
        - Missing values are linear interpolated (faster). If None equal weights are used.
    tol,rtol : float, default=1e-6
        | Relative  error for intervals or absolute integral error to stop integration.
    kwargs :
        additional parameters to pass to funktion
        if parname is in kwargs it is overwritten

    Returns
    -------
    float

    Notes
    -----
    What is the meaning of tol in Simpson method?
    See parQuadratureSimpson.

    Examples
    --------
    ::

     distrib =scipy.stats.norm(loc=1,scale=0.2)
     x=np.linspace(0,1,1000)
     pdf=np.c_[x,distrib.pdf(x)].T
     # define function
     f1=lambda x,p1,p2,p3:js.dA(np.c_[x,x*p1+x*x*p2+p3].T)
     # calc the weighted integral
     result=js.formel.parQuadratureSimpson(f1,0,1,parname='p2',weights=pdf,tol=0.01,p1=1,p3=1e-2,x=x)
     # something simple should be 1
     js.formel.simpleQuadratureSimpson(js.formel.gauss,-10,10,'x',mean=0,sigma=1)

    References
    ----------
    .. [1] https://en.wikipedia.org/wiki/Adaptive_Simpson's_method


    """
    if lowlimit == uplimit:
        # return function with parname=a ; to be consistent
        result = funktion(**dict(kwargs, **{parname: lowlimit}))
        return result
    if lowlimit > uplimit:
        lowlimit, uplimit = uplimit, lowlimit

    def _memoize(f):
        """
        avoid multiple calculations of same values at borders in each interation
        saves factor 3-4 in time
        """
        f.memo = {}

        def _helper(x):
            if x not in f.memo:
                # this overwrites the kwargs[parname] with x
                Y = f(**dict(kwargs, **{parname: x}))
                if isinstance(Y, dA): Y = Y.Y
                f.memo[x] = Y
                if weights is not None:
                    f.memo[x] *= np.interp(x, weights[0], weights[1])
            return f.memo[x]

        return _helper

    stack = [[lowlimit, uplimit, tol]]
    funkt = _memoize(funktion)
    Integral = 0
    Err = 0
    # do adaptive integration
    while stack:  # is not empty
        [x1, x2, err] = stack.pop()
        m = (x1 + x2) / 2.
        I1 = (funkt(x1) + 4 * funkt(m) + funkt(x2)) * (x2 - x1) / 6.  # Simpson rule.
        mleft = (x1 + m) / 2.
        Ileft = (funkt(x1) + 4 * funkt(mleft) + funkt(m)) * (m - x1) / 6.  # Simpson rule.
        mright = (m + x2) / 2.
        Iright = (funkt(m) + 4 * funkt(mright) + funkt(x2)) * (x2 - m) / 6.  # Simpson rule.
        # does the new point improve better than interval err on relative scale
        if np.all(np.abs(Ileft + Iright - I1) < 15 * rtol * (Ileft + Iright + (Ileft + Iright - I1) / 15.)) or \
                np.all(np.abs((Ileft + Iright - I1)) < 15 * err):
            # good enough in this interval
            Integral += (Ileft + Iright + (Ileft + Iright - I1) / 15.)
            Err += abs((Ileft + Iright - I1) / 15.)
        else:
            # split interval to improve with new points
            stack.append([x1, m, err / 2])
            stack.append([m, x2, err / 2])
    return Integral


sQS = simpleQuadratureSimpson


def convolve(A, B, mode='same', normA=False, normB=False):
    r"""
    Convolve A and B  with proper tracking of the output X axis.

    Approximate the convolution integral as the discrete, linear convolution of two one-dimensional sequences.
    Missing values are linear interpolated to have matching steps. Values outside of X ranges are set to zero.

    Parameters
    ----------
    A,B : dataArray, ndarray
        To be convolved arrays (length N and M).
         - dataArray convolves Y with Y values
         - ndarray A[0,:] is X and A[1,:] is Y
    normA,normB : bool, default False
        Determines if A or B should be normalised that :math:`\int_{x_{min}}^{x_{max}} A(x) dx = 1`.
    mode : 'full','same','valid', default 'same'
        See example for the difference in range.
         - 'full'  Returns the convolution at each point of overlap,
                   with an output shape of (N+M-1,).
                   At the end-points of the convolution, the signals do not overlap completely,
                   and boundary effects may be seen.
         - 'same'  Returns output of length max(M, N).
                   Boundary effects are still visible.
         - 'valid' Returns output of length M-N+1.

    Returns
    -------
    dataArray
        with attributes from A

    Notes
    -----
     - :math:`A\circledast B (t)= \int_{-\infty}^{\infty} A(x) B(t-x) dx = \int_{x_{min}}^{x_{max}} A(x) B(t-x) dx`
     - If A,B are only 1d array use np.convolve.
     - If attributes of B are needed later use .setattr(B,'B-') to prepend 'B-' for B attributes.

    Examples
    --------
    Demonstrate the difference between modes
    ::

     import jscatter as js;import numpy as np
     s1=3;s2=4;m1=50;m2=10
     G1=js.formel.gauss(np.r_[0:100.1:0.1],mean=m1,sigma=s1)
     G2=js.formel.gauss(np.r_[-30:30.1:0.2],mean=m2,sigma=s2)
     p=js.grace()
     p.title('Convolution of Gaussians (width s mean m)')
     p.subtitle(r's1\S2\N+s2\S2\N=s_conv\S2\N ;  m1+m2=mean_conv')
     p.plot(G1,le='mean 50 sigma 3')
     p.plot(G2,le='mean 10 sigma 4')
     ggf=js.formel.convolve(G1,G2,'full')
     p.plot(ggf,le='full')
     gg=js.formel.convolve(G1,G2,'same')
     p.plot(gg,le='same')
     gg=js.formel.convolve(G1,G2,'valid')
     p.plot(gg,le='valid')
     gg.fit(js.formel.gauss,{'mean':40,'sigma':1},{},{'x':'X'})
     p.plot(gg.modelValues(),li=1,sy=0,le='fit m=$mean s=$sigma')
     p.legend(x=100,y=0.1)
     p.xaxis(max=150,label='x axis')
     p.yaxis(min=0,max=0.15,label='y axis')
     p.save(js.examples.imagepath+'/convolve.jpg')

    .. image:: ../../examples/images/convolve.jpg
     :align: center
     :height: 300px
     :alt: convolve


    References
    ----------
    .. [1] Wikipedia, "Convolution", http://en.wikipedia.org/wiki/Convolution.

    """
    # convert to array
    if hasattr(A, '_isdataArray'):
        AY = A.Y
        AX = A.X
    else:
        AX = A[0, :]
        AY = A[1, :]
    if normA:
        AY = AY /np.trapz(AY, AX)
    if hasattr(B, '_isdataArray'):
        BY = B.Y
        BX = B.X
    else:
        BX = B[0, :]
        BY = B[1, :]
    if normB:
        BY = BY /np.trapz(BY, BX)
    # create a combined x scale
    dx = min(np.diff(AX).min(), np.diff(BX).min())
    ddx = 0.1 * dx  # this accounts for the later >= BX.min() to catch problems with numerical precision
    XX = np.r_[min(AX.min(), BX.min()):max(AX.max(), BX.max()) + dx:dx]
    # interpolate missing values
    # if x scale is equal this is nearly no overhead
    AXX = XX[(XX >= AX.min() - ddx) & (XX <= AX.max() + ddx)]
    AY_xx = np.interp(AXX, AX, AY, left=0, right=0)
    BXX = XX[(XX >= BX.min() - ddx) & (XX <= BX.max() + ddx)]
    BY_xx = np.interp(BXX, BX, BY, left=0, right=0)
    if len(AXX) < len(BXX):
        # AXX always the larger one; this is also done in C source
        AXX, BXX = BXX, AXX
    # convolve
    res = np.convolve(AY_xx, BY_xx, mode=mode) * dx
    # define x scale
    # n,nleft,nright,length to reproduce C-source of convolve
    n = BXX.shape[0]
    l = AXX.shape[0]
    xx = np.r_[AX.min() + BX.min():AX.max() + BX.max() + dx:dx]
    if mode == 'full':  # length=l+n-1
        nleft = 0
        nright = l + n - 1
    elif mode == 'valid':  # length=l-n+1
        nleft = n - 1
        nright = l
    else:  # mode=='same'  # length=l
        nleft = (n - 1) // 2
        nright = nleft + l
    xx = xx[nleft:nright]
    result = dA(np.c_[xx, res].T)
    result.setattr(A)
    return result


def _sphereAverage_old(function, relError=300, *args, **kwargs):
    """
    Vectorized spherical average - non-parallel

    A Fibonacci lattice or Monte Carlo integration with pseudo random grid is used.

    Parameters
    ----------
    function : function
        Function to evaluate returning a list of return values (all are integrated)
        function  gets cartesian coordinate of point on unit sphere as first argument
    relError : float, default 300
        Determines how points on sphere are selected for integration
         - >=1  Fibonacci Lattice with relError*2+1 points (min 15 points)
         - 0<1 Pseudo random points on sphere (see randomPointsOnSphere).
               Stops if relative improvement in mean is less than relError
               (uses steps of 40 new points).
               Final error is (stddev of N points) /sqrt(N) as for Monte Carlo methods.
               even if it is not a correct 1-sigma error in this case.
    passPoints : bool
        If the function accepts an Nx3 array of points these will be passed.
        The function return value should index the points result in axis 0.
        This might speedup dependent on the function.
    args,kwargs :
        Forwarded to function.

    Returns
    -------
    array
        Values from function and appended Monte Carlo error estimates.
        To separate use `values, error = res.reshape(2,-1)`

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np

     def fp(singlepoint):
        return js.formel.xyz2rphitheta(singlepoint)[1:]
     js.formel.sphereAverage(fp,relError=500)
     js.formel.sphereAverage(fp,relError=0.01)

     def fps(allpoints):
        res = js.formel.xyz2rphitheta(allpoints)[:,1:]
        return res
     js.formel.sphereAverage(fps,r=1,passPoints=1)




    """
    passPoints = kwargs.pop('passPoints', False)

    if relError < 0:
        relError = abs(relError)
    if relError == 0:
        print('Try again with relError > 0')
        return

    if 0 < relError < 1:
        steps = 40
        points = rphitheta2xyz(randomPointsOnSphere(NN=steps, skip=0))
        npoints = steps
        if passPoints:
            results = np.array(function(points, *args, **kwargs), ndmin=1)
        else:
            results = np.r_[[np.array(function(point, *args, **kwargs), ndmin=1) for point in points]]
        prevmean = results.mean(axis=0).real

        while 1:
            points = rphitheta2xyz(randomPointsOnSphere(NN=steps, skip=npoints))
            npoints += steps
            if passPoints:
                result = np.array(function(points, *args, **kwargs), ndmin=1)
            else:
                result = np.r_[[np.array(function(point, *args, **kwargs), ndmin=1) for point in points]]
            results = np.r_[results, result]
            mean = results.mean(axis=0).real
            # var = results.var(axis=0,ddof=1)**0.5
            if np.all(abs(mean - prevmean) < relError * abs(mean)):
                break
            prevmean = mean

    elif relError >= 1:
        qfib = fibonacciLatticePointsOnSphere(max(relError, 7), 1)
        points = rphitheta2xyz(qfib)  # to cartesian
        if passPoints:
            results = np.array(function(points, *args, **kwargs), ndmin=2)
        else:
            results = np.r_[[np.array(function(point, *args, **kwargs), ndmin=1) for point in points]]

    return np.r_[results.mean(axis=0), results.std(axis=0) / np.sqrt(results.shape[0] - 1)]


# noinspection PyIncorrectDocstring
def parDistributedAverage(funktion, sig, parname, type='normal', nGauss=30, **kwargs):
    """
    Vectorized average assuming a single parameter is distributed with width sig. Shortcut pDA.

    Function average over a parameter with weights determined from probability distribution.
    Gaussian quadrature over given distribution or summation with weights is used.
    All columns are integrated except .X for dataArray.

    Parameters
    ----------
    funktion : function
        Function to integrate with distribution weight.
        Function needs to return dataArray. All columns except .X are integrated.
    sig : float
        Standard deviation from mean (or root of variance) describing the width the  distribution, see Notes.
    parname : string
        Name of the parameter of funktion which shows a distribution.
    type : 'normal','lognorm','gamma','lorentz','uniform','poisson','schulz','duniform', default 'normal'
        Type of the distribution
    kwargs : parameters
       Any additonal kword parameter to pass to function.
       The value of parname will be the mean value of the distribution.
    nGauss : float , default=30
        Order of quadrature integration as number of intervals in Gauss–Legendre quadrature over distribution.
        Distribution is integrated in probability interval [0.001..0.999].
    ncpu : int, optional
        Number of cpus in the pool.
        Set this to 1 if the integrated function uses multiprocessing to avoid errors.
         - 0   -> all cpus are used
         - int>0      min (ncpu, mp.cpu_count)
         - int<0      ncpu not to use

    Returns
    -------
    dataArray
        as returned from function with
         - .parname_mean = mean of parname
         - .parname_std  = standard deviation of parname (root of variance, input parameter)

    Notes
    -----
    The used distributions are from scipy.stats.
    Choose the distribution according to the problem.

    *mean* is the value in kwargs[parname]. mean is the expectation value of the distributed variable
    and *sig²* is the variance as the expectation of the squared deviation from the mean.
    Distributions may be parametrized differently  :

    * norm :
        | mean , std
        | stats.norm(loc=mean,scale=sig)
    * lognorm :
        | mean and sig evaluate to mean and std
        | mu=math.log(mean**2/(sig+mean**2)**0.5)
        | nu=(math.log(sig/mean**2+1))**0.5
        | stats.lognorm(s=nu,scale=math.exp(mu))
    * gamma :
        | mean and sig evaluate to mean and std
        | stats.gamma(a=mean**2/sig**2,scale=sig**2/mean)
        | Same as SchulzZimm
    * lorentz = cauchy:
        | mean and std are not defined. Use FWHM instead to describe width.
        | sig=FWHM
        | stats.cauchy(loc=mean,scale=sig))
    * uniform :
        | Continuous distribution.
        | sig is width
        | stats.uniform(loc=mean-sig/2.,scale=sig))
    * schulz
        | Same as gamma
    * poisson:
        stats.poisson(mu=mean,loc=sig)
    * duniform:
        | Uniform distribution integer values.
        | sig>1
        | stats.randint(low=mean-sig, high=mean+sig)

    For more distribution look into this source code and use it appropriate with scipy.stats.

    Examples
    --------
    ::

     import jscatter as js
     p=js.grace()
     q=js.loglist(0.1,5,500)
     sp=js.ff.sphere(q=q,radius=5)
     p.plot(sp,sy=[1,0.2],legend='single radius')
     p.yaxis(scale='l',label='I(Q)')
     p.xaxis(scale='n',label='Q / nm')
     sig=0.2
     p.title('radius distribution with width %.g' %(sig))
     sp2=js.formel.pDA(js.ff.sphere,sig,'radius',type='normal',q=q,radius=5,nGauss=100)
     p.plot(sp2,li=[1,2,2],sy=0,legend='normal 100 points Gauss ')
     sp4=js.formel.pDA(js.ff.sphere,sig,'radius',type='normal',q=q,radius=5,nGauss=30)
     p.plot(sp4,li=[1,2,3],sy=0,legend='normal 30 points Gauss  ')
     sp5=js.formel.pDA(js.ff.sphere,sig,'radius',type='normal',q=q,radius=5,nGauss=5)
     p.plot(sp5,li=[1,2,5],sy=0,legend='normal 5 points Gauss  ')
     sp3=js.formel.pDA(js.ff.sphere,sig,'radius',type='lognormal',q=q,radius=5)
     p.plot(sp3,li=[3,2,4],sy=0,legend='lognormal')
     sp6=js.formel.pDA(js.ff.sphere,sig,'radius',type='gamma',q=q,radius=5)
     p.plot(sp6,li=[2,2,6],sy=0,legend='gamma ')
     sp9=js.formel.pDA(js.ff.sphere,sig,'radius',type='schulz',q=q,radius=5)
     p.plot(sp9,li=[3,2,2],sy=0,legend='SchulzZimm ')
     # an unrealistic example
     sp7=js.formel.pDA(js.ff.sphere,1,'radius',type='poisson',q=q,radius=5)
     p.plot(sp7,li=[1,2,6],sy=0,legend='poisson ')
     sp8=js.formel.pDA(js.ff.sphere,1,'radius',type='duniform',q=q,radius=5)
     p.plot(sp8,li=[1,2,6],sy=0,legend='duniform ')
     p.legend()

    """
    npoints = 1000
    limit = 0.001
    mean = kwargs[parname]
    # define the distribution with parameters
    if type == 'poisson':
        distrib = stats.poisson(mu=mean, loc=sig)
    elif type == 'duniform':
        sigm = max(sig, 1)
        distrib = stats.randint(low=mean - sigm, high=mean + sigm)
    elif type == 'lognorm':
        mu = math.log(mean ** 2 / (sig + mean ** 2) ** 0.5)
        nu = (math.log(sig / mean ** 2 + 1)) ** 0.5
        distrib = stats.lognorm(s=nu, scale=math.exp(mu))
    elif type == 'gamma' or type == 'schulz':
        distrib = stats.gamma(a=mean ** 2 / sig ** 2, scale=sig ** 2 / mean)
    elif type == 'lorentz' or type == 'cauchy':
        distrib = stats.cauchy(loc=mean, scale=sig)
    elif type == 'uniform':
        distrib = stats.uniform(loc=mean - sig / 2., scale=sig)
    else:  # type=='norm'  default
        distrib = stats.norm(loc=mean, scale=sig)

    # get starting and end values for integration
    a = distrib.ppf(limit)
    b = distrib.ppf(1 - limit)
    if type in ['poisson', 'duniform']:
        # discrete distributions
        x = np.r_[int(a):int(b + 1)]
        w = distrib.pmf(x)
        result = [funktion(**dict(kwargs, **{parname: xi})) for xi in x]
        if isinstance(result[0], dA):
            result[0][:, :] = np.sum([result[i] * wi for i, wi in enumerate(w)], axis=0) / w.sum()
            result[0].X = result[1].X
        else:
            result[0] = np.sum([result[i] * wi for i, wi in enumerate(w)], axis=0) / w.sum()
        result = result[0]
    else:
        # here we use the fixedGauss for integration
        x = np.linspace(a, b, npoints)
        pdf = np.c_[x, distrib.pdf(x)].T
        # calc the weighted integral
        result = parQuadratureFixedGauss(funktion, a, b, parname=parname, n=nGauss, weights=pdf, **kwargs)
        normfactor = np.trapz(pdf[1], pdf[0])
        if isinstance(result, dA):
            result.Y = result.Y /normfactor
        else:
            result = result /normfactor
    if isinstance(result, dA):
        try:
            delattr(result, parname)
        except AttributeError:
            pass
        # calc mean and std and store in result
        setattr(result, parname + '_mean', distrib.mean())
        setattr(result, parname + '_std', distrib.std())
        if type == 'lorentz' or type == 'cauchy':
            setattr(result, parname + '_FWHM', 2 * sig)

    return result


pDA = parDistributedAverage


# noinspection PyIncorrectDocstring
def multiParDistributedAverage(funktion, sigs, parnames, types='normal', N=30, ncpu=1, **kwargs):
    r"""
    Vectorized average assuming multiple parameters are distributed in intervals. Shortcut mPDA.

    Function average over multiple distributed parameters with weights determined from probability distribution.
    The probabilities for the parameters are multiplied as weights and a weighted sum is calculated
    by Monte-Carlo integration.

    Parameters
    ----------
    funktion : function
        Function to integrate with distribution weight.
    sigs : list of float
        List of widths for parameters.
        Sigs are the standard deviation from mean (or root of variance), see Notes.
    parnames : string
        List of names of the parameters which show a distribution.
    types : list of 'normal', 'lognorm', 'gamma', 'lorentz', 'uniform', 'poisson', 'schulz', 'duniform', default 'normal'
        List of types of the distributions.
        If types list is shorter than parnames the last is repeated.
    kwargs : parameters
       Any additonal kword parameter to pass to function.
       The value of parnames that are distributed will be the mean value of the distribution.
    N : float , default=30
        Number of points over distribution ranges.
        Distributions are integrated in probability intervals :math:`[e^{-4} \ldots 1-e^{-4}]`.
    ncpu : int, default=1, optional
        Number of cpus in the pool for parallel excecution.
        Set this to 1 if the integrated function uses multiprocessing to avoid errors.
         - 0   -> all cpus are used
         - int>0      min (ncpu, mp.cpu_count)
         - int<0      ncpu not to use

    Returns
    -------
    dataArray
        as returned from function with
         - .parname_mean = mean of parname
         - .parname_std  = standard deviation of parname

    Notes
    -----
    Calculation of an average over D multiple distributed parameters by conventional integration requires
    :math:`N^D` function evaluations which is quite time consuming. Monte-Carlo integration at N points
    with random combinations of parameters requires only N evaluations.

    The given function of fixed parameters :math:`q_j` and polydisperse parameters :math:`p_i`
    with width :math:`s_i` related to the indicated distribution (types) is integrated as

    .. math:: f_{mean}(q_j,p_i,s_i) = \frac{\sum_h{f(q_j,x^h_i)\prod_i{w_i(x^h_i)}}}{\sum_h \prod_i w_i(x^h_i)}

    Each parameter :math:`p_i` is distributed along values :math:`x^h_i` with probability :math:`w_i(x^h_i)`
    describing the probability distribution with mean :math:`p_i` and sigma :math:`s_i`.
    Intervals for a parameter :math:`p_i` are choosen to represent the distribution
    in the interval :math:`[w_i(x^0_i) = e^{-4} \ldots \sum_h w_i(x^h_i) = 1-e^{-4}]`

    The distributed values :math:`x^h_i` are determined as pseudorandom numbers of N points with dimension
    len(i) for Monte-Carlo integration.

    - For a single polydisperse parameter use parDistributedAverage.

    - During fitting it has to be accounted for the information content of the experimental data.
      As in the example below it might be better to use a single width for all parameters to reduce
      the number of redundant parameters.

    The used distributions are from scipy.stats.
    Choose the distribution according to the problem and check needed number of points N.

    *mean* is the value in kwargs[parname]. mean is the expectation value of the distributed variable
    and *sig²* are the variance as the expectation of the squared deviation from the mean.
    Distributions may be parametrized differently  :

    * norm :
        | mean , std
        | stats.norm(loc=mean,scale=sig)
    * lognorm :
        | mean and sig evaluate to mean and std
        | mu=math.log(mean**2/(sig+mean**2)**0.5)
        | nu=(math.log(sig/mean**2+1))**0.5
        | stats.lognorm(s=nu,scale=math.exp(mu))
    * gamma :
        | mean and sig evaluate to mean and std
        | stats.gamma(a=mean**2/sig**2,scale=sig**2/mean)
        | Same as SchulzZimm
    * lorentz = cauchy:
        | mean and std are not defined. Use FWHM instead to describe width.
        | sig=FWHM
        | stats.cauchy(loc=mean,scale=sig))
    * uniform :
        | Continuous distribution.
        | sig is width
        | stats.uniform(loc=mean-sig/2.,scale=sig))
    * poisson:
        stats.poisson(mu=mean,loc=sig)
    * schulz
        | same as gamma
    * duniform:
        | Uniform distribution integer values.
        | sig>1
        | stats.randint(low=mean-sig, high=mean+sig)

    For more distribution look into this source code and use it appropriate with scipy.stats.

    Examples
    --------
    The example of a cuboid with independent polydispersity on all edges.
    To use the function in fitting please encapsulate it in a model function hiding the list parameters.
    ::

     import jscatter as js
     type=['norm','schulz']
     p=js.grace()
     q=js.loglist(0.1,5,500)
     sp=js.ff.cuboid(q=q,a=4,b=4.1,c=4.3)
     p.plot(sp,sy=[1,0.2],legend='single cube')
     p.yaxis(scale='l',label='I(Q)')
     p.xaxis(scale='n',label='Q / nm')
     p.title('Cuboid with independent polydispersity on all 3 edges')
     p.subtitle('Using Monte Carlo integration; 30 points are enough here!')
     sp1=js.formel.mPDA(js.ff.cuboid,sigs=[0.2,0.3,0.1],parnames=['a','b','c'],types=type,q=q,a=4,b=4.1,c=4.2,N=10)
     p.plot(sp1,li=[1,2,2],sy=0,legend='normal 10 points')
     sp2=js.formel.mPDA(js.ff.cuboid,sigs=[0.2,0.3,0.1],parnames=['a','b','c'],types=type,q=q,a=4,b=4.1,c=4.2,N=30)
     p.plot(sp2,li=[1,2,3],sy=0,legend='normal 30 points')
     sp3=js.formel.mPDA(js.ff.cuboid,sigs=[0.2,0.3,0.1],parnames=['a','b','c'],types=type,q=q,a=4,b=4.1,c=4.2,N=90)
     p.plot(sp3,li=[3,2,4],sy=0,legend='normal 100 points')
     p.legend(x=2,y=1000)
     # p.save(js.examples.imagepath+'/multiParDistributedAverage.jpg')

    .. image:: ../../examples/images/multiParDistributedAverage.jpg
     :align: center
     :height: 300px
     :alt: multiParDistributedAverage

    During fitting encapsulation might be done like this ::

     def polyCube(a,b,c,sig,N):
        res = js.formel.mPDA(js.ff.cuboid,sigs=[sig,sig,sig],parnames=['a','b','c'],types='normal',q=q,a=a,b=b,c=c,N=N)
        return res

    """
    em4 = np.exp(-4)

    # make lists
    if isinstance(sigs, numbers.Number):
        sigs = [sigs]
    if isinstance(parnames, numbers.Number):
        parnames = [parnames]
    if isinstance(types, str):
        types = [types]

    dim = len(parnames)
    if len(sigs) != len(parnames):
        raise AttributeError('len of parnames and sigs is different!')
    # extend missing types
    types.extend(types[-1:] * dim)

    # pseudorandom numbers in interval [0,1]
    distribvalues = randomPointsInCube(N, 0, dim)

    weights = np.zeros_like(distribvalues)
    distribmeans = np.zeros(dim)
    distribstds = np.zeros(dim)

    # determine intervals and scale to it
    for i, (parname, sig, type) in enumerate(zip(parnames, sigs, types)):
        mean = kwargs[parname]
        # define the distribution with parameters
        if type == 'poisson':
            distrib = stats.poisson(mu=mean, loc=sig)
        elif type == 'duniform':
            sigm = max(sig, 1)
            distrib = stats.randint(low=mean - sigm, high=mean + sigm)
        elif type == 'lognorm':
            mu = math.log(mean ** 2 / (sig + mean ** 2) ** 0.5)
            nu = (math.log(sig / mean ** 2 + 1)) ** 0.5
            distrib = stats.lognorm(s=nu, scale=math.exp(mu))
        elif type == 'gamma' or type == 'schulz':
            distrib = stats.gamma(a=mean ** 2 / sig ** 2, scale=sig ** 2 / mean)
        elif type == 'lorentz' or type == 'cauchy':
            distrib = stats.cauchy(loc=mean, scale=sig)
        elif type == 'uniform':
            distrib = stats.uniform(loc=mean - sig / 2., scale=sig)
        else:  # type=='norm'  default
            distrib = stats.norm(loc=mean, scale=sig)

        # get starting and end values for integration, then scale pseudorandom numbers to interval [0..1]
        a = distrib.ppf(em4)  # about 0.02
        b = distrib.ppf(1 - em4)
        distribvalues[:, i] = a + distribvalues[:, i] * (b - a)
        try:
            # continuous  distributions
            weights[:, i] = distrib.pdf(distribvalues[:, i])
        except AttributeError:
            # discrete distributions
            weights[:, i] = distrib.pmf(distribvalues[:, i])
        distribmeans[i] = distrib.mean()
        distribstds[i] = distrib.std()

    # prepare for pool
    if ncpu < 0:
        ncpu = max(mp.cpu_count() + ncpu, 1)
    elif ncpu > 0:
        ncpu = min(mp.cpu_count(), ncpu)
    else:
        ncpu = mp.cpu_count()

    # calculate the values and calc weighted sum
    if ncpu == 1 or mp.current_process().name != 'MainProcess':
        result = [funktion(**dict(kwargs, **{p: d for p, d in zip(parnames, dv)})) for dv in distribvalues]
    else:
        with mp.Pool(ncpu) as pool:
            jobs = [pool.apply_async(funktion, [], dict(kwargs, **{p: d for p, d in zip(parnames, dv)}))
                    for dv in distribvalues]
            result = [job.get() for job in jobs]

    w = weights.prod(axis=1)
    if isinstance(result[0], dA):
        result[0].Y = np.sum([result[i].Y * wi for i, wi in enumerate(w)], axis=0) / w.sum()
    else:
        result[0] = np.sum([result[i] * wi for i, wi in enumerate(w)], axis=0) / w.sum()

    result = result[0]

    if isinstance(result, dA):
        # use mean and std and store in result
        for parname, mean, std in zip(parnames, distribmeans, distribstds):
            setattr(result, parname + '_mean', mean)
            setattr(result, parname + '_std', std)
            if type == 'lorentz' or type == 'cauchy':
                setattr(result, parname + '_FWHM', 2 * sig)

    return result


mPDA = multiParDistributedAverage


def scatteringFromSizeDistribution(q, sizedistribution, size=None, func=None, weight=None, **kwargs):
    r"""
    Average function assuming one multimodal parameter like bimodal.

    Distributions might be mixtures of small and large particles bi or multimodal.
    For predefined distributions see formel.parDistributedAverage with examples.
    The weighted average over given sizedistribution is calculated.

    Parameters
    ----------
    q : array of float;
        Wavevectors to calculate scattering; unit = 1/unit(size distribution)
    sizedistribution : dataArray or array
        Explicit given distribution of sizes as [ [list size],[list probability]]
    size : string
        Name of the parameter describing the size (may be also something different than size).
    func : lambda or function, default beaucage
        Function that describes the form factor with first arguments (q,size,...)
        and should return dataArray with .Y as result as eg func=js.ff.sphere.
    kwargs :
        Any additional keyword arguments passed to  for func.
    weight : function
        Weight function dependent on size.
        E.g. weight = lambda R:rho**2 * (4/3*np.pi*R**3)**2
        with V= 4pi/3 R**3 for normalized form factors to account for
        forward scattering of volume objects of dimension 3.

    Returns
    -------
    dataArray
        Columns [q,I(q)]

    Notes
    -----
    We have to discriminate between formfactor normalized to 1 (e.g. beaucage) and
    form factors returning the absolute scattering (e.g. sphere) including the contrast.
    The later contains already :math:`\rho^2 V^2`, the first not.

    We need for normalized formfactors P(q) :math:`I(q) = n \rho^2 V^2 P(q)` with  :math:`n` as number density
    :math:`\rho` as difference in average scattering length (contrast), V as volume of particle (~r³ ~ mass)
    and use :math:`weight = \rho^2 V(R)^2`

    .. math:: I(q)= \sum_{R_i} [  weight(R_i) * probability(R_i) * P(q, R_i , *kwargs).Y  ]

    For a gaussian chain with :math:`R_g^2=l^2 N^{2\nu}` and monomer number N (nearly 2D object)
    we find :math:`N^2=(R_g/l)^{1/\nu}` and the forward scattering as weight :math:`I_0=b^2 N^2=b^2 (R_g/l)^{1/\nu}`

    Examples
    --------
    The contribution of different simple sizes to Beaucage ::

     import jscatter as js
     q=js.loglist(0.01,6,100)
     p=js.grace()
     # bimodal with equal concentration
     bimodal=[[12,70],[1,1]]
     Iq=js.formel.scatteringFromSizeDistribution(q=q,sizedistribution=bimodal,
                                                 d=3,weight=lambda r:(r/12)**6,func=js.ff.beaucage)
     p.plot(Iq,legend='bimodal 1:1 weight ~r\S6 ')
     Iq=js.formel.scatteringFromSizeDistribution(q=q,sizedistribution=bimodal,d=3,func=js.ff.beaucage)
     p.plot(Iq,legend='bimodal 1:1 weight equal')
     # 2:1 concentration
     bimodal=[[12,70],[1,5]]
     Iq=js.formel.scatteringFromSizeDistribution(q=q,sizedistribution=bimodal,d=2.5,func=js.ff.beaucage)
     p.plot(Iq,legend='bimodal 1:5 d=2.5')
     p.yaxis(label='I(q)',scale='l')
     p.xaxis(scale='l',label='q / nm\S-1')
     p.title('Bimodal size distribution Beaucage particle')
     p.legend(x=0.2,y=10000)
     #p.save(js.examples.imagepath+'/scatteringFromSizeDistribution.jpg')

    .. image:: ../../examples/images/scatteringFromSizeDistribution.jpg
     :width: 50 %
     :align: center
     :alt: scatteringFromSizeDistribution


    Three sphere sizes::

     import jscatter as js
     q=js.loglist(0.001,6,1000)
     p=js.grace()
     # trimodal with equal concentration
     trimodal=[[10,50,500],[1,0.01,0.00001]]
     Iq=js.formel.scatteringFromSizeDistribution(q=q,sizedistribution=trimodal,size='radius',func=js.ff.sphere)
     p.plot(Iq,legend='with aggregates')
     p.yaxis(label='I(q)',scale='l',max=1e13,min=1)
     p.xaxis(scale='l',label='q / nm\S-1')
     p.text(r'minimum \nlargest',x=0.002,y=1e10)
     p.text(r'minimum \nmiddle',x=0.02,y=1e7)
     p.text(r'minimum \nsmallest',x=0.1,y=1e5)
     p.title('trimodal spheres')
     p.subtitle('first minima indicated')
     #p.save(js.examples.imagepath+'/scatteringFromSizeDistributiontrimodal.jpg')

    .. image:: ../../examples/images/scatteringFromSizeDistributiontrimodal.jpg
     :width: 50 %
     :align: center
     :alt: scatteringFromSizeDistribution


    """
    if weight is None:
        weight = lambda r: 1.
    sizedistribution = np.array(sizedistribution)
    result = []
    if size is None:
        for spr in sizedistribution.T:
            result.append(weight(spr[0]) * spr[1] * func(q, spr[0], **kwargs).Y)
    else:
        for spr in sizedistribution.T:
            kwargs.update({size: spr[0]})
            result.append(weight(spr[0]) * spr[1] * func(q, **kwargs).Y)
    result = dA(np.c_[q, np.r_[result].sum(axis=0)].T)
    result.setColumnIndex(iey=None)
    result.formfactor = str(func.__name__)
    result.formfactorkwargs = str(kwargs)
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def viscosity(mat='h2o', T=293.15):
    """
    Viscosity of pure solvents. For buffer solvents use bufferviscosity.

    Parameters
    ----------
    mat : string  'h2o','d2o','toluol','methylcyclohexan',  default h2o
        Solvent
    T : float
        Temperature T in Kelvin  default 293K

    Returns
    -------
    float
        viscosity in Pa*s
         water H2O ~ 0.001 Pa*s =1 cPoise             # Poise=0.1 Pa*s

    References
    ----------
    .. [1]  The Viscosity of Toluene in the Temperature Range 210 to 370 K
            M. J. Assael, N.K. Dalaouti, J.H., Dymond International Journal of Thermophysics, Vol. 21,291  No. 2, 2000
            #  accuracy +- 0.4 % laut paper Max error von Experiment data

    .. [2] Thermal Offset Viscosities of Liquid H2O, D2O, and T2O
           C. H. Cho, J. Urquidi,  S. Singh, and G. Wilse Robinson  J. Phys. Chem. B 1999, 103, 1991-1994


    """
    temp = T
    if re.match('^' + mat, 'toluol'):
        # print 'Material Toluol  Temperatur', temp , ' Viscosity in mPas (=cP)   ',
        # critical temperature and coefficients
        Tc, ck0, ck1, ck2, ck3, ck4 = 591.75, 34.054, -219.46, 556.183, -653.601, 292.762
        T = temp / Tc
        vis29315 = 0.0005869  # Pas
        vis = vis29315 * math.exp(ck0 + ck1 * T + ck2 * T * T + ck3 * T * T * T + ck4 * T * T * T * T)
        return vis * 1000
    elif re.match('^' + mat, 'methylcyclohexan'):
        # print 'Material  Methylcyclohexan Temperatur', temp , ' Viscosity in mPas (=cP)'
        vis = 0.001 * math.exp(-4.48 + 1217. / temp)
        return vis * 1000
    elif re.match('^' + mat, 'd2o'):
        # print 'Material D2O  Temperatur', temp , ' Viscosity in mPas (=cP)   ',
        T0 = 231.832  # reference Temperature
        ck0 = 0.0
        ck1 = 1.0
        ck2 = 2.7990E-3  # Koeffizienten
        ck3 = -1.6342E-5
        ck4 = 2.9067E-8
        gamma = 1.55255
        dT = temp - T0
        vis231832 = 885.60402  # cPK^gamma
        vis = vis231832 * (ck0 + ck1 * dT + ck2 * dT ** 2 + ck3 * dT ** 3 + ck4 * dT ** 4) ** (-gamma)
        # print vis
        return vis * 1e-3
    else:
        # print 'Material H2O  Temperatur', temp , ' Viscosity in mPas (=cP)   ',
        T0 = 225.334  # reference Temperature
        ck0 = 0.0
        ck1 = 1.0
        ck2 = 3.4741E-3  # Koeffizienten
        ck3 = -1.7413E-5
        ck4 = 2.7719E-8
        gamma = 1.53026
        dT = temp - T0
        vis225334 = 802.25336  # cPK^gamma
        vis = vis225334 * 1 / ((ck0 + ck1 * dT + ck2 * dT ** 2 + ck3 * dT ** 3 + ck4 * dT ** 4) ** gamma)
        # print vis
        return vis * 1e-3


def _convertfromUltrascan():
    """
    Internal usage to document how bufferComponents.txt was generated
    Get xml file from ultrascan and convert to ascii file to read on module load (faster than xmltree)

    We use only the fields we need here.

    Ultrascan is released under  GNU Lesser General Public License, version 3.
    See notice in bufferComponents.txt

    """
    import xml.etree.ElementTree
    buffers = xml.etree.ElementTree.parse('bufferComponents.xml').getroot()
    bl = []  # new bufferlines
    bl += ['# buffer coefficients for density (dci) and viscosity (vci) as read from Ultrascan 3 ' + '\n']
    content = ['name'] + ['dc0', 'dc1', 'dc2', 'dc3', 'dc4', 'dc5'] + ['vc0', 'vc1', 'vc2', 'vc3', 'vc4', 'vc5'] + [
        'unit', 'range']
    bl += ['# ' + ' '.join(content) + '\n']
    for buff in buffers:
        name = buff.attrib['name'].title().replace(' ', '').replace('-', '')
        if name[0].isdigit(): name = name[1:] + name[0]
        line = [name]
        line += [buff[0].attrib[attrib] for attrib in ['c0', 'c1', 'c2', 'c3', 'c4', 'c5']]
        line += [buff[1].attrib[attrib] for attrib in ['c0', 'c1', 'c2', 'c3', 'c4', 'c5']]
        line += [buff.attrib[attrib].strip().replace(' ', '_') for attrib in ['unit', 'range']]
        bl += [' '.join(line) + '\n']
    bl.sort()
    with io.open(os.path.join(_path_, 'data', 'bufferComponents.txt'), 'w') as _f:
        _f.writelines(bl)


def bufferviscosity(composition, T=293.15, show=False):
    """
    Viscosity of water with inorganic substances as used in biological buffers.

    Solvent with composition of H2O and D2O  and additional components at temperature T.
    Ternary solutions allowed. Units are mol; 1l h2o = 55.50843 mol
    Based on data from ULTRASCAN3 [1]_ supplemented by the viscosity of H2O/D2O mixtures for conc=0.

    Parameters
    ----------
    composition : list of compositional strings
        Compositional strings of chemical name as 'float'+'name'
        First float is content in Mol followed by component name as
        'h2o' or 'd2o' light and heavy water were mixed with prepended fractions.
         ['1.5urea','0.1sodiumchloride','2h2o','1d2o']
         for 1.5 M urea + 100 mM NaCl in a 2:1 mixture of h2o/d2o.
         By default '1h2o' is assumed.
    T : float, default 293.15
        Temperature in K
    show : bool, default False
        Show composition and validity range of components and result in mPas.

    Returns
    -------
    float
        Viscosity in Pa*s

    Notes
    -----
    - Viscosities of H2O/D2O mixtures mix by linear interpolation between concentrations (accuracy 0.2%) [2]_.
    - The change in viscosity due to components is added based on data from Ultrascan3 [1]_.
    - Multicomponent mixtures are composed of binary mixtures.
    - "Glycerol%" is in unit "%weight/weight" for range="0-32%, here the unit is changed to weight% insthead of M.
    - Propanol1, Propanol2 are 1-Propanol, 2-Propanol


    References
    ----------
    .. [1] http://www.ultrascan3.uthscsa.edu/
    .. [2] Viscosity of light and heavy water and their mixtures
           Kestin Imaishi Nott Nieuwoudt Sengers, Physica A: Statistical Mechanics and its Applications 134(1):38-58
    .. [3] Thermal Offset Viscosities of Liquid H2O, D2O, and T2O
           C. H. Cho, J. Urquidi,  S. Singh, and G. Wilse Robinson  J. Phys. Chem. B 1999, 103, 1991-1994

    availible components::

     h2o1 d2o1
    """
    if isinstance(composition, str):
        composition = [composition]
    cd2o = 0
    ch2o = 0
    nwl = {}  # nonwaterlist
    # decompose composition
    for compo in composition:
        compo = compo.lower()
        decomp = re.findall(r'\d+\.\d+|\d+|\D+', compo)
        if not re.match(r'\d', decomp[0]):
            raise KeyError('Component %s missing concentration ' % compo)
        component = ''.join(decomp[1:])
        conc = float(decomp[0])  # in Mol
        if component in ['h2o1', 'h2o']:
            ch2o += conc
        elif component in ['d2o1', 'd2o']:
            cd2o += conc
        else:
            nwl[component] = (conc,) + (_bufferDensityViscosity[component][6:14])
    if ch2o == 0 and cd2o == 0:
        # default if no water composition was given
        ch2o = 1  #
    # temperature dependent viscosity of h20/d2o mixture as basis in mPas (Ultrascan units for below)
    ch2od2o = (ch2o + cd2o)
    ch2o = ch2o / ch2od2o
    cd2o = cd2o / ch2od2o
    visc = (ch2o * viscosity(mat='h2o', T=T) + cd2o * viscosity(mat='d2o', T=T)) * 1000.
    # coefficints all for c=0 give water viscosity (which is not always correct!!)
    # coefficients[i>0] give increase from conc =0
    #  so add them up
    vc = np.r_[0.].repeat(6)  # sum coefficients
    ff = np.r_[1., 1e-3, 1e-2, 1e-3, 1e-4, 1e-6]  # standard powers
    for k, v in nwl.items():
        c = v[0]  # concentration (converted to mM)
        coefficients = v[1:7]  # coefficients
        range = v[8]  # validity range
        cp = np.r_[0, c ** 0.5, c, c * c, c ** 3, c ** 4]  # concentration powers
        if show:
            print('%20s %12.3f M valid: %20s' % (k, c, range))
        vc += coefficients * cp
    if show:
        print('  h2o %.3f d2o %.3f => visc %.3f mPas' % (ch2o, cd2o, visc))
    visc += np.sum(vc * ff)  # multiply by standard powers
    if show:
        print('            mixture => %.3f mPas' % visc)
    return visc / 1000.  # return use Pa*s


# complete the docstring from above
_avlist = sorted(_bufferDensityViscosity.keys())
_i = 0
while _i < len(_avlist):
    bufferviscosity.__doc__ += '     ' + ''.join([' %-25s' % cc for cc in _avlist[_i:_i + 3]]) + '\n'
    _i += 3
bufferviscosity.__doc__ += '\n'


def waterdensity(composition, T=293.15, units='mol', showvalidity=False):
    """
    Density of water with inorganic substances (salts).

    Solvent with composition of H2O and D2O  and additional inorganic components at temperature T.
    Ternary solutions allowed. Units are mol; 1l h2o = 55.50843 mol

    Parameters
    ----------
    composition : list of compositional strings
        | Compositional string of chemical formula as 'float'+'chemical char' + integer
        | First float is content in mol (is later normalised to sum of contents)
        | chemical letter + number of atoms in formula (single atoms append 1 ,fractional numbers allowed)
        | e.g.
        | 'h2o1' or 'd2o1' light and heavy water with 'd1' for deuterium
        | 'c3h8o3' or 'c3h1d7o3' partial deuterated glycerol
        | ['55.55h2o1','2.5Na1Cl1'] for 2.5 mol NaCl added to  1l h2o (55.55 mol)
        | ['20H2O1','35.55D2O1','0.1Na1Cl1'] h2o/d2o mixture with 100mMol NaCl
    units : default='mol'
        Anything except 'mol' unit is mass fraction
        'mol' units is mol and mass fraction is calculated as mass=[mol]*mass_of_molecule
        e.g. 1l Water with 123mM NaCl   ['55.5H2O1','0.123Na1Cl1']
    T : float, default=293.15
        temperature in K
    showvalidity : bool, default False
        Show additionally validity range for temperature and concentration according to [4]_.
        - Temperature range in °C
        - concentration in wt % or up to a saturated solution (satd)
        - error in 1/100 % see [4]_.

    Returns
    -------
    float
        Density in g/ml

    Notes
    -----
    - D2O maximum density 1.10596 at T=273.15+11.23 K [1]_ .
    - For mixtures of H2O/D2O molar volumes add with an accuracy of about 2e-4 cm**3/mol
      compared to 18 cm**3/mol molar volume [3]_.
    - Additional densities of binary aqueous solutions [4]_.

    References
    ----------
    .. [1] The dilatation of heavy water
           K. Stokland, E. Ronaess and L. Tronstad Trans. Faraday Soc., 1939,35, 312-318 DOI: 10.1039/TF9393500312
    .. [2] Effects of Isotopic Composition, Temperature, Pressure, and Dissolved Gases on the Density of Liquid Water
           George S. Kell JPCRD 6(4) pp. 1109-1131 (1977)
    .. [3] Excess volumes for H2O + D2O liquid mixtures
           Bottomley G Scott R  Australian Journal of Chemistry 1976 vol: 29 (2) pp: 427
    .. [4] Densities of binary aqueous solutions of 306 inorganic substances
           P. Novotny, O. Sohnel  J. Chem. Eng. Data, 1988, 33 (1), pp 49–55   DOI: 10.1021/je00051a018

    availible components::

     h2o1 d2o1
     TRIS c4h11n1o3
     TABS c8h19n1o6s1

    """
    mw = 18.01528  # mol weight water
    T -= 273.15

    #: water density
    def wdensity(T, a0, a1, a2, a3, a4, a5, b):
        return (a0 + a1 * T + a2 * T ** 2 + a3 * T ** 3 + a4 * T ** 4 + a5 * T ** 5) / (1 + b * T) / 1000.

    # 5-100 °C
    # D2O max density 1.10596 at T=11,23°C from Stokeland Trans. Faraday Soc., 1939,35, 312-31
    # we use here 1104.633 instead of the original 1104.7056 of Kell to get the max density correct
    cD2O = [1104.633, 28.88152, -7.652899e-3, -136.61854e-6, 534.7350e-9, -1361.843e-12, 25.91488e-3]
    # 0-150 K
    cH2O = [999.84252, 16.945227, -7.9870641e-3, -46.170600e-6, 105.56334e-9, -280.54337e-12, 16.879850e-3]

    # additional density due to added inorganic components
    def _getadddensity(c, TT, decompp):
        pp = _aquasolventdensity[decompp]
        if decompp == 'c4h11n1o3':
            return pp[0] * c ** pp[1]
        elif decompp == 'c8h19n1o6s1':
            return pp[0] * c ** pp[1]
        else:
            if showvalidity:
                print(decompp, ': Temperaturerange: ', pp[7], ' concentration: ', pp[8], ' error %:', pp[6])
            return (pp[0] * c + pp[1] * c * TT + pp[2] * c * TT * TT + pp[3] * c ** (3 / 2.) + pp[4] * c ** (
                    3 / 2.) * TT + pp[5] * c ** (3 / 2.) * TT * TT) * 1e-3

    cd2o = 0
    ch2o = 0
    nonwaterlist = {}
    adddensity = 0
    if isinstance(composition, str):
        composition = [composition]
    for compo in composition:
        compo = compo.lower()
        decomp = re.findall(r'\d+\.\d+|\d+|\D+', compo)
        if not re.match(r'\d', decomp[0]):  # add a 1 as concentration in front if not there
            decomp = [1] + decomp
        if not re.match(r'\d+\.\d+|\d+', decomp[-1]):
            raise KeyError('last %s Element missing following number ' % decomp[-1])
        mass = np.sum([Elements[ele][1] * float(num) for ele, num in zip(decomp[1:][::2], decomp[1:][1::2])])
        if units.lower() != 'mol':
            # we convert here from mass to mol
            concentration = float(decomp[0]) / mass
        else:
            concentration = float(decomp[0])  # concentration of this component
        decomp1 = ''.join(decomp[1:])
        if decomp1 == 'h2o1':
            ch2o += concentration
        elif decomp1 == 'd2o1':
            cd2o += concentration
        else:
            nonwaterlist[decomp1] = concentration
    wff = (1000 / mw) / (ch2o + cd2o)
    for k, v in nonwaterlist.items():
        # additional density due to components
        adddensity += _getadddensity(v * wff, T, k)
    density = cd2o / (cd2o + ch2o) * wdensity(T, cD2O[0], cD2O[1], cD2O[2], cD2O[3], cD2O[4], cD2O[5], cD2O[6])
    density += ch2o / (cd2o + ch2o) * wdensity(T, cH2O[0], cH2O[1], cH2O[2], cH2O[3], cH2O[4], cH2O[5], cH2O[6])
    return density + adddensity


# complete the docstring from above
_aqlist = sorted(_aquasolventdensity.keys())
_i = 0
while _i < len(_aqlist):
    waterdensity.__doc__ += '     ' + ''.join([' %-12s' % cc for cc in _aqlist[_i:_i + 6]]) + '\n'
    _i += 6
waterdensity.__doc__ += '\n'


def scatteringLengthDensityCalc(composition, density=None, T=293, units='mol', mode='all'):
    """
    Scattering length density of composites and water with inorganic components for xrays and neutrons.

    Parameters
    ----------
    composition : list of concentration + chemical formula
        A string with chemical formula as letter + number and prepended concentration in mol or mmol.
        E.g. '0.1C3H8O3' or '0.1C3H1D7O3' for glycerol and deuterated glycerol ('D' for deuterium).
         - For single atoms append 1 to avoid confusion.
           Fractional numbers allowed, but think of meaning (Isotope mass fraction??)
         - For compositions use a list of strings preceded by mass fraction or concentration
           in mol of component. This will be normalized to total amount

        Examples:
         - ['4.5H2O1','0.5D2O1'] mixture of 10% heavy and 90% light water.
         - ['1.0h2o','0.1c3h8o3'] for 10% mass glycerol added to  100% h2o with units='mass'
         - ['55000H2O1','50Na3P1O4','137Na1Cl1'] for a 137mMol NaCl +50mMol phophate H2O buffer (1l is 55000 mM H2O)
         - ['1Au1']  gold with density 19.302 g/ml

        Remember to adjust density.
    density : float, default=None
        Density in g/cm**3 = g/ml.
         - If not given function waterdensity is tried to calculate the solution density with
           inorganic components. In this case 'h2o1' and/or 'd2o1' need to be in composition.
         - Measure by weighting a volume from pipette (lower accuracy) or densiometry (higher accuracy).
         - Estimate for deuterated compounds from protonated density according to additional D.
           Mass change is given with mode='all'.
    units : 'mol'
        Anything except 'mol' prepended unit is mass fraction (default).
        'mol' prepended units is mol and mass fraction is calculated as mass=[mol]*mass_of_molecule
        e.g. 1l Water with 123mmol NaCl   ['55.5H2O1','0.123Na1Cl1']
    mode :
        - 'xsld'      xray scattering length density       in  nm**-2
        - 'edensity'  electron density                     in e/nm**3
        - 'ncohsld'   coherent scattering length density   in  nm**-2
        - 'incsld'    incoherent scattering length density in  nm**-2
        - 'all'       [xsld, edensity, ncohsld, incsld,
                       masses, masses full protonated, masses full deuterated,
                       d2o/h2o fraction in composition]
    T : float, default=293
        Temperature in °K

    Returns
    -------
    float, list
        sld corresponding to mode

    Notes
    -----
    - edensity=be*massdensity/weightpermol*sum_atoms(numberofatomi*chargeofatomi)
    - be = scattering length electron =µ0*e**2/4/pi/m=2.8179403267e-6 nm
    - masses, masses full protonated, masses full deuterated for each chemical in composition.
    - In mode 'all' the masses can be used to calc the deuterated density if same volume is assumed.
      e.g. fulldeuterated_density=protonated_density/massfullprotonated*massfulldeuterated

    For density reference of H2O/D2O see waterdensity.

    Examples
    --------
    ::

     # 5% D2O in H2O with 10% mass NaCl
     js.formel.scatteringLengthDensityCalc(['9.5H2O1','0.5D2O1','1Na1Cl1'],units='mass')
     # protein NaPi buffer in D2O prevalue in mmol; 55000 mmol H2O is 1 liter.
     js.formel.scatteringLengthDensityCalc(['55000D2O1','50Na3P1O4','137Na1Cl1'])
     # silica
     js.formel.scatteringLengthDensityCalc('1Si1O2',density=2.65)
     # gold
     js.formel.scatteringLengthDensityCalc(['1Au1'],density=19.32)
     # PEG1000
     js.formel.scatteringLengthDensityCalc(['1C44H88O23'],density=1.21)

    """
    edensity = []
    bcdensity = []
    bincdensity = []
    total = 0
    # totalmass = 0
    d2o = 0
    h2o = 0
    massfullprotonated = []
    massfulldeuterated = []
    totalmass = []
    if not isinstance(density, (numbers.Number, np.ndarray)):
        density = waterdensity(composition, T=T, units=units)
    density = float(density)
    if isinstance(composition, str):
        composition = [composition]
    for compo in composition:
        compo = compo.lower()
        # decompose in numbers and characters
        decomp = re.findall(r'\d+\.\d+|\d+|\D+', compo)
        if not re.match(r'\d', decomp[0]):  # add a 1 as concentration in front if not there
            decomp = [1] + decomp
        mass = np.sum([Elements[ele][1] * float(num) for ele, num in zip(decomp[1:][::2], decomp[1:][1::2])])
        if units.lower() == 'mol':
            # if units=mol we convert here from mol to mass fraction
            massfraction = float(decomp[0]) * mass
        else:
            massfraction = float(decomp[0])
        sumZ = 0
        b_coherent = 0
        b_incoherent = 0
        # check for completeness at end
        if not re.match(r'\d+\.\d+|\d+', decomp[-1]):
            raise KeyError('last %s Element missing following number ' % decomp[-1])
        massfullprotonated += [0]
        massfulldeuterated += [0]
        for ele, num in zip(decomp[1:][::2], decomp[1:][1::2]):
            if ele in Elements.keys():
                num = float(num)
                sumZ += Elements[ele][0] * num
                massfullprotonated[-1] += (Elements['h'][1] * num) if ele in ['h', 'd'] else (Elements[ele][1] * num)
                massfulldeuterated[-1] += (Elements['d'][1] * num) if ele in ['h', 'd'] else (Elements[ele][1] * num)
                b_coherent += Elements[ele][2] * num
                b_incoherent += Elements[ele][3] * num
            else:
                print('decomposed to \n', decomp)
                raise KeyError('"%s" not found in Elements' % ele)

        # density[g/cm^3] / mass[g/mol]= N in mol/cm^3 --> N*Z is charge density
        if ''.join(decomp[1:]) == 'h2o1': h2o += massfraction
        if ''.join(decomp[1:]) == 'd2o1': d2o += massfraction
        edensity.append(massfraction * density * (constants.N_A / 1e21) / mass * sumZ)
        bcdensity.append(massfraction * density * (constants.N_A / 1e21) / mass * b_coherent)
        bincdensity.append(massfraction * density * (constants.N_A / 1e21) / mass * b_incoherent)
        totalmass += [mass]
        total += massfraction
    if mode[0] == 'e':
        return sum(edensity) / total
    elif mode[0] == 'x':
        return sum(edensity) / total * felectron
    elif mode[0] == 'n':
        return sum(bcdensity) / total
    elif mode[0] == 'i':
        return sum(bincdensity) / total
    else:
        return sum(edensity) / total * felectron, \
               sum(edensity) / total, \
               sum(bcdensity) / total, \
               sum(bincdensity) / total, \
               totalmass, \
               massfullprotonated, \
               massfulldeuterated, \
               d2o / (h2o + d2o) if h2o + d2o != 0 else 0


def watercompressibility(d2ofract=1, T=278, units='psnmg'):
    """
    Isothermal compressibility of H2O and D2O mixtures.

    Compressibility in units  ps^2*nm/(g/mol) or in 1/bar. Linear mixture according to d2ofract.

    Parameters
    ----------
    d2ofract : float, default 1
        Fraction D2O
    T : float, default 278K
        Temperature  in K
    units : string 'psnmg'
        ps^2*nm/(g/mol) or 1/bar

    Returns
    -------
    float

    Notes
    -----
    To get kT*compressibility =compr*k_B/Nav*300/cm**3    in  hwater 1.91e-24 cm**3 at 20°C

    References
    ----------
    .. [1] Isothermal compressibility of Deuterium Oxide at various Temperatures
          Millero FJ and Lepple FK   Journal of chemical physics 54,946-949 (1971)   http://dx.doi.org/10.1063/1.1675024
    .. [2] Precise representation of volume properties of water at one atmosphere
          G. S. Kell J. Chem. Eng. Data, 1967, 12 (1), pp 66–69  http://dx.doi.org/10.1021/je60032a018

    """
    t = T - 273.15

    def h2o(t):
        ll = (50.9804 -
              0.374957 * t +
              7.21324e-3 * t ** 2 -
              64.1785e-6 * t ** 3 +
              0.343024e-6 * t ** 4 -
              0.684212e-9 * t ** 5)
        return 1e-6 * ll

    def d2o(t):
        return 1e-6 * (53.61 - 0.4717 * t + 0.009703 * t ** 2 - 0.0001015 * t ** 3 + 0.0000005299 * t ** 4)

    comp_1overbar = d2ofract * d2o(t) + (1 - d2ofract) * h2o(t)
    # MMTK units  ps, nm, g/mol
    if units == 'psnmg':
        # factor=1e-8*m*s**2/(g/Nav)
        factor = 1e-8 * 1e9 * 1e12 ** 2  # /(6.0221366999999997e+23/6.0221366999999997e+23)
    else:
        factor = 1
    compressibility_psnmgUnits = comp_1overbar * factor
    return compressibility_psnmgUnits


def dielectricConstant(material='d2o', T=293.15, conc=0, delta=5.5):
    r"""
    Dielectric constant of H2O and D2O buffer solutions.

    Dielectric constant :math:`\epsilon` of H2O and D2O (error +- 0.02) with added buffer salts.

    .. math:: \epsilon (c)=\epsilon (c=0)+2c\: delta\;  for\; c<2M

    Parameters
    ----------
    material : string 'd2o' (default)   or 'h2o'
        Material 'd2o' (default) or 'h2o'
    T : float
        Temperature in °C
    conc : float
        Salt concentration in mol/l.
    delta : float
        Total excess polarisation dependent on the salt and presumably on the temperature!


    Returns
    -------
    float
        Dielectric constant

    Notes
    -----
    ======  ========== ===========================
    Salt    delta(+-1) deltalambda (not used here)
    ======  ========== ===========================
    HCl     -10            0
    LiCl     7            -3.5
    NaCl     5.5          -4   default
    KCl      5            -4
    RbCl     5            -4.5
    NaF      6            -4
    KF       6.5          -3.5
    NaI     -7.5          -9.5
    KI      -8            -9.5
    MgCI,   -15           -6
    BaCl2   -14           -8.5
    LaCI.   -22           -13.5
    NaOH    -10.5         -3
    Na2SO.  -11           -9.5
    ======  ========== ===========================

    References
    ----------
    .. [1] Dielectric Constant of Water from 0 to 100
           C. G . Malmberg and A. A. Maryott
           Journal of Research of the National Bureau of Standards, 56,1 ,369131-56--1 (1956) Research Paper 2641
    .. [2] Dielectric Constant of Deuterium Oxide
          C.G Malmberg, Journal of Research of National Bureau of Standards, Vol 60 No 6, (1958) 2874
          http://nvlpubs.nist.gov/nistpubs/jres/60/jresv60n6p609_A1b.pdf
    .. [3] Dielectric Properties of Aqueous Ionic Solutions. Parts I and II
          Hasted et al. J Chem Phys 16 (1948) 1   http://link.aip.org/link/doi/10.1063/1.1746645

    """
    if material == 'h2o':
        diCo = lambda t: 87.740 - 0.4008 * (t - 273.15) + 9.398e-4 * (t - 273.15) ** 2 - 1.410e-6 * (t - 273.15) ** 3
        return diCo(T) + 2 * delta * conc
    elif material == 'd2o':
        diCo = lambda t: 87.48 - 0.40509 * (t - 273.15) + 9.638e-4 * (t - 273.15) ** 2 - 1.333e-6 * (t - 273.15) ** 3
    return diCo(T) + 2 * delta * conc


###################################################

def cstar(Rg, Mw):
    r"""
    Overlap concentration :math:`c^*` for a polymer.

    Equation 3 in [1]_ (Cotton) defines :math:`c^*` as overlap concentration of space filling volumes
    corresponding to a cube or sphere with edge/radius equal to :math:`R_g`

    .. math:: \frac{ M_w }{ N_A R_g^3} \approx c^* \approx \frac{3M_w}{4N_A \pi R_g^3}

    while equ. 4 uses cubes with :math:`2R_g` (Graessley) :math:`c^* = \frac{ M_w }{ N_A 2R_g^3 }` .


    Parameters
    ----------
    Rg : float  in nm
        radius of gyration
    Mw : float
        molecular weight

    Returns
    -------
    float : x3
        Concentration limits
        [cube_rg, sphere_rg, cube_2rg] in units g/l.

    References
    ----------
    .. [1]  Overlap concentration of macromolecules in solution
            Ying, Q. & Chu, B. Macromolecules 20, 362–366 (1987)

    """
    cstar_sphere = 3. * Mw / (constants.Avogadro * 4 * np.pi * (Rg * 1E-9) ** 3) / 1000  # in g/l
    cstar_cube = Mw / (constants.Avogadro * (Rg * 1E-9) ** 3) / 1000  # in g/l
    cstar_cube2 = Mw / (constants.Avogadro * (2 * Rg * 1E-9) ** 3) / 1000  # in g/l
    return cstar_cube, cstar_sphere, cstar_cube2


def Dtrans(Rh, Temp=293.15, solvent='h2o', visc=None):
    """
    Translational diffusion of a sphere.

    Parameters
    ----------
    Rh : float
        Hydrodynamic radius in nm.
    Temp : float
        Temperature in K.
    solvent : float
        Solvent type as in viscosity; used if visc==None.
    visc : float
        Viscosity in Pas => H2O ~ 0.001 Pas =1 cPoise.
        If visc=None the solvent viscosity is calculated from
        function viscosity(solvent ,temp) with solvent eg 'h2o' (see viscosity).

    Returns
    -------
    float
        Translational diffusion coefficient : float in nm^2/ns.

    """

    if visc is None:
        visc = viscosity(solvent, Temp)  # unit Pa*s= kg/m/s
    D0 = constants.k * Temp / (6 * math.pi * visc * Rh * 1e-9)  # Rh in m   D0 in m**2/s
    return D0 * 1e9  # with conversion to unit nm**2/ns


D0 = Dtrans


def Drot(Rh, Temp=293.15, solvent='h2o', visc=None):
    """
    Rotational diffusion of a sphere.

    Parameters
    ----------
    Rh : float
        Hydrodynamic radius in nm.
    Temp : float
        Temperature   in K.
    solvent : float
        Solvent type as in viscosity; used if visc==None.
    visc : float
        Viscosity in Pas => H2O ~ 0.001 Pa*s =1 cPoise.
        If visc=None the solvent viscosity is calculated from
        function viscosity(solvent ,temp) with solvent eg 'h2o'.

    Returns
    -------
    float
        Rotational diffusion coefficient in 1/ns.

    """

    if visc is None:
        visc = viscosity(solvent, Temp)  # conversion from Pa*s= kg/m/s
    Dr = constants.k * Temp / (8 * math.pi * visc * (Rh * 1e-9) ** 3)  # Rh in m
    return Dr * 1e-9  # 1/ns


def bicelleRh(Q, rim, thickness, k=1/0.6):
    r"""
    Hydrodynamic radius Rh of an ideal bicelle corrected for head group area.

    Parameters
    ----------
    Q : float
        Ratio of lipid composition
    rim : float
        Radius of the rim.
    thickness : float
        Thickness of the bicelle planar region
    k : float
        Head group area ratio. like 1/0.6 for rim DHCP 1nm² and planar DMPC 0.6nm²

    Returns
    -------
        [Rh : float, R: float, R + rim]

        R radius of the planar region

    Notes
    -----
    Bicelle radius R with lipid area correction factor k [1]_ :

    .. math:: R = \frac{1}{2} k r Q [\pi +(\pi^2 + 8k/Q)^{1/2}]

    Rh of a (rectangular) disk with radius :math:`r^{\prime}` and thickness *t* (same for a longer rod t>r') [2]_ :

    .. math::  R_h = \frac{3}{2}r^{\prime} \Big[[1+(\frac{t}{2r^{\prime}})^2]^{1/2}-\frac{t}{2r^{\prime}} +
                         \frac{2r^{\prime}}{t} ln\big(\frac{t}{2r^{\prime}} +
                         [1+(\frac{t}{2r^{\prime}})^2]^{1/2}\big)\Big]^{-1}

    with :math:`r^{\prime} = R+r` outer radius, rim radius :math:`r`, lipid ratio :math:`Q`, thickness *t*

    It should be noted that in the references reporting this equation the hydrodynamic radius
    from DLS measurements is reported to be concentration dependent.
    This results from ignoring the structure factor effects
    (see :py:func:`~jscatter.structurefactor.hydrodynamicFunct`) and leads to misinterpretation of the disc radius.


    References
    ----------
    .. [1] Structural Evaluation of Phospholipid Bicelles for Solution-State Studies of Membrane-Associated Biomolecules
           Glover, et al.Biophysical Journal 81(4), 2163–2171 (2001)

    .. [2] Quasielastic Light-Scattering Studies of Aqueous Biliary Lipid Systems.
           Mixed Micelle Formation in Bile Salt-Lecithin Solutions
           Mazer et al.Biochemistry 19, 601–615 (1980), https://doi.org/10.1021/bi00545a001

    """
    R = 0.5*k*rim*Q*(np.pi+(np.pi**2+8*k/Q)**0.5)
    rr = R + rim
    to2r = thickness/2/rr
    tor1 = (1 + to2r**2)**0.5
    Rh = 1.5*rr/(-to2r + tor1 + np.log(to2r + tor1) / to2r)

    return Rh, R, rr


def molarity(objekt, c, total=None):
    """
    Calculates the molarity.

    Parameters
    ----------
    objekt : object,float
        Objekt with method .mass() or molecular weight in Da.
    c : float
        Concentration in g/ml -> mass/Volume
    total : float, default None
        Total volume in milliliter  [ml]
        Concentration is calculated by c[g]/total[ml] if given.

    Returns
    -------
    float
        molarity in mol/liter (= mol/1000cm^3)

    """
    if c > 1:
        print('c limited to 1')
        c = 1.
    if hasattr(objekt, 'mass'):
        mass = objekt.mass()
    else:
        mass = objekt
    if total is not None:
        c = abs(float(c) / (float(total)))  # pro ml (cm^^3)  water density =1000g/liter
    if c > 1:
        print('concentration c has to be smaller 1 unit is g/ml')
        return
    weightPerl = c * 1000  # weight   per liter
    numberPerl = (weightPerl / (mass / constants.N_A))
    molarity = numberPerl / constants.N_A
    return molarity


def T1overT2(tr=None, Drot=None, F0=20e6, T1=None, T2=None):
    r"""
    Calculates the T1/T2 from a given rotational correlation time tr or Drot for proton relaxation measurement.

    tr=1/(6*D_rot)  with rotational diffusion D_rot and correlation time tr.

    Parameters
    ----------
    tr : float
        Rotational correlation time.
    Drot : float
        If given tr is calculated from Drot.
    F0 : float
        NMR frequency e.g. F0=20e6 Hz=> w0=F0*2*np.pi is for Bruker Minispec
        with B0=0.47 Tesla
    T1 : float
        NMR T1 result in s
    T2 : float
        NMR T2 resilt in s     to calc t12 directly

    Returns
    -------
    float
        T1/T2

    Notes
    -----

    :math:`J(\omega)=\tau/(1+\omega^2\tau^2)`

    :math:`T1^{-1}=\frac{\sigma}{3} (2J(\omega_0)+8J(2\omega_0))`

    :math:`T2^{-1}=\frac{\sigma}{3} (3J(0)+ 5J(\omega_0)+2J(2\omega_0))`

    :math:`tr=T1/T2`

    References
    ----------
    .. [1] Intermolecular electrostatic interactions and Brownian tumbling in protein solutions.
           Krushelnitsky A
           Physical chemistry chemical physics 8, 2117-28 (2006)
    .. [2] The principle of nuclear magnetism A. Abragam Claredon Press, Oxford,1961


    """
    w0 = F0 * 2 * np.pi
    J = lambda w, tr: tr / (1 + w ** 2 * tr ** 2)
    if Drot is not None:
        tr = 1. / (6 * Drot)

    t1sig3 = 1. / (2. * J(w0, tr) + 8. * J(2 * w0, tr))
    t2sig3 = 1. / (3. * tr + 5 * J(w0, tr) + J(2 * w0, tr))
    if T1 is not None:
        print('T1: %(T1).3g sigma = %(sigma).4g' % {'T1': T1, 'sigma': t1sig3 * 3. / T1})
    if T2 is not None:
        print('T2: %(T2).3g sigma = %(sigma).4g' % {'T2': T2, 'sigma': t2sig3 * 3. / T2})
    return t1sig3 / t2sig3


def DrotfromT12(t12=None, Drot=None, F0=20e6, Tm=None, Ts=None, T1=None, T2=None):
    """
    Rotational correlation time from  T1/T2 or T1 and T2 from NMR proton relaxation measurement.

    Allows to rescale by temperature and viscosity.

    Parameters
    ----------
    t12 : float
        T1/T2 from NMR with unit seconds
    Drot : float
        !=None means output Drot instead of rotational correlation time.
    F0 : float
        Resonance frequency of NMR instrument. For Hydrogen F0=20 MHz => w0=F0*2*np.pi
    Tm: float
        Temperature of measurement in K.
    Ts :  float
        Temperature needed for Drot   -> rescaled by visc(T)/T.
    T1 : float
        NMR T1 result in s
    T2 : float
        NMR T2 result in s     to calc t12 directly
        remeber if the sequence has a factor of 2

    Returns
    -------
    float
        Correlation time or Drot

    Notes
    -----
    See T1overT2

    """
    if T1 is not None and T2 is not None and t12 is None:
        t12 = T1 / T2
    if Tm is None:
        Tm = 293
    if Ts is None:
        Ts = Tm
    if t12 is not None:
        diff = lambda tr, F0: T1overT2(tr=tr, Drot=None, F0=F0, T1=None, T2=None) - t12
        # find tr where diff is zero to invert the equation
        trr = scipy.optimize.brentq(diff, 1e-10, 1e-5, args=(F0,))
        # rescale with visc(T)/T
        tr = trr * (Tm / viscosity('d2o', T=Tm)) / (Ts / viscosity('d2o', T=Ts))
        print('tau_rot: {trr:.3g} at Tm={Tm:.5g} \ntau_rot: {tr:.5g} at Ts={Ts:.3g} \n  '
              '(scalled by Tm/viscosity(Tm)/(T/viscosity(T)) = {rv:.4g}'.
              format(trr=trr, Tm=Tm, tr=tr, Ts=Ts, rv=tr / trr))
    else:
        raise Exception('give t12 or T1 and T2')
    # temp = T1overT2(trr, F0=F0, T1=T1, T2=T2)
    print('D_rot= : %(drot).4g ' % {'drot': 1 / (6 * tr)})
    if Drot is not None:
        Drot = 1 / (6 * tr)
        print('returns Drot')
        return Drot
    return tr


def sedimentationProfileFaxen(t=1e3, rm=48, rb=85, number=100, rlist=None, c0=0.01, s=None, Dt=1.99e-11, w=246,
                              Rh=10, visc='h2o', temp=293, densitydif=None):
    """
    Faxen solution to the Lamm equation of sedimenting particles in centrifuge; no bottom part.

    Bottom equillibrium distribution is not in Faxen solution included.
    Results in particle distribution along axis for time t.

    Parameters
    ----------
    t : float
        Time after start in seconds. If list, results at these times is given as dataList.
    rm : float
        Axial position of meniscus in mm.
    rb : float
        Axial position of bottom in mm.
    rlist : array, optional
        Explicit list of radial values to use between rm=max(rlist) and rb=min(rlist)
    number : integer
        Number of points between rm and rb to calculate.
    c0 : float
        Initial concentration in cell; just a scaling factor.
    s : float
        Sedimentation coefficient in Svedberg; 77 S is r=10 nm particle in H2O.
    Dt : float
        Translational diffusion coefficient in m**2/s; 1.99e-11 is r=10 nm particle.
    w : float
        Radial velocity rounds per second; 246 rps=2545 rad/s  is 20800g in centrifuge fresco 21.
    Rh : float
        Hydrodynamic radius in nm ; if given  Dt and s are calculated from Rh.
    visc : float, 'h2o','d2o'
        Viscosity in units Pas.
        If 'h2o' or 'd2o' the corresponding viscosity at given temperature is used.
    densitydif : float
        Density difference between solvent and particle in g/ml.
        Protein in 'h2o'=> is used =>1.37-1.= 0.37 g/cm**3
    temp : float
        temperature in K.

    Returns
    -------
    dataArray, dataList
        Concentration distribution : dataArray, dataList
         .pelletfraction is the content in pellet as fraction already diffused out
         .rmeniscus

    Notes
    -----
    Default values are for Heraeus Fresco 21 at 21000g.

    References
    ----------
    .. [1] Über eine Differentialgleichung aus der physikalischen Chemie.
           Faxén, H. Ark. Mat. Astr. Fys. 21B:1-6 (1929)

    """
    # get solvent viscosity
    if visc in ['h2o', 'd2o']:
        visc = viscosity(visc, temp)
    if densitydif is None:
        densitydif = 0.37  # protein - water
    densitydif *= 1e3  # to kg/m³
    svedberg = 1e-13

    if Rh is not None:
        Dt = constants.k * temp / (6 * math.pi * visc * Rh * 1e-9)
        s = 2. / 9. / visc * densitydif * (Rh * 1e-9) ** 2
    else:
        s *= svedberg  # to SI units

    rm = rm /1000.
    rb = rb /1000.  # end
    r = np.r_[rm:rb:number * 1j]  # nn points
    if rlist is not None:
        rm = min(rlist)
        # rb = max(rlist)  # not used here
        r = rlist / 1000.
    w = w * 2 * np.pi

    timelist = dL()
    for tt in np.atleast_1d(t):
        ct = (0.5 * c0 * np.exp(-2. * s * w ** 2 * tt))
        cr = (1 - scipy.special.erf((rm * (w ** 2 * s * tt + np.log(rm) - np.log(r))) / (2. * np.sqrt(Dt * tt))))
        timelist.append(dA(np.c_[r * 1000, cr * ct].T))
        timelist[-1].time = tt
        timelist[-1].rmeniscus = rm
        timelist[-1].w = w
        timelist[-1].Dt = Dt
        timelist[-1].c0 = c0
        timelist[-1].viscosity = visc
        timelist[-1].sedimentation = s / svedberg
        timelist[-1].pelletfraction = 1 - scipy.integrate.simps(y=timelist[-1].Y, x=timelist[-1].X) / (
                max(r) * 1000 * c0)
        timelist[-1].modelname = inspect.currentframe().f_code.co_name
        if Rh is not None: timelist[-1].Rh = Rh
    if len(timelist) == 1:
        return timelist[0]
    return timelist


def sedimentationProfile(t=1e3, rm=48, rb=85, number=100, rlist=None, c0=0.01, S=None, Dt=None, omega=246,
                         Rh=10, temp=293, densitydif=0.37, visc='h2o'):
    r"""
    Concentration profile of sedimenting particles in a centrifuge including bottom equilibrium distribution.

    Approximate solution to the Lamm equation including the bottom equilibrium distribution
    which is not included in the Faxen solution. This calculates equ. 28 in [1]_.
    Results in particle concentration profile between rm and rb for time t with a equal distribution at the start.

    Parameters
    ----------
    t : float or list
        Time after centrifugation start in seconds.
        If list, a dataList for all times is returned.
    rm : float
        Axial position of meniscus in mm.
    rb : float
        Axial position of bottom in mm.
    number : int
        Number of points between rm and rb to calculate.
    rlist : list of float
        Explicit list of positions where to calculate eg to zoom bottom.
    c0 : float
        Initial concentration in cell; just a scaling factor.
    S : float
        Sedimentation coefficient in units Svedberg; 82 S is r=10 nm protein in H2O at T=20C.
    Dt : float
        Translational diffusion coefficient in m**2/s; 1.99e-11 is r=10 nm particle.
    omega : float
        Radial velocity rounds per second; 14760rpm = **246 rps** = 1545 rad/s  is 20800g in centrifuge fresco 21.
    Rh : float
        Hydrodynamic radius in nm ; if given the Dt and s are calculated from this.
    densitydif : float
        Density difference between solvent and particle in g/ml;
        Protein in 'h2o' => 1.37-1.= 0.37 g/cm**3.
    visc : float, 'h2o', 'd2o'
        Viscosity of the solvent in Pas. (H2O ~ 0.001 Pa*s =1 cPoise)
        If 'h2o' or 'd2o' the corresponding viscosity at given temperature is used.
    temp : float
        temperature in K.

    Returns
    -------
    dataArray, dataList
        Concentration profile
        Columns  [position in [mm]; conc ; conc_meniscus_part; conc_bottom_part]

    Notes
    -----
    From [1]_:"The deviations from the expected results are smaller than 1% for simulated curves and are valid for a
    great range of molecular masses from 0.4 to at least 7000 kDa. The presented approximate solution,
    an essential part of LAMM allows the estimation of s and D with an accuracy comparable
    to that achieved using numerical solutions, e.g the program SEDFIT of Schuck et al."

    Default values are for Heraeus Fresco 21 at 21000g.

    Examples
    --------
    Cleaning from aggregates by sedimantation.
    Sedimentation of protein (R=2 nm) with aggregates of 100nm size.
    ::

     import numpy as np
     import jscatter as js
     t1=np.r_[60:1.15e3:11j]  # time in seconds

     # open plot()
     p=js.grace(1.5,1.5)
     p.multi(2,1)

     # calculate sedimentation profile for two different particles
     # data correspond to Fresco 21 with dual rotor
     # default is solvent='h2o',temp=293
     g=21000. # g # RZB number
     omega=g*246/21000
     D2nm=js.formel.sedimentationProfile(t=t1,Rh=2,densitydif=0.37, number=1000)
     D50nm=js.formel.sedimentationProfile(t=t1,Rh=50,densitydif=0.37, number=1000)

     # plot it
     p[0].plot(D2nm,li=[1,2,-1],sy=0,legend='t=$time s' )
     p[1].plot(D50nm,li=[1,2,-1],sy=0,legend='t=$time s' )

     # pretty up
     p[0].yaxis(min=0,max=0.05,label='concentration')
     p[1].yaxis(min=0,max=0.05,label='concentration')
     p[1].xaxis(label='position mm')
     p[0].xaxis(label='')
     p[0].text(x=70,y=0.04,string=r'R=2 nm \nno sedimantation')
     p[1].text(x=70,y=0.04,string=r'R=50 nm \nfast sedimentation')
     p[0].legend(x=42,y=0.05,charsize=0.5)
     p[1].legend(x=42,y=0.05,charsize=0.5)
     p[0].title('Concentration profile in first {0:} s'.format(np.max(t1)))
     p[0].subtitle('2nm and 50 nm particles at 21000g ')
     #p.save(js.examples.imagepath+'/sedimentation.jpg')

    .. image:: ../../examples/images/sedimentation.jpg
     :align: center
     :height: 300px
     :alt: convolve


    Sedimentation (up concentration) of unilamellar liposomes of DOPC.
    The density of DOPC is about 1.01 g/ccm in water with 1 g/ccm.
    Lipid volume fraction is 33% for 50nm radius (10% for 200 nm) for a bilayer thickness of 6.5 nm. ::

     import numpy as np
     import jscatter as js

     t1=np.r_[100:6e3:11j]  # time in seconds

     # open plot()
     p=js.grace(1.5,1.5)
     p.multi(2,1)

     # calculate sedimentation profile for two different particles
     # data correspond to Fresco 21 with dual rotor
     # default is solvent='h2o',temp=293
     g=21000. # g # RZB number
     omega=g*246/21000
     D100nm=js.formel.sedimentationProfile(t=t1,Rh=50,c0=0.05,omega=omega,rm=48,rb=85,densitydif=0.003)
     D400nm=js.formel.sedimentationProfile(t=t1,Rh=200,c0=0.05,omega=omega,rm=48,rb=85,densitydif=0.001)

     # plot it
     p[0].plot(D100nm,li=[1,2,-1],sy=0,legend='t=$time s' )
     p[1].plot(D400nm,li=[1,2,-1],sy=0,legend='t=$time s' )

     # pretty up
     p[0].yaxis(min=0,max=0.2,label='concentration')
     p[1].yaxis(min=0,max=0.2,label='concentration')
     p[1].xaxis(label='position mm')
     p[0].xaxis(label='')
     p[0].text(x=70,y=0.15,string='D=100 nm')
     p[1].text(x=70,y=0.15,string='D=400 nm')
     p[0].legend(x=42,y=0.2,charsize=0.5)
     p[1].legend(x=42,y=0.2,charsize=0.5)
     p[0].title('Concentration profile in first {0:} s'.format(np.max(t1)))
     p[0].subtitle('at 21000g ')



    References
    ----------
    .. [1] A new approximate whole boundary solution of the Lamm equation
           for the analysis of sedimentation velocity experiments
           J. Behlke, O. Ristau  Biophysical Chemistry 95 (2002) 59–68

    """
    # do all in SI units
    svedberg = 1e-13  # s

    if visc in ['h2o', 'd2o']:
        visc = viscosity(visc, temp)  # in Pa*s= kg/m/s
    densitydif *= 1e3  # g/ccm to kg/m³
    if isinstance(t, numbers.Number):
        t = np.r_[t]

    if Rh is not None:
        Dt = constants.k * temp / (6 * math.pi * visc * Rh * 1e-9)
        S = 2. * densitydif * (Rh * 1e-9) ** 2 / (9. * visc)
    else:
        S *= svedberg

    rm = rm /1000.  # meniscus in m
    rb = rb /1000.  # bottom in m
    r = np.r_[rm:rb:number * 1j]  # nn points in m
    if rlist is not None:  # explicit given list between meniscus and bottom
        r = rlist / 1000.
    # create variables for calculation
    omega = omega * 2 * np.pi  # in rad
    taulist = 2 * S * omega ** 2 * np.atleast_1d(t)  # timevariable for moving boundary

    # define functions using scipy and numpy functions
    erfc = scipy.special.erfc  # complementary error function
    erfcx = scipy.special.erfcx  # scaled complementary error function
    exp = np.exp
    sqrt = np.sqrt

    # moving meniscus part
    eps = 2 * Dt / (S * omega ** 2 * rm ** 2)
    w = 2 * (r / rm - 1)
    b = 1 - eps / 2.
    nn = 200

    def c1(tau):
        # moving boundary
        return erfc(
            (exp(tau / 2.) - 0.5 * w - 1 + 0.25 * eps * (exp(-tau / 2.) - exp(tau / 2.))) / sqrt(eps * (exp(tau) - 1)))

    def c2(tau):
        # error:  exp(b*w/eps) goes infinity even if erfc is zero
        # set above values to zero as it happens for large fast sedimenting particles
        ex = b * w / eps
        tm1 = 2 * (exp(tau / 2.) - 1)
        cc = np.zeros_like(ex)
        cc[ex < nn] = -exp(ex[ex < nn]) / (1 - b) * erfc((w[ex < nn] + b * tm1) / (2 * sqrt(eps * tm1)))
        return cc

    def c3(tau):
        # same as for c2
        tm1 = 2 * (exp(tau / 2.) - 1)
        xxerfc = (w + tm1 * (2 - b)) / (2 * sqrt(eps * tm1))
        ex = (w + tm1 * (1 - b)) / eps
        res = np.zeros_like(ex)
        res[ex < nn] = (2 - b) / (1 - b) * exp(ex[ex < nn]) * erfc(xxerfc[ex < nn])
        return res

    # final meniscus part
    cexptovercfax = lambda tau: c1(tau) + c2(tau) + c3(tau)

    # bottom part
    epsb = 2 * Dt / (S * omega ** 2 * rb ** 2)
    d = 1 - epsb / 2.
    z = 2 * (r / rb - 1)
    c4 = lambda tau: -erfc((d * tau - z) / (2 * sqrt(epsb * tau)))
    c5 = lambda tau: -exp(d * z / epsb) / (1 - d) * erfc((-z - d * tau) / (2 * sqrt(epsb * tau)))
    c6 = lambda tau: (2 - d) / (1 - d) * exp(((1 - d) * tau + z) / epsb) * erfc(
        (-z - (2 - d) * tau) / (2 * sqrt(epsb * tau)))
    # final bottom part
    cexptovercbottom = lambda tau: c4(tau) + c5(tau) + c6(tau)

    timelist = dL()
    for tau in taulist:
        bottom = cexptovercbottom(tau) * c0 / 2. / exp(tau)
        meniscus = cexptovercfax(tau) * c0 / 2. / exp(tau)
        timelist.append(dA(np.c_[r * 1000, meniscus + bottom, meniscus, bottom].T))
        timelist[-1].time = tau / (2 * S * omega ** 2)
        timelist[-1].rmeniscus = rm
        timelist[-1].rbottom = rb
        timelist[-1].w = w
        timelist[-1].Dt = Dt
        timelist[-1].c0 = c0
        timelist[-1].viscosity = visc
        timelist[-1].sedimentation = S / svedberg
        timelist[-1].modelname = inspect.currentframe().f_code.co_name
        # timelist[-1].pelletfraction=1-scipy.integrate.simps(y=timelist[-1].Y, x=timelist[-1].X)/(max(r)*1000*c0)
        if Rh is not None:
            timelist[-1].Rh = Rh
        timelist[-1].columnname = 'position; concentration; conc_meniscus_part; conc_bottom_part'
        timelist[-1].setColumnIndex(iey=None)
    if len(timelist) == 1:
        return timelist[0]
    return timelist


def sedimentationCoefficient(M, partialVol=None, density=None, visc=None):
    r"""
    Sedimentation coefficient of a sphere in a solvent.

    :math:`S = M (1-\nu \rho)/(N_A 6\pi \eta R)` with :math:`V = 4/3\pi R^3 = \nu M`


    Parameters
    ----------
    M : float
        Mass of the sphere or protein in units Da.
    partialVol : float
        Partial specific volume :math:`\nu` of the particle in units ml/g = l/kg.
        Default is 0.73 ml/g for proteins.
    density : float
        Density :math:`\rho` of the solvent in units g/ml=kg/l.
        Default is H2O at 293.15K
    visc : float
        Solvent viscosity :math:`\eta` in Pas.
        Default H2O at 293.15K

    Returns
    -------
    float
        Sedimentation coefficient in units Svedberg (1S = 1e-13 sec )


    """
    if visc is None:
        visc = viscosity()
    if density is None:
        density = waterdensity('h2o1')
    if partialVol is None:
        partialVol = 0.73  # partial specific volume of proteins in ml/g
    m = M / constants.N_A * 0.001  # mass in kg
    Rh = (m * (partialVol * 0.001) * 3. / 4. / np.pi) ** (1 / 3.)  # in units m
    return m * (1 - partialVol * density) / (6 * np.pi * visc * Rh) / 1e-13
