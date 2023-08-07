# -*- coding: utf-8 -*-
import setuptools
from setuptools import dist

# dist.Distribution().fetch_build_eggs(['Cython>=0.20', 'numpy>=1.21'])
import os
import glob
import io
import numpy.distutils.core
from numpy.distutils.fcompiler import get_default_fcompiler
from Cython.Build import cythonize
from numpy.distutils.extension import Extension as npExtension
from setuptools.extension import Extension as stExtension

# this is to get the __version__ from version.py
with open('src/jscatter/version.py', 'r') as f:  exec(f.read())

with io.open('README.rst', encoding='utf-8') as readme_file:
    long_description = readme_file.read()

EXTENSIONS = []
# find fortran files
fs = glob.glob(os.path.join('src', 'jscatter', 'source', '*.f9[05]'))
fs.sort()
if get_default_fcompiler(requiref90=True):
    EXTENSIONS.append(npExtension(name='jscatter.fscatter',
                                sources=fs,
                                extra_f90_compile_args=['-fopenmp'],
                                libraries=['gomp'],
                                # extra_f90_compile_args=['--debug','-fbounds-check'],
                                # f2py_options=['--debug-capi']
                                ))

# cython and c compilation
c_extensions = [stExtension(name='jscatter.libs.cubature._cubature',
                          sources=[
                              'src/jscatter/libs/cubature/cpackage/hcubature.c',
                              'src/jscatter/libs/cubature/cpackage/pcubature.c',
                              'src/jscatter/libs/cubature/get_ptr.c',
                              'src/jscatter/libs/cubature/_cubature.pyx',
                          ],
                          # include_dirs = [numpy.get_include()],
                          language='c'),
                stExtension('jscatter.libs.cubature._test_integrands',
                          sources=['src/jscatter/libs/cubature/_test_integrands.pyx'],
                          # include_dirs = [numpy.get_include()],
                          language='c'),
                ]
EXTENSIONS.extend(cythonize(c_extensions, compiler_directives={'linetrace': True,
                                                               'language_level': "3"}))

EXTENSIONS.append(stExtension(name='jscatter.libs.surface',
                                                 sources=['src/jscatter/source/SASA_surface.c'],
                                                 extra_compile_args=[],
                                                 include_dirs=['Include', '/usr/local/include']))

description = ("Combines dataArrays with attributes for fitting, plotting"
               "and analysis including models for Xray and neutron scattering")

fileext = ['*.txt', '*.rst', '*.dat', '*.html', '*.ipynb', '*.md', '*.f95', '*.f90',
           '*.tiff', '*.png', '*.jpg', '*.agr', '*.gif',
           '*.Dq', '*.pdb', '*.pdh', '*.cif', '*.fq', '*.gz']

numpy.distutils.core.setup(name='jscatter',
                           version=__version__,
                           description=description,
                           long_description=long_description,
                           long_description_content_type='text/x-rst',
                           author='Ralf Biehl',
                           author_email='ra.biehl@fz-juelich.de',
                           url='https://gitlab.com/biehl/jscatter',
                           project_urls={"Documentation": "http://jscatter.readthedocs.io/",
                                         "Source Code": "https://gitlab.com/biehl/jscatter",
                                         "Live Demo": "https://mybinder.org/v2/gl/biehl%2Fjscatter/master?filepath="
                                                      "src%2Fjscatter%2Fexamples%2Fnotebooks"},
                           platforms=["linux", "osx", "windows"],
                           classifiers=[
                               'Development Status :: 5 - Production/Stable',
                               'Intended Audience :: Science/Research',
                               'Operating System :: POSIX :: Linux',
                               'Operating System :: MacOS :: MacOS X',
                               'Operating System :: Microsoft :: Windows :: Windows 10',
                               'Programming Language :: Python :: 3.8',
                               'Programming Language :: Python :: 3.9',
                               'Programming Language :: Python :: 3.10',
                               'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                               'Programming Language :: Python',
                               'Topic :: Scientific/Engineering :: Physics'],
                           include_package_data=True,
                           package_dir={'': 'src'},
                           py_modules=[],
                           packages=setuptools.find_packages('src'),
                           package_data={'': fileext},
                           # data_files=datafiles,
                           dependency_links=[''],
                           install_requires=["numpy >= 1.20 ",
                                             "numpydoc>=1.1.0",
                                             "scipy >= 1.8",
                                             "matplotlib >= 3",
                                             "Pillow >= 8.1",
                                             "MDAnalysis >= 2.1.0",
                                             "cython",
                                             "fabio",
                                             "pdb2pqr",
                                             "requests",
                                             "nglview",
                                             "emcee"],
                           ext_modules=EXTENSIONS,
                           test_suite='jscatter.test.suite'
                           )
