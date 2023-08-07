.. _label_Examples:

Examples
========

These examples show how to use Jscatter. Use  *showExampleList* to get a full list
or look in :py:func:`~.examples.showExampleList`.
A general introduction is in :ref:`Beginners Guide / Help`

Most functions descriptions contain an *Example* sections with more specific examples.

.. contents::
    :local:
    :depth: 2

Examples are mainly based on XmGrace for plotting as this is more convenient for
interactive inspection of data and used for most of the shown plots.

Matplotlib can be used by setting ``usempl=True`` in ``runExample`` and ``showExample``
(automatically set if Grace is not present).
With matplotlib the plots are not optimized but still show the possibilities.


.. autosummary::
    ~jscatter.examples.showExampleList
    ~jscatter.examples.showExample
    ~jscatter.examples.runExample
    ~jscatter.examples.runAll

.. |binder| image:: https://img.shields.io/badge/launch-jscatter-F5A252.svg?logo=data:image/png;base64,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
            :alt: link to mybinder
            :target: https://mybinder.org/v2/gl/biehl%2Fjscatter/master?filepath=src%2Fjscatter%2Fexamples%2Fnotebooks

Try Jscatter Demo in a Jupyter Notebook at |binder| .


In a nutshell
-------------
Daily use example to show how short it can be.

Comments are shown in next examples.

.. literalinclude:: ../../examples/example_daily_use.py
    :language: python
.. image:: ../../examples/DiffusionFit_ErrPlot.jpg
    :align: left
    :height: 300px
    :alt: Picture about diffusion fit with residuals
.. image:: ../../examples/DiffusionFit.jpg
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit
.. image:: ../../examples/effectiveDiffusion.jpg 
    :align: center
    :height: 300px
    :alt: diffusion fit result

Build models 
------------

How to build simple models
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_buildsimpleModels.py
    :language: python

How to build a more complex model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_buildComplexModel.py
    :language: python
.. image:: ../../examples/interactingParticles.jpeg
    :align: center
    :height: 300px
    :alt: Image of interacting particles scattering

Fitting
-------

1D fits with attributes
^^^^^^^^^^^^^^^^^^^^^^^
Some Sinusoidal fits with different kinds to use data attributes

.. literalinclude:: ../../examples/example_SinusoidalFitting.py
    :language: python
    :lines: 1-28
.. image:: ../../examples/SinusoidalFit0.png
    :align: center
    :height: 300px
    :alt: SinusoidialFit

A **2D** fit using an attribute *B* stored in the data as second dimension.
This might be extended to several attributes allowing **multidimensional fitting**.

.. literalinclude:: ../../examples/example_SinusoidalFitting.py
    :language: python
    :lines: 29-

.. image:: ../../examples/SinusoidalFit.png
    :align: center
    :height: 300px
    :alt: SinusoidialFit

2D fitting
^^^^^^^^^^
Unlike the previous we use here data with two dimensions in X,Z coordinates.
Additional one could use again attributes.

Another example is shown in `Fitting the 2D scattering of a lattice`_.

.. literalinclude:: ../../examples/example_2DFitting.py
    :language: python

.. image:: ../../examples/Sinusoidal2D.png
    :align: center
    :height: 300px
    :alt: Sinusoidial3D


Simple diffusion fit of not so simple diffusion case
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here the long part with description from the first example.

This is the diffusion of a protein in solution. This is NOT constant as for Einstein diffusion.

These simulated data are similar to data measured by Neutron Spinecho Spectroscopy, which measures on the length scale
of the protein and therefore also rotational diffusion contributes to the signal.
At low wavevectors additional the influence of the structure factor leads to an upturn,
which is neglected in the simulated data.
To include the correction :math:`D_T(q)=D_{T0} H(q)/S(q)` look at :func:`~.structurefactor.hydrodynamicFunct`.

For details see this tutorial review `Biehl et al. Softmatter 7,1299 (2011) <http://juser.fz-juelich.de/record/11985/files/FZJ-11985.pdf>`_


.. literalinclude:: ../../examples/example_simple_diffusion.py
    :language: python
    :end-before: # This is the basis of the simulated data above

.. image:: ../../examples/DiffusionFit.jpg
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit

.. literalinclude:: ../../examples/example_simple_diffusion.py
    :language: python
    :start-after: p.save('DiffusionFit.png')

.. image:: ../../examples/effectiveDiffusion.jpg 
    :align: center
    :height: 300px
    :alt: diffusion fit result


A long example for diffusion and how to analyze step by step
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This is a long example to show possibilities.

A main feature of the fit is that we can change from a constant fit parameters to a parameter
dependent one by simply changing A to [A].


.. literalinclude:: ../../examples/example_fit_diffusion.py
    :language: python
    :lines: 2-


Fitting a multiShellcylinder in various ways
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_fit_multicylinder.py
    :language: python
    :lines: 2-


Fitting the 2D scattering of a lattice
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
This example shows how to fit a 2D scattering pattern as e.g. measured by small angle scattering.

As a first step one should fit radial averaged data to limit the lattice constants to reasonable ranges
and deduce reasonable values for background and other parameters.

Because of the topology of the problem with a large plateau and small minima most
fit algorithm (using a gradient) will fail.
One has to take care that the first estimate of the starting parameters (see above) is
already close to a very good guess or one may use a method to find a global minimum as
*differential_evolution* or brute force scanning. This requires some time.

In the following we limit the model to a few parameters.
One needs basically to include more as e.g. the orientation of the crystal in 3D and more
parameters influencing the measurement.
Prior knowledge about the experiment as e.g. a prefered orientation during a shear experiment
is helpful information.

Another possibility is to normalize the data e.g. to peak maximum=1 with high q data also fixed.

As a good practice it is useful to first fit 1D data to fix some parameters and add e.g. orientation
in a second step with 2D fitting.


.. literalinclude:: ../../examples/example_2DFitting_CrystalPeaks.py
    :language: python
    :lines: 1-
.. image:: ../../examples/2Dhex_org.png
    :align: center
    :width: 300px
    :alt: Ewald2
.. image:: ../../examples/2Dhex_fit.png
    :align: center
    :width: 300px
    :alt: Ewald2

Using cloudscattering as fit model
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
At the end a complex shaped object: A cube decorated with spheres of different scattering length.


.. literalinclude:: ../../examples/example_cloudscattering.py
    :lines: 1-
.. image:: ../../examples/cubeWithSpheres.png
    :align: center
    :height: 300px
    :alt: cubeWithSpheres

Bayesian inference for fitting
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
method='bayes' uses Bayesian inference for modeling and the MCMC algorithms for sampling
(we use `emcee <https://emcee.readthedocs.io>`_).
Requires a larger amount of function evaluations but *returns errors* from Bayesian statistical analysis and
allows inclusion of prior knowledge about parameters and restrictions.

The example shows how some knowledge about parameters A and d that can be used for the prior.
We assume here that the amplitude A is distributed around 1 within a Gaussian distribution
and D around 0.09.

The evaluation might take somewhat longer for bayes (here 100s on my desktop).

.. literalinclude:: ../../examples/example_fit_bayes.py
    :lines: 1-
.. image:: ../../examples/images/bayescorner_withprior.jpg
    :align: center
    :height: 300px
    :alt: bayescorner_withprior


Analyses SAS data
-----------------


How to smooth Xray data and make an inset in the plot
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
SAS data often have a large number of points at higher Q.
The best way to get reasonable statistics there is to reduce the number of points
by averaging in intervals (see .prune). Spline gives trustless results.

These are real data from X33 beamline, EMBL Hamburg.

.. literalinclude:: ../../examples/example_smooth_xraydata.py
    :language: python

.. image:: ../../examples/smooth_xraydata.png
    :align: center
    :height: 300px
    :alt: smooth_xraydata

Analyse SAS data
^^^^^^^^^^^^^^^^
In small angle scattering a typical situation is that you want to measure a formfactor (particle shape)
or structure factor (particle interaction). For this a concentration series is measured and
we need to extrapolate to zero concentration to get the formfactor.
Afterwards we can divide the measurement by the formfactor to get the structure factor.
So we have three key parts :
    - Correction for transmission, dark and empty cell scattering to get instrument independent datasets.
    - Extrapolating concentration scaled data to get the formfactor.
    - Divide by formfactor to get structure factor

**Correction**

Brulet at al [1]_ describe the data correction for SANS, which is in principle also valid for SAXS,
if incoherent contributions are neglected.

The difference is, that SAXS has typical transmission around ~0.3 for 1mm water sample in quartz cell
due to absorption, while in SANS typical values are around ~0.9 for D2O.
Larger volume fractions in the sample play a more important rule for SANS as hydrogenated ingredients
reduce the transmission significantly, while in SAXS still the water and the cell (quartz) dominate.

One finds for a sample inside of a container with thicknesses (:math:`z`)
for sample, buffer (solvent), empty cell and empty beam measurement (omitting the overall q dependence):

.. math:: I_s = \frac{1}{z_S}\big((\frac{I_S-I_{dark}}{T_S}-I_{b}T_S\big) -\big(\frac{I_{EC}-I_{dark}}{T_{EC}}-I_{b}T_{EC})\big) -
                \frac{1}{z_B}\big((\frac{I_B-I_{dark}}{T_B}-I_{b}T_B\big) -\big(\frac{I_{EC}-I_{dark}}{T_{EC}}-I_{b}T_{EC})\big)

where
 - :math:`I_s`      is the interesting species
 - :math:`I_S`      is the sample of species in solvent (buffer)
 - :math:`I_B`      is the pure solvent (describing a constant background)
 - :math:`I_{dark}` is the dark current measurement. For Pilatus detectors equal zero.
 - :math:`I_b`      is the empty beam measurement
 - :math:`I_{EC}`   is the empty cell measurement
 - :math:`z_x`      corresponding sample thickness
 - :math:`T_x`      corresponding transmission

The recurring pattern :math:`\big((\frac{I-I_{dark}}{T}-I_{b}T\big)` shows that the the beam tail
(border of primary beam not absorbed by the beam stop) is attenuated by the corresponding sample.

For equal sample thickness :math:`z` the empty beam is included in subtraction of :math:`I_B` :

.. math:: I_s = \frac{1}{z} \big((\frac{I_S-I_{dark}}{T_S}-I_{b}T_S) - (\frac{I_B-I_{dark}}{T_B}-I_{b}T_B)\big)

- The simple case

   If the transmissions are nearly equal as for e.g. protein samples with low concentration (:math:`T_S \approx T_B`)
   we only need to subtract the transmission and dark current corrected buffer measurement from the sample.

   .. math:: I_s = \frac{1}{z} \big((\frac{I_S-I_{dark}}{T_S}) - (\frac{I_B-I_{dark}}{T_B}\big)

- Higher accuracy for large volume fractions

   For larger volume fractions :math:`\Phi` the transmission might be different and we have to take into account that
   only :math:`1-\Phi` of solvent contributes to :math:`I_S`.
   We may incorporate this in the sense of an optical density changing the effective thickness
   :math:`\frac{1}{z_B}\rightarrow\frac{1-\Phi}{z_B}` resulting in different thicknesses :math:`z_S \neq z_B`

.. [1] Improvement of data treatment in small-angle neutron scattering
       Brûlet et al Journal of Applied Crystallography 40, 165-177 (2007)

**Extrapolation and dividing**

We assume that the above correction was correctly applied and we have a transmission corrected
sample and buffer (background) measurement. This is what you typically get from SANS instruments
as e.g KWS1-3 from MLZ Garching or D11-D33 at ILL, Grenoble.

The key part is ``dataff=datas.extrapolate(molarity=0)[0]`` to extrapolate to zero molarity.

.. literalinclude:: ../../examples/example_analyseSASData.py
    :language: python
.. image:: ../../examples/SAS_sf_extraction.png
    :align: center
    :height: 300px
    :alt: SAS_sf_extraction


How to fit SANS data including the resolution for different detector distances
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
First this example shows the influence of smearing, then how to do a fit including
 smearing a la Pedersen. The next example can do the same.

.. literalinclude:: ../../examples/example_SANSsmearing.py
    :language: python

.. image:: ../../examples/SANSsmearing.jpg
    :align: center
    :height: 300px
    :alt: Picture about SANS smearing


Fitting multiple smeared data together
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
In the following example all smearing types may be mixed and can be fitted together.
For details and more examples on smearing see :py:func:`jscatter.sas.smear`

This examples shows SAXS/SANS smearing with different collimations.

.. literalinclude:: ../../examples/example_fitwithsmearing.py
    :language: python
    :end-before: sys.exit()  # end

.. image:: ../../examples/images/smearedfitexample.png
    :align: center
    :height: 300px
    :alt: Picture about smearing/desmearing


Smearing and desmearing of SAX and SANS data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Here we examine the effect of instrumental smearing for SAX (Kratky Camera, line! ) and SANS
and how we can use the Lake algorithm for desmearing.

The conclusion is that because of the increased noise it is in most cases more effective to fit smeared models
than to desmear data and fit these.
The additional advantage is that at the edges (eg detector limits) we can desmear a model correctly
while we need assumptions for the data (e.g. low Q Guinier behavior, high Q as constant)
which are sometimes difficult to justify.

.. literalinclude:: ../../examples/example_SASdesmearing.py
    :language: python

.. image:: ../../examples/SASdesmearing.png
    :align: center
    :height: 300px
    :alt: Picture about smearing/desmearing


Multilamellar Vesicles
^^^^^^^^^^^^^^^^^^^^^^
Here we look at the various effects appearing for vesicles and how they change the scattering.

.. literalinclude:: ../../examples/example_multilamellarVesicle.py
    :language: python
    :lines: 2-

The first image shows how a multilamellar vesicles changes the shape
of the membrane correlation peak with increasing dislocations of the centers.

.. image:: ../../examples/multilamellar1.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar1

Larger number of lamella shifts the correlation peak to higher Q.

.. image:: ../../examples/multilamellar2.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar2

The shell formfactor determines the high Q minima.
This allows to access the structure of e.g. bilayers.

.. image:: ../../examples/multilamellar3.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar3

Multilamellar and unilamellar can be distinguished with the aid of the appearing correlation peaks.
See below.

.. image:: ../../examples/multilamellar4.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar4

**A more realistic example for DPPC**

We use a simplified model with 3 box layers and approximate thickness and scattering length densities.
Kučerka uses a multi Gaussian profile.


.. literalinclude:: ../../examples/example_multilamellarVesiclereal.py
    :language: python
    :lines: 2-
.. image:: ../../examples/multilamellar5.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar5

**Multilamellar SAXS example for DPPC**

The first minima with following increase is a result of the near matching condition for bilayers in SAXS.
Additionally we observe characteristic peaks/shoulders in the first increase/top as
a result of multilamellar interference.
See for comparison Kučerka et al. Langmuir 23, 1292 (2007) https://doi.org/10.1021/la062455t .

We use again the simplified model with 3 box layers and approximate thickness from above

.. literalinclude:: ../../examples/example_multilamellarVesicleSAXS.py
    :language: python
    :lines: 2-
.. image:: ../../examples/multilamellar5SAXS.png
    :align: center
    :height: 300px
    :alt: Picture multilamellar5SAXS



2D oriented scattering
^^^^^^^^^^^^^^^^^^^^^^

**Formfactors of oriented particles or particle complexes**

.. literalinclude:: ../../examples/example_2D_orientedScattering.py
    :language: python
    :lines: 2-
.. image:: ../../examples/2D_5coreshell.png
    :align: left
    :height: 300px
    :alt: 2D scattering coreshell
.. image:: ../../examples/2D_5spheres.png
    :align: center
    :height: 300px
    :alt: 2D scattering

**Oriented crystal structure factors in 2D**

.. literalinclude:: ../../examples/example_2D_structurefactors.py
    :language: python
    :lines: 5-
.. image:: ../../examples/smallCubeAsymmetric.png
    :align: center
    :height: 300px
    :alt: 2D scattering coreshell
.. image:: ../../examples/smallCube10degreeRotation.png
    :align: center
    :height: 300px
    :alt: 2D scattering

**Ewald Sphere of simple cubic lattice**

.. literalinclude:: ../../examples/example_EwaldSphere.py
    :language: python
    :lines: 1-
.. image:: ../../examples/Ewald2.png
    :align: left
    :height: 300px
    :alt: Ewald2
.. image:: ../../examples/Ewald.png
    :align: center
    :height: 300px
    :alt: Ewald2


A nano cube build of different lattices
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. include:: ../../examples/example_comparisonLattices.py
    :start-after: """
    :end-before:  END

.. literalinclude:: ../../examples/example_comparisonLattices.py
    :language: python
    :lines: 23-69
.. image:: ../../examples/LatticeComparison.png
    :align: center
    :height: 300px
    :alt: LatticeComparison

.. include:: ../../examples/example_comparisonLattices.py
    :start-after: #start2
    :end-before:  #end2
.. literalinclude:: ../../examples/example_comparisonLattices.py
    :language: python
    :lines: 83-115
.. image:: ../../examples/LatticeComparison2.png
    :align: center
    :height: 300px
    :alt: LatticeComparison2


.. include:: ../../examples/example_comparisonLattices.py
    :start-after: #start3
    :end-before:  #end3
.. literalinclude:: ../../examples/example_comparisonLattices.py
    :language: python
    :lines: 132-
.. image:: ../../examples/LatticeComparison3.png
    :align: center
    :height: 300px
    :alt: LatticeComparison3


Linear Pearls with connecting coils
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The example uses cloudscattering to build a line of spheres.
Between the spheres are Gaussian coils to represent chains connecting the spheres.
The model :py:func:`~.formfactor.linearPearls` is very similar build
but uses a simpler build of the linear chain.

.. literalinclude:: ../../examples/example_connected_linearPearls.py
    :lines: 1-
.. image:: ../../examples/connected_linearPearls.png
    :align: center
    :height: 300px
    :alt: example_connected_linearPearls



Dynamic models
--------------

A comparison of different dynamic models in frequency domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_dynamics.py
    :language: python
    :lines: 2-
.. image:: ../../examples/DynamicModels.png
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit

Protein incoherent scattering in frequency domain
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We look at a protein in solution that shows translational and rotational diffusion
with atoms local restricted in a harmonic potential.

This is what is expected for the incoherent scattering of a protein (e.g. at 50mg/ml concentration).
A contribution of methyl rotation is missing.

For details see Fast internal dynamics in alcohol dehydrogenase The Journal of Chemical Physics 143, 075101 (2015);
    https://doi.org/10.1063/1.4928512

Here we use a reading of a PDB structure with only CA atoms for a simple model.
This can be improved using the bio module accessing positions
and selecting hydrogen atoms or adding coherent scattering.

First we look at the separate contributions :

.. literalinclude:: ../../examples/example_inelasticNeutronScattering.py
    :language: python
    :end-before: # all together in a combined model

.. image:: ../../examples/inelasticNeutronScattering.png
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit

Now we add the above components to a combined model.

.. literalinclude:: ../../examples/example_inelasticNeutronScattering.py
    :language: python
    :start-after: # all together in a combined model


.. image:: ../../examples/Ribonuclease_inelasticNeutronScattering.png
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit


Hydrodynamic function
^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_HydrodynamicFunction.py
    :language: python
    :lines: 1-
.. image:: ../../examples/HydrodynamicFunction.png
    :align: center
    :height: 300px
    :alt: Picture HydrodynamicFunction

Biomacromolecules (bio)
-----------------------
Examples using the biomacromolecule module (bio) for protein and DNA scattering.

Selective partial deuteration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Partial deuteration of protein complexes is a promising tool for examination of protein structure function
relationship.
E.g. see an interesting example about the complex in the cyanobacterial circadian clock system
Sugiyama et al, Nature Communications Biology (2022).  https://doi.org/10.1038/s42003-022-03143-z

Here  we see how to selectively deuterate domains or specific aminoacids and how scattering is influenced.
The deuteration is considered in all bio methods.

.. literalinclude:: ../../examples/example_bio_partialdeuteratedprotein.py
    :lines: 1-
.. image:: ../../examples/images/bio_protein_partialmatching.png
    :align: center
    :height: 300px
    :alt: bio_protein_partialmatching.png


Protein scattering and effective diffusion
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Protein scattering for different molecular weight proteins at 10 g/l concentration.

See `Exploring internal protein dynamics by neutron spin echo spectroscopy <https://doi.org/10.1039/C0SM00683A>`_
for details. Meanwhile the ADH pdb structure was improved.


.. literalinclude:: ../../examples/example_bio_proteinformfactoranddiffusion.py
    :lines: 1-
.. image:: ../../examples/images/bio_protein_formfactor+Diffusion.png
    :align: center
    :height: 300px
    :alt: bio_protein_formfactor+Diffusion.png


Protein density determination
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
We compare measured protein density data with the density calculated by Jscatter
to check the SESVolume accuracy in the module :py:mod:`jscatter.bio` .

Respective references are given in ``js.examples.datapath+'/proteinSpecificVolumes.txt'``

.. literalinclude:: ../../examples/example_bio_proteinVolume.py
    :lines: 1-
.. image:: ../../examples/images/proteinDensityTest.png
    :align: center
    :height: 300px
    :alt: protein Density

Cα coarse grain radius
^^^^^^^^^^^^^^^^^^^^^^
We calculate an appropriate Size of residues dummy atoms for Cα atom models to get a
reasonable protein scattering intensity.

.. literalinclude:: ../../examples/example_bio_proteinCoarseGrainRadius.py
    :lines: 1-
.. image:: ../../examples/images/proteinCacoarsegrainRadius.png
    :align: center
    :height: 300px
    :alt: proteinCacoarsegrainRadius.png



Other stuff
-----------

Sedimentation of two particle sizes and resulting scattering: a Simulation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_Sedimentation.py
    :language: python
    :lines: 1-35
.. image:: ../../examples/Sedimentation.jpg
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit

.. literalinclude:: ../../examples/example_Sedimentation.py
    :language: python
    :lines: 36-
.. image:: ../../examples/bimodalScattering.jpg
    :align: center
    :height: 300px

Create a stacked chart of some curves
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. literalinclude:: ../../examples/example_grace_stackeddata.py
    :language: python
    :lines: 1-
.. image:: ../../examples/stackedGaussians.jpeg
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit


----------

.. automodule:: jscatter.examples
    :members:

