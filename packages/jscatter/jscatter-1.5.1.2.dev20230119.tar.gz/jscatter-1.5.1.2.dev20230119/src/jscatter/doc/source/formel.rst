formel
======

.. automodule:: jscatter.formel
    :noindex:

Functions
---------
.. autosummary::
   loglist
   gauss
   lorentz
   voigt
   lognorm
   box
   Ea
   boseDistribution
   schulzDistribution

Quadrature
----------
Routines for efficient integration of parameter dependent vector functions.

.. autosummary::
   parQuadratureSimpson
   parQuadratureFixedGauss
   parQuadratureFixedGaussxD
   parQuadratureAdaptiveGauss
   parQuadratureAdaptiveClenshawCurtis
   parAdaptiveCubature
   ~jscatter.parallel.sphereAverage
   convolve

Distribution of parameters
--------------------------
Experimental data might be influenced by multimodal parameters (like multiple sizes)
or by one or several parameters distributed around a mean value.

.. autosummary::
    parDistributedAverage
    multiParDistributedAverage
    scatteringFromSizeDistribution

Utilities
---------
Helpers for integration, parallelisation and function evaluation in 3D space

.. autosummary::
   ~jscatter.parallel.doForList
   memoize
   xyz2rphitheta
   rphitheta2xyz
   rotationMatrix
   ~jscatter.parallel.fibonacciLatticePointsOnSphere
   ~jscatter.parallel.randomPointsOnSphere
   ~jscatter.parallel.randomPointsInCube
   ~jscatter.parallel.haltonSequence
   qEwaldSphere
   smooth
   imageHash

Centrifugation
--------------
.. autosummary::
   sedimentationCoefficient
   sedimentationProfile
   sedimentationProfileFaxen                                                                                                                                     

NMR
---
.. autosummary::
   DrotfromT12
   T1overT2
   
Material Data
-------------
.. autosummary::   
   scatteringLengthDensityCalc
   waterdensity
   bufferviscosity
   dielectricConstant
   watercompressibility
   cstar
   molarity
   viscosity
   Dtrans
   Drot
   bicelleRh


Constants and Tables
--------------------
.. autosummary::
    eijk
    ~jscatter.data.felectron
    ~jscatter.data.radiusBohr
    ~jscatter.data.Elements
    ~jscatter.data.vdwradii
    ~jscatter.data.xrayFFatomic
    ~jscatter.data.Nscatlength
    ~jscatter.data.aaHydrophobicity

-----

.. automodule:: jscatter.formel
    :members:
    :exclude-members: pQFG, pQFGxD, pQAG, pAC, pQACC, pQS, sQS, pDA, mPDA, D0

.. autoclass:: jscatter.formel.imageHash
    :members:

.. automodule:: jscatter.data
    :members:
    :exclude-members: xrayFFatomic, Nscatlength, vdwradii, Elements

.. autodata:: jscatter.data.xrayFFatomic
    :no-value:

.. autodata:: jscatter.data.Elements
    :no-value:

.. autodata:: jscatter.data.Nscatlength
    :no-value:

.. autodata:: jscatter.data.vdwradii
    :no-value:

.. autodata:: jscatter.data.aaHydrophobicity
    :no-value:

.. automodule:: jscatter.parallel
    :members:

   
   