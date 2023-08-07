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
This module contains the scattering functions.

"""
import numpy as np
import scipy
import os
import re
import subprocess
import shutil
import tempfile
import numbers

from .. import formel
from .mda import MDAnalysis as mda

try:
    import pymol2
except ImportError:
    pymol2 = False


__all__ = ['runHydropro', 'readHydroproResult']


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_dataline(words):
    """
    Test if line words starts with float.
    wf : list of strings

    """
    try:
        return is_float(words[1]) and is_float(words[0])
    except IndexError:
        return False


def runHydropro(atomgroup, outfile=None, type=1, T=20, visc=0, AER=None, NSIG=-1, SIGMAX=4.0, SIGMIN=3.0,
                MW=None, soldensity=1.11, solvent='d2o', showoutput=0, hydropro='hydropro10-lnx.exe'):
    """
    Diffusion tensor, Dtrans, Drot, S and more from PDB structure using HYDROPRO.

    HYDROPRO computes the hydrodynamic properties of rigid macromolecules from PDB structures.
    This wrapper writes the input file for HYDROPRO [1]_  hydropro.dat, runs HYDROPRO and reads the result file.
    The hydropro executable named 'hydropro10-lnx.exe' needs to be in the PATH. Download from [2]_.

    Use :py:func:`~.readHydroproResult` to read an existing result file.

    Parameters
    ----------
    atomgroup : atomgroup, string
        A MDAnalysis atomgroup (e.g. uni.select_atoms('protein') or the filename of a PDB structure.
        If the filename contains a prepended path this is used as working directory wor the output.
    outfile : string, default None
        Output filename to use, by default a name is generated from residue names and Rg.
    type : 1,2,4
        - 1 -- Atomic-level primary model, shell calculation
        - 2 -- Residue-level primary model, shell calculation
        - 4 -- Residue-level primary model, bead calculation
    T : float default 20
        Temperature in °C.
    visc : float , default 0
        Viscosity in poise=0.1*Pa*s.
        0 means calc from temperature T for solvent.
    AER : float, default depends on type
        The value of the hydrodynamic radius, in Å
        type 1 default to 2.9 A
        type 2 default to 4.8 A
        type 4 default to 6.1 A
    NSIG : int, default -1
        NSIG (INTEGER) Number of values of the radius of the mini bead.
        -1 autodetermine SIGMIN SIGMAX
    SIGMAX : float, default 4.0
        Lowest value of sigma, the mini bead radius
    SIGMIN : float, default 3.0
        Highest value of sigma, the mini bead radius
    MW : float, default None
        Molecular weight; if None calculated from universe
    soldensity : float,default 1.1
        Solvent density  1.1 is d2o
    solvent : 'd2o' or 'h2o'
        Solvent
    showoutput : 0
        Show output of hydropro 0 ->minimal; None ->No output; other ->full output
    hydropro : string, default 'hydropro10-lnx.exe'
        Filename of the hydropro executable in PATH.

    Returns
    -------
    dict with results of 6x6 mobility matrix with 4 3x3 matrices
        - 'DTT' : translational 3x3 matrix, units nm^2/ps
        - 'DRR' : rotational 3x3 matrix, units 1/ps
        - 'DTR' ='DRT'^T : translational rotational coupling, units nm/ps
        -  other keys with units as given in values

    Examples
    --------
    ::

     import jscatter as js
     uni = js.bio.scatteringUniverse('3rn3',addHydrogen=False)
     H = js.bio.runHydropro(uni.atoms)
     uni.qlist = np.r_[0.01:2:0.1]
     D = js.bio.diffusionTRUnivTensor(uni,DTT=H['DTT'],DRR=H['DRR'],DRT=H['DRT'])


    References
    ----------
    .. [1] Prediction of hydrodynamic and other solution properties of rigid proteins
           from atomic- and residue-level models
           A. Ortega, D. Amorós, J. Garc1a de la Torre,
           Biophys. J. 101, 892-898 (2011)
    .. [2] http://leonardo.inf.um.es/macromol/programs/hydropro/hydropro.htm


    """
    path = os.getcwd()
    # noinspection PyAugmentAssignment
    if hasattr(atomgroup, 'write'):
        if outfile is None:
            # generate a specific name
            aminos = [mda.lib.util.convert_aa_code(res)
                      for res in atomgroup.select_atoms('protein').residues[:5].resnames]
            nucleic = [r[0] for r in atomgroup.select_atoms('nucleic').residues[:5].resnames]
            pdbfile = ''.join(aminos+nucleic)[:5]
            if not pdbfile: pdbfile = 'compl'
            pdbfile += f'{atomgroup.total_mass():.0f}'
        else:
            pdbfile=outfile
        Rg = atomgroup.radius_of_gyration()
        pdbfile = pdbfile+f'Rg{10*Rg:.0f}T{T:.0f}'
        pdbfile = pdbfile[:20]
        atomgroup.write(pdbfile+'.pdb')
        if MW is None:
            MW=atomgroup.total_mass()
        if np.alltrue(atomgroup.atoms.names == 'CA'):
            # for Calpha models
            AER = 4.8  # in A for Ca models
        else:
            AER = 2.9  # in A for atomic models
    elif os.path.isfile(atomgroup+'.pdb') or os.path.isfile(atomgroup):
        path, file = os.path.split(atomgroup)
        pdbfile, _ = os.path.splitext(file)
        if AER is None:
            if type == 1:
                AER = 2.9
            elif type == 2:
                AER = 4.8
            elif type == 4:
                AER = 6.1
    else:
        raise ValueError('Input is not atomgroup nor pdb file!')

    if len(pdbfile) > 38:
        raise NameError('PDB filename to long. Should be not more than 38 char.')


    # generate the input file
    zeilen = []
    zeilen.append(pdbfile)             # title
    zeilen.append(pdbfile)             # Name for output file
    zeilen.append(pdbfile+'.pdb')      # Structural (PBD) file
    zeilen.append(f'{type:.0f},                  !Type of calculation ')     # type of calculation
    zeilen.append(f'{AER:.1f},                   !AER, radius of the atomic elements')
    zeilen.append(f'{NSIG:.1f},                  !NSIG ANzahl R zwischen min max')
    if NSIG != -1:
        zeilen.append(f'{SIGMIN:.1f},              !Minimum radius of beads in the shell (SIGMIN)')
        zeilen.append(f'{SIGMAX:.1f},              !Maximum radius of beads in the shell (SIGMAX)')
    zeilen.append(f'{T:.1f},           !T (temperature, C)')
    if visc == 0:
        visc = formel.viscosity(mat=solvent, T=273.15+T) * 10
    zeilen.append(f'{visc:.4f},                !ETA ')
    zeilen.append(f'{MW:.1f},                  !RM (Molecular weigth)')
    zeilen.append('-1.0,                       !partial specific volume, cm3/g')
    zeilen.append(f'{soldensity:.2f},          !Solvent density, g/cm3')
    zeilen.append('0,               !NQ Number of values of Q')
    zeilen.append('0,               !Number of intervals for the distance distribution')
    zeilen.append('0,               !Number of trials for MC calculation of covolume')
    zeilen.append('1                 !IDIF=1 (yes) for full diffusion tensors')
    zeilen.append('*                 !End of file')

    hydroprodatpath = os.path.join(path, 'hydropro.dat')
    with open(hydroprodatpath, 'w') as f:
        f.writelines(' \n'.join(zeilen))

    hydroproexe = shutil.which(hydropro)
    if not hydroproexe:
        raise FileNotFoundError('No hydropro executable found in PATH.')

    p = subprocess.run(hydroproexe, shell=True, capture_output=True, cwd=path)

    if p.stderr != '':
        for line in p.stderr.split(b'\n'):
            print('hydropro_std_err>', line)

    if showoutput:
        for line in p.stdout.split(b'\n'):
            print('hydropro>', line)

    elif showoutput is not None:
        linestoshow = [b'poise', b'Molecular weight', b'Translational']
        for line in p.stdout.split(b'\n'):
            if any(word in line for word in linestoshow):
                print('hydropro>', line)
    #
    result = readHydroproResult(os.path.join(path, pdbfile)+'-res.txt')

    return result


def readHydroproResult(file='.res'):
    """
    Reads the result file of HYDROPRO.

    Parameters
    ----------
    file          filename in dir or full path without dir

    Returns
    -------
    dict with results of 6x6 mobility matrix with 4 3x3 matrizes
        - 'DTT' : translational 3x3 matrix, units nm^2/ps
        - 'DRR' : rotational 3x3 matrix, units 1/ps
        - 'DTR' ='DRT'^T : tranlational rotational coupling, units nm/ps
        -  other keys with units as given in values


    """
    with open(file) as f:
        zeilen = f.readlines()

    H = []
    result = {}
    empty = re.compile('^\s*$')
    for zeile in zeilen:
        if empty.match(zeile):
            continue
        words = zeile.split()
        if is_dataline(words):
            H.append([float(w) for w in words])
        elif ':' in zeile:
            try:
                words = zeile.split(':')
                key = words[0].strip().replace(' ','_')
                vals = words[1].split()
                if is_float(vals[0]):
                    val = float(vals[0])
                    result[key] = (val,) + tuple(vals[1:])
            except:
                pass
    aH = np.array(H)
    result['DTT'] = aH[:3, :3] * 1.e+2
    result['DTR'] = aH[:3, 3:] * 1.e-5
    result['DRT'] = aH[3:, :3] * 1.e-5
    result['DRR'] = aH[3:, 3:] * 1.e-12

    return result


def savePymolpng(atomgroup, fname, rotate=[]):
    """
    Save png image of current configuration using Pymol.

    A simplified method to make png images.
    For more control use this function as a template and adopt it to your needs.
    Pymol needs to be installed (version >2.4)

    Parameters
    ----------
    atomgroup : atomgroup
        Atomgroup to show in plot.
    fname : string
        Filename
    rotate : list 3xfloat
        Angles to rotate around ['x','y','z'] axis.
        Missing values are zero.

    """
    if isinstance(rotate,numbers.Number):
        rotate = [rotate]
    if pymol2:
        with pymol2.PyMOL() as p1:
            with tempfile.TemporaryDirectory() as tdir:
                name = os.path.splitext(atomgroup.universe.filename)[0] + '.pdb'
                tfile = os.path.join(tdir, name)
                atomgroup.write(tfile)
                p1.cmd.load(tfile)

                for ax, angle in zip(['x','y','z'], rotate):
                    p1.cmd.rotate(ax, angle, 'all')

                # set colors
                p1.cmd.color('red', 'ss h')
                p1.cmd.color('yellow', 'ss s')
                p1.cmd.color('blue', 'ss l+')
                p1.cmd.set('cartoon_nucleic_acid_color', 'yellow')
                p1.cmd.set('cartoon_ladder_color', 'green')
                p1.cmd.set('cartoon_discrete_colors',1)
                p1.cmd.set('cartoon_ring_mode', 1)
                p1.cmd.color('green', '(resn DA+DC+DG+DT)')

                # make png
                p1.cmd.png(fname, width=600, height=600, dpi=-1, ray=1)

    else:
        print('Pymol needed but Pymol not installed or old version.')










