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

r"""
Models describing dynamic processes mainly for inelastic neutron scattering.

- Models in the time domain have a parameter t for time. -> intermediate scattering function :math:`I(t,q)`
- Models in the frequency domain have a parameter w for frequency and _w appended. ->
  dynamic structure factor :math:`S(w,q)`

Models in time domain can be transformed to frequency domain by :py:func:`~.dynamic.time2frequencyFF`
implementing the Fourier transform :math:`S(w,q)=F(I(t,q))`.

In time domain the combination of processes :math:`I_i(t,q)` is done by multiplication,
including instrument resolution :math:`R(t,q)`:

:math:`I(t,q)=I_1(t,q)I_2(t,q)R(t,q)`.
::

 # multiplying and creating new dataArray
 I(t,q) = js.dA( np.c[t, I1(t,q,..).Y*I2(t,q,..).Y*R(t,q,..).Y ].T)

In frequency domain it is a convolution, including the instrument resolution.

:math:`S(w,q) = S_1(w,q) \otimes S_2(w,q) \otimes R(w,q)`.
::

 conv=js.formel.convolve
 S(w,q)=conv(conv(S1(w,q,..),S2(w,q,..)),res(w,q,..),normB=True)      # normB normalizes resolution

FFT from time domain by :py:func:`time2frequencyFF` may include the resolution where it acts like a
window function to reduce spectral leakage with vanishing values at :math:`t_{max}`.
If not used :math:`t_{max}` needs to be large (see tfactor) to reduce spectral leakage.

The last step is to shift the model spectrum to the symmetry point of the instrument
as found in the resolution measurement and optional binning over frequency channels.
Both is done by :py:func:`~.dynamic.shiftAndBinning`.

**Example**

Let us describe the diffusion of a particle inside a diffusing invisible sphere
by mixing time domain and frequency domain.
::

 resolutionparameter={'s0':5,'m0':0,'a0':1,'bgr':0.00}
 w=np.r_[-100:100:0.5]
 resolution=js.dynamic.resolution_w(w,**resolutionparameter)
 # model
 def diffindiffSphere(w,q,R,Dp,Ds,w0,bgr):
     # time domain with transform to frequency domain
     diff_w=js.dynamic.time2frequencyFF(js.dynamic.simpleDiffusion,resolution,q=q,D=Ds)
     # last convolution in frequency domain, resolution is already included in time domain.
     Sx=js.formel.convolve(js.dynamic.diffusionInSphere_w(w=w,q=q,D=Dp,R=R),diff_w)
     Sxsb=js.dynamic.shiftAndBinning(Sx,w=w,w0=w0)
     Sxsb.Y+=bgr       # add background
     return Sxsb
 #
 Iqw=diffindiffSphere(w=w,q=5.5,R=0.5,Dp=1,Ds=0.035,w0=1,bgr=1e-4)


For more complex systems with different scattering length or changing contributions the fraction of
contributing atoms (with scattering length) has to be included.

Accordingly, if desired, the mixture of coherent and incoherent scattering needs to be accounted for
by corresponding scattering length.
This additionally is dependent on the used instrument e.g. for spin echo only 1/3 of the incoherent scattering
contributes to the signal.
An example model for protein dynamics is given in :ref:`Protein incoherent scattering in frequency domain`.

A comparison of different dynamic models in frequency domain is given in examples.
:ref:`A comparison of different dynamic models in frequency domain`.

For conversion to energy use
E = ℏ*w = js.dynamic.hbar*w with h/2π = 4.13566/2π [µeV*ns] = 0.6582 [µeV*ns]

Return values are dataArrays were useful.
To get only Y values use .Y

"""

import inspect
import math
import os
import sys
import numbers

import numpy as np
from numpy import linalg as la
import scipy
import scipy.integrate
import scipy.interpolate
import scipy.constants
import scipy.special as special

from . import dataArray as dA
from . import dataList as dL
from . import formel
from .formel import convolve

try:
    from . import fscatter

    useFortran = True
except ImportError:
    useFortran = False

pi = np.pi
_path_ = os.path.realpath(os.path.dirname(__file__))

#: Planck constant in µeV*ns
h = scipy.constants.Planck / scipy.constants.e * 1E15  # µeV*ns

#: h/2π  reduced Planck constant in µeV*ns
hbar = h/2/pi  # µeV*ns

try:
    # change in scipy 18
    spjn = special.spherical_jn
except AttributeError:
    spjn = lambda n, z: special.jv(n + 1 / 2, z) * np.sqrt(pi / 2) / (np.sqrt(z))


def simpleDiffusion(q, t, D, w=0, amplitude=1):
    """
    Intermediate scattering function for diffusing particles.

    .. math:: I(q,t)=Ae^{-q^2 (Dt + 0.5w^2t^2)}

    Parameters
    ----------
    q : float, array
        Wavevector
    t : float, array
        Times
    amplitude : float
        Prefactor
    D : float
        Diffusion coefficient in units [ [q]**-2/[t] ]
    w : float
        Width of diffusion coefficient distribution in D units.

    Returns
    -------
    dataArray


    """
    result = dA(np.c_[t, amplitude * np.exp(-q ** 2 * (D * t + 1 / 2. * abs(w) * w * t * t))].T)
    result.amplitude = amplitude
    result.Diffusioncoefficient = D
    result.wavevector = q
    result.columnname = 't;Iqt'
    result.setColumnIndex(iey=None)
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def doubleDiffusion(q, t, A0, D0, w0=0, A1=0, D1=0, w1=0):
    """
    Two exponential decaying functions describing diffusion.

    .. math:: I(q,t)=A_1e^{-q^2 (D_1t + 0.5w_1^2t^2)} + A_2e^{-q^2 (D_2t + 0.5w_2^2t^2)}

    Parameters
    ----------
    q : float, array
        Wavevector
    t : float, array
        Time list
    A0,A1 : float
        Prefactor
    D0,D1 : float
        Diffusion coefficient in units [ [q]**-2/[t] ]
    w0,w1 : float
        Width of diffusion coefficient distributions in D units.

    Returns
    -------
    dataArray

    """
    result = dA(np.c_[t, A0 * np.exp(-q ** 2 * (D0 * t + 1 / 2. * abs(w0) * w0 * t * t)) +
                      A1 * np.exp(-q ** 2 * (D1 * t + 1 / 2. * abs(w1) * w1 * t * t))].T)
    result.amplitude0 = amplitude0
    result.D0 = D0
    result.wavevector = q
    result.amplitude1 = amplitude1
    result.D1 = D1
    result.modelname = inspect.currentframe().f_code.co_name
    result.columnname = 't;Iqt'
    result.setColumnIndex(iey=None)
    return result


def cumulantDiff(t, q, k0=0, k1=0, k2=0, k3=0, k4=0, k5=0):
    """
    Cumulant of order ki with cumulants as diffusion coefficients.

    .. math:: I(t,q)=k0 exp(-q^2(k_1x+1/2(k_2x)^2+1/6(k_3x)^3+1/24(k_4x)^4+1/120(k_5x)^5))

    Parameters
    ----------
    t : array
        Time
    q : float
        Wavevector
    k0 : float
        Amplitude
    k1 : float
        Diffusion coefficient in units of 1/([q]*[t])
    k2,k3,k4,k5 : float
        Higher coefficients in same units as k1

    Returns
    -------
    dataArray :

    """
    t = np.atleast_1d(t)
    res = k0 * (
        np.exp(-q ** 2. * (k1 * t +
                           1 / 2. * abs(k2) * k2 * t * t +
                           1. / 6 * k3 * k3 * k3 * t * t * t +
                           1. / 24 * abs(k4) * k4 * k4 * k4 * t * t * t * t +
                           1. / 120 * (k5 * t) ** 5)))
    result = dA(np.c_[t, res].T)
    result.k0tok5 = [k0, k1, k2, k3, k4, k5]
    result.wavevector = q
    result.modelname = inspect.currentframe().f_code.co_name
    result.columnname = 't;Iqt'
    result.setColumnIndex(iey=None)
    return result


def cumulant(x, k0=0, k1=0, k2=0, k3=0, k4=0, k5=0):
    r"""
    Cumulant of order ki.

    .. math:: I(x) = k_0 exp(-k_1x+1/2k_2x^2-1/6 k_3x^3+1/24k_4x^4-1/120k_5x^5)

    Parameters
    ----------
    x : float
        Wavevector
    k0,k1, k2,k3,k4,k5 : float
        Cumulant coefficients;  units 1/x
         - k0 amplitude
         - k1 expected value
         - k2 variance with :math:`\sqrt(k2/k1) =` relative standard deviation
         - higher order see Wikipedia

    Returns
    -------
    dataArray

    """
    x = np.atleast_1d(x)
    res = k0 * np.exp(- k1 * x
                      + 1 / 2. * k2 * x ** 2
                      - 1 / 6. * k3 * x ** 3
                      + 1 / 24 * k4 * x ** 4
                      - 1 / 120 * k5 * x ** 5)
    result = dA(np.c_[x, res].T)
    result.k0tok5 = [k0, k1, k2, k3, k4, k5]
    result.modelname = inspect.currentframe().f_code.co_name
    result.columnname = 't;Iqt'
    result.setColumnIndex(iey=None)
    return result


def cumulantDLS(t, A, G, sigma, skewness=0, bgr=0.):
    r"""
    Cumulant analysis for dynamic light scattering assuming Gaussian size distribution.

    .. math:: I(t,q) = A exp(-t/G) \big( 1+(sigma/G t)^2/2. - (skewness/G t)^3/6. \big) + bgr

    Parameters
    ----------
    t : array
        Time
    A : float
        Amplitude at t=0; Intercept
    G : float
        Mean relaxation time as 1/decay rate in units of t.
    sigma : float
        - relative standard deviation if a gaussian distribution is assumed
        - should be smaller 1 or the Taylor expansion is not valid
        - k2=variance=sigma**2/G**2
    skewness : float,default 0
        Relative skewness k3=skewness**3/G**3
    bgr : float; default 0
        Constant background

    Returns
    -------
    dataArray

    References
    ----------
    .. [1] Revisiting the method of cumulants for the analysis of dynamic light-scattering data
          Barbara J. Frisken APPLIED OPTICS  40, 4087 (2001)

    """
    t = np.atleast_1d(t)
    if skewness == 0:
        res = A * np.exp(-t / G) * (1 + (sigma / G * t) ** 2 / 2.) + bgr
    else:
        res = A * np.exp(-t / G) * (1 + (sigma / G * t) ** 2 / 2. - (skewness / G * t) ** 3 / 6.) + bgr
    result = dA(np.c_[t, res].T)
    result.A = A
    result.relaxationtime = G
    result.sigma = sigma
    result.skewness = skewness
    result.elastic = bgr
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    return result


def stretchedExp(t, gamma, beta, amp=1):
    r"""
    Stretched exponential function.

    .. math:: I(t) = amp\, e^{-(t\gamma)^\beta}

    Parameters
    ----------
    t : array
        Times
    gamma : float
        Relaxation rate in units 1/[unit t]
    beta : float
        Stretched exponent
    amp : float default 1
        Amplitude

    Returns
    -------
    dataArray

    """
    t = np.atleast_1d(t)
    res = amp * np.exp(-(t * gamma) ** beta)
    result = dA(np.c_[t, res].T)
    result.amp = amp
    result.gamma = gamma
    result.beta = beta
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    return result


def jumpDiffusion(t, Q, t0, l0):
    r"""
    Incoherent intermediate scattering function of translational jump diffusion in the time domain.

    Parameters
    ----------
    t : array
        Times, units ns
    Q : float
        Wavevector, units nm
    t0 : float
        Residence time, units ns
    l0 : float
        Mean square jump length, units nm

    Returns
    -------
        dataArray

    Notes
    -----
    We use equ. 3-5 from [1]_ for random jump diffusion as

    .. math:: T(Q,t) = exp(-\Gamma(Q)t)

    with residence time :math:`\tau_0` and mean jump length :math:`<l^2>^{1/2}_{av}`
    and diffusion constant :math:`D` in

    .. math:: \Gamma(Q) = \frac{DQ^2}{1+DQ^2\tau_0}

    .. math:: D=\frac{ <l^2>_{av}}{6\tau_0}



    References
    ----------
    .. [1]  Experimental determination of the nature of diffusive motions of water molecules at low temperatures
            J. Teixeira, M.-C. Bellissent-Funel, S. H. Chen, and A. J. Dianoux
            Phys. Rev. A 31, 1913 – Published 1 March 1985

    """
    t = np.atleast_1d(t)
    D = l0 ** 2 / 6. / t0
    gamma = D * Q * Q / (1 + D * Q * Q * t0)

    tdif = np.exp(-gamma * t)
    result = dA(np.c_[t, tdif].T)
    result.residencetime = t0
    result.jumplength = l0
    result.diffusioncoefficient = D
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    return result


def methylRotation(t, q, t0=0.001, fraction=1, rhh=0.12, beta=0.8):
    r"""
    Incoherent intermediate scattering function of CH3 methyl rotation in the time domain.

    Parameters
    ----------
    t : array
        List of times, units ns
    q : float
        Wavevector, units nm
    t0 : float, default 0.001
        Residence time, units ns
    fraction : float, default 1
        Fraction of protons contributing.
    rhh : float, default=0.12
        Mean square jump length, units nm
    beta : float, default 0.8
        exponent

    Returns
    -------
        dataArray

    Notes
    -----
    According to [1]_:

    .. math:: I(q,t) = (EISF + (1-EISF) e^{-(\frac{t}{t_0})^{\beta}} )

    .. math:: EISF=\frac{1}{3}+\frac{2}{3}\frac{sin(qr_{HH})}{qr_{HH}}

    with
    :math:`t_0` residence time,
    :math:`r_{HH}` proton jump distance.

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     # make a plot of the spectrum
     w=np.r_[-100:100]
     ql=np.r_[1:15:1]
     iqwCH3=js.dL([js.dynamic.time2frequencyFF(js.dynamic.methylRotation,'elastic',w=np.r_[-100:100:0.1],q=q )
                                                 for q in ql])
     p=js.grace()
     p.plot(iqwCH3,le='CH3')
     p.yaxis(min=1e-5,max=10,scale='l')


    References
    ----------
    .. [1] M. Bée, Quasielastic Neutron Scattering (Adam Hilger, 1988).
    .. [2] Monkenbusch et al. J. Chem. Phys. 143, 075101 (2015)


    """
    t = np.atleast_1d(t)
    EISF = (1 + 2 * np.sinc(q * rhh / np.pi)) / 3.
    Iqt = (1 - fraction) + fraction * (EISF + (1 - EISF) * np.exp(-(t / t0) ** beta))

    result = dA(np.c_[t, Iqt].T)
    result.wavevector = q
    result.residencetime = t0
    result.rhh = rhh
    result.beta = beta
    result.EISF = EISF
    result.methylfraction = fraction
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    return result


def diffusionHarmonicPotential(t, q, rmsd, tau, beta=0, ndim=3):
    r"""
    ISF corresponding to the standard OU process for diffusion in harmonic potential for dimension 1,2,3.

    The intermediate scattering function corresponding to the standard OU process
    for diffusion in an harmonic potential [1]_. It is used for localized translational motion in
    incoherent neutron scattering [2]_ as improvement for the diffusion in a sphere model.
    Atomic motion may be restricted to ndim=1,2,3 dimensions and are isotropic averaged.
    The correlation is assumed to be exponential decaying.

    Parameters
    ----------
    t : array
        Time values in units ns
    q : float
        Wavevector in unit 1/nm
    rmsd : float
        Root mean square displacement <u**2>**0.5 in potential in units nm.
        <u**2>**0.5 is the width of the potential
        According to [2]_  5*u**2=R**2 compared to the diffusion in a sphere.
    tau : float
        Correlation time :math:`\tau_0` in units ns.
        Diffusion constant in sphere Ds=u**2/tau
    beta : float, default 0
        Exponent in correlation function :math:`\rho(t)`.
         - beta=0 :  :math:`\rho(t) = exp(-t/\tau_0)`
           normal liquids where memory effects are presumably weak or negligible [2]_.
         - 0<beta,inf : :math:`\rho(t,beta) = (1+\frac{t}{\beta\tau_0})^{-\beta}`. See [2]_ equ. 21a.
           supercooled liquids or polymers, where memory effects may be important correlation functions
           with slower decay rates should be introduced [2]_. See [2]_ equ. 21b.
    ndim : 1,2,3, default=3
        Dimensionality of the diffusion potential.

    Returns
    -------
        dataArray

    Notes
    -----
    We use equ. 18-20 from [2]_ and correlation time :math:`\tau_0`
    with equal amplitudes :math:`u` in the dimensions as


    3 dim case:

    .. math:: I_s(Q,t) = e^{-Q^2\langle u^2_x \rangle (1-\rho(t))}

    2 dim case:

    .. math:: I_s(Q,t) = \frac{\pi^{0.5}}{2} e^{-g^2(t)} \frac{erfi(g(t))}{g(t)} \ with \
              g(t) = \sqrt{Q^2\langle u^2_x \rangle (1-\rho(t))}

    1 dim case:

    .. math:: I_s(Q,t) = \frac{\pi^{0.5}}{2} \frac{erf(g(t))}{g(t)} \ with \
              g(t) = \sqrt{Q^2\langle u^2_x \rangle (1-\rho(t))}

    with *erf* as the error function and *erfi* is the imaginary error function *erf(iz)/i*

    Examples
    --------
    ::

     import numpy as np
     import jscatter as js
     t=np.r_[0.1:6:0.1]
     p=js.grace()
     p.plot(js.dynamic.diffusionHarmonicPotential(t,1,2,1,1),le='1D ')
     p.plot(js.dynamic.diffusionHarmonicPotential(t,1,2,1,2),le='2D ')
     p.plot(js.dynamic.diffusionHarmonicPotential(t,1,2,1,3),le='3D ')
     p.legend()
     p.yaxis(label='I(Q,t)')
     p.xaxis(label='Q / ns')
     p.subtitle('Figure 2 of ref Volino J. Phys. Chem. B 110, 11217')

    References
    ----------
    .. [1] Quasielastic neutron scattering and relaxation processes in proteins: analytical and simulation-based models
           G. R. Kneller Phys. ChemChemPhys. ,2005, 7,2641–2655
    .. [2] Gaussian model for localized translational motion: Application to incoherent neutron scattering
           F. Volino, J.-C. Perrin and S. Lyonnard, J. Phys. Chem. B 110, 11217–11223 (2006)

    """
    erf = special.erf
    erfi = special.erfi
    q2u2 = q ** 2 * rmsd ** 2
    if beta <=0:
        ft = (1 - np.exp(-t / tau))
    else:
        ft = (1 - (1+t/tau/beta)**(-beta))
    ft[t == 0] = 1e-8  # avoid zero to prevent zero division and overwrite later with EISF
    if ndim == 3:
        Iqt = np.exp(-q2u2 * ft)
        EISF = np.exp(-q2u2)
        Iqt[t == 0] = EISF
    elif ndim == 2:
        q2u2exp = q2u2 * ft
        Iqt = 0.5 * pi ** 0.5 * np.exp(-q2u2exp) * erfi(q2u2exp ** 0.5) / q2u2exp ** 0.5
        EISF = 0.5 * pi ** 0.5 * np.exp(-q2u2) * erfi(q2u2 ** 0.5) / q2u2 ** 0.5
        Iqt[t == 0] = EISF
    elif ndim == 1:
        q2u2exp = q2u2 * ft
        Iqt = 0.5 * pi ** 0.5 * erf(q2u2exp ** 0.5) / q2u2exp ** 0.5
        EISF = 0.5 * pi ** 0.5 * erf(q2u2 ** 0.5) / q2u2 ** 0.5
        Iqt[t == 0] = EISF
    else:
        raise Exception('ndim should be one of 1,2,3 ')

    result = dA(np.c_[t, Iqt].T)
    result.tau = tau
    result.Ds = rmsd ** 2 / tau
    result.rmsd = rmsd
    result.EISF = EISF
    result.wavevector = q
    result.dimension = ndim
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    return result


def finiteZimm(t, q, NN=None, pmax=None, l=None, Dcm=None, Dcmfkt=None, tintern=0., mu=0.5, viscosity=1.,
               ftype=None, rk=None, Temp=293):
    r"""
    Zimm dynamics of a finite chain with N beads with internal friction and hydrodynamic interactions.

    The Zimm model describes the conformational dynamics of an ideal chain with hydrodynamic interaction between beads.
    The single chain diffusion is represented by Brownian motion of beads connected by harmonic springs.
    Coherent + incoherent scattering.

    Parameters
    ----------
    t : array
        Time in units nanoseconds.
    q: float, array
        Scattering vector in units nm^-1.
        If q is list a dataList is returned  otherwise a dataArray is returned.
    NN : integer
        Number of chain beads.
    l : float, default 1
        Bond length between beads; units nm.
    pmax : integer, list of float, default is NN
        - integer => maximum mode number taken into account.
        - list    => list of amplitudes :math:`a_p > 0` for individual modes
          to allow weighing. Not given modes have weight zero.
    Dcm : float
        Center of mass diffusion in nm²/ns
         - :math:`=0.196 k_bT/(R_e visc)` for theta solvent with :math:`\mu=0.5`
         - :math:`=0.203 k_bT/(R_e visc)` for good solvent  with :math:`\mu=0.6`
    Dcmfkt : array 2xN, function
        Function f(q) or array with [qi, f(qi)] as correction for Dcm like Diff = Dcm*f(q).
        e.g. for inclusion of structure factor and hydrodynamic function with f(q)=H(Q)/S(q).
        Missing values are interpolated.
        Only array input can be pickled to speedup  by using formel.memoize .
    tintern : float>0
        Additional relaxation time due to internal friction between neighbouring beads in units ns.
    mu : float in range [0.01,0.99]
        :math:`\mu` describes solvent quality.
         - <0.5 collapsed
         - =0.5 theta solvent 0.5 (gaussian chain)
         - =0.6 good solvent
         - >0.6 swollen chain
    viscosity : float
        :math:`\eta` in units cPoise=mPa*s  e.g. water :math:`visc(T=293 K) =1 mPas`
    Temp : float, default 273+20
        Temperature  in Kelvin.
    ftype : 'czif', default = 'zif'
        Type of internal friction and interaction modification.
         - Default Zimm is used with :math:`t_{intern}=0`
         - 'zif' Internal friction between neighboring beads in chain [3]_.
            :math:`t_{zp}=t_z p^{-3\mu}+t_{intern}`
         - 'czif' Bead confining harmonic potential with internal friction, only for :math:`\mu=0.5` [6]_ .
            The beads are confined in an additional harmonic potential with :math:`\frac{1}{2}k_c(r_n-0)^2` leading to
            a more compact configuration.  :math:`rk= k_c/k` describes the relative strength
            compared to the force between beads :math:`k`.
    rk : None , float
        :math:`rk= k_c/k` describes the relative force constant for *ftype* 'czif'.

    Returns
    -------
     dataArray : for single q
     dataList : for multiple q
      - [time; Sqt; Sqt_inf; Sqtinc; Sqtz]
      - time units ns
      - Sqt is coherent scattering with diffusion and mode contributions
      - Sqt_inf is coherent scattering with ONLY diffusion (no internal modes)
      - Sqtinc is incoherent scattering with diffusion and mode contributions (no separate diffusion)
      - Sqt0 is coherent scattering with diffusion and mode contributions, but no Dcmfkt => f(q)=1
      - .q wavevector
      - .modecontribution  :math:`a_p` of coherent modes i in sequence as in PRL 71, 4158 equ (3)
      - .Re
      - .tzimm => Zimm time or rotational correlation time
      - .t_p  characteristic times
      - .... use .attr for all attributes

    Notes
    -----
    The Zimm model describes beads connected by harmonic springs with hydrodynamic interaction.
    The :math:`\mu` parameter scales between theta solvent :math:`\mu=0.5` and good solvent :math:`\mu=0.6`
    (excluded volume or swollen chain). The coherent intermediate scattering function :math:`S(q,t)/S(q,0)` is

    .. math:: \frac{S(q,t)}{S(q,0)} = \frac{1}{N} e^{-q^2D_{cm}t}\sum_{n,m}^N e^{-\frac{1}{6}q^2B(n,m,t)}

    .. math:: B(n,m,t)=|n-m|^{2\mu}l^2 + \sum_{p=1}^{N-1} A_p cos(\pi pn/N)cos(\pi pm/N) (1-e^{-t/t_{zp}})

    and for incoherent intermediate scattering function the same with :math:`n=m` in the first sum.

    with
     - :math:`A_p = a_p\frac{4R_e^2}{\pi^2}\frac{1}{p^{2\mu+1}}` mode amplitude  (usual :math:`a_p=1`)
     - :math:`t_{zp} = t_z p^{-3\mu}` mode relaxation time
     - :math:`t_z = \eta R_e^3/(\sqrt(3\pi) k_bT)` Zimm mode relaxation time
     - :math:`R_e=l N^{\mu}` end to end distance
     - :math:`k=3kT/l^2`                      force constant between beads
     - :math:`\xi=6\pi\eta l`                single bead friction in solvent with viscosity :math:`\eta`
     - :math:`a_p` additional amplitude for suppression of specific modes e.g. by topological constraints (see [5]_).
     - :math:`D_{cm} = \frac{8}{3(6\pi^3)^{1/2}} \frac{k_bT}{\eta R_e} = 0.196 \frac{k_bT}{\eta R_e}`

    Modifications (*ftype*) for internal friction and additional interaction:

    - ZIF : Zimm with internal friction between neighboring beads in chain [3]_ [4]_.
            - :math:`t_{zp}=t_z p^{{-3\mu}}+t_{intern}`
            - :math:`\xi_i=t_{intern}k=t_{intern}3k_bT/l^2`  internal friction per bead

    - CZIF : Compacted Zimm with internal friction [6]_.
             Restricted to :math:`\mu=0.5` , a combination with excluded volume is not valid.
             In [9]_ the beads are confined in an additional harmonic potential around the origin with
             :math:`\frac{1}{2}k_c(r_n-0)^2` leading to a more compact configuration.
             :math:`rk= k_c/k` describes the relative strength compared to the force between beads :math:`k`.
             Typically :math:`rk << 1` .

             - The mode amplitude prefactor changes from Zimm type to modified confined amplitudes

               .. math:: A_p =\frac{4Nl^2}{\pi^2}\frac{1}{p^2}\Rightarrow
                         A_p^c = \frac{4Nl^2}{\pi^2}\frac{1}{\frac{N^2k_c}{\pi^2k}+p^2}

             - The mode relaxation time changes from Zimm type to modified confined
               with :math:`t_{z} = \frac{\eta N^{3/2} l^3}{\sqrt(3\pi) k_bT}`

               .. math:: t_{zp} = t_z \frac{1}{p^{3/2}} \Rightarrow
                         t_{zp}^c =  t_z \frac{p^{1/2}}{\frac{N^2k_c}{\pi^2k} + p^2}

             - :math:`R_e^c` allows to determine :math:`k_c/k` from small angle scattering data

                .. math:: (R_e^c)^2 = \frac{2l^2}{\sqrt{k_c/k}}tanh(\frac{N}{2}\sqrt{k_c/k})

             - For a free diffusing chain we assume here (not given in [9]_ ) that the additional potential
               is :math:`\frac{1}{2}k_c(r_n-r_0)^2` with :math:`r_0` as the polymer center of mass.
               As the Langevin equation only depends on position distances the internal motions are not affected.
               The center of mass diffusion :math:`D_{cm}` can be calculated similar to the Zimm  :math:`D_{cm}` in [1]_
               assuming a Gaussian configuration with width :math:`R_e`. We find

                .. math:: D_{cm} = \frac{kT}{\xi_{p=0}} = \frac{8}{3(6\pi^3)^{1/2}} \frac{kT}{\eta R_e}

             - With :math:`rk=k_c/k \rightarrow 0` the original Zimm is recovered for amplitudes,
               relaxation and :math:`R_e` .

    From above the triple Dcm,l,N are fixed.
     - If 2 are given 3rd is calculated.
     - If all 3 are given the given values are used.

    For an example see `example_Zimm`.
    To speedup see example :py:func:`~.formel.memoize`

    Examples
    --------
    Coherent and incoherent contributions to Rouse dynamics.
    To mix the individual q dependent contributions have to be weighted with the according formfactor respectivly
    incoherent scattering length and instrument specific measurement technique.
    ::

     import jscatter as js
     import numpy as np
     t = js.loglist(0.02, 100, 40)
     q=np.r_[0.1:2:0.2]
     l=0.38  # nm , bond length amino acids
     zz = js.dynamic.finiteZimm(t, q, 124, 7, l=0.38, Dcm=0.37, tintern=0., Temp=273 + 60)
     p=js.grace()
     p.multi(2,1)
     p[0].xaxis(scale='log')
     p[0].yaxis(label='I(q,t)\scoherent')
     p[1].xaxis(label=r't / ns',scale='log')
     p[1].yaxis(label=r'I(q,t)\sincoherent')
     p[0].title('Zimm dynamics in a solvent')
     for i, z in enumerate(zz, 1):
         p[0].plot(z.X, z.Y, line=[1, 1, i], symbol=0, legend='q=%g' % z.q)
         p[0].plot(z.X, z._Sqt_inf, line=[3, 2, i], symbol=0, legend='q=%g diff' % z.q)
         p[1].plot(z.X, z._Sqtinc, line=[1, 2, i], symbol=0, legend='q=%g diff' % z.q)

     #p.save(js.examples.imagepath+'/Zimmcohinc.jpg')

    .. image:: ../../examples/images/Zimmcohinc.jpg
     :align: center
     :width: 50 %
     :alt: Zimm



    References
    ----------
    .. [1]  Doi Edwards Theory of Polymer dynamics
            in appendix the equation is found
    .. [2]  Nonflexible Coils in Solution: A Neutron Spin-Echo Investigation of
            Alkyl-Substituted Polynorbonenes in Tetrahydrofuran
            Michael Monkenbusch et al.Macromolecules 2006, 39, 9473-9479
            The exponential is missing a "t"
            http://dx.doi.org/10.1021/ma0618979

    about internal friction

    .. [3]  Exploring the role of internal friction in the dynamics of unfolded proteins using simple polymer models
            Cheng et al.JOURNAL OF CHEMICAL PHYSICS 138, 074112 (2013)  http://dx.doi.org/10.1063/1.4792206
    .. [4]  Rouse Model with Internal Friction: A Coarse Grained Framework for Single Biopolymer Dynamics
            Khatri, McLeish|  Macromolecules 2007, 40, 6770-6777  http://dx.doi.org/10.1021/ma071175x

    mode contribution factors from

    .. [5]  Onset of Topological Constraints in Polymer Melts: A Mode Analysis by Neutron Spin Echo Spectroscopy
            D. Richter et al.PRL 71,4158-4161 (1993)
    .. [6]  Looping dynamics of a flexible chain with internal friction at different degrees of compactness.
            Samanta, N., & Chakrabarti, R. (2015).
            Physica A: Statistical Mechanics and Its Applications, 436, 377–386.
            https://doi.org/10.1016/j.physa.2015.05.042

    """
    kb = 1.3806505e-23  # in SI units J/K
    # convert to Pa*s
    viscosity *= 1e-3
    q = np.atleast_1d(q)
    # check mu between 0.1 and 0.9
    mu = max(mu, 0.01)
    mu = min(mu, 0.99)
    # avoid l=0 from stupid users
    if l == 0: l = None
    # and linear interpolate prefactor
    ffact = 8 / (3 * 6 ** 0.5 * np.pi ** (3 / 2))
    fact = ffact + (mu - 0.5) / (0.6 - 0.5) * (0.203 - 0.196)
    NN = int(NN)
    if pmax is None: pmax = NN
    # if a list pmax of modes is given these are amplitudes for the modes
    # pmax is length of list
    if isinstance(pmax, numbers.Number):
        pmax = min(int(pmax), NN)
        modeamplist = np.ones(pmax)
    elif isinstance(pmax, list):
        modeamplist = np.abs(pmax)
    else:
        raise TypeError('pmax should be integer or list of amplitudes')

    # create correction for diffusion
    if Dcmfkt is not None:
        if formel._getFuncCode(Dcmfkt):
            # is already an interpolation function
            Dcmfunktion = Dcmfkt
        elif np.shape(Dcmfkt)[0] == 2:
            Dcmfunktion = lambda qq: dA(Dcmfkt).interp(qq)
        else:
            raise TypeError('Shape of Dcmfkt is not 2xN!')
    else:
        # by default no correction
        Dcmfunktion = lambda qq: 1.

    if ftype == 'czif':
        # compacted zimm with internal friction
        if mu != 0.5:
            raise ValueError('For ftype "czif" only mu=0.5 is allowed. ')

        if Dcm is None and l is not None and NN is not None:
            # Re = end to end distance
            Re = (2 * l ** 2 / rk ** 0.5 * np.tanh(NN / 2 * rk ** 0.5))**0.5
            # center of mass diffusion constant  in nm^2/ns
            Dcm = fact * kb * Temp / (Re * 1e-9 * viscosity) * 1e9
        elif Dcm is not None and l is None and NN is not None:
            Re = fact * kb * Temp / (Dcm * 1e-9 * viscosity) * 1e9
            l = Re * (rk ** 0.5 / 2 / np.tanh(NN / 2 * rk ** 0.5)) ** 0.5
        elif Dcm is not None and l is not None and NN is None:
            Re = fact * kb * Temp / (Dcm * 1e-9 * viscosity) * 1e9
            NN = 2 / rk ** 0.5 * np.arctanh(rk * Re ** 2 / 2 / l ** 2 )
        elif Dcm is not None and l is not None and NN is not None:
            Re = 2 * l ** 2 / rk ** 0.5 * np.tanh(NN / 2 * rk ** 0.5)
        else:
            raise TypeError('finiteZimm takes at least 2 arguments from Dcm, NN, l')
        # determine mode relaxation times
        # slowest zimm time
        tz1 = viscosity * NN ** (3 / 2) * (l * 1e-9) ** 3 / (np.sqrt(3 * pi) * kb * Temp) * 1e9
        # mode amplitudes
        p = np.r_[1:len(modeamplist) + 1]
        modeamplist = 4 * NN * l ** 2 / pi ** 2 * modeamplist

        tzp = tz1 * p ** 0.5 / (NN ** 2 / np.pi ** 2 * rk + p ** 2) + abs(tintern)
        modeamplist = modeamplist / (NN ** 2 / np.pi ** 2 * rk + p ** (2 * mu + 1))
    else:
        # ZIF with constant internal friction time added as default

        if Dcm is None and l is not None and NN is not None:
            Re = l * NN ** mu  # end to end distance
            Dcm = fact * kb * Temp / (Re * 1e-9 * viscosity) * 1e9  # diffusion constant  in nm^2/ns
        elif Dcm is not None and l is None and NN is not None:
            Re = fact * kb * Temp / (Dcm * 1e-9 * viscosity) * 1e9  # end to end distance
            l = Re / NN ** mu  # bond length
        elif Dcm is not None and l is not None and NN is None:
            Re = fact * kb * Temp / (Dcm * 1e-9 * viscosity) * 1e9  # end to end distance
            NN = int((Re / l) ** (1. / mu))
        elif Dcm is not None and l is not None and NN is not None:
            Re = l * NN ** mu
        else:
            raise TypeError('finiteZimm takes at least 2 arguments from Dcm,NN,l')

        # determine mode relaxation times
        # slowest zimm time
        tz1 = viscosity * (Re * 1e-9) ** 3 / (np.sqrt(3 * pi) * kb * Temp) * 1e9
        # mode amplitudes
        p = np.r_[1:len(modeamplist) + 1]
        modeamplist = 4 * Re ** 2 / pi ** 2 * modeamplist
        # characteristic Zimm time of mode p adding internal friction ti
        tzp = tz1 * p ** (-3 * mu) + abs(tintern)
        modeamplist = modeamplist / (p ** (2 * mu + 1))
        ftype = 'zif'

    # prepend 0 and append infinite time
    t = np.r_[0, np.atleast_1d(t)]

    # calc array of mode contributions including first constant element as list

    # do the calculation as an array of bnm=[n*m , len(t)] elements
    # sum up contributions for modes: all, diff+ mode1, only diffusion, t=0 amplitude for normalisation
    if useFortran:
        BNM = fscatter.dynamic.bnmt(t, NN, l, mu, modeamplist, tzp)
        BNMmodes = BNM[:, -len(modeamplist):]
        BNMi = BNM[:, len(t):2*len(t)]
        BNM = BNM[:, :len(t)]

    else:
        raise ImportError('finiteZimm only with working Fortran.')

    result = dL()
    for qq in q:
        # diffusion for all t
        Sqt = np.exp(-qq ** 2 * Dcm * Dcmfunktion(qq) * t[1:])  # only diffusion contribution
        Sqt0 = np.exp(-qq ** 2 * Dcm * t[1:])  # only diffusion contribution
        # amplitude at t=0
        expB0 = np.sum(np.exp(-qq ** 2 / 6. * BNM[:, 0]))  # is S(qq,t=0)/Sqt coherent
        expB0i = np.sum(np.exp(-qq ** 2 / 6. * BNMi[:, 0]))  # is S(qq,t=0)/Sqt incoherent
        # diffusion for infinite times in modes
        expBinf = np.sum(np.exp(-qq ** 2 / 6. * np.sum(BNMmodes, axis=1)))  # is S(qq,t=inf)/Sqt
        # contribution all modes
        expB = np.sum(np.exp(-qq ** 2 / 6. * BNM[:, 1:]), axis=0)  # coherent
        expBi = np.sum(np.exp(-qq ** 2 / 6. * BNMi[:, 1:]), axis=0)  # incoherent
        # contribution only first modes
        result.append(np.c_[t[1:],
                            Sqt * expB / expB0,  # Zimm with H/S
                            Sqt * expBinf / expB0,  # no internal modes
                            Sqt * expBi / expB0i,  # incoherent contributions
                            Sqt0 * expB / expB0].T)  # pure Zimm , no H/S modification
        result[-1].modecontribution = (np.sum(np.exp(-qq ** 2 / 6. * BNMmodes), axis=0) / expB0).flatten()
        result[-1].q = qq
        result[-1].Re = Re
        result[-1].ll = l
        result[-1].pmax = pmax
        result[-1].Dcm = Dcm
        result[-1].effectiveDCM = Dcm * Dcmfunktion(qq)
        DZimm = fact * kb * Temp / (Re * 1e-9 * viscosity) * 1e9
        result[-1].DZimm = DZimm
        result[-1].mu = mu
        result[-1].viscosity = viscosity
        result[-1].Temperature = Temp
        result[-1].tzimm = tz1
        result[-1].moderelaxationtimes = tzp
        result[-1].tintern = tintern
        result[-1].modeAmplist = modeamplist
        result[-1].Drot = 1. / 6. / tz1
        result[-1].N = NN
        result[-1].columnname = ' time; Sqt; Sqt_inf; Sqtinc; Sqtz'
        result[-1].ftype = ftype
        result[-1].rk = rk
    if len(result) == 1:
        return result[0]
    result.setColumnIndex(iey=None)
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def finiteRouse(t, q, NN=None, pmax=None, l=None, frict=None, Dcm=None, Wl4=None, Dcmfkt=None, tintern=0.,
                Temp=293, ftype=None, specm=None, specb=None, rk=None):
    r"""
    Rouse dynamics of a finite chain with N beads of bonds length l and internal friction.

    The Rouse model describes the conformational dynamics of an ideal chain.
    The single chain diffusion is represented by Brownian motion of beads connected by harmonic springs.
    No excluded volume, random thermal force, drag force with solvent,
    no hydrodynamic interaction and optional internal friction.
    Coherent + incoherent scattering.


    Parameters
    ----------
    t : array
        Time in units nanoseconds
    q : float, list
        Scattering vector, units nm^-1
        For a list a dataList is returned otherwise a dataArray is returned
    NN : integer
        Number of chain beads.
    l : float, default 1
        Bond length between beads; unit nm.
    pmax : integer, list of floats
        - integer => maximum mode number (:math:`a_p=1`)
        - list    => :math:`a_p` list of amplitudes>0 for individual modes
          to allow weighing; not given modes have weight zero
    frict : float
        Friction of a single bead/monomer :math:`\xi = 6\pi\eta l`, units Pas*m=kg/s=1e-6 g/ns.

        A sphere with R=0.1 nm in H2O(20°C) (1 mPas) => 1.89e-12 Pas*m

    Wl4 : float
        :math:`W_l^4` Characteristic value to calc friction and Dcm.

        :math:`D_{cm}=\frac{W_l^4}{3R_e^2}` and characteristic Rouse variable
        :math:`\Omega_Rt=(q^2/6)^2 W_l^4 t`
    Dcm : float
        Center of mass diffusion in nm^2/ns.
         - :math:`D_{cm}=k_bT/(N\xi)`     with :math:`\xi` = friction of single bead in solvent
         - :math:`D_{cm}=W_l^4/(3Nl^2)=W_l^4/(3Re^2)`
    Dcmfkt : array 2xN, function
        Function f(q) or array with [qi, f(qi) ] as correction for Dcm like Diff = Dcm*f(q).
        e.g. for inclusion of structure factor or hydrodynamic function with f(q)=H(Q)/S(q).
        Missing values are interpolated.
        Only array input can be pickled to speedup  by using formel.memoize .
    tintern : float>0
        Relaxation time due to internal friction between neighbouring beads in ns.
    ftype : 'rni', 'rap','nonspec', 'specrif', 'crif', default = 'rif'
        Type of internal friction. See [7]_ for a description and respective references.
         - *'rif'*: Internal friction between neighboring beads in chain. :math:`t_{rp}=t_r p^{-2}+t_{intern}`
         - *'rni'*: Rouse model with non-local interactions (RNI).
           Additional friction between random close approaching beads. :math:`t_{rp}=t_r p^{-2}+N/p t_{intern}`
         - *'rap'*: Rouse model with anharmonic potentials due to stiffness of the chain
           :math:`t_{rp}=t_r p^{-2}+t_{intern}ln(N/p\pi)`
         - *'specrif'*: Specific interactions of strength :math:`b` between beads separated by *m* bonds.
           See [7]_. :math:`t_{rp}=t_r p^{-2} (1+bm^2)^{-1} + (1+m^2/(1+bm^2))t_{intern}`
         - *'crif'*: Bead confining potential with internal friction. The beads are confined in an additional
           harmonic potential with :math:`\frac{1}{2}k_c(r_n-0)^2` leading to a more compact configuration.
           :math:`rk= k_c/k` describes the relative strength compared to the force between beads :math:`k`.
    Temp : float
        Temperature  Kelvin = 273+T[°C]
    specm,specb: float
        Parameters *m, b* used in internal friction models 'spec' and 'specrif'.
    rk : None , float
        :math:`rk= k_c/k` describes the relative force constant for *ftype* 'crif'.

    Returns
    -------
     dataArray : for single q
     dataList : multiple q
      - [time; Sqt; Sqt_inf; Sqtinc]
      - time units ns
      - Sqt is coherent scattering with diffusion and mode contributions
      - Sqt_inf is coherent scattering with ONLY diffusion
      - Sqtinc is incoherent scattering with diffusion and mode contributions (no separate diffusion)
      - .q wavevector
      - .Wl4
      - .Re     end to end distance :math:`R_e^2=l^2N`
      - .trouse rotational correlation time or rouse time
                :math:`tr_1 = \xi N^2 l^2/(3 \pi^2 k_bT)= <R_e^2>/(3\pi D_{cm}) = N^2\xi/(pi^2k)`
      - .tintern relaxation time due to internal friction
      - .tr_p characteristic times   :math:`tr_p=tr_1 p^{-2}+t_{intern}`
      - .beadfriction
      - .ftype type of internal friction
      - .... use .attr to see all attributes

    Notes
    -----
    The Rouse model for the coherent intermediate scattering function :math:`S(q,t)/S(q,0)` is [1]_ [2]_ :

    .. math:: \frac{S(q,t)}{S(q,0)} = \frac{1}{N} e^{-q^2D_{cm}t} \sum_{n,m}^N e^{-\frac{1}{6}q^2B(n,m,t)}

    .. math:: B(n,m,t)=|n-m|^{2\mu}l^2 +
                                \sum_{p=1}^{N-1} A_p cos(\pi pn/N)cos(\pi pm/N) (1-e^{-t/t_{rp}})

    and for incoherent intermediate scattering function the same with :math:`n=m` in the first sum.

    with
     - :math:`A_p = a_p\frac{4R_e^2}{\pi^2}\frac{1}{p^2}` mode amplitude  (usual :math:`a_p=1`)
     - :math:`t_{rp} = \frac{t_r}{p^2}` mode relaxation time with Rouse time
       :math:`t_r =\frac{\xi N R_e^2 }{3\pi^2 k_bT} = \frac{R_e^2}{3\pi^2 D_{cm}} = \frac{N^2 \xi}{\pi^2 k}`
     - :math:`D_{cm}=kT/{N\xi}`        center of mass diffusion
     - :math:`k=3k_bT/l^2`             force constant k between beads.
     - :math:`\xi=6\pi visc R`         single bead friction :math:`\xi` in solvent (e.g. surrounding melt)
     - :math:`t_{intern}=\xi_i/k`        additional relaxation time due to internal friction :math:`\xi_i`

    Modifications (*ftype*) for internal friction and additional interaction (see [7]_ and [9]_):

    - RIF : Rouse with internal friction between neighboring beads in chain [3]_ [4]_.
            - :math:`t_{rp}=t_r p^{-2}+t_{intern}`
            - :math:`\xi_i=t_{intern}k=t_{intern}3k_bT/l^2`  internal friction per bead
    - RNI : Rouse model with non-local interactions as additional friction between spatial close beads [5]_ .
            - :math:`t_{rp}=t_r p^{-2}+Nt_{intern}/p`
    - RAP : Rouse model with anharmonic potentials in bonds describing the stiffness of the chain [6]_.
            - :math:`t_{rp}=t_r p^{-2}+t_{intern}ln(N/p\pi)`
    - SPECRIF : Specific interactions of relative strength :math:`b` between beads separated by *m* bonds.
            Internal friction between neighboring beads as in RIF is added.

            - :math:`t_{rp}=t_r p^{-2} (1+bm^2)^{-1} + (1+\frac{m^2}{1+bm^2})t_{intern}`
            - :math:`b=k_{specific}/k_{neighbor}` relative strength of both interactions.
            - The interaction is between **all** pairs separated by m.
    - CRIF : Compacted Rouse with internal friction [9]_.
             The beads are confined in an additional harmonic potential with
             :math:`\frac{1}{2}k_c(r_n-0)^2` leading to a more compact configuration.
             :math:`rk= k_c/k` describes the relative strength compared to the force between beads :math:`k`.
             Typically :math:`rk << 1` .

             - The mode amplitude prefactor changes from Rouse type to modified confined amplitudes

               .. math:: A_p =\frac{4R_e^2}{\pi^2}\frac{1}{p^2}\Rightarrow
                         A_p^c = \frac{4R_e^2}{\pi^2}\frac{1}{\frac{N^2k_c}{\pi^2k}+p^2}

             - The mode relaxation time changes from Rouse type to modified confined

               .. math:: t_{rp} = \frac{t_r}{p^2} \Rightarrow
                         t_{rp}^c =  \frac{t_r}{\frac{N^2k_c}{\pi^2k} + p^2}

             - :math:`R_e` allows to determine :math:`k_c/k` from small angle scattering data

                .. math:: R_e^2 = \frac{2l^2}{\sqrt{k_c/k}}tanh(\frac{N}{2}\sqrt{k_c/k})
             - We assume here that the additional potential is :math:`\frac{1}{2}k_c(r_n-r_0)^2` with :math:`r_0`
               as the polymer center of mass. As the Langevin equation only depends on relative distances the
               internal motions are not affected. The center of mass diffusion :math:`D_{cm}=f(R_e)` is not affected
               as the mode dependent friction coefficients dont change [9]_.
             - With :math:`rk=k_c/k \rightarrow 0` the original Rouse is recovered for amplitudes,
               relaxation and :math:`R_e` .

    A combination of different effects is possible [7]_ (but not implemented).

    The amplitude :math:`A_p` allows for additional suppression of specific modes
    e.g. by topological constraints (see [8]_).

    From above the triple Dcm,l,NN are fixed.
     - If 2 are given 3rd is calculated
     - If all 3 are given the given values are used

    For an example see `example_Zimm`.
    To speedup see example :py:func:`~.formel.memoize`

    Examples
    --------
    Coherent and incoherent contributions to Rouse dynamics.
    To mix the individual q dependent contributions have to be weighted with the according formfactor respectivly
    incoherent scattering length and instrument specific measurement technique.
    ::

     import jscatter as js
     import numpy as np
     t = js.loglist(0.02, 100, 40)
     q=np.r_[0.1:2:0.2]
     l=0.38  # nm , bond length amino acids
     rr = js.dynamic.finiteRouse(t, q, 124, 7, l=0.38, Dcm=0.37, tintern=0., Temp=273 + 60)
     p=js.grace()
     p.multi(2,1)
     p[0].xaxis(scale='log')
     p[0].yaxis(label='I(q,t)\scoherent')
     p[1].xaxis(label=r't / ns',scale='log')
     p[1].yaxis(label=r'I(q,t)\sincoherent')
     p[0].title('Rouse dynamics in a solvent')
     for i, z in enumerate(rr, 1):
         p[0].plot(z.X, z.Y, line=[1, 1, i], symbol=0, legend='q=%g' % z.q)
         p[0].plot(z.X, z._Sqt_inf, line=[3, 2, i], symbol=0, legend='q=%g diff' % z.q)
         p[1].plot(z.X, z._Sqtinc, line=[1, 2, i], symbol=0, legend='q=%g diff' % z.q)

     #p.save(js.examples.imagepath+'/Rousecohinc.jpg')

    .. image:: ../../examples/images/Rousecohinc.jpg
     :align: center
     :width: 50 %
     :alt: Rouse

    References
    ----------
    .. [1]  Doi Edwards Theory of Polymer dynamics
            in the appendix the equation is found
    .. [2]  Nonflexible Coils in Solution: A Neutron Spin-Echo Investigation of
            Alkyl-Substituted Polynorbonenes in Tetrahydrofuran
            Michael Monkenbusch et al.Macromolecules 2006, 39, 9473-9479
            The exponential is missing a "t"
            http://dx.doi.org/10.1021/ma0618979

    about internal friction

    .. [3]  Exploring the role of internal friction in the dynamics of unfolded proteins using simple polymer models
            Cheng et al.JOURNAL OF CHEMICAL PHYSICS 138, 074112 (2013)  http://dx.doi.org/10.1063/1.4792206
    .. [4]  Rouse Model with Internal Friction: A Coarse Grained Framework for Single Biopolymer Dynamics
            Khatri, McLeish|  Macromolecules 2007, 40, 6770-6777  http://dx.doi.org/10.1021/ma071175x
    .. [5]  Origin of internal viscosities in dilute polymer solutions
            P. G. de Gennes
            J. Chem. Phys. 66, 5825 (1977); https://doi.org/10.1063/1.433861
    .. [6]  Microscopic theory of polymer internal viscosity: Mode coupling approximation for the Rouse model.
            Adelman, S. A., & Freed, K. F. (1977).
            The Journal of Chemical Physics, 67(4), 1380–1393. https://doi.org/10.1063/1.435011
    .. [7]  Internal friction in an intrinsically disordered protein - Comparing Rouse-like models with experiments
            A. Soranno, F. Zosel, H. Hofmann
            J. Chem. Phys. 148, 123326 (2018)  http://aip.scitation.org/doi/10.1063/1.5009286
    .. [8]  Onset of topological constraints in polymer melts: A mode analysis by neutron spin echo spectroscopy
            D. Richter, L. Willner, A. Zirkel, B. Farago, L. J. Fetters, and J. S. Huang
            Phys. Rev. Lett. 71, 4158  https://doi.org/10.1103/PhysRevLett.71.4158
    .. [9]  Looping dynamics of a flexible chain with internal friction at different degrees of compactness.
            Samanta, N., & Chakrabarti, R. (2015).
            Physica A: Statistical Mechanics and Its Applications, 436, 377–386.
            https://doi.org/10.1016/j.physa.2015.05.042

    """
    kb = 1.3806505e-23  # in SI units  J/K
    # assure flatt arrays
    t = np.atleast_1d(t)
    q = np.atleast_1d(q)
    # avoid l=0
    if l == 0: l = None
    NN = int(NN)
    if pmax is None: pmax = NN
    # if a list pmax of modes is given these are amplitudes for the modes
    # pmax is length of list
    if isinstance(pmax, numbers.Number):
        pmax = min(int(pmax), NN)
        modeamplist = np.ones(pmax)
    elif isinstance(pmax, list):
        modeamplist = np.abs(pmax)
    else:
        raise TypeError('pmax should be integer or list of amplitudes')

    # create correction for diffusion
    if Dcmfkt is not None:
        if formel._getFuncCode(Dcmfkt):
            # is already an interpolation function
            Dcmfunktion = Dcmfkt
        elif np.shape(Dcmfkt)[0] == 2:
            Dcmfunktion = lambda qq: dA(Dcmfkt).interp(qq)
        else:
            raise TypeError('Shape of Dcmfkt is not 2xN!')
    else:
        # by default no correction
        Dcmfunktion = lambda qq: 1.

    # calc the cases of not given parameters for Dcm,NN,l
    # kB*Temp is in SI so convert all to SI then back to ns
    if rk is not None:
        # [9]_ equ 17  for rk->0 this goes to l*NN**0.5
        Re = 2 * l ** 2 / rk ** 0.5 * np.tanh(NN / 2 * rk ** 0.5)
    else:
        # end to end distance
        Re = l * np.sqrt(NN)
    # friction or Dcm must be given
    # Dcm is independent of rk as no HI in Rouse
    if Dcm is not None and frict is not None:
        pass
    elif Dcm is not None and frict is None:
        frict = kb * Temp / NN / (Dcm * 1e-9)  # diffusion constant  in nm^2/ns
    elif Dcm is None and frict is not None:
        Dcm = kb * Temp / NN / frict * 1e9  # diffusion constant  in nm^2/ns
    elif Dcm is None and frict is None and Wl4 is not None:
        Dcm = Wl4 / (3 * Re ** 2)
        frict = kb * Temp / NN / (Dcm * 1e-9)
    else:
        raise TypeError('fqtfiniteRouse takes at least 1 arguments from Dcm, frict, Wl4')

    # slowest relaxation time is rouse time
    tr1 = frict * NN ** 2 * l ** 2 / (3 * pi ** 2 * kb * Temp) * 1e-9
    # different models for internal friction
    p = np.r_[1:len(modeamplist) + 1]
    modeamplist = 4 * Re ** 2 / pi ** 2 * modeamplist
    if ftype == 'rni':
        # rouse with non-local interactions
        # frict = f_s + p *f_i
        trp = tr1 / p ** 2 + NN * abs(tintern) / p
        modeamplist = modeamplist / p ** 2
    elif ftype == 'rap':
        # rouse model with anharmonic potentials
        trp = tr1 / p ** 2 + abs(tintern) * np.log(NN / p * np.pi)
        modeamplist = modeamplist / p ** 2
    elif ftype == 'specrif':
        # rouse model with specific interactions between bead separated by specm of relative strength specb
        # + rif
        trp = tr1 / p ** 2 / (1 + specb * specm ** 2) + (1 + specm ** 2 / (1 + specb * specm ** 2)) * abs(tintern)
        modeamplist = modeamplist / p ** 2
    elif ftype == 'crif':
        # compacted rouse with internal friction
        trp = tr1 / (NN ** 2 / np.pi ** 2 * rk + p ** 2) + abs(tintern)
        modeamplist = modeamplist / (NN ** 2 / np.pi ** 2 * rk + p ** 2)
    else:
        # RIF with constant internal friction time added as default
        trp = tr1 / p ** 2 + abs(tintern)
        modeamplist = modeamplist / p ** 2
        ftype = 'rif'

    # prepend 0
    t = np.r_[0, np.atleast_1d(t)]

    # do the calculation as an array of bnm=[n*m , len(t)] elements
    # sum up contributions for modes: all, diff+ mode1, only diffusion, t=0 amplitude for normalisation
    if useFortran:
        RNM = fscatter.dynamic.bnmt(t, NN, l, 0.5, modeamplist, trp)
        RNMmodes = RNM[:, -len(modeamplist):]
        RNMi = RNM[:, len(t):(2*len(t))]  # incoherent
        RNM = RNM[:, :len(t)]  # coherent
    else:
        raise ImportError('finiteRouse only with working Fortran.')

    result = dL()
    for qq in q:
        # diffusion for all t
        Sqt = np.exp(-qq ** 2 * Dcm * Dcmfunktion(qq) * t[1:])  # only diffusion contribution
        # amplitude at t=0
        expB0 = np.sum(np.exp(-qq ** 2 / 6. * RNM[:, 0]))  # is S(qq,t=0)/Sqt  # coherent
        expB0i = np.sum(np.exp(-qq ** 2 / 6. * RNMi[:, 0]))  # is S(qq,t=0)/Sqt incoherent
        # diffusion for infinite times in modes
        expBinf = np.sum(np.exp(-qq ** 2 / 6. * np.sum(RNMmodes, axis=1)))  # is S(qq,t=inf)/Sqt
        # contribution all modes
        expB = np.sum(np.exp(-qq ** 2 / 6. * RNM[:, 1:]), axis=0)  # coherent
        expBi = np.sum(np.exp(-qq ** 2 / 6. * RNMi[:, 1:]), axis=0)  # incoherent
        # contribution only first modes
        result.append(dA(np.c_[t[1:], Sqt * expB / expB0, Sqt * expBinf / expB0,  Sqt * expBi / expB0i].T))
        result[-1].setColumnIndex(iey=None)
        result[-1].modecontribution = (np.sum(np.exp(-qq ** 2 / 6. * RNMmodes), axis=0) / expB0).flatten()
        result[-1].q = qq
        result[-1].Re = Re
        result[-1].ll = l
        result[-1].pmax = pmax
        result[-1].Dcm = Dcm
        result[-1].effectiveDCM = Dcm * Dcmfunktion(qq)
        result[-1].Dcmrouse = kb * Temp / NN / frict * 1e9
        result[-1].Temperature = Temp
        result[-1].trouse = tr1
        result[-1].tintern = tintern
        result[-1].moderelaxationtimes = trp
        result[-1].modeamplitudes = modeamplist
        result[-1].beadfriction = frict
        result[-1].Drot = 1. / 6. / tr1
        result[-1].N = NN
        result[-1].internalfriction_g_ns = (tintern * 1e-9) * 3 * kb * Temp / (l * 1e-9) ** 2 * 1e-6
        result[-1].columnname = 'time; Sqt; Sqt_inf; Sqtinc'
        result[-1].ftype = ftype
        result[-1].rk = rk
        if specm is not None:
            result[-1].specm = specm
            result[-1].specb = specb
    if len(result) == 1:
        return result[0]
    result.setColumnIndex(iey=None)
    result.modelname = inspect.currentframe().f_code.co_name
    return result


@formel.memoize()
def _msd_trap(t, u, rt, gamma=1):
    # defined here to memoize it
    #  msd in trap ; equ 4 right part
    res = np.zeros_like(t) + u ** 2
    res[t < rt * 30] = 6 * u ** 2 * (1 - formel.Ea(-(t[t < rt * 30] / rt) ** gamma, gamma))
    return res


def diffusionPeriodicPotential(t, q, u, rt, Dg, gamma=1):
    r"""
    Fractional diffusion of a particle in a periodic potential.

    The diffusion describes a fast dynamics inside of the potential trap with a mean square displacement
    before a jump and a fractional long time diffusion. For fractional coefficient gamma=1 normal diffusion
    is recovered.

    Parameters
    ----------
    t : array
        Time points, units ns.
    q : float
        Wavevector, units 1/nm
    u : float
        Root mean square displacement in the trap, units nm.
    rt : float
        Relaxation time  of fast dynamics in the trap; units ns ( = 1/lambda in [1]_ )
    gamma : float
        Fractional exponent gamma=1 is normal diffusion
    Dg : float
        Long time fractional diffusion coefficient; units nm**2/ns.

    Returns
    -------
    dataArray :
        [t, Iqt , Iqt_diff, Iqt_trap]

    Notes
    -----
    We use equ. 4 of [1]_ for fractional diffusion coefficient :math:`D_{\gamma}` with fraction :math:`\gamma` as

    .. math:: I(Q,t) = exp(-\frac{1}{6}Q^2 msd(t))

    .. math:: msd(t) = \langle (x(t)-x(0))^2 \rangle =
              6\Gamma^{-1}(\gamma+1)D_{\gamma}t^{\gamma} + 6\langle u^2 \rangle (1-E_{\gamma}(-(\lambda t)^{\gamma}))

    with the Mittag Leffler function :math:`E_{\gamma}(-at^{\gamma})` and Gamma function :math:`\Gamma`
    and :math:`\lambda =1/r_t`.

    The first term in *msd* describes the long time fractional diffusion
    while the second describes the additional mean-square displacement inside the trap :math:`\langle u^2 \rangle`.

    For :math:`\gamma=1 \to E_{\gamma}(-at^{\gamma}) \to exp(-at)` simplifying the equation to normal diffusion
    with traps.

    Examples
    --------
    Example similar to protein diffusion in a mesh of high molecular weight PEG as found in [1]_.
    ::

     import jscatter as js
     import numpy as np
     t=js.loglist(0.1,50,100)
     p=js.grace()
     for i,q in enumerate(np.r_[0.1:2:0.3],1):
         iq=js.dynamic.diffusionPeriodicPotential(t,q,0.5,5,0.036)
         p.plot(iq,symbol=[1,0.3,i],legend='q=$wavevector')
         p.plot(iq.X,iq._Iqt_diff,sy=0,li=[1,0.5,i])
     p.title('Diffusion in periodic potential traps')
     p.subtitle('lines show long time diffusion contribution')
     p.yaxis(max=1,min=1e-2,scale='log',label='I(Q,t)/I(Q,0)')
     p.xaxis(min=0,max=50,label='t / ns')
     p.legend(x=110,y=0.8)
     # p.save(js.examples.imagepath+'/fractalDiff.jpg')

    .. image:: ../../examples/images/fractalDiff.jpg
     :align: center
     :height: 300px
     :alt: fractalDiff


    References
    ----------
    .. [1] Gupta, S.; Biehl, R.; Sill, C.; Allgaier, J.; Sharp, M.; Ohl, M.; Richter, D.
           Macromolecules 2016, 49 (5), 1941.

    """
    # q=np.atleast_1d(q)
    # mean square displacement for diffusion in periodic potential no trap; equ 4 left part
    msd = lambda t, Dg, u, rt, gamma=1: 6 * Dg * t ** gamma / scipy.special.gamma(gamma + 1)

    # Trap contribution in _msd_trap. This is memoized as it is independent of the wavevector
    # but for fitting with several Q it is needed multiple times. Cache size is 128 entries.

    # the above but extrapolation to t=0 without trap as contribution of long time diffusion at short times
    msd_0 = lambda t, Dg, u, rt, gamma=1: 6 * Dg * t ** gamma / scipy.special.gamma(gamma + 1) + 6 * u ** 2
    # intermediate scattering function of diffusion in periodic...
    sqt = lambda q, t, Dg, u, rt, gamma=1: np.exp(-q ** 2 / 6 * (msd(t, Dg, u, rt, gamma)))
    sqttrap = lambda q, t, Dg, u, rt, gamma=1: np.exp(-q ** 2 / 6 * (_msd_trap(t, u, rt, gamma)))
    sqt_0 = lambda q, t, Dg, u, rt, gamma=1: np.exp(-q ** 2 / 6 * msd_0(t, Dg, u, rt, gamma))

    result = dA(np.c_[t, sqt(q, t, Dg, u, rt, gamma) * sqttrap(q, t, Dg, u, rt, gamma),
                      sqt_0(q, t, Dg, u, rt, gamma),
                      sqttrap(q, t, Dg,u, rt, gamma)].T)
    result.wavevector = q
    result.fractionalDiffusionCoefficient = Dg
    result.displacement_u = u
    result.relaxationtime = rt
    result.fractionalCoefficient_gamma = gamma
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt;Iqt_diff;Iqt_trap'
    return result


def zilmanGranekBicontinious(t, q, xi, kappa, eta, mt=1, amp=1, eps=1, nGauss=60):
    r"""
    Dynamics of bicontinuous micro emulsion phases. Zilman-Granek model as equ B10 in [1]_. Coherent scattering.

    On very local scales (however larger than the molecular size) Zilman and Granek represent the amphiphile layer
    in the bicontinuous network as consisting of an ensemble of independent patches at random orientation of size
    equal to the correlation length xi.
    Uses Gauss integration and multiprocessing.

    Parameters
    ----------
    t : array
        Time values in ns
    q : float
        Scattering vector in 1/A
    xi : float
        Correlation length related to the size of patches which are locally planar
        and determine the width of the peak in static data. unit A
        A result of the teubnerStrey model to e.g. SANS data. Determines kmin=eps*pi/xi .
    kappa : float
        Apparent single membrane bending modulus, unit kT
    eta : float
        Solvent viscosity, unit kT*A^3/ns=100/(1.38065*T)*eta[unit Pa*s]
        Water about 0.001 Pa*s = 0.000243 kT*A^3/ns
    amp : float, default = 1
        Amplitude scaling factor
    eps : float, default=1
        Scaling factor in range [1..1.3] for kmin=eps*pi/xi and rmax=xi/eps. See [1]_.
    mt : float, default 0.1
        Membrane thickness in unit A as approximated from molecular size of material. Determines kmax=pi/mt.
        About 12 Angstrom for tenside C10E4.
    nGauss : int, default 60
        Number of points in Gauss integration

    Returns
    -------
        dataList

    Notes
    -----
    See equ B10 in [1]_ :

    .. math:: S(q,t) = \frac{2\pi\xi^2}{a^4} \int_0^1 d\mu \int_0^{r_{max}} dr rJ_0(qr\sqrt{1-\mu^2})
                       e^{-kT/(2\pi\kappa)q^2\mu^2 \int_{k_{min}}^{k_{max}} dk[1-J_0(kr)e^{w(k)t}]/k^3}

    with :math:`\mu = cos(\sphericalangle(q,surface normal))` , :math:`J_0` as Bessel function of order 0

    - For technical reasons, in order to avoid numerical difficulties,
      the real space upper (rmax integration) cutoff was realized by multiplying the
      integrand with a Gaussian having a width of eps*xi and integrating over [0,3*eps*xi].

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     t=js.loglist(0.1,30,20)
     p=js.grace()
     iqt=js.dynamic.zilmanGranekBicontinious(t=t,q=np.r_[0.03:0.2:0.04],xi=110,kappa=1.,eta=0.24e-3,nGauss=60)
     p.plot(iqt)

     # to use the multiprocessing in a fit of data use memoize
     data=iqt                          # this represent your measured data
     tt=list(set(data.X.flatten))      # a list of all time values
     tt.sort()

     # use correct values from data for q     -> interpolation is exact for q and tt
     zGBmem=js.formel.memoize(q=data.q,t=tt)(js.dynamic.zilmanGranekBicontinious)
     def mfitfunc(t, q, xi, kappa, eta, amp):
        # this will calculate in each fit step for for Q (but calc all) and then take from memoized values
        res= zGBmem(t=t, q=q, xi=xi, kappa=kappa, eta=eta, amp=amp)
        return res.interpolate(q=q,X=t)[0]
     # use mfitfunc for fitting with multiprocessing


    References
    ----------
    .. [1] Dynamics of bicontinuous microemulsion phases with and without amphiphilic block-copolymers
           M. Mihailescu, M. Monkenbusch et al
           J. Chem. Phys. 115, 9563 (2001); http://dx.doi.org/10.1063/1.1413509

    """

    tt = np.r_[0., t]
    qq = np.r_[q]
    result = dL()
    nres = formel.doForList(_zgbicintegral, looplist=qq, loopover='q', t=tt, xi=xi, kappa=kappa, eta=eta, mt=mt,
                              eps=eps, nGauss=nGauss)
    for qi, res in zip(qq, nres):
        S0 = res[0]
        result.append(dA(np.c_[t, res[1:]].T))
        result[-1].setColumnIndex(iey=None)
        result[-1].Y *= amp / S0
        result[-1].q = qi
        result[-1].xi = xi
        result[-1].kappa = kappa
        result[-1].eta = eta
        result[-1].eps = eps
        result[-1].mt = mt
        result[-1].amp = amp
        result[-1].setColumnIndex(iey=None)
        result[-1].columnname = 't;Iqt'

    return result


def _zgbicintegral(t, q, xi, kappa, eta, eps, mt, nGauss):
    """integration of gl. B10 in Mihailescu, JCP 2001"""
    quad = formel.parQuadratureFixedGauss
    aquad = formel.parQuadratureAdaptiveGauss

    def _zgintegrand_k(k, r, t, kappa, eta):
        """kmin-kmax integrand of gl. B10 in Mihailescu, JCP 2001"""
        tmp = -kappa / 4. / eta * k ** 3 * t
        res = (1. - special.j0(k * r) * np.exp(tmp)) / k ** 3
        return res

    def _zgintegral_k(r, t, xi, kappa, eta):
        """kmin-kmax integration of gl. B10 in Mihailescu, JCP 2001
        integration is done in 2 intervals to weight the lower stronger.
        """
        kmax = pi / mt
        # use higher accuracy at lower k
        res0 = aquad(_zgintegrand_k, eps * pi / xi, kmax / 8., 'k', r=r, t=t[None, :], kappa=kappa, eta=eta,
                     rtol=0.1 / nGauss, maxiter=250)
        res1 = aquad(_zgintegrand_k, kmax / 8., kmax, 'k', r=r, t=t[None, :], kappa=kappa, eta=eta, rtol=1. / nGauss,
                     maxiter=250)
        return res0 + res1

    def _zgintegrand_mu_r(r, mu, q, t, xi, kappa, eta):
        """Mu-r integration of gl. B10 in Mihailescu, JCP 2001
        aus numerischen Gruenden Multiplikation mit Gaussfunktion mit Breite xi"""
        tmp = (-1 / (2 * pi * kappa) * q * q * mu * mu * _zgintegral_k(r, t, xi, kappa, eta)[0] - r * r / (
                2 * (eps * xi) ** 2))
        tmp[tmp < -500] = -500  # otherwise overflow error in np.exp
        y = r * special.j0(q * r * np.sqrt(1 - mu ** 2)) * np.exp(tmp - r ** 2 / (2 * (eps * xi) ** 2))
        return y

    def _gaussBorder(mu, q, t, xi, kappa, eta):
        # For technical reasons, in order to avoid numerical difficulties, the real
        # space upper cutoff was realized by multiplying the integrand with a
        # Gaussian having a width of eps*xi.
        y = quad(_zgintegrand_mu_r, 0, eps * 3 * xi, 'r', mu=mu, q=q, t=t, xi=xi, kappa=kappa, eta=eta, n=nGauss)
        return y

    y = quad(_gaussBorder, 0., 1., 'mu', q=q, t=t, xi=xi, kappa=kappa, eta=eta, n=nGauss)
    return y


def zilmanGranekLamellar(t, q, df, kappa, eta, mu=0.001, eps=1, amp=1, mt=0.1, nGauss=40):
    r"""
    Dynamics of lamellar microemulsion phases.  Zilman-Granek model as Equ 16 in [1]_. Coherent scattering.

    Oriented lamellar phases at the length scale of the inter membrane distance and beyond are performed
    using small-angle neutrons scattering and neutron spin-echo spectroscopy.

    Parameters
    ----------
    t : array
        Time in ns
    q : float
        Scattering vector
    df : float
        - film-film distance. unit A
        - This represents half the periodicity of the structure,
          generally denoted by d=0.5df which determines the peak position and determines kmin=eps*pi/df
    kappa : float
        Apparent single membrane bending modulus, unit kT
    mu : float, default 0.001
        Angle between q and surface normal in unit rad.
        For lamellar oriented system this is close to zero in NSE.
    eta : float
        Solvent viscosity, unit kT*A^3/ns = 100/(1.38065*T)*eta[unit Pa*s]
        Water about 0.001 Pa*s = 0.000243 kT*A^3/ns
    eps : float, default=1
        Scaling factor in range [1..1.3] for kmin=eps*pi/xi and rmax=xi/eps
    amp : float, default 1
        Amplitude scaling factor
    mt : float, default 0.1
        Membrane thickness in unit A as approximated from molecular size of material. Determines kmax=pi/mt
        About 12 Angstrom for  tenside C10E4.
    nGauss : int, default 40
        Number of points in Gauss integration

    Returns
    -------
        dataList

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     t=js.loglist(0.1,30,20)
     ql=np.r_[0.08:0.261:0.03]
     p=js.grace()
     iqt=js.dynamic.zilmanGranekLamellar(t=t,q=ql,df=100,kappa=1,eta=2*0.24e-3)
     p.plot(iqt)

    Notes
    -----
    See equ 16 in [1]_ :

    .. math:: S(q,t) \propto \int_0^{r_{max}} dr r J_0(q_{\perp}r)
                      exp \Big( -\frac{kT}{2\pi\kappa} q^2\mu^2
                      \int_{k_{min}}^{k_{max}} \frac{dk}{k^3} [1-J_0(kr) e^{w^\infty(k)t}] \Big)

    with :math:`w^{\infty(k) = k^3\kappa/4\overline{\eta}}`, :math:`\mu = cos(\sphericalangle(q,surface normal))` ,
     :math:`J_0` as Bessel function of order 0. For details see [1]_.



    The integrations are done by nGauss point Gauss quadrature, except for the kmax-kmin integration which is done by
    adaptive Gauss integration with rtol=0.1/nGauss k< kmax/8 and rtol=1./nGauss k> kmax/8.

    References
    ----------
    .. [1] Neutron scattering study on the structure and dynamics of oriented lamellar phase microemulsions
           M. Mihailescu, M. Monkenbusch, J. Allgaier, H. Frielinghaus, D. Richter, B. Jakobs, and T. Sottmann
           Phys. Rev. E 66, 041504 (2002)

    """

    tt = np.r_[0., t]
    qq = np.atleast_1d(q)
    result = dL()
    nres = formel.doForList(_zglamintegral, looplist=qq, loopover='q', t=tt, kappa=kappa, eta=eta, df=df, mu=mu,
                              mt=mt, eps=eps, nGauss=nGauss)
    for qi, res in zip(qq, nres):
        S0 = res[0]
        result.append(dA(np.c_[t, res[1:]].T))
        result[-1].setColumnIndex(iey=None)
        result[-1].Y *= amp / S0
        result[-1].q = qi
        result[-1].df = df
        result[-1].kappa = kappa
        result[-1].eta = eta
        result[-1].eps = eps
        result[-1].mt = mt
        result[-1].amp = amp
        result[-1].setColumnIndex(iey=None)
        result[-1].columnname = 't;Iqt'

    return result


def _zglamintegral(t, q, df, kappa, eta, eps, mu, mt, nGauss):
    """integration of gl. 16"""
    # quad=scipy.integrate.quad
    quad = formel.parQuadratureFixedGauss
    aquad = formel.parQuadratureAdaptiveGauss

    def _zgintegrand_k(k, r, t, kappa, eta):
        """kmin-kmax integrand o"""
        tmp = -kappa / 4. / eta * k ** 3 * t
        res = (1. - special.j0(k * r) * np.exp(tmp)) / k ** 3
        return res

    def _zgintegral_k(r, t, df, kappa, eta):
        """
        kmin-kmax integration of gl. B10 in Mihailescu, JCP 2001
        """
        kmax = pi / mt
        # use higher accuracy at lower k
        res0 = aquad(_zgintegrand_k, eps * pi / df, kmax / 8., 'k', r=r, t=t[None, :], kappa=kappa, eta=eta,
                     rtol=0.1 / nGauss, maxiter=250)
        res1 = aquad(_zgintegrand_k, kmax / 8., kmax, 'k', r=r, t=t[None, :], kappa=kappa, eta=eta, rtol=1. / nGauss,
                     maxiter=250)
        return res0 + res1

    def _zgintegrand_r(r, mu, q, t, df, kappa, eta):
        """Mu-r integration """
        smu = np.sin(mu)
        tmp = (-1 / (2 * pi * kappa) * q * q * (1 - smu ** 2) * _zgintegral_k(r, t, df, kappa, eta)[0])
        tmp[tmp < -500] = -500  # otherwise overflow error in np.exp
        y = r * special.j0(q * r * smu) * np.exp(tmp)
        return y

    y = quad(_zgintegrand_r, 0, df / eps, 'r', mu=mu, q=q, t=t, df=df, kappa=kappa, eta=eta, n=nGauss)
    return y


def integralZimm(t, q, Temp=293, viscosity=1.0e-3, amp=1, rtol=0.02, tol=0.02, limit=50):
    r"""
    Conformational dynamics of an ideal chain with hydrodynamic interaction, coherent scattering.

    Integral version Zimm dynamics.

    Parameters
    ----------
    t : array
        Time points in ns
    q : float
        Wavevector in 1/nm
    Temp : float
        Temperature in K
    viscosity : float
        Viscosity in cP=mPa*s
    amp : float
        Amplitude
    rtol,tol : float
        Relative and absolute tolerance in scipy.integrate.quad
    limit : int
        Limit in scipy.integrate.quad.

    Returns
    -------
        dataArray

    Notes
    -----
    The Zimm model describes the conformational dynamics of an ideal chain with hydrodynamic
    interaction between beads. We use equ 85 and 86 from [1]_ as

    .. math:: S(Q,t) = \frac{12}{Q^2l^2} \int_0^{\infty} e^{-u-(\Omega_Z t)^{2/3} g(u(\Omega_Z t)^{2/3})} du

    with

    .. math:: g(y) = \frac{2}{\pi} \int_0^{\infty} x^{-2}cos(xy)(1-e^{-2^{-0.5}x^{2/3}}) dx

    .. math:: \Omega_z = \frac{kTQ^3}{6\pi\eta_s}

    See [1]_ for details.

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     t=np.r_[0:10:0.2]
     p=js.grace()
     for q in np.r_[0.26,0.40,0.53,0.79,1.06]:
        iqt=js.dynamic.integralZimm(t=t,q=q,viscosity=0.2e-3)
        p.plot(iqt)
        #p.plot((iqt.X*iqt.q**3)**(2/3.),iqt.Y)

    References
    ----------
    .. [1] Neutron Spin Echo Investigations on the Segmental Dynamics of Polymers in Melts, Networks and Solutions
           in Neutron Spin Echo Spectroscopy Viscoelasticity Rheology
           Volume 134 of the series Advances in Polymer Science pp 1-129
           DOI 10.1007/3-540-68449-2_1

    """
    quad = scipy.integrate.quad
    kb = 1.3806503e-23  # J/K
    tt = np.r_[t] * 1e-9
    tt[t == 0] = 1e-20  # avoid zero
    # Zimm diffusion coefficient
    OmegaZ = (q * 1e9) ** 3 * kb * Temp / (6 * pi * viscosity)

    _g_integrand = lambda x, y: math.cos(y * x) / x / x * (1 - math.exp(-x ** (3. / 2.) / math.sqrt(2)))
    _g = lambda y: 2. / pi * quad(_g_integrand, 0, np.inf, args=(y,), epsrel=rtol, epsabs=tol, limit=limit)[0]

    _z_integrand = lambda u, t: math.exp(-u - (OmegaZ * t) ** (2. / 3.) * _g(u * (OmegaZ * t) ** (2. / 3.)))

    y1 = [quad(_z_integrand, 0, np.inf, args=(ttt,), epsrel=rtol, epsabs=tol, limit=limit)[0] for ttt in tt]

    result = dA(np.c_[t, amp * np.r_[y1]].T)
    result.setColumnIndex(iey=None)
    result.columnname = 't;Iqt'
    result.q = q
    result.OmegaZimm = OmegaZ
    result.Temperature = Temp
    result.viscosity = viscosity
    result.amplitude = amp
    return result


def transRotDiffusion(t, q, cloud, Dr, Dt=0, lmax='auto'):
    r"""
    Translational + rotational diffusion of an object (dummy atoms); dynamic structure factor in time domain.

    A cloud of dummy atoms can be used for coarse graining of a non-spherical object e.g. for amino acids in proteins.
    On the other hand its just a way to integrate over an object e.g. a sphere or ellipsoid (see example).
    We use [2]_ for an objekt of arbitrary shape modified for incoherent scattering.

    Parameters
    ----------
    t : array
        Times in ns.
    q : float
        Wavevector in units 1/nm
    cloud : array Nx3, Nx4 or Nx5 or float
        - A cloud of N dummy atoms with positions cloud[:3] in units nm that describe an object .
        - If given, cloud[3] is the incoherent scattering length :math:`b_{inc}` otherwise its equal 1.
        - If given, cloud[4] is the coherent scattering length :math:`b_{coh}` otherwise its equal 1.
        - If cloud is single float the value is used as radius of a sphere with 10x10x10 grid points.
    Dr : float
        Rotational diffusion constant (scalar) in units 1/ns.
    Dt : float, default=0
        Translational diffusion constant (scalar) in units nm²/ns.
    lmax : int
        Maximum order of spherical bessel function.
        'auto' -> lmax > 2π r.max()*q/6.

    Returns
    -------
        dataArray :
            Columns [t; Iqtinc; Iqtcoh; Iqttrans]
             - .radiusOfGyration
             - .Iq_coh  coherent scattering (formfactor)
             - .Iq_inc  incoherent scattering
             - .wavevector
             - .rotDiffusion
             - .transDiffusion
             - .lmax

    Notes
    -----
    We calculate the field autocorrelation function given in equ 24 in [2]_ for an arbitrary rigid object
    without additional internal dynamic as

    .. math:: I(q,t) = e^{-q^2D_tt} I_{rot}(q,t) = e^{-q^2D_tt} \sum_l S_{l,i/c}(q)e^{-l(l+1)D_rt}

    where :math:`I_{rot}(q,t)` is the rotational diffusion contribution and

    .. math:: S_{l,c}(q) &= 4\pi \sum_m |\sum_i b_{i,coh} j_l(qr_i) Y_{l,m}(\Omega_i)|^2  & coherent scattering \\

              S_{l,i}(q) &= \sum_m \sum_i (2l+1) b_{i,inc}^2 |j_l(qr_i)|^2   & incoherent scattering\\

    and coh/inc scattering length :math:`b_{i,coh/inc}`, position vector :math:`r_i` and orientation of atoms
    :math:`\Omega_i`, spherical Bessel function :math:`j_l(x)`, spherical harmonics :math:`Y_{l,m}(\Omega_i)`.


    - The incoherent intermediate scattering function is res.Y/res.Iq_inc or res._Iqtinc/res.Iq_inc
    - The coherent   intermediate scattering function is res._Iqtcoh/res.Iq_coh
    - For real scattering data as backscattering or spinecho coherent and incoherent have to be mixed according
      to the polarisation conditions of the experiment accounting also for spin flip probability of coherent and
      incoherent scattering. For the simple case of non-polarised  measurement we get

    .. math:: I(q,t)/I(q,0) = \frac{I_{coh}(q,t)+I_{inc}(q,t)}{I_{coh}(q,0)+I_{inc}(q,0)}



    Examples
    --------
    A bit artificial look at only rotational diffusion of a superball build from dummy atoms.
    (rotational diffusion should only show if also translational diffusion is seen)
    Change p to change from spherical shape (p=1) to cube (p>10) or star like (p<0.5)
    (use grid.show() to take a look at the shape)
    The coherent contribution is suppressed for low q if the particle is spherical .
    ::

     import jscatter as js
     import numpy as np
     R=2;NN=10
     ql=np.r_[0.4:2.:0.3,2.1:15:2]
     t=js.loglist(0.001,50,50)
     # get superball
     p2=1
     grid=js.ff.superball(ql,R,p=p2,nGrid=NN,returngrid=True)
     Drot=js.formel.Drot(R)
     Dtrans=js.formel.Dtrans(R)
     p=js.grace(1.5,1)
     p.new_graph(xmin=0.23,xmax=0.43,ymin=0.25,ymax=0.55)
     iqt=js.dL([js.dynamic.transRotDiffusion(t,q,grid.XYZ,Drot,lmax=30) for q in ql])

     for i,iiqt in enumerate(iqt,1):
         p[0].plot(iiqt.X,iiqt.Y/iiqt.Iq_inc,li=[1,3,i],sy=0,le=f'q={iiqt.wavevector:.1f} nm\S-1')
         p[0].plot(iiqt.X,iiqt._Iqtcoh/iiqt.Iq_coh,li=[3,3,i],sy=0,le=f'q={iiqt.wavevector:.1f} nm\S-1')

     p[1].plot(iqt.wavevector,iqt.Iq_coh.array/grid.numberOfAtoms(),li=1)
     p[1].plot(iqt.wavevector,iqt.Iq_inc.array/grid.numberOfAtoms(),li=1)
     p[0].xaxis(scale='l',label='t / ns',max=200,min=0.001)
     p[0].yaxis(scale='n',label='I(q,t)/I(q,0)')
     p[1].xaxis(scale='n',label='q / nm\S-1')
     p[1].yaxis(scale='l',label='I(q,t=0)')

     p[0].legend(x=60,y=1.1,charsize=0.7)
     p[0].title(f'rotational diffusion of superball with p={p2:.2f}')
     p[0].subtitle(f'coh relevant only at high q for sphere')
     p[1].subtitle('coh + inc scattering')
     p[0].text(x=0.0015,y=0.8,string=r'lines inc\ndashed coh',charsize=1.5)
     #p.save(js.examples.imagepath+'/rotDiffusion.jpg')

     # Second example
     # non-polarized experiment
     p=js.grace(1.5,1)
     grid=js.ff.superball(ql,R,p=1.,nGrid=10,returngrid=True)
     iqt=js.dL([js.dynamic.transRotDiffusion(t,q,grid.XYZ,Drot,Dtrans,lmax=30) for q in ql])
     for i,iiqt in enumerate(iqt,1):
         p.plot(iiqt.X,(iiqt._Iqtinc+iiqt._Iqtcoh)/(iiqt.Iq_inc+iiqt.Iq_coh),li=[1,3,i],sy=0,le=f'q={iiqt.wavevector:.1f} nm\S-1')
         p.plot(iiqt.X,iiqt._Iqtcoh/iiqt.Iq_coh,li=[3,3,i],sy=0,le=f'q={iiqt.wavevector:.1f} nm\S-1')

     p.xaxis(scale='l',label='t / ns',max=200,min=0.001)
     p.yaxis(scale='n',label='I(q,t)/I(q,0)')
     p[0].legend(x=60,y=1.1,charsize=0.7)
     p[0].title(f'translational/rotational diffusion of superball with p={p2:.2f}')
     p[0].text(x=0.0015,y=0.5,string=r'lines coh+inc\ndashed only coh',charsize=1.5)
     #p.save(js.examples.imagepath+'/transrotDiffusion.jpg')

    .. image:: ../../examples/images/rotDiffusion.jpg
     :width: 50 %
     :align: center
     :alt: rotDiffusion

    .. image:: ../../examples/images/transrotDiffusion.jpg
     :width: 50 %
     :align: center
     :alt: transrotDiffusion



    References
    ----------
    .. [1] Incoherent scattering law for neutron quasi-elastic scattering in liquid crystals.
           Dianoux, A., Volino, F. & Hervet, H. Mol. Phys. 30, 37–41 (1975).
    .. [2] Effect of rotational diffusion on quasielastic light scattering from fractal colloid aggregates.
           Lindsay, H., Klein, R., Weitz, D., Lin, M. & Meakin, P. Phys. Rev. A 38, 2614–2626 (1988).

    """
    Ylm = special.sph_harm
    #: Lorentzian
    expo = lambda t, ll1D: np.exp(-ll1D * t)
    if isinstance(cloud, numbers.Number):
        R = cloud
        NN = 10
        grid = np.mgrid[-R:R:1j * NN, -R:R:1j * NN, -R:R:1j * NN].reshape(3, -1).T
        inside = lambda xyz, R: la.norm(grid, axis=1) < R
        cloud = grid[inside(grid, R)]
    if cloud.shape[1] == 5:
        # last columns are incoherent and coherent scattering length
        blinc = cloud[:, 3]
        blcoh = cloud[:, 4]
        cloud = cloud[:, :3]
    elif cloud.shape[1] == 4:
        # last column is scattering length
        blinc = cloud[:, 3]
        blcoh = np.ones(cloud.shape[0])
        cloud = cloud[:, :3]
    else:
        blinc = np.ones(cloud.shape[0])
        blcoh = blinc
    t = np.array(t, float)
    bi2 = blinc ** 2
    r, p, th = formel.xyz2rphitheta(cloud).T
    pp = p[:, None]
    tt = th[:, None]
    qr = q * r
    if not isinstance(lmax, numbers.Integral):
        # lmax = pi * r.max() * q  / 6. # a la Cryson
        lmax = min(max(2 * int(pi * qr.max() / 6.), 6), 100)

    # We calc here the field autocorrelation function as in equ 24
    # incoherent with i=j ->  Sum_m(Ylm) leads to (2l+1)/4pi
    bjlylminc = [(bi2 * spjn(l, qr) ** 2 * (2 * l + 1)).sum() for l in np.r_[:lmax + 1]]
    # add time dependence
    Iqtinc = np.c_[[bjlylminc[l].real * expo(t, l * (l + 1) * Dr) for l in np.r_[:lmax + 1]]].sum(axis=0)
    Iq_inc = np.sum(bjlylminc).real

    # coh is sum over i then (abs)squared and sum over m    see Lindsay equ 19 or 20
    bjlylmcoh = [4 * np.pi * np.sum(np.abs((blcoh * spjn(l, qr) * Ylm(np.r_[-l:l + 1], l, pp, tt).T).sum(axis=1)) ** 2)
                 for l in np.r_[:lmax + 1]]
    Iqtcoh = np.c_[[bjlylmcoh[l].real * expo(t, l * (l + 1) * Dr) for l in np.r_[:lmax + 1]]].sum(axis=0)
    Iq_coh = np.sum(bjlylmcoh).real

    Iq_trans = np.exp(-q ** 2 * Dt * t)
    result = dA(np.c_[t, Iq_trans * Iqtinc, Iq_trans * Iqtcoh].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 't; Iqtinc; Iqtcoh; Iqttrans'
    result.radiusOfGyration = np.sum(r ** 2) ** 0.5
    result.Iq_coh = Iq_coh
    result.Iq_inc = Iq_inc
    result.wavevector = q
    result.rotDiffusion = Dr
    result.transDiffusion = Dt
    result.lmax = lmax
    return result


# noinspection PyIncorrectDocstring
def resolution(t, s0=1, m0=0, s1=None, m1=None, s2=None, m2=None, s3=None, m3=None,
               s4=None, m4=None, s5=None, m5=None,s6=None, m6=None, s7=None, m7=None,
               a0=1, a1=1, a2=1, a3=1, a4=1, a5=1, a6=1, a7=1, bgr=0, resolution=None):
    r"""
    Resolution in time domain as multiple Gaussians for inelastic measurement
    as back scattering or time of flight instrument.

    Multiple Gaussians define the function to describe a resolution measurement.
    Use ```resolution_w``` to fit with the appropriate normalized Gaussians and this function
    to implicit Fourier transform a signal. See Notes.

    Parameters
    ----------
    t : array
        Times
    s0,s1,... : float
        Width of Gaussian functions representing a resolution measurement.
        The number of si not None determines the number of Gaussians.
    m0, m1,.... : float, None
        Means of the Gaussian functions representing a resolution measurement.
    a0, a1,.... : float, None
        Amplitudes of the Gaussian functions representing a resolution measurement.
    bgr : float, default=0
        Background
    resolution : dataArray
        Resolution with attributes sigmas, amps which are used instead of si, ai.
         - If resolution is from `w` domain this represents the Fourier transform from `w` to `t` domain.
           `means` are NOT used from `w` domain as these result only in a phase shift, instead m0..m5 are used.
         - If from `t` domain the resolution is recalculated with same parameters for new t.


    Returns
    -------
        dataArray

    Notes
    -----
    In a typical inelastic experiment the resolution is measured by e.g. a vanadium measurement (elastic scatterer).
    In `t` domain (Neutron Spin Echo) this is a carbon black sample for small Q or e.g. Zirconium for higher Q.
    In `w` domain the resolution is described by a multi Gaussian function as in resw=resolution_w(w,...) with
    amplitudes ai_w, width si_w and common mean m_w.

    resolution(t,resolution_w=resw) defines the Fourier transform of resolution_w using the same coefficients
    as an implicit Fourier transform.
    mi_t are set by default to zero as mi_w lead only to a phase shift. It is easiest to shift w values in
    w domain as it corresponds to a shift of the elastic line.

    Beside the fitting of resolution measurements the pair of `resolution_w` and `resolution` allows
    a Fourier transform from `w` to `t` domain of any signal. If `resolution_w` is used for fitting
    of data in the `w` domain then ```ft = resolution(t=..,resolution=resolution_w_fit)```
    represents the Fourier transform.

    The used Gaussians are normalized that they are a pair of Fourier transforms:

    .. math:: R_t(t,m_i,s_i,a_i)=\sum_i a_i s_i e^{-\frac{1}{2}s_i^2 t^2} \Leftrightarrow
              R_w(w,m_i,s_i,a_i)= \sum_i a_i e^{-\frac{1}{2}(\frac{w-m_i}{s_i})^2}

    under the Fourier transform defined as

    .. math:: F(f(t)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt

    .. math:: F(f(w)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(\omega) e^{i\omega t} d\omega


    Examples
    --------
    Using the result of a fit in w domain to represent the resolution in time domain :
    ::

     import jscatter as js
     import numpy as np
     # resw is a resolution in w domain maybe as a result from a fit to vanadium data
     # resw contains all parameters
     w=np.r_[-100:100:0.5]
     resw=js.dynamic.resolution_w(w, s0=12, m0=0, a0=2)
     # representing the Fourier transform of resw as a gaussian transforms to time domain
     t=np.r_[0:1:0.01]
     rest=js.dynamic.resolution(t,resolution=resw)
     t2=np.r_[0:0.5:0.005]
     rest2=js.dynamic.resolution(t2,resolution=rest)


    """
    def gauss(x, mean, sigma):
        return np.exp(-0.5 * (x - mean) ** 2 / sigma ** 2) / np.sqrt(2 * pi) / sigma

    if resolution is None:
        means = [m0, m1, m2, m3, m4, m5, m6, m7]
        sigmas = [s0, s1, s2, s3, s4, s5, s6, s7]
        amps = [a0, a1, a2, a3, a4, a5, a6, a7]
    else:
        if resolution.modelname[-1] == 'w':
            means = [m0, m1, m2, m3, m4, m5, m6, m7]
            sigmas = [1. / s if s is not None else s for s in resolution.sigmas]
            amps = resolution.amps
        else:
            means = resolution.means
            sigmas = resolution.sigmas
            amps = resolution.amps
    t = np.atleast_1d(t)
    Y = np.r_[[a * gauss(t, m, s) for s, m, a in zip(sigmas, means, amps)
                                                if (s is not None) & (m is not None)]].sum(axis=0)
    result = dA(np.c_[t, Y + bgr].T)
    result.setColumnIndex(iey=None)
    result.modelname = inspect.currentframe().f_code.co_name
    result.columnname = 't; Rqt'
    result.means = means
    result.sigmas = sigmas
    result.amps = amps
    return result


##################################################################
# frequency domain                                               #
##################################################################

# noinspection PyBroadException
def getHWHM(data, center=0, gap=0, base=False):
    """
    Find half width at half maximum (left/right) of a distribution around center.

    The hwhm is determined from linear spline between Y values to find (Y.max-Y.min)/2
    left and right of the max value. Requirement increasing X values and a flat background.
    If nothing is found an empty list is returned.

    For sparse data a fit with a peak function like a Gaussian/Lorezian is prefered.

    Parameters
    ----------
    data : dataArray
        Distribution
    center: float, default=0
        Center (symmetry point) of data.
        If None the position of the maximum is used.
    gap : float, default 0
        Exclude values around center as it may contain a singularity.
        Excludes values within X<= abs(center-gap).
        The gap should be large enough to reach the baseline on left/right peak side.

    Returns
    -------
        list of float with hwhm X>0 , X<0 if existing

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np

     x = np.r_[0:10:200j]
     data = js.formel.gauss(x,3,0.3)
     data.Y += 2
     HWHM = js.dynamic.getHWHM(data,3,1.1)
     # => (2*np.log(2))**0.5*0.3 = 1.177 * sigma = 0.353

    """
    gap = abs(gap)
    if center is None:
        # determine center
        center = data.X[data.Y.argmax()]
    data1 = data[:, (data.X >= center) & (data.X <= center + gap)]
    data2 = data[:, (data.X <= center) & (data.X >= center - gap)]
    data1.X = data1.X - center
    data2.X = data2.X - center
    res = []

    # right of center
    max = data1.Y.max()
    min = data1.Y.min()
    if np.all(np.diff(data1.X) > 0):
        hwhm1 = np.interp((max - min) / 2. + min, data1.Y.astype(float)[::-1], data1.X.astype(float)[::-1])
        res.append(np.abs(hwhm1))
    else:
        res.append(None)

    # left of center
    max = data2.Y.max()
    min = data2.Y.min()
    if np.all(np.diff(data2.X) > 0):
        hwhm2 = np.interp((max - min) / 2. + min, data2.Y.astype(float), data2.X.astype(float))
        res.append(np.abs(hwhm2))
    else:
        res.append(None)

    return res


def elastic_w(w):
    """
    Elastic line; dynamic structure factor in w domain.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns

    Returns
    -------
        dataArray

    """
    Iqw = np.zeros_like(w)
    Iqw[np.abs(w) < 1e-8] = 1.
    result = dA(np.c_[w, Iqw].T)
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.modelname = inspect.currentframe().f_code.co_name
    return result


def transDiff_w(w, q, D):
    r"""
    Translational diffusion; dynamic structure factor in w domain.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q : float
        Wavevector in nm**-1
    D : float
        Diffusion constant in nm**2/ns

    Returns
    -------
         dataArray

    Notes
    -----
    Equ 33 in [1]_

    .. math:: I(\omega,q) = \frac{1}{\pi} \frac{Dq^2}{(Dq^2)^2 + \omega^2}

    References
    ----------
    .. [0] Scattering of Slow Neutrons by a Liquid
           Vineyard G Physical Review 1958 vol: 110 (5) pp: 999-1010

    """
    dw = q * q * D
    res = 1 / pi * dw / (dw * dw + w * w)
    result = dA(np.c_[w, res].T)
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.modelname = inspect.currentframe().f_code.co_name
    result.wavevector = q
    result.D = D
    return result


def jumpDiff_w(w, q, t0, r0):
    r"""
    Jump diffusion; dynamic structure factor in w domain.

    Jump diffusion as a Markovian random walk. Jump length distribution is a Gaussian
    with width r0 and jump rate distribution with width G (Poisson).
    Diffusion coefficient D=r0**2/2t0.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q : float
        Wavevector in nm**-1
    t0 : float
        Mean residence time in a Poisson distribution of jump times. In units ns.
        G = 1/tg = Mean jump rate
    r0 : float
        Root mean square jump length in 3 dimensions <r**2> = 3*r_0**2


    Returns
    -------
         dataArray

    Notes
    -----
    Equ 6 + 8 in [1]_ :

    .. math:: S_{inc}(q,\omega) = \frac{1}{\pi} \frac{\Delta\omega}{\Delta\omega^2 + \omega^2}

              with \;  \Delta\omega = \frac{1-e^{-q^2 r_0^2/2}}{t_0}



    References
    ----------
    .. [1] Incoherent neutron scattering functions for random jump diffusion in bounded and infinite media.
           Hall, P. L. & Ross, D. K. Mol. Phys. 42, 637–682 (1981).

    """
    Ln = lambda w, dw: dw / (dw * dw + w * w) / pi
    dw = 1. / t0 * (1 - np.exp(-q ** 2 * r0 ** 2 / 2.))
    result = dA(np.c_[w, Ln(w, dw)].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.wavevector = q
    result.meanresidencetime = t0
    result.meanjumplength = r0
    return result


_erfi = special.erfi
_G = special.gamma
_h1f1 = special.hyp1f1
_erf = special.erf
_Gi = special.gammainc


def diffusionHarmonicPotential_w(w, q, tau, rmsd, ndim=3, nmax='auto'):
    r"""
    Diffusion in a harmonic potential for dimension 1,2,3 (isotropic averaged), dynamic structure factor in w domain.

    An approach worked out by Volino et al.[1]_ assuming Gaussian confinement and leads to a more efficient
    formulation by replacing the expression for diffusion in a sphere with a simpler expression pertaining
    to a soft confinement in harmonic potential. Ds = ⟨u**2⟩/t0

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q : float
        Wavevector in nm**-1
    tau : float
        Mean correlation time time. In units ns.
    rmsd : float
        Root mean square displacement (width) of the Gaussian in units nm.
    ndim : 1,2,3, default=3
        Dimensionality of the potential.
    nmax : int,'auto'
        Order of expansion.
        'auto' -> nmax = min(max(int(6*q * q * u2),30),1000)

    Returns
    -------
         dataArray

    Notes
    -----
    Volino et al.[1]_ compared the behaviour of this approach to the well known expression for diffusion in a sphere.
    Even if the details differ, the salient features of both models match if the radius R**2 ≃ 5*u0**2 and
    the diffusion constant inside the sphere relates to the relaxation time of particle correlation t0= ⟨u**2⟩/Ds
    towards the Gaussian with width u0=⟨u**2⟩**0.5.

    .. math:: I_s(Q_x,\omega) = A_0(Q) + \sum_n^{\infty} A_n(Q) L_n(\omega)
              \; with \; L_n(\omega) = \frac{\tau_0 n}{\pi (n^2+ \omega^2\tau_0^2)}

    ndim=3
     Here we use the Fourier transform of equ 23 with equ. 27a+b in [1]_.
     For order n>30 the Stirling approximation for n! in equ 27b of [1]_ is used.

     .. math:: A_0(Q) = e^{-Q^2\langle u^2_x \rangle}

     .. math:: A_n(Q,\omega) = e^{-Q^2\langle u^2_x \rangle} \frac{(Q^2\langle u^2_x \rangle)^n}{n!}

    ndim=2
     Here we use the Fourier transform of equ 23 with equ. 28a+b in [1]_.

    .. math:: A_0(Q) = \frac{\sqrt{\pi} e^{-Q^2\langle u^2_x \rangle}}{2}
                       \frac{erfi(\sqrt{Q^2\langle u^2_x \rangle})}{\sqrt{Q^2\langle u^2_x \rangle}}

    .. math:: A_n(Q,\omega) = \frac{\sqrt{\pi} (Q^2\langle u^2_x \rangle)^n}{2}
                              \frac{F_{1,1}(1+n;3/2+n;-Q^2\langle u^2_x \rangle)}{\Gamma(3/2+n)}

    with :math:`F_{1,1}(a,b,z)` Kummer confluent hypergeometric function, Gamma function :math:`\Gamma`
    and *erfi* is the imaginary error function *erf(iz)/i*


    ndim=1
     The equation given by Volino (29a+b in [1]_) seems to be wrong as a comparison with the Fourier transform and
     the other dimensions shows.
     Use the model from time domain and use FFT as shown in the example.

     For experts: To test this remove a flag in the source code and compare.


    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     t2f=js.dynamic.time2frequencyFF
     dHP=js.dynamic.diffusionHarmonicPotential
     w=np.r_[-100:100]
     ql=np.r_[1:14.1:6j]
     iqt3=js.dL([js.dynamic.diffusionHarmonicPotential_w(w=w,q=q,tau=0.14,rmsd=0.34,ndim=3) for q in ql])
     iqt2=js.dL([js.dynamic.diffusionHarmonicPotential_w(w=w,q=q,tau=0.14,rmsd=0.34,ndim=2) for q in ql])
     # as ndim=1 is a wrong solution use this instead
     # To move spectral leakage out of our window we increase w and interpolate.
     # The needed factor (here 23) depends on the quality of your data and background contribution.
     # You may test it using ndim=2 in this example.
     iqt1=js.dL([t2f(dHP,'elastic',w=w*23,q=q, rmsd=0.34, tau=0.14 ,ndim=1).interpolate(w) for q in ql])

     p=js.grace()
     p.multi(2,3)
     p[1].title('diffusionHarmonicPotential for ndim= 1,2,3')
     for i,(i3,i2,i1) in enumerate(zip(iqt3,iqt2,iqt1)):
         p[i].plot(i3,li=1,sy=0,le='q=$wavevector nm\S-1')
         p[i].plot(i2,li=2,sy=0)
         p[i].plot(i1,li=4,sy=0)
         p[i].yaxis(scale='log')
         if i in [1,2,4,5]:p[i].yaxis(ticklabel=0)
         p[i].legend(x=5,y=1, charsize=0.7)


    References
    ----------
    .. [1] Gaussian model for localized translational motion: Application to incoherent neutron scattering.
           Volino, F., Perrin, J. C. & Lyonnard, S. J. Phys. Chem. B 110, 11217–11223 (2006).

    """
    w = np.array(w, float)
    u2 = rmsd ** 2
    if not isinstance(nmax, numbers.Integral):
        nmax = min(max(int(6 * q * q * u2), 30), 1000)
    Ln = lambda w, t0, n: t0 / pi * n / (n * n + w * w * t0 * t0)  # equ 25a

    if ndim == 3:
        # 3D case
        A0 = lambda q: np.exp(-q * q * u2)  # EISF  equ 27a

        def An(q, n):
            s = (n < 30)  # select not to large n and use for the other the Stirling equation
            An = np.r_[
                (q * q * u2) ** n[s] / special.factorial(n[s]), (q * q * u2 / n[~s] * np.e) ** n[~s] / (
                        2 * pi * n[~s]) ** 0.5]
            An *= np.exp(-q * q * u2)
            return An

        n = np.r_[:nmax] + 1
        an = An(q, n)
        sel = np.isfinite(an)  # remove An with inf or nan
        Iqw = (an[sel, None] * Ln(w, tau, n[sel, None])).sum(axis=0)  # equ 23 after ft
        Iqw[np.abs(w) < 1e-8] += A0(q)

    elif ndim == 2:
        # 2D case
        A0 = lambda q: pi ** 0.5 / 2. * np.exp(-q * q * u2) * _erfi((q * q * u2) ** 0.5) / (
                q * q * u2) ** 0.5  # EISF  equ 28a
        An = lambda q, n: pi ** 0.5 / 2. * (q * q * u2) ** n * _h1f1(1 + n, 1.5 + n, -q * q * u2) / _G(
            1.5 + n)  # equ 28b
        n = np.r_[:nmax] + 1
        Iqw = (An(q, n)[:, None] * Ln(w, tau, n[:, None])).sum(axis=0)  # equ 23 after ft
        Iqw[np.abs(w) < 1e-8] += A0(q)

    elif ndim == 1 and False:
        print(' THis seems to be wrong as given in the paper')
        # 1D case
        A0 = lambda q: pi ** 0.5 / 2. * _erf((q * q * u2) ** 0.5) / (q * q * u2) ** 0.5  # EISF  equ 29a
        An = lambda q, n: (_G(0.5 + n) - _Gi(0.5 + n, q * q * u2)) / (2 * (q * q * u2) ** 0.5 * _G(1 + n))  # equ 29b
        n = np.r_[:nmax] + 1
        an = An(q, n)
        sel = np.isfinite(an)  # remove An with inf or nan
        Iqw = (an[sel, None] * Ln(w, tau, n[sel, None])).sum(axis=0)  # equ 23 after ft
        Iqw[np.abs(w) < 1e-8] += A0(q)
    else:
        raise Exception('ndim should be one of 2 or 3; for 1 use fourier tranform from time domain, see doc.')


    result = dA(np.c_[w, Iqw].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.u0 = rmsd
    result.dimension = ndim
    result.wavevector = q
    result.meancorrelationtime = tau
    result.gaussWidth = rmsd
    result.nmax = nmax
    result.Ds = rmsd ** 2 / tau
    return result


#: First 99 coefficients from Volino for diffusionInSphere_w
# VolinoCoefficient=np.loadtxt(os.path.join(_path_,'data','VolinoCoefficients.dat')) # numpy cannot load because of utf8
with open(os.path.join(_path_, 'data', 'VolinoCoefficients.dat')) as f: VolinoC = f.readlines()
VolinoCoefficient = np.array([line.strip().split() for line in VolinoC if line[0] != '#'], dtype=float)


def diffusionInSphere_w(w, q, D, R):
    r"""
    Diffusion inside of a sphere; dynamic structure factor in w domain.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q : float
        Wavevector in nm**-1
    D : float
        Diffusion coefficient in units nm**2/ns
    R : float
        Radius of the sphere in units nm.

    Returns
    -------
         dataArray

    Notes
    -----
    Here we use equ. 33 in [1]_

    .. math:: S(q,\omega) = A_0^0(q) \delta(\omega) + \frac{1}{\pi}
              \sum_{l,n\ne 0,0}(2l+1)A_n^l(q) \frac{(x_n^l)^2D/a^2}{[(x_n^l)^2D/a^2]^2 + \omega^2}

    with :math:`x_n^l` as the first 99 solutions of equ 27 a+b as given in [1]_ and

    .. math:: A_0^0(q) = \big[ \frac{3j_1(qa)}{qa} \big]^2 , \; (l,n) = (0,0)

    .. math:: A_n^l(q) &= \frac{6(x_n^l)^2}{(x_n^l)^2-l(l+1)}
                         \big[\frac{qaj_{l+1}(qa)-lj_l(qa)}{(qa)^2-(x_n^l)^2}\big]^2 \; for \;  qa\ne x_n^l

                       &= \frac{3}{2}j_l^2(x_n^l) \frac{(x_n^l)^2-l(l+1)}{(x_n^l)^2} \; for \;  qa = x_n^l

    This is valid for qR<20 with accuracy of ~0.001 as given in [1]_.
    If we look at a comparison with free diffusion the valid range seems to be smaller.

    A comparison of diffusion in different restricted geometry is show in example
    :ref:`A comparison of different dynamic models in frequency domain`.


    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     w=np.r_[-100:100]
     ql=np.r_[1:14.1:1.3]
     p=js.grace()
     iqw=js.dL([js.dynamic.diffusionInSphere_w(w=w,q=q,D=0.14,R=0.2) for q in ql])
     p.plot(iqw)
     p.yaxis(scale='l')



    References
    ----------
    .. [1] Neutron incoherent scattering law for diffusion in a potential of spherical symmetry:
           general formalism and application to diffusion inside a sphere.
           Volino, F. & Dianoux, A. J.,  Mol. Phys. 41, 271–279 (1980).
           https://doi.org/10.1080/00268978000102761

    """
    nmax = 99
    qR = q * R
    x = VolinoCoefficient[1:nmax, 0]  # x_n_l
    x2 = x ** 2
    l = VolinoCoefficient[1:nmax, 1].astype(int)
    # n = VolinoCoefficient[1:50, 2].astype(int)
    w = np.array(w, float)

    Ln = lambda w, g: g / (g * g + w * w)
    A0 = lambda qa: (3 * spjn(1, qa) / qa) ** 2

    def Anl(qa):
        # equ 31 a+b in [1]_
        res = np.zeros_like(x)
        s = (x == qa)
        if np.any(s):
            res[s] = 1.5 * spjn(l[s], x[s]) ** 2 * (x2[s] - l[s] * (l[s] + 1)) / x2[s]
        if np.any(~s):
            s = ~s  # not s
            res[s] = 6 * x2[s] / (x2[s] - l[s] * (l[s] + 1)) * (
                    (qa * spjn(l[s] + 1, qa) - l[s] * spjn(l[s], qa)) / (qa ** 2 - x2[s])) ** 2
        return res

    Iqw = 1 / pi * (((2 * l + 1) * Anl(qR))[:, None] * Ln(w, x2[:, None] * D / R ** 2)).sum(axis=0)  # equ 33
    Iqw[np.abs(w) < 1e-8] += A0(q)

    result = dA(np.c_[w, Iqw].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.radius = R
    result.wavevector = q
    result.diffusion = D
    return result


def rotDiffusion_w(w, q, cloud, Dr, lmax='auto'):
    r"""
    Rotational diffusion of an object (dummy atoms); dynamic structure factor in w domain.

    A cloud of dummy atoms can be used for coarse graining of a non-spherical object e.g. for amino acids in proteins.
    On the other hand its just a way to integrate over an object e.g. a sphere or ellipsoid.
    We use [2]_ for an objekt of arbitrary shape modified for incoherent scattering.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q : float
        Wavevector in units 1/nm
    cloud : array Nx3, Nx4 or Nx5 or float
        - A cloud of N dummy atoms with positions cloud[:3] that describe an object.
        - If given, cloud[3] is the incoherent scattering length :math:`b_{inc}` otherwise its equal 1.
        - If given, cloud[4] is the coherent scattering length otherwise its equal 1.
        - If cloud is single float the value is used as radius of a sphere with 10x10x10 grid.
    Dr : float
        Rotational diffusion constant in units 1/ns.
    lmax : int
        Maximum order of spherical bessel function.
        'auto' -> lmax > 2pi*r.max()*q/6.

    Returns
    -------
        dataArray
            Columns [w; Iqwinc; Iqwcoh]
            Input parameters as attributes.

    Notes
    -----
    See :py:func:`~.dynamic.transRotDiffusion` for more details.
    The Fourier transform of the *exp* function is a Lorentzian so the *exp* should be exchange.


    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     R=2;NN=10
     Drot=js.formel.Drot(R)
     ql=np.r_[0.5:15.:2]
     w=np.r_[-100:100:0.1]
     grid=js.ff.superball(ql,R,p=1,nGrid=NN,returngrid=True)
     p=js.grace()
     iqwR1=js.dL([js.dynamic.rotDiffusion_w(w,q,grid.XYZ,Drot) for q in ql])
     p.plot(iqwR1,le=f'NN={NN:.0f} q=$wavevector nm\S-1')
     p.yaxis(scale='l')
     p.legend()

    References
    ----------
    .. [1] Incoherent scattering law for neutron quasi-elastic scattering in liquid crystals.
           Dianoux, A., Volino, F. & Hervet, H. Mol. Phys. 30, 37–41 (1975).
    .. [2] Effect of rotational diffusion on quasielastic light scattering from fractal colloid aggregates.
           Lindsay, H., Klein, R., Weitz, D., Lin, M. & Meakin, P. Phys. Rev. A 38, 2614–2626 (1988).

    """
    Ylm = special.sph_harm
    #: Lorentzian
    Ln = lambda w, g: g / (g * g + w * w) / pi
    if isinstance(cloud, numbers.Number):
        R = cloud
        NN = 10
        grid = np.mgrid[-R:R:1j * NN, -R:R:1j * NN, -R:R:1j * NN].reshape(3, -1).T
        inside = lambda xyz, R: la.norm(grid, axis=1) < R
        cloud = grid[inside(grid, R)]
    if cloud.shape[1] == 5:
        # last columns are incoherent and coherent scattering length
        blinc = cloud[:, 3]
        blcoh = cloud[:, 4]
        cloud = cloud[:, :3]
    elif cloud.shape[1] == 4:
        # last column is scattering length
        blinc = cloud[:, 3]
        blcoh = np.ones(cloud.shape[0])
        cloud = cloud[:, :3]
    else:
        blinc = np.ones(cloud.shape[0])
        blcoh = blinc
    w = np.array(w, float)
    bi2 = blinc ** 2
    r, p, t = formel.xyz2rphitheta(cloud).T
    pp = p[:, None]
    tt = t[:, None]
    qr = q * r
    if not isinstance(lmax, numbers.Integral):
        # lmax = pi * r.max() * q  / 6. # a la CRYSON (SANS/SAXS)
        # we need a factor of 2 more compared to CRYSON for Q>10 nm**-1
        lmax = min(max(2 * int(pi * qr.max() / 6. * 2), 7), 100)
    # We calc here the field autocorrelation function as in equ 24
    # Fourier transform of the exp result in lorentz function
    # incoherent with i=j ->  Sum_m(Ylm) leads to (2l+1)/4pi
    bjlylminc = [(bi2 * spjn(l, qr) ** 2 * (2 * l + 1)).sum() for l in np.r_[:lmax + 1]]
    # add Lorentzian
    Iqwinc = np.c_[[bjlylminc[l].real * Ln(w, l * (l + 1) * Dr) for l in np.r_[:lmax + 1]]].sum(axis=0)
    Iq_inc = np.sum(bjlylminc).real

    # coh is sum over i then squared and sum over m    see Lindsay equ 19
    bjlylmcoh = [4 * np.pi * np.sum(np.abs((blcoh * spjn(l, qr) * Ylm(np.r_[-l:l + 1], l, pp, tt).T).sum(axis=1)) ** 2)
                 for l in np.r_[:lmax + 1]]
    Iqwcoh = np.c_[[bjlylmcoh[l].real * Ln(w, l * (l + 1) * Dr) for l in np.r_[:lmax + 1]]].sum(axis=0)
    Iq_coh = np.sum(bjlylmcoh).real

    result = dA(np.c_[w, Iqwinc, Iqwcoh].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 'w; Iqwinc; Iqwcoh'
    result.radiusOfGyration = np.sum(r ** 2) ** 0.5
    result.Iq_coh = Iq_coh
    result.Iq_inc = Iq_inc
    result.wavevector = q
    result.rotDiffusion = Dr
    result.lmax = lmax
    return result


def nSiteJumpDiffusion_w(w, q, N, t0, r0):
    r"""
    Random walk among N equidistant sites (isotropic averaged); dynamic structure factor in w domain.

    E.g. for CH3 group rotational jump diffusion over 3 sites.

    Parameters
    ----------
    w : array
        Frequencies in 1/ns
    q: float
        Wavevector in units 1/nm
    N : int
        Number of jump sites, jump angle 2pi/N
    r0 : float
        Distance of sites from center of rotation.
        For CH3 eg 0.12 nm.
    t0 : float
        Rotational correlation time.

    Returns
    -------
        dataArray

    Notes
    -----
    Equ. 24 [1]_ :

    .. math:: S_{inc}^{rot}(Q,\omega) = B_0(Qa)\delta(\omega) + \frac{1}{\pi} \sum_{n=1}^{N-1} B_n(Qa)
                                        \frac{\tau_n}{1+(\omega\tau_n)^2}

    with :math:`\tau_1=\frac{\tau}{1-cos(2\pi/N)}` , :math:`\tau_n=\tau_1\frac{sin^2(\pi/N)}{sin^2(n\pi/N)}`

    .. math:: B_n(Qa) = \frac{1}{N} \sum_{p=1}^{N} j_0 \Big( 2Qa sin(\frac{\pi p}{N}) \Big) cos(n\frac{2\pi p}{N})

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     w=np.r_[-100:100:0.1]
     ql=np.r_[1:14.1:1.3]
     p=js.grace()
     iqw=js.dL([js.dynamic.nSiteJumpDiffusion_w(w=w,q=q,N=3,t0=0.01,r0=0.12) for q in ql])
     p.plot(iqw)
     p.yaxis(scale='l')

    References
    ----------
    .. [1] Incoherent scattering law for neutron quasi-elastic scattering in liquid crystals.
           Dianoux, A., Volino, F. & Hervet, H., Mol. Phys. 30, 37–41 (1975).
           https://doi.org/10.1080/00268977500102721

    """
    w = np.array(w, float)
    #: Lorentzian
    Ln = lambda w, tn: tn / (1 + (w * tn) ** 2) / pi

    def Bn(qa, n):
        return np.sum([spjn(0, 2 * qa * np.sin(pi * p / N)) * np.cos(n * 2 * pi * p / N) for p in np.r_[:N] + 1]) / N

    B0 = np.sum([spjn(0, 2 * q * r0 * np.sin(pi * p / N)) for p in np.r_[:N] + 1]) / N
    t1 = t0 / (1 - np.cos(2 * pi / N))
    tn = lambda n: t1 * np.sin(pi / N) ** 2 / np.sin(n * pi / N) ** 2

    Iqw = np.c_[[Bn(q * r0, n) * Ln(w, tn(n)) for n in np.r_[1:N]]].sum(axis=0)
    Iqw[np.abs(w) < 1e-8] += B0
    result = dA(np.c_[w, Iqw].T)
    result.modelname = inspect.currentframe().f_code.co_name
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    result.r0 = r0
    result.wavevector = q
    result.t0 = t0
    result.N = N
    return result


# noinspection PyIncorrectDocstring
def resolution_w(w, s0=1, m0=0, s1=None, m1=None, s2=None, m2=None, s3=None, m3=None,
                 s4=None, m4=None, s5=None, m5=None,s6=None, m6=None, s7=None, m7=None,
                 a0=1, a1=1, a2=1, a3=1, a4=1, a5=1, a6=1, a7=1, bgr=0, resolution=None):
    r"""
    Resolution as multiple Gaussians for inelastic measurement as backscattering or time of
    flight instrument in w domain.

    Multiple Gaussians define the function to describe a resolution measurement.
    Use only a common mi to account for a shift.
    See resolution for transform to time domain.

    Parameters
    ----------
    w : array
        Frequencies
    s0,s1,... : float
        Sigmas of several Gaussian functions representing a resolution measurement.
        The number of si not none determines the number of Gaussians.
    m0, m1,.... : float, None
        Means of the Gaussian functions representing a resolution measurement.
    a0, a1,.... : float, None
        Amplitudes of the Gaussian functions representing a resolution measurement.
    bgr : float, default=0
        Background
    resolution : dataArray
        Resolution with attributes sigmas, amps which are used instead of si, ai.
         - If from t domain this represents the Fourier transform from w to t domain.
           The means are NOT used from as these result only in a phase shift, instead m0..m5 are used.
         - If from w domain the resolution is recalculated.

    Returns
    -------
        dataArray
            .means
            .amps
            .sigmas

    Notes
    -----
    In a typical inelastic experiment the resolution is measured by e.g. a vanadium measurement (elastic scatterer).
    This is described in w domain by a multi Gaussian function as in resw=resolution_w(w,...) with
    amplitudes ai_w, width si_w and common mean m_w.
    resolution(t,resolution_w=resw) defines the Fourier transform of resolution_w using the same coefficients.
    mi_t are set by default to 0 as mi_w lead only to a phase shift. It is easiest to shift w values in w domain as it
    corresponds to a shift of the elastic line.

    The used Gaussians are normalized that they are a pair of Fourier transforms:

    .. math:: R_t(t,m_i,s_i,a_i)=\sum_i a_i s_i e^{-\frac{1}{2}s_i^2 t^2} \Leftrightarrow
              R_w(w,m_i,s_i,a_i)=\sum_i a_i e^{-\frac{1}{2}(\frac{w-m_i}{s_i})^2}

    under the Fourier transform  defined as

    .. math:: F(f(t)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt

    .. math:: F(f(w)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(\omega) e^{i\omega t} d\omega


    Examples
    --------
    Transform from and to time domain
    ::

     import jscatter as js
     import numpy as np
     # resw is a resolution in w domain maybe as a result from a fit to vanadium data
     # resw contains all parameters
     w=np.r_[-100:100:0.5]
     resw=js.dynamic.resolution_w(w, s0=12, m0=0, a0=2)

     w2=np.r_[0:50:0.2]
     rest2=js.dynamic.resolution_w(w2,resolution=resw)

     # representing the Fourier transform of to time domain
     t=np.r_[0:1:0.01]
     rest=js.dynamic.resolution(t,resolution=resw)

    Sequential fit in w domain to a measurement with realistic data.
    The data file is from the SPHERE instrument at MLZ Garching (usually not gziped).
    The file needs to be split to be easily read.
    ::

     import jscatter as js
     import numpy as np
     import gzip

     with gzip.open(js.examples.datapath +'/Vana.inx.gz','rt') as f:
        lines = f.readlines()
     vana = js.dL()
     for j in np.r_[0:int(len(lines)//(563))]:
         vana.append(js.dA(lines[j*563:(j+1)*563],lines2parameter=[0,2,3],usecols=[1,2,3]))
         vana[-1].q=float(vana[-1].line_2[0])  # extract q values

     start={'s0':0.5,'m0':0,'a0':1,'s1':1,'m1':0,'a1':1,'s2':10,'m2':0,'a2':1,'bgr':0.0073}
     dm=5
     for van in vana[:1]:
         van.setlimit(m0=[-dm,dm],m1=[-dm,dm],m2=[-dm,dm],m3=[-dm,dm],m4=[-dm,dm],m5=[-dm,dm])
         van.fit(js.dynamic.resolution_w,start,{},{'w':'X'})
         van.showlastErrPlot(yscale='l', fitlinecolor=11)

     # vana[7].savelastErrPlot(js.examples.imagepath+'/resolutionfit.jpg')

    .. image:: ../../examples/images/resolutionfit.jpg
     :align: center
     :width: 50 %
     :alt: worm

    """
    def gauss(x, mean, sigma):
        return np.exp(-0.5 * ((x - mean) / sigma) ** 2)

    if resolution is None:
        means = [m0, m1, m2, m3, m4, m5, m6, m7]
        sigmas = [s0, s1, s2, s3, s4, s5, s6, s7]
        amps = [a0, a1, a2, a3, a4, a5, a6, a7]
    else:
        if resolution.modelname[-1] == 'w':
            # resolution from w domain
            means = resolution.means
            sigmas = resolution.sigmas
            amps = resolution.amps
        else:
            means = [m0, m1, m2, m3, m4, m5, m6, m7]
            sigmas = [1. / s if s is not None else s for s in resolution.sigmas]
            amps = resolution.amps
    w = np.atleast_1d(w)
    if isinstance(resolution, str):  # elastic
        Y = np.zeros_like(w)
        Y[np.abs(w - m0) < 1e-8] = 1.
        integral = 1
    else:
        Y = np.r_[
            [a * gauss(w, m, s) for s, m, a in zip(sigmas, means, amps) if (s is not None) & (m is not None)]].sum(
            axis=0)
        integral = np.trapz(Y, w)
    result = dA(np.c_[w, Y + bgr].T)
    result.setColumnIndex(iey=None)
    result.modelname = inspect.currentframe().f_code.co_name
    result.columnname = 'w;Rw'
    result.means = means
    result.sigmas = sigmas
    result.amps = amps
    result.integral = integral
    return result


def time2frequencyFF(timemodel, resolution, w=None, tfactor=7, **kwargs):
    r"""
    Fast Fourier transform from time domain to frequency domain for inelastic neutron scattering.

    Shortcut t2fFF calls this function.

    Parameters
    ----------
    timemodel : function, None
        Model for I(t,q) in time domain. t in units of ns.
        The values for t are determined from w as :math:`t=[0..n_{max}]\Delta t` with :math:`\Delta t=1/max(|w|)`
        and :math:`n_{max}=w_{max}/\sigma_{min} tfactor`.
        :math:`\sigma_{min}` is the minimal width of the Gaussians given in resolution.
        If None a constant function (elastic scattering) is used.
    resolution : dataArray, float, string
        dataArray that describes the resolution function as multiple Gaussians (use resolution_w).
        A nonzero bgr in resolution is ignored and needs to be added afterwards.
         - float : value is used as width of a single Gaussian in units 1/ns (w is needed below).
                   Resolution width is in the range of 6 1/ns (IN5 TOF) to 1 1/ns (Spheres BS).
         - string : no resolution ('elastic')
    w : array
        Frequencies for the result, e.g. from experimental data.
        If w is None the frequencies resolution.X are used.
        This allows to use the fit of a resolution to be used with same w values.
    kwargs : keyword args
        Additional keyword arguments that are passed to timemodel.
    tfactor : float, default 7
        Factor to determine max time for timemodel to minimize spectral leakage.
        tmax=1/(min(resolution_width)*tfactor) determines the resolution to decay as :math:`e^{-tfactor^2/2}`.
        The time step is dt=1/max(|w|). A minimum of len(w) steps is used (which might increase tmax).
        Increase tfactor if artifacts (wobbling) from the limited time window are visible as the limited time interval
        acts like a window function (box) for the Fourier transform.

    Returns
    -------
    dataArray :     A symmetric spectrum of the Fourier transform is returned.

      .Sq     :math:`\rightarrow S(q)=\int_{-\omega_{min}}^{\omega_{max}} S(Q,\omega)d\omega
      \approx \int_{-\infty}^{\infty} S(Q,\omega)d\omega = I(q,t=0)`

              Integration is done by a cubic spline in w domain on the 'raw' fourier transform of timemodel.

      .Iqt    *timemodel(t,kwargs)* dataArray as returned from timemodel.
              Implicitly this is the Fourier transform to time domain after a successful fit in w domain.
              Using a heuristic model in time domain as multiple Gaussians or stretched exponential allows a convenient
              transform to time domain of experimental data.


    Notes
    -----
    We use Fourier transform with real signals. The transform is defined as

    .. math:: F(f(t)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt

    .. math:: F(f(w)) =  \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} f(\omega) e^{i\omega t} d\omega

    The resolution function is defined as (see resolution_w)

    .. math:: R_w(w,m_i,s_i,a_i)&= \sum_i a_i e^{-\frac{1}{2}(\frac{w-m_i}{s_i})^2} = F(R_t(t)) \\

                &=\frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty}
                  \sum_i{a_i s_i e^{-\frac{1}{2}s_i^2t^2}} e^{-i\omega t} dt

    using the resolution in time domain with same coefficients
    :math:`R_t(t,m_i,s_i,a_i)=\sum_i a_i s_i e^{-\frac{1}{2}s_i^2 t^2}`

    The Fourier transform of a timemodel I(q,t) is

    .. math:: I(q,w) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} I(q,t) e^{-i\omega t} dt

    The integral is calculated by Fast Fourier transform as

    .. math:: I(q,m\Delta w) = \frac{1}{\sqrt{2\pi}} \Delta t \sum_{n=-N}^{N} I(q,n\Delta t) e^{-i mn/N}

    :math:`t_{max}=tfactor/min(s_i)`.
    Due to the cutoff at :math:`t_{max}` a wobbling might appear indicating spectral leakage.
    Spectral leakage results from the cutoff, which can be described as multiplication with a box function.
    The corresponding Fourier Transform of the box is a *sinc* function visible in the frequency spectrum as wobbling.
    If the resolution is included in time domain, it acts like a window function to reduce
    spectral leakage with vanishing values at :math:`t_{max}=N\Delta t`.
    The second possibility (default) is to increase :math:`t_{max}` (increase tfactor)
    to make the *sinc* sharp and with low wobbling amplitude.

    **Mixed domain models**

    Associativity and Convolution theorem allow to mix models from frequency domain and time domain.
    After transformation to frequency domain the w domain models have to be convoluted with the FFT transformed model.

    Examples
    --------
    Other usage example with a comparison of w domain and transformed from time domain can be found in
    :ref:`A comparison of different dynamic models in frequency domain` or in the example of
    :py:func:`diffusionHarmonicPotential_w`.

    Compare transDiffusion transform from time domain with direct convolution in w domain.
    ::

     import jscatter as js
     import numpy as np
     w=np.r_[-100:100:0.5]
     start={'s0':6,'m0':0,'a0':1,'s1':None,'m1':0,'a1':1,'bgr':0.00}
     resolution=js.dynamic.resolution_w(w,**start)
     p=js.grace()
     D=0.035;qq=3  # diffusion coefficient of protein alcohol dehydrogenase (140 kDa) is 0.035 nm**2/ns
     p.title('Inelastic spectrum IN5 like')
     p.subtitle(r'resolution width about 6 ns\S-1\N, Q=%.2g nm\S-1\N' %(qq))
     # compare diffusion with convolution and transform from time domain
     diff_ffw=js.dynamic.time2frequencyFF(js.dynamic.simpleDiffusion,resolution,q=qq,D=D)
     diff_w=js.dynamic.transDiff_w(w, q=qq, D=D)
     p.plot(diff_w,sy=0,li=[1,3,3],le=r'original diffusion D=%.3g nm\S2\N/ns' %(D))
     p.plot(diff_ffw,sy=[2,0.3,2],le='transform from time domain')
     p.plot(diff_ffw.X,diff_ffw.Y+diff_ffw.Y.max()*1e-3,sy=[2,0.3,7],le=r'transform from time domain with 10\S-3\N bgr')
     # resolution has to be normalized in convolve
     diff_cw=js.dynamic.convolve(diff_w,resolution,normB=1)
     p.plot(diff_cw,sy=0,li=[1,3,4],le='after convolution in w domain')
     p.plot(resolution.X,resolution.Y/resolution.integral,sy=0,li=[1,1,1],le='resolution')
     p.yaxis(min=1e-6,max=5,scale='l',label='S(Q,w)')
     p.xaxis(min=-100,max=100,label='w / ns\S-1')
     p.legend()
     p.text(string=r'convolution edge ==>\nmake broader and cut',x=10,y=8e-6)

    Compare the resolutions direct and from transform from time domain.
    ::

     p=js.grace()
     fwres=js.dynamic.time2frequencyFF(None,resolution)
     p.plot(fwres,le='fft only resolution')
     p.plot(resolution,sy=0,li=2,le='original resolution')

    Compare diffusionHarmonicPotential to show simple usage
    ::

     import jscatter as js
     import numpy as np
     t2f=js.dynamic.time2frequencyFF
     dHP=js.dynamic.diffusionHarmonicPotential
     w=np.r_[-100:100]
     ql=np.r_[1:14.1:6j]
     iqw=js.dL([js.dynamic.diffusionHarmonicPotential_w(w=w,q=q,tau=0.14,rmsd=0.34,ndim=3) for q in ql])
     # To move spectral leakage out of our window we increase w and interpolate.
     # The needed factor (here 23) depends on the quality of your data and background contribution.
     iqt=js.dL([t2f(dHP,'elastic',w=w*13,q=q, rmsd=0.34, tau=0.14 ,ndim=3,tfactor=14).interpolate(w) for q in ql])

     p=js.grace()
     p.multi(2,3)
     p[1].title('Comparison direct and FFT  for ndim= 3')
     for i,(iw,it) in enumerate(zip(iqw,iqt)):
         p[i].plot(iw,li=1,sy=0,le='q=$wavevector nm\S-1')
         p[i].plot(it,li=2,sy=0)
         p[i].yaxis(min=1e-5,max=2,scale='log')
         if i in [1,2,4,5]:p[i].yaxis(ticklabel=0)
         p[i].legend(x=5,y=1, charsize=0.7)

    """

    if w is None:  w = resolution.X
    if timemodel is None:
        timemodel = lambda t, **kwargs: dA(np.c_[t, np.ones_like(t)].T)
    gauss = lambda t, si: si * np.exp(-0.5 * (si * t) ** 2)

    if isinstance(resolution, numbers.Number):
        si = np.r_[resolution]
        ai = np.r_[1]
        # mi = np.r_[0]
    elif isinstance(resolution, str):
        si = np.r_[0.5]  # just a dummy
        ai = np.r_[1]
        # mi = np.r_[0]
    else:
        # filter for given values (remove None) and drop bgr in resolution
        sma = np.r_[[[si, mi, ai] for si, mi, ai in zip(resolution.sigmas, resolution.means, resolution.amps)
                     if (si is not None) & (mi is not None)]]
        si = sma[:, 0, None]
        # mi = sma[:, 1, None]  # ignored
        ai = sma[:, 2, None]

    # determine the times and differences dt
    dt = 1. / np.max(np.abs(w))
    nn = int(np.max(w) / si.min() * tfactor)
    nn = max(nn, len(w))
    tt = np.r_[0:nn] * dt

    # calc values
    if isinstance(resolution, str):
        timeresol = np.ones_like(tt)
    else:
        timeresol = ai * gauss(tt, si)  # resolution normalized to timeresol(w=0)=1
        if timeresol.ndim > 1:
            timeresol = np.sum(timeresol, axis=0)
        timeresol = timeresol / (timeresol[0])  # That  S(Q)= integral[-w_min,w_max] S(Q,w)= = I(Q, t=0)
    kwargs.update(t=tt)
    tm = timemodel(**kwargs)
    RY = timeresol * tm.Y  # resolution * timemodel
    # make it symmetric zero only once
    RY = np.r_[RY[:0:-1], RY]
    # do rfft from -N to N
    # using spectrum from -N,N the shift theorem says we get a
    # exp[-j*2*pi*f*N/2] phase leading to alternating sign => use the absolute value
    wn = 2 * pi * np.fft.rfftfreq(2 * nn - 1, dt)  # frequencies
    wY = dt * np.abs(np.fft.rfft(RY).real) / (2 * pi)  # fft

    # now try to average or interpolate for needed w values
    wn = np.r_[-wn[:0:-1], wn]
    wY = np.r_[wY[:0:-1], wY]
    integral = scipy.integrate.simps(wY, wn)

    result = dA(np.c_[wn, wY].T)
    result.setattr(tm)
    try:
        result.modelname += '_t2w'
    except AttributeError:
        result.modelname = '_t2w'
    result.Sq = integral
    result.Iqt = tm
    result.timeresol = timeresol
    result.setColumnIndex(iey=None)
    result.columnname = 'w;Iqw'
    return result


t2fFF = time2frequencyFF


def shiftAndBinning(data, w=None, dw=None, w0=0):
    """
    Shift spectrum and average (binning) in intervals.

    The intention is to shift spectra and average over intervals.
    It should be used after convolution with the instrument resolution, when singular values
    at zero are smeared by resolution.

    Parameters
    ----------
    data : dataArray
        Data (from model) to be shifted and averaged in intervals to meet experimental data.
    w : array
        New X values (e.g. from experiment). If w is None data.X values are used.
    w0 : float
        Shift by w0 that wnew=wold+w0
    dw : float, default

        Average over intervals between [w[i]-dw,w[i]+dw] to average over a detector pixel width.
        If None dw is half the interval to neighbouring points.
        If 0 the value is only linear interpolated to w values and not averaged (about 10 times faster).

    Notes
    -----
    For averaging over intervals scipy.interpolate.CubicSpline is used with integration in the intervals.

    Returns
    -------
    dataArray

    Examples
    --------
    ::

     import jscatter as js
     import numpy as np
     w=np.r_[-100:100:0.5]
     start={'s0':6,'m0':0,'a0':1,'s1':None,'m1':0,'a1':1,'bgr':0.00}
     resolution=js.dynamic.resolution_w(w,**start)
     p=js.grace()
     p.plot(resolution)
     p.plot(js.dynamic.shiftAndBinning(resolution,w0=5,dw=0))

    """
    if w is None:  w = data.X.copy()
    data.X += w0
    if dw == 0:
        iwY = data.interp(w)
    else:
        if dw is None:
            dw = np.diff(w)
        else:
            dw = np.zeros(len(w) - 1) * dw
        csp = scipy.interpolate.CubicSpline(data.X, data.Y)
        iwY = [csp.integrate(wi - dwl, wi + dwr) / (dwl + dwr) for wi, dwl, dwr in zip(w, np.r_[0, dw], np.r_[dw, 0])]
    result = dA(np.c_[w, iwY].T)
    result.setattr(data)
    result.setColumnIndex(data)

    return result


def dynamicSusceptibility(data, Temp):
    r"""
    Transform from S(w,q) to the  imaginary  part  of  the  dynamic susceptibility.

    .. math::

        \chi (w,q) &= \frac{S(w,q)}{n(w)} (gain side)

                   &= \frac{S(w,q)}{n(w)+1} (loss side)

    with Bose distribution for integer spin particles

    .. math:: with \ n(w)=\frac{1}{e^{hw/kT}-1}

    Parameters
    ----------
    data : dataArray
        Data to transform with w units in 1/ns
    Temp : float
        Measurement temperature in K.

    Returns
    -------
        dataArray

    Notes
    -----
    "Whereas relaxation processes on different time scales are usually hard to identify
    in S(w,q), they appear as distinct peaks in dynamic susceptibility with associated
    relaxation times :math:´1/2\piw´ [1]_."


    References
    ----------
    .. [1] H. Roh et al. ,Biophys. J. 91, 2573 (2006)

    Examples
    --------
    ::

     start={'s0':5,'m0':0,'a0':1,'bgr':0.00}
     w=np.r_[-100:100:0.5]
     resolution=js.dynamic.resolution_w(w,**start)
     # model
     def diffindiffSphere(w,q,R,Dp,Ds,w0,bgr):
         diff_w=js.dynamic.transDiff_w(w,q,Ds)
         rot_w=js.dynamic.diffusionInSphere_w(w=w,q=q,D=Dp,R=R)
         Sx=js.formel.convolve(rot_w,diff_w)
         Sxsb=js.dynamic.shiftAndBinning(Sx,w=w,w0=w0)
         Sxsb.Y+=bgr       # add background
         return Sxsb
     #
     q=5.5;R=0.5;Dp=1;Ds=0.035;w0=1;bgr=1e-4
     Iqw=diffindiffSphere(w,q,R,Dp,Ds,w0,bgr)
     IqwR=js.dynamic.diffusionInSphere_w(w,q,Dp,R)
     IqwT=js.dynamic.transDiff_w(w,q,Ds)
     Xqw=js.dynamic.dynamicSusceptibility(Iqw,293)
     XqwR=js.dynamic.dynamicSusceptibility(IqwR,293)
     XqwT=js.dynamic.dynamicSusceptibility(IqwT,293)
     p=js.grace()
     p.plot(Xqw)
     p.plot(XqwR)
     p.plot(XqwT)
     p.yaxis(scale='l',label='X(w,q) / a.u.')
     p.xaxis(scale='l',label='w / ns\S-1')


    """
    ds = data.copy()

    ds.Y[ds.X > 0] = ds.Y[ds.X > 0] / formel.boseDistribution(ds.X[ds.X > 0], Temp).Y
    ds.Y[ds.X < 0] = ds.Y[ds.X < 0] / (formel.boseDistribution(-ds.X[ds.X < 0], Temp).Y + 1)
    ds.Y[ds.X == 0] = 0
    ds.modelname = data.modelname + '_Susceptibility'
    return ds
