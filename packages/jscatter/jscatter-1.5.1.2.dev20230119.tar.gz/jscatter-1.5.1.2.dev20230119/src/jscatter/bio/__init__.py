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
The aim of the biomacromolecules (bio) module is the calculation of static and dynamic scattering properties
of biological molecules as proteins or DNA (and later the analysis of MD simulations).

- Functions are provided to calculate **SAXS/SANS** formfactors, effective diffusion
  or intermediate scattering functions as measured by SAXS/SANS, Neutron Spinecho Spectroscopy (**NSE**),
  BackScattering (**BS**) or TimeOfFlight (**TOF**) methods.

- For the handling of atomic structures as PDB files (https://www.rcsb.org/) we use the library
  `MDAnalysis <https://www.mdanalysis.org/>`_ which allows **reading/writing of PDB files** and
  molecular dynamics trajectory files of various formats and MD simulation tools.

- PDB structures contain in most cases no hydrogen atoms.
  There are several possibilities to **add hydrogens** to existing PDB structures
  (see Notes in :py:func:`~jscatter.bio.mda.pdb2pqr`).
  We use the algorithm  pdb2pqr (allows debumping and optimization) or a simpler algorithm from PyMol.

- **Mode analysis** allows deformations of structures or calculation of dynamic properties.
  Deformation modes can be used to fit a protein structure to SAXS/SANS data (also simultaneous).

- To inspect the content of a universe or changes in a structure Pymol, VMD or other visualization viewers can be used.
  In a Jupyter notebook nglview can be used.

.. image:: ../../examples/images/mode_animation.gif
 :align: center
 :width: 50 %
 :alt: mode_animation

|mdanalysis|

  .. |mdanalysis| image:: https://img.shields.io/badge/powered%20by-MDAnalysis-orange.svg?logoWidth=16&logo=data:image/x-icon;base64,AAABAAEAEBAAAAEAIAAoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJD+XwCY/fEAkf3uAJf97wGT/a+HfHaoiIWE7n9/f+6Hh4fvgICAjwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACT/yYAlP//AJ///wCg//8JjvOchXly1oaGhv+Ghob/j4+P/39/f3IAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJH8aQCY/8wAkv2kfY+elJ6al/yVlZX7iIiI8H9/f7h/f38UAAAAAAAAAAAAAAAAAAAAAAAAAAB/f38egYF/noqAebF8gYaagnx3oFpUUtZpaWr/WFhY8zo6OmT///8BAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgICAn46Ojv+Hh4b/jouJ/4iGhfcAAADnAAAA/wAAAP8AAADIAAAAAwCj/zIAnf2VAJD/PAAAAAAAAAAAAAAAAICAgNGHh4f/gICA/4SEhP+Xl5f/AwMD/wAAAP8AAAD/AAAA/wAAAB8Aov9/ALr//wCS/Z0AAAAAAAAAAAAAAACBgYGOjo6O/4mJif+Pj4//iYmJ/wAAAOAAAAD+AAAA/wAAAP8AAABhAP7+FgCi/38Axf4fAAAAAAAAAAAAAAAAiIiID4GBgYKCgoKogoB+fYSEgZhgYGDZXl5e/m9vb/9ISEjpEBAQxw8AAFQAAAAAAAAANQAAADcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAjo6Mb5iYmP+cnJz/jY2N95CQkO4pKSn/AAAA7gAAAP0AAAD7AAAAhgAAAAEAAAAAAAAAAACL/gsAkv2uAJX/QQAAAAB9fX3egoKC/4CAgP+NjY3/c3Nz+wAAAP8AAAD/AAAA/wAAAPUAAAAcAAAAAAAAAAAAnP4NAJL9rgCR/0YAAAAAfX19w4ODg/98fHz/i4uL/4qKivwAAAD/AAAA/wAAAP8AAAD1AAAAGwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALGxsVyqqqr/mpqa/6mpqf9KSUn/AAAA5QAAAPkAAAD5AAAAhQAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADkUFBSuZ2dn/3V1df8uLi7bAAAATgBGfyQAAAA2AAAAMwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB0AAADoAAAA/wAAAP8AAAD/AAAAWgC3/2AAnv3eAJ/+dgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA9AAAA/wAAAP8AAAD/AAAA/wAKDzEAnP3WAKn//wCS/OgAf/8MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIQAAANwAAADtAAAA7QAAAMAAABUMAJn9gwCe/e0Aj/2LAP//AQAAAAAAAAAA
    :alt: Powered by MDAnalysis
    :target: https://www.mdanalysis.org
"""

import numpy as np
import warnings
from .. import _platformname

if _platformname[0] == 'Windows':
    warnings.warn('On windows there is no fortran compiler, therefore no bio module.')
else:
    from .mda import *
    from .scatter import *
    from .nma import *
    from .utilities import *
    from ..libs.HullRad import hullRad


# warnings.simplefilter("error", np.VisibleDeprecationWarning)
# warnings.simplefilter(action='ignore', category=np.VisibleDeprecationWarning)
# warnings.simplefilter(action='ignore', category=DeprecationWarning)


