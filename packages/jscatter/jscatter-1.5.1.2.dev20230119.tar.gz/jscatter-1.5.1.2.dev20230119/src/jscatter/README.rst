**The aim of Jscatter is treatment of experimental data and models**:

.. image:: ../../examples/Jscatter.jpeg
    :width: 200px
    :align: right
    :height: 200px
    :alt: Jscatter Logo

* Reading and analyzing experimental data with associated attributes as temperature, wavevector, comment, ....
* Multidimensional fitting taking attributes into account.
* Providing useful models for **neutron and X-ray scattering** form factors, structure factors
  and dynamic models (quasi elastic neutron scattering) and other topics.
* Simplified plotting with paper ready quality.
* Easy model building for non programmers.
* Python scripts/Jupyter Notebooks to document data evaluation and modelling.


.. |citation| image:: https://img.shields.io/badge/DOI-10.1371%2Fjournal.pone.0218789-blue
            :target: https://doi.org/10.1371/journal.pone.0218789

.. |binder| image:: https://img.shields.io/badge/launch-jscatter-F5A252.svg?logo=data:image/png;base64,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
            :alt: link to mybinder
            :target: https://mybinder.org/v2/gl/biehl%2Fjscatter/master?filepath=src%2Fjscatter%2Fexamples%2Fnotebooks

.. |install| image:: https://img.shields.io/pypi/v/jscatter?labelColor=black?logoColor=blue   :alt: PyPI
    :target: https://pypi.org/project/jscatter/

.. |license| image:: https://img.shields.io/badge/license-GPLv3-orange
            :target: https://www.gnu.org/licenses/gpl-3.0.en.html

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/jscatter?color=orange   :alt: PyPI - Python Version
            :target: https://pypi.org/project/jscatter/

.. |docs| image:: https://img.shields.io/readthedocs/jscatter?color=orange
            :alt: Read the Docs
            :target: https://jscatter.readthedocs.io/en/latest/

.. |beginners| image:: https://img.shields.io/badge/Beginners-Guide-orange
            :alt: Beginners Guide
            :target: https://jscatter.readthedocs.io/en/latest/BeginnersGuide.html

|binder|  |citation|  |install| |license| |pyversion| |docs| |beginners|



**Main concept**

- Data are **organised** in :py:class:`~.dataArray` / :py:class:`~.dataList` with attributes
  as .temperature, .wavevector, .pressure  and methods for filter, merging and more.
  See :ref:`What are dataArray/dataList`.
- Multidimensional, attribute dependent **fitting** (least square Levenberg-Marquardt,
  Bayesian fit, differential evolution, ...).
  See :ref:`Fitting experimental data` or :py:meth:`~.dataarray.dataList.fit`.
- Provide relative simple **plotting** commands to allow a fast view on data and possible later pretty up.
  See :ref:`Plotting in XmGrace` or :ref:`mpl` for an interface to matplotlib.
- User write models using the existing **model library** or self created models.
  See :ref:`How to build simple models` and :ref:`How to build a more complex model`.

  The model library contains routines e.g. for vectorized quadrature (:ref:`formel`)
  or specialised models for scattering as :ref:`formfactor (ff)`, :ref:`structurefactor (sf)`, :ref:`dynamic`
  and :ref:`biomacromolecules (bio)`.



**Exemplary functions**:

    .. collapse:: Physical equations and useful formulas as quadrature of vector functions

        - :py:func:`~.formel.scatteringLengthDensityCalc` -> Electron density, coh and inc neutron scattering length, mass.
        - :py:func:`~.smallanglescattering.smear` -> Smearing enabling simultaneous fits of differently smeared SANS/SAXS data.
        - :py:func:`~.smallanglescattering.desmear` -> Desmearing according to the Lake algorithm for the above.

        See :ref:`formel` and :ref:`smallanglescattering (sas)`

    .. collapse:: Particle Formfactors

        - :py:func:`~.formfactor.polymer.ringPolymer` -> General formfactor of a polymer ring.
        - :py:func:`~.formfactor.polymer.alternatingCoPolymer` -> Alternating linear copolymer between collapsed.
           and swollen states
        - :py:func:`~.formfactor.composed.multiShellSphere` -> Formfactor of multi shell spherical particles.
        - :py:func:`~.formfactor.composed.multiShellCylinder` -> Formfactor of multi shell cylinder particles with caps.
        - :py:func:`~.cloudscattering.orientedCloudScattering` -> 2D scattering of an oriented cloud of scatterers.

        See :ref:`formfactor (ff)`

    .. collapse:: Particle Structurefactors

        - :py:func:`~.structurefactor.fluid.RMSA` -> Rescaled MSA structure factor for dilute charged colloidal dispersions.
        - :py:func:`~.structurefactor.fluid.twoYukawa` -> Structure factor for a two Yukawa potential in mean spherical approximation.
        - :py:func:`~.structurefactor.fluid.hydrodynamicFunct` -> Hydrodynamic function from hydrodynamic pair interaction.

        See :ref:`structurefactor (sf)`

    .. collapse:: Dynamics

        - :py:func:`~.dynamic.finiteZimm` -> Zimm model with internal friction -> intermediate scattering function.
        - :py:func:`~.dynamic.diffusionHarmonicPotential` -> Diffusion in harmonic potential-> intermediate scattering function.
        - :py:func:`~.dynamic.methylRotation` -> Incoherent intermediate scattering function of CH3 methyl rotation.

        See :ref:`dynamic`

    .. collapse:: biomacromoleules

        - :py:func:`~.bio.scatter.scatIntUniv` -> Neutron/Xray scattering of protein/DNA with contrast to solvent.
        - :py:func:`~.bio.scatter.intScatFuncYlm` -> Diffusional dynamics of protein/DNA with contrast to solvent.
        - :py:func:`~.bio.scatter.diffusionTRUnivTensor` -> Effective diffusion from 6x6 diffusion tensor.
        - :py:func:`~.bio.scatter.intScatFuncOU` -> ISF I(q,t) for Ornstein-Uhlenbeck process of normal mode domain motions.

        See :ref:`biomacromolecules (bio)`

**How to use Jscatter**
 see :ref:`label_Examples` and :ref:`Beginners Guide / Help` or
 try Jscatter live at |binder| .


.. literalinclude:: ../../examples/example_simple_diffusion.py
    :language: python
    :end-before: if 1:
.. image:: ../../examples/DiffusionFit.jpg
    :align: center
    :height: 300px
    :alt: Picture about diffusion fit


**Shortcuts**::

    import jscatter as js
    js.showDoc()                  # Show html documentation in browser
    exampledA=js.dA('test.dat')   # shortcut to create dataArray from file
    exampledL=js.dL('test.dat')   # shortcut to create dataList from file
    p=js.grace()                  # create plot in XmGrace
    p=js.mplot()                  # create plot in matplotlib
    p.plot(exampledL)             # plot the read dataList

.. currentmodule:: jscatter

.. autosummary::
    jscatter.usempl
    jscatter.headless
    jscatter.version

----------------

| If not otherwise stated in the files:
|
| written by Ralf Biehl at the Forschungszentrum Jülich ,
| Jülich Center for Neutron Science 1 and Institute of Complex Systems 1
|    Jscatter is a program to read, analyse and plot data
|    Copyright (C) 2015-2021  Ralf Biehl
|
|    This program is free software: you can redistribute it and/or modify
|    it under the terms of the GNU General Public License as published by
|    the Free Software Foundation, either version 3 of the License, or
|    (at your option) any later version.
|
|    This program is distributed in the hope that it will be useful,
|    but WITHOUT ANY WARRANTY; without even the implied warranty of
|    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
|    GNU General Public License for more details.
|
|    You should have received a copy of the GNU General Public License
|    along with this program.  If not, see <http://www.gnu.org/licenses/>.


**Intention and Remarks**

**Genesis**

This package was programmed because of my personal need to fit multiple datasets together which differ
in attributes defined by the measurements. A very common thing that is not included in numpy/scipy or
most other fit programs. What I wanted is a numpy *ndarray* with its matrix like functionality
for evaluating my data, but including attributes related to the data e.g. from a measurement.
For multiple measurements I need a list of these with variable length. ==> dataArray and dataList.

As the used models are repeatedly the same a module with physical models was growing.
A lot of these models are used frequently in Small Angle Scattering programs like SASview or SASfit.
For my purpose the dynamic models as diffusion, ZIMM, ROUSE and other things mainly for protein dynamics
were missing.

Some programs (under open license) are difficult to extend as the models are hidden in classes,
or the access/reusage includes a special designed interface to get parameters instead of simple function calls.
Here Python functions are easier to use for the non-programmers as most PhD-students are.
Models are just Python functions (or one line lambda functions) with the arguments accessed by their name
(keyword arguments). Scripting in Python with numpy/scipy is easy to learn even without
extended programming skills.

The main difficulty beside finding the right model for your problem is proper multidimensional fitting
including errors. This is included in *dataArray/dataList* using scipy.optimize to allow
fitting of the models in an simple and easy way.
The user can concentrate on reading data / model fitting / presenting results.


**Scripting over GUI**

Documentation of the evaluation of scientific data is difficult in GUI based programs
(sequence of clicking buttons ???). Script oriented evaluation (MATLAB, Python, Jupyter,....)
allows easy repetition with stepwise improvement and at the same time document what was done.

Complex models have multiple contributions, background contribution, ...
which can easily be defined in a short script including a documentation.
I cannot guess if the background in a measurement is const linear, parabolic or whatever and
each choice is also a limitation.
Therefore the intention is to supply not obvious and complex models (with a scientific reference)
and allow the user to adopt them to their needs e.g. add background and amplitude or resolution convolution.
Simple models are fast implemented in one line as lambda functions or more complex things in scripts.
The mathematical basis as integration or linear algebra can be used from scipy/numpy.


**Plotting**

`Matplotlib <https://matplotlib.org/>`_ seems to be the standard for numpy/scipy users.
You can use it if you want. If you try to plot fast and live (interactive) it is complicated and slow.
3D plotting has strong limitations.

Frequently I run scripts that show results of different datasets and I want to keep these
for comparison open and be able to modify the plot. Some of this is possible in matplotlib but not the default.
As I want to think about physics and not plotting, I like more xmgrace, with a GUI interface
after plotting. A simple one line command should result in a 90% finished plot,
final 10% fine adjustment can be done in the GUI if needed or from additional commands.
I adopted the original Graceplot module (python interface to XmGrace) to my needs and added
dataArray functionality. For the errorPlot of a fit a simple matplotlib interface is included.
Meanwhile, the module mpl is a rudimentary interface to matplotlib to make plotting easier for beginners.

The nice thing about Xmgrace is that it stores the plot as ASCII text instead of the JPG or PDF.
So its easy to reopen the plot and change the plot later if your supervisor/boss/reviewer asks
for log-log or other colors or whatever. For data inspection zoom, hide of data, simple fitting
for trends and else are possible on WYSIWYG/GUI basis.
If you want to retrieve the data (or forgot to save your results separately) they are accessible
in the ASCII file. Export in scientific paper quality is possible.
A simple interface for annotations, lines, .... is included.
Unfortunately its only 2D but this is 99% of my work.

**Speed/Libraries**

The most common libraries for scientific computing in python are NumPy and SciPy and these are the
main obligatory dependencies for Jscatter (later added matplotlib and Pillow for image reading).
Python in combination with numpy can be quite fast if the ndarrays methods are used consequently
instead of explicit for loops.
E.g. the numpy.einsum function immediately uses compiled C to do the computation.
(`See this <http://ipython-books.github.io/featured-01/>`_ and look for "Why are NumPy arrays efficient").
SciPy offers all the math needed and optimized algorithms, also from blas/lapack.
To speed up, if needed, on a multiprocessor machine the module :ref:`parallel` offers
an easy interface to the standard python module *multiprocessing* within a single command.
If your model still needs long computing time and needs speed up the common
methods as Cython, Numba or f2py (Fortran) should be used in your model.
As these are more difficult the advanced user may use it in their models.

A nice blog about possible speedups is found at
`Julia vs Python <https://www.ibm.com/developerworks/community/blogs/jfp/entry/Python_Meets_Julia_Micro_Performance?lang=en>`_.
Nevertheless the critical point in these cases is the model and not the small overhead in
dataArray/dataList or fitting.

As some models depend on f2py and Fortran code an example is provided how to use f2py and finally contribute
a function in Jscatter. :ref:`Extending/Contributing/Fortran`

Some resources :

 - `python-as-glue <https://docs.scipy.org/doc/numpy-1.10.1/user/c-info.python-as-glue.html>`_
 - `Julia vs Python <https://www.ibm.com/developerworks/community/blogs/jfp/entry/Python_Meets_Julia_Micro_Performance?lang=en>`_
 - `Getting the Best Performance out of NumPy <http://ipython-books.github.io/featured-01/>`_

**Development environment/ Testing**

The development platform is mainly current Linux (Manjaro/Rocky Linux (CentOS)) with testing on Gitlab
(Ubuntu docker image).
I regularly use Jscatter on macOS and on our Linux cluster. The code is Python 3.x compatible.
I rarely use Windows (only if a manufacturer of an instrument forces me...)
Jscatter works under native Windows 10, except things that rely on pipes or gfortran as the
connection to XmGrace and the DLS module which calls CONTIN through a pipe.
As matplotlib is slow fits give no intermediate output.

... Meanwhile (2021) Windows Subsystem for Linux (WSL) is the best choice to run Jscatter on Windows as any
Linux runs natively without limitations.


