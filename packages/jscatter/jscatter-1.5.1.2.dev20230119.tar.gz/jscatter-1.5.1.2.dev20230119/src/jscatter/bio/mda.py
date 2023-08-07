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
mda module contains functions to prepare/use MDAnalysis universes for scattering.

scattering length is in nm units

"""

import os
import sys
import re
import numbers
from collections import defaultdict
import gzip
import io
import urllib
import shutil
import tempfile
import subprocess

import numpy as np
import numpy.linalg as la
from scipy.interpolate import interp1d

import MDAnalysis
from MDAnalysis.core.topologyattrs import AtomAttr, ResidueAttr, AtomStringAttr, Atomtypes
from MDAnalysis.core.groups import Atom, AtomGroup, Residue, ResidueGroup
from MDAnalysis.topology.guessers import guess_types

from pdb2pqr.main import build_main_parser, main_driver, \
                        drop_water as pdb2pqr_drop_water, \
                        setup_molecule as pdb2pqr_setup_molecule,\
                        non_trivial as pdb2pqr_non_trivial, \
                        print_pqr as pdb2pqr_print_pqr, \
                        print_pdb as pdb2pqr_print_pdb
import pdb2pqr.io as pdb2pqr_io

try:
    import pymol2
except (ModuleNotFoundError, ImportError):
    pymol2 = False

from .. import data
from .. import formel
# noinspection PyUnresolvedReferences
from .. import fscatter
from ..libs import SASAsurface as sasa

Nscatlength = data.Nscatlength
neutronFFgroup = data.neutronFFgroup
xrayFFatomic = data.xrayFFatomic
xrayFFatomicdummy = data.xrayFFatomicdummy
xrayFFgroupdummy = data.xrayFFgroupdummy
xrayFFgroup = data.xrayFFgroup

pi = np.pi
identity3x3 = np.identity(3)
zero3x3 = np.zeros((3, 3))
QLIST = data.QLIST

# add deuterium to MDAnalysis tables
MDAnalysis.topology.tables.masses['D'] = data.Elements['d'][1]
MDAnalysis.topology.tables.vdwradii['D'] = MDAnalysis.topology.tables.vdwradii['H']

__all__ = ['copyUnivProp', 'getSurfaceVolumePoints', 'getNativeContacts', 'getDistanceMatrix', 'scatteringUniverse',
    'pdb2pqr', 'fastpdb2pqr', 'addH_Pymol', 'fetch_pdb', 'mergePDBModel', 'xrayFFgroup', 'neutronFFgroup']


ucopylist = ['d2oFract', 'temperature', 'solvent', 'solventDensity', 'error',
            'amideHexFract', 'histidinExchange', 'bcDensitySol', 'b2_incSol', 'probe_radius',
            'iscalphamodel', 'explicitResidueFormFactorAmpl', 'xsldSolvent', 'edensitySolvent', 'SESVolume',
             'SASVolume', 'SASArea']


def copyUnivProp(universe, objekt, addlist=[]):
    """
    Copies important universe properties from universe to object if they exist.

    The default list is in js.bio.ucopylist

    Parameters
    ----------
    universe : MDAnalysis universe
    objekt : objekt
        Objekt to copy to
    addlist : additional attribute list


    """
    for attr in ucopylist + addlist:
        # noinspection PyBroadException
        try:
            if hasattr(universe, attr):
                if hasattr(getattr(universe, attr), '__call__'):
                    aa = getattr(universe, attr)()  # as test to call
                    setattr(objekt, attr, getattr(universe, attr)())
                else:
                    setattr(objekt, attr, getattr(universe, attr))
        except:
            pass


class XRayFormFactor(AtomAttr):
    """
    coherent Xray formfactors amplitude in unit nm

    """
    attrname = 'faxs'
    singular = 'fax'
    dtype = np.float32  # object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]
    QLIST=QLIST
    transplants = defaultdict(list)

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros((n_atoms, QLIST.shape[0]))

    def get_atoms(self, atomgroup):
        # Get values from single atom by interpolation to qlist
        fxq = interp1d(self.QLIST, self.values[atomgroup.ix], kind='linear')
        return fxq(atomgroup.universe.qlist)

    def set_atoms(self, atomgroup, values):
        # set values for atom
        # we set the ff for QLIST (first is zero) and interpolate for qlist in get
        if values == 'types':
            # use atom types
            for typ in np.unique(atomgroup.types):
                try:
                    self.values[atomgroup.select_atoms('type '+typ).ix] = xrayFFatomic[typ.capitalize()].array[1]
                except KeyError:
                    # this happens e.g. for metals like MG to be recognised as type M -> try the names instead
                    ag = atomgroup.select_atoms('type ' + typ)
                    for a in ag:
                        self.values[a.ix] = xrayFFatomic[a.name.capitalize()].array[1]
        elif isinstance(values, str):
            # set all to same type
            self.values[atomgroup.ix] = xrayFFatomic[values.capitalize()].array[1]
        elif isinstance(values, np.ndarray) and np.shape(values) == self.QLIST.shape:
            # explicit given formfactor
            self.values[atomgroup.ix] = values
        else:
            raise AttributeError('values does not fit allowed XRayFormFactor amplitude input.')

    def get_residues(self, res_group):
        # coherent residue formfactors need to be calculated or taken from saved dict
        qlist = res_group.universe.qlist

        if isinstance(res_group.ix, numbers.Integral):
            try:
                if res_group.universe.explicitResidueFormFactorAmpl:
                    # provoke explicit calculation
                    raise KeyError()
                # get from list, if KeyError it is calculated
                return xrayFFgroup[res_group.resname.upper()].interp(qlist)
            except KeyError:
                # for a single residue
                atoms = res_group.atoms
                utypes = list(np.unique(atoms.types))
                ufax = np.c_[[xrayFFatomic[a.capitalize()][1] for a in utypes]]
                ff = np.c_[self.QLIST, ufax.T].T
                iff = [utypes.index(a)+1 for a in atoms.types]
                fa = [ff[i, 0] for i in iff]
                ff[1:, :] = ff[1:, :]/ff[1:, :1]  # normalize
                # Debye with interpolation
                cog = atoms.posnm.mean(axis=0)
                res = fscatter.cloud.scattering_debye(qlist,
                                                      atoms.posnm - cog,       # positions
                                                      fa,                      # atom fax
                                                      iff,                     # formfactor row sequence
                                                      ff,                      # normalized formfactors
                                                      0)                       # parallel

                # fa are always positive => sign(sum(fa)) is always positive
                val = res[1]**0.5
                return val
        else:
            # for a residue group list
            vals = np.empty((res_group.ix.shape[0], len(qlist)))
            for i, rg in enumerate(res_group):
                vals[i] = rg.fax
        return vals

    def typesScatteringAmplitudeQ0_ag(ag):
        """xray scattering amplitude atom group
        """
        # need to avoid interp in atom.fax for qlist so reconstruct from xrayFFatomicdummy
        values = np.zeros_like(ag.ix, dtype=np.float32)
        for typ in np.unique(ag.types):
            values[ag.types == typ] = xrayFFatomic[typ.capitalize()].array[1, 0]
        return values

    def typesScatteringAmplitudeQ0_r(r):
        """xray scattering amplitude residue
                """
        try:
            if r.universe.explicitResidueFormFactorAmpl:
                raise KeyError()
            return xrayFFgroup[r.resname.upper()].Y[0]
        except KeyError:
            return r.atoms.fax0().sum()

    def typesScatteringAmplitudeQ0_rg(rg):
        """xray scattering amplitude residue group
                """
        return np.r_[[r.fax0() for r in rg]]

    transplants[AtomGroup].append(('fax0', typesScatteringAmplitudeQ0_ag))
    transplants[Residue].append(('fax0', typesScatteringAmplitudeQ0_r))
    transplants[ResidueGroup].append(('fax0', typesScatteringAmplitudeQ0_rg))


class XRayFormFactorDummy(AtomAttr):
    """
    Coherent Xray formfactor amplitude dummy atoms in unit nm

    values contains coherent_scattering_amplitude for global QLIST

    Specific qlist values in get_atoms will be linear interpolated



    """
    attrname = 'faxdumys'
    singular = 'faxdumy'
    dtype=np.float32  # object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]
    QLIST=QLIST
    transplants = defaultdict(list)

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros((n_atoms, QLIST.shape[0]))

    def get_atoms(self, atomgroup):
        # Get values from single atom by interpolation
        fxq = interp1d(self.QLIST, self.values[atomgroup.ix], kind='linear')
        return fxq(atomgroup.universe.qlist)

    def set_atoms(self, atomgroup, values):
        # set values for atoms for all QLSIT
        if values=='types':
            # use atom types
            for typ in np.unique(atomgroup.types):
                try:
                    self.values[atomgroup.select_atoms('type '+typ).ix] = xrayFFatomicdummy[typ.capitalize()].array[1]
                except KeyError:
                    # this happens e.g. for metals like MG recognised as type M -> try the names instead which is MG
                    ag = atomgroup.select_atoms('type ' + typ)
                    for a in ag:
                        self.values[a.ix] = xrayFFatomicdummy[a.name.capitalize()].array[1]

        elif isinstance(values, str):
            # set all to same type
            self.values[atomgroup.ix] = xrayFFatomicdummy[values.capitalize()][1]
        elif isinstance(values, np.ndarray) and np.shape(values) == self.QLIST.shape:
            # explicit given formfactor
            self.values[atomgroup.ix] = values
        else:
            raise AttributeError('values does not fit allowed XRayFormFactor amplitude input.')

    def get_residues(self, res_group):
        # coherent residue formfactors need to be calculated or taken from saved dict
        qlist = res_group.universe.qlist

        if isinstance(res_group.ix, numbers.Integral):
            try:
                if res_group.universe.explicitResidueFormFactorAmpl:
                    # provoke explicit calculation
                    raise KeyError()
                # get from list, if KeyError it is calculated
                return xrayFFgroupdummy[res_group.resname.upper()].interp(qlist)
            except KeyError:
                # for a single residue
                atoms = res_group.atoms
                utypes = list(np.unique(atoms.types))
                ufax = np.c_[[xrayFFatomicdummy[a.capitalize()][1] for a in utypes]]
                ff = np.c_[self.QLIST, ufax.T].T
                iff = [utypes.index(a)+1 for a in atoms.types]
                fa = [ff[i, 0] for i in iff]
                ff[1:, :] = ff[1:, :]/ff[1:, :1]  # normalize
                cog = atoms.posnm.mean(axis=0)
                res = fscatter.cloud.scattering_debye(qlist,
                                                      atoms.posnm - cog,  # positions
                                                      fa,                 # atom faxdumy
                                                      iff,                # type index in ff
                                                      ff,                 # normalized formfactors for each type
                                                      0)                  # parallel
                val = res[1]**0.5
                return val
        else:
            # for a residue group list
            vals = np.empty((res_group.ix.shape[0], len(qlist)))
            for i, rg in enumerate(res_group):
                vals[i] = rg.faxdumy
        return vals

    def typesScatteringAmplitudeQ0_ag(ag):
        """xray scattering amplitude dummy atom group
        """
        # need to avoid interp in atom.faxdumy for qlist so reconstruct from xrayFFatomicdummy
        values = np.zeros_like(ag.ix, dtype=np.float32)
        for typ in np.unique(ag.types):
            values[ag.types == typ] = xrayFFatomicdummy[typ.capitalize()].array[1, 0]
        return values

    def typesScatteringAmplitudeQ0_r(r):
        """xray scattering amplitude dummy residue
        """
        try:
            if r.universe.explicitResidueFormFactorAmpl:
                raise KeyError()
            return xrayFFgroupdummy[r.resname.upper()].Y[0]
        except KeyError:
            return r.atoms.fax0dumy().sum()

    def typesScatteringAmplitudeQ0_rg(rg):
        """xray scattering amplitude dummy residue group
        """
        return np.r_[[r.fax0dumy() for r in rg]]

    transplants[AtomGroup].append(('fax0dumy', typesScatteringAmplitudeQ0_ag))
    transplants[Residue].append(('fax0dumy', typesScatteringAmplitudeQ0_r))
    transplants[ResidueGroup].append(('fax0dumy', typesScatteringAmplitudeQ0_rg))


class incXRayFormFactor(AtomAttr):
    """
    incoherent Xray formfactors = formfactor_amplitude**2 in unit nm²

    incoherent sums as sum(inx**2) different to coherent

    """
    attrname = 'fi2xs'
    singular = 'fi2x'
    dtype=np.float32  # object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]
    QLIST=QLIST

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros((n_atoms, QLIST.shape[0]))

    def get_atoms(self, atomgroup):
        # Get values from single atom
        fxq = interp1d(self.QLIST, self.values[atomgroup.ix], kind='linear')
        return fxq(atomgroup.universe.qlist)

    def set_atoms(self, atomgroup, values):
        # set values for atom
        if values=='types':
            # use atom types
            for typ in np.unique(atomgroup.types):
                try:
                    self.values[atomgroup.select_atoms('type '+typ).ix] = xrayFFatomic[typ.capitalize()][2]
                except KeyError:
                    # this happens e.g. for metals like MG to be recognised as type M -> try the names instead
                    ag = atomgroup.select_atoms('type ' + typ)
                    for a in ag:
                        self.values[a.ix] = xrayFFatomic[a.name.capitalize()].array[1]
        elif isinstance(values, str):
            # set all to same type
            self.values[atomgroup.ix] = xrayFFatomic[values.capitalize()][2]
        elif isinstance(values, np.ndarray) and np.shape(values) == self.QLIST.shape:
            # explicit given formfactor
            self.values[atomgroup.ix] = values
        else:
            raise AttributeError('values does not fit allowed XRayFormFactor amplitude input.')

    def get_residues(self, res_group):
        # coherent residue formfactors need to be calculated or taken from saved dict
        qlist = res_group.universe.qlist

        if isinstance(res_group.ix, numbers.Integral):
            # for a single residue
            atoms = res_group.atoms
            utypes = list(np.unique(atoms.types))
            ufax = np.c_[[xrayFFatomic[a.capitalize()][2] for a in utypes]].sum(axis=0)
            vals = np.interp(qlist, self.QLIST, ufax, ufax[0], ufax[-1])
        else:
            # for a residue group list
            vals = np.empty((res_group.ix.shape[0], len(qlist)))
            for i, rg in enumerate(res_group):
                atoms = rg.atoms
                utypes = list(np.unique(atoms.types))
                ufax = np.c_[[xrayFFatomic[a.capitalize()][2] for a in utypes]].sum(axis=0)
                vals[i] = np.interp(qlist, self.QLIST, ufax, ufax[0], ufax[-1])
        return vals


class nFormFactor(AtomAttr):
    """
    Neutron coherent scattering amplitude in unit nm

    The return value should reflect the deuteration of individual atoms and possible hd exchange

    """
    attrname = 'fans'
    singular = 'fan'
    dtype=np.float32
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]
    QLIST = QLIST
    hcoh, hinc = Nscatlength['h']
    dcoh, dinc = Nscatlength['d']
    transplants = defaultdict(list)

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        return np.zeros(n_atoms)

    def get_atoms(self, atomgroup):
        # for neutrons the scattering length is a constant independent on q
        # return array for all q
        # this is frequently changed during fitting and should be always updated
        # (maybe in the calling function, then return only scalar)
        ql = atomgroup.universe.qlist.shape[0]
        # atomic formfactor for neutrons q independent
        return np.tile(self.values[atomgroup.ix], (ql, 1)).T

    def set_atoms(self, atomgroup, values):
        # here we set the values for atomic neutron scattering amplitudes
        # including deuteration and hd exchange

        # solvent H coh scattering respecting the d2o fraction in solvent
        solventcoh = self.hcoh + atomgroup.universe.d2oFract*(self.dcoh - self.hcoh)

        if values == 'types':
            # set it according to types, for H,D with solvent exchange and deuteration
            for typ in np.unique(atomgroup.types):
                agt = atomgroup.select_atoms('type ' + typ)
                if typ == 'H' or typ=='D':
                    # account for partial deuteration
                    bd = self.hcoh + agt.deuteration * (self.dcoh-self.hcoh)
                    # account for possible HD exchange
                    bdex = bd + agt.hdexchange * (solventcoh - bd)
                    self.values[agt.ix] = bdex
                else:
                    try:
                        # some scattering length are complex, we use only real part
                        self.values[agt.ix] = np.real(Nscatlength[typ.lower()][0])
                    except KeyError:
                        # this happens e.g. for metals like MG to be recognised as type M -> try the names instead
                        for a in agt:
                            self.values[a.ix] = Nscatlength[a.name.lower()][0]
        elif isinstance(values, str):
            # set all same type according to string name
            try:
                self.values[atomgroup.ix] = Nscatlength[values.lower()][0]
            except KeyError:
                raise KeyError('Key should be an element name like C,O,N,...')
        elif isinstance(values, np.ndarray) and (values.shape == atomgroup.ix.shape):
            # set explicit values
            self.values[atomgroup.ix] = values
        else:  # isinstance(values, (int,float)):
            # explicit values
            self.values[atomgroup.ix] = values

    def get_residues(self, res_group):
        # coherent residue formfactors for residue coarse graining
        # these need to be calculated (if all atoms are present)
        # or taken from saved dict with averaged values for e.g CA model

        # the actual needed qlist of the universe
        qlist = res_group.universe.qlist
        # a const normalized formfactor for the atoms, QLIST is reference q list
        ff=np.c_[self.QLIST, np.ones_like(self.QLIST)].T
        if isinstance(res_group.ix, numbers.Integral):
            try:
                if res_group.universe.explicitResidueFormFactorAmpl:
                    # provoke explicit calculation
                    raise KeyError()
                # get from list, if KeyError it is calculated
                return neutronFFgroup[res_group.resname.upper()].interp(qlist)
            except KeyError:
                # for a single residue
                # We use the Debye scattering to calc it for a residue, interpolation for correct q is done in fscatter
                # the sign of fan.sum needs to be recovered as sum(x**2)**0.5 loses contrast information in matching
                atoms = res_group.atoms
                cog = atoms.posnm.mean(axis=0)
                res = fscatter.cloud.scattering_debye(qlist,
                                                      atoms.posnm - cog,      # positions
                                                      self.values[atoms.ix],  # fan for atoms
                                                      [1]*atoms.ix.shape[0],  # all same constant formfactor row 1
                                                      ff,                     # normalized formfactor
                                                      0)                      # ncpu parallel execution

                # formfactor amplitude is root of formfactor
                # this is valid only for small Q
                val = res[1]**0.5 * np.sign(self.values[atoms.ix].sum())
                return val
        else:
            # for a residue group list
            vals = np.empty((len(res_group), len(qlist)))
            for i, rg in enumerate(res_group):
                vals[i] = rg.fan
            return vals

    def set_residues(self, values):
        raise TypeError('Set atom attributes instead of residueAttr.')

    def typesScatteringAmplitudeQ0_ag(ag):
        """neutron scattering amplitude atom group
        """
        # because of constant atomic neutron formfactor we just take first
        return ag.fans[:, 0]

    def typesScatteringAmplitudeQ0_r(r):
        """neutron scattering amplitude residue
        """
        try:
            if r.universe.explicitResidueFormFactorAmpl:
                raise KeyError()
            return neutronFFgroup[r.resname.upper()].Y[0]
        except KeyError:
            return r.atoms.fan0().sum()

    def typesScatteringAmplitudeQ0_rg(rg):
        """neutron scattering amplitude residue group
        """
        return np.r_[[r.fan0() for r in rg]]

    transplants[AtomGroup].append(('fan0', typesScatteringAmplitudeQ0_ag))
    transplants[Residue].append(('fan0', typesScatteringAmplitudeQ0_r))
    transplants[ResidueGroup].append(('fan0', typesScatteringAmplitudeQ0_rg))


class incnFormFactor(AtomAttr):
    """
    Incoherent neutron formfactor amplitude as fomrfactor_amplitude**2 in unit nm²

    The return value should reflect the deuteration of individual atoms and possible hd exchange

    """
    attrname = 'fi2ns'
    singular = 'fi2n'
    dtype = np.float32
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]
    QLIST = QLIST
    hcoh, hinc = Nscatlength['h']
    dcoh, dinc = Nscatlength['d']
    hinc2=hinc**2
    dinc2=dinc**2

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        return np.zeros(n_atoms)

    def get_atoms(self, atomgroup):
        # solvent scattering length density with d2o fraction
        return self.values[atomgroup.ix]

    def set_atoms(self, atomgroup, values):
        # here we set the values for incoherent atomic neutron scattering amplitudes
        if values=='types':
            # set it according to types

            # solvent H coh scattering respecting the d2o fraction in solvent
            solventinc = self.hinc2 + atomgroup.universe.d2oFract*(self.dinc2 - self.hinc2)

            for typ in np.unique(atomgroup.types):
                agt = atomgroup.select_atoms('type ' + typ)
                if typ == 'H' or typ=='D':
                    # account for partial deuteration
                    bi = self.hinc2 + agt.deuteration * (self.dinc2-self.hinc2)
                    # account for possible HD exchange
                    biex = bi + agt.hdexchange * (solventinc - bi)
                    self.values[agt.ix] = biex
                else:
                    try:
                        self.values[agt.ix] = Nscatlength[typ.lower()][1]**2
                    except KeyError:
                        # this happens e.g. for metals like MG to be recognised as type M -> try the names instead
                        for a in agt:
                            self.values[a.ix] = Nscatlength[a.name.lower()][1]**2
        elif isinstance(values, str):
            # set all same type
            self.values[atomgroup.ix] = Nscatlength[values.lower()][1]**2
        elif isinstance(values, np.ndarray) and (values.shape == atomgroup.ix.shape):
            # set explicit values
            self.values[atomgroup.ix] = values
        else:  # isinstance(values, (int,float)):
            # explicit values
            self.values[atomgroup.ix] = values

    def get_residues(self, res_group):
        # incoherent of a residue is sum of incfin**2
        # vals = np.empty(len(res_group))
        if isinstance(res_group.ix, numbers.Integral):
            return self.values[res_group.atoms.ix].sum()
        else:
            return np.array([self.values[rg.atoms.ix].sum() for rg in res_group])


class deuteration(AtomAttr):
    """
    Deuteration level. Only H can be deuterated to D.
    For intermediate levels we use statistical average.
    """
    attrname = 'deuteration'
    singular = 'deuteration'
    dtype=np.float32  # object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros(n_atoms)

    def get_atoms(self, atomgroup):
        # Get values from single atom including exchange with the solvent
        return self.values[atomgroup.ix]

    def set_atoms(self, atomgroup, values):
        assert (0 <= values <= 1), 'deuteration values should be in interval [0..1] !'

        # set values for all in atomgroup
        self.values[atomgroup.ix] = values

        # update neutron coh + incoh only for the relevant H,D
        ag = atomgroup.select_atoms('type H or type D')
        ag.fans = 'types'
        ag.fi2ns = 'types'


class hdexchangable(AtomAttr):
    """
    Deuteration level. Only H can be deuterated to D.
    For intermediate levels we use statistical average.

    set as 3x tuple with exchangeable fraction for ( H bonded to O,S,sidechain N; backbone N-H, histidine -H*)
    default (1, universe.amideHexFract,u.histidinExchange) = (1, 0.9, 0.5)

    """
    attrname = 'hdexchange'
    singular = 'hdexchange'
    dtype=np.float32  # object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros(n_atoms)

    def get_atoms(self, atomgroup):
        # Get values from single atom including exchange with the solvent
        return self.values[atomgroup.ix]

    def set_atoms(self, atomgroup, values):
        if values == 'default':
            # default values for normal conditions
            u = atomgroup.universe
            values = (1, max(min(u.amideHexFract, 1), 0), max(min(u.histidinExchange, 1), 0))
        if isinstance(values, (tuple, set, list)) and np.shape(values) == (3,):
            # explicit given fractions
            u = atomgroup.universe
            if not u.bonds:
                # this may need vdwradii for unknown types
                u.atoms.guess_bonds()
            # backbone H bonded to N exchange to fraction 0.9
            backboneH = atomgroup.select_atoms('type H and bonded type N and bonded backbone')

            # histidin hydrogens can exchange to fraction 0.5
            histidinH = atomgroup.select_atoms('(resname HSD or resname HIS) and type H*')

            # H bonded to 'OSN' show complete exchange
            exchangeableH  = atomgroup.select_atoms('type H and bonded type O')
            exchangeableH += atomgroup.select_atoms('type H and bonded type S')
            exchangeableH += atomgroup.select_atoms('type H and bonded type N and not bonded backbone')

            self.values[exchangeableH.ix] = values[0]
            self.values[backboneH.ix] = values[1]
            self.values[histidinH.ix] = values[2]
        else:
            # allow explicit given values  for groups
            self.values[atomgroup.ix] = values
        atomgroup.fans = 'types'
        atomgroup.fi2ns = 'types'


class positionUnitsnm(AtomAttr):
    """
    Geometric center position in units nm

    """
    attrname = 'posnm'
    singular = 'posnm'
    dtype = object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        return np.zeros(n_atoms)

    @staticmethod
    def get_atoms(atomgroup):
        # Get values from single atom including exchange with the solvent
        if isinstance(atomgroup.ix, numbers.Integral):
            return atomgroup.position / 10
        else:
            return atomgroup.positions / 10

    @staticmethod
    def set_atoms(atomgroup, values):
        if isinstance(atomgroup.ix, numbers.Integral):
            atomgroup.position = values * 10
        else:
            atomgroup.positions = values * 10

    @staticmethod
    def get_residues(res_group):
        # incoherent of a residue is sum of incfin**2
        # vals = np.empty(len(res_group))
        if isinstance(res_group.ix, numbers.Integral):
            return res_group.atoms.posnm.mean(axis=0)
        else:
            posnm = np.zeros((res_group.ix.shape[0], 3))
            posnm[:, :] = [rg.atoms.posnm.mean(axis=0) for rg in res_group]
            return posnm

    @staticmethod
    def get_segments(seg_group):
        # incoherent of a residue is sum of incfin**2
        # vals = np.empty(len(res_group))
        if isinstance(seg_group.ix, numbers.Integral):
            return seg_group.atoms.posnm.mean(axis=0)
        else:
            posnm = np.zeros((seg_group.ix.shape[0], 3))
            posnm[:, :] = [sg.atoms.posnm.mean(axis=0) for sg in seg_group]
            return posnm


class surfacename(AtomStringAttr):
    """
    Is surface atoms indicator

    """
    attrname = 'surface'
    singular = 'surface'
    dtype = object
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.array(['' for _ in range(n_atoms)], dtype=object)

    def get_residues(self, res_group):
        """
        Residue is surface if any atom is in surface

        """
        if isinstance(res_group.ix, numbers.Integral):
            val = self.values[res_group.atoms.ix]
            return np.unique(val[val != ''])[0] if np.any(val != '') else ''
        else:
            return [rg.surface for rg in res_group]


class surfaceData(AtomAttr):
    """
    Surface atoms properties
    [1x surface area, 1x SAS surface volume, 1x hydration shell volume, 3x area mean position]


    """
    attrname = 'surfdata'
    singular = 'surfdata'
    dtype = np.float32
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.zeros((n_atoms, 6))

    def get_atoms(self, ag):
        return self.values[ag.ix, :]

    def set_atoms(self, ag, values):
        if isinstance(values, str) and values == 'default':
            self.values[ag.ix, :] = 0
        else:
            self.values[ag.ix, :] = values

    def get_residues(self, res_group):
        # equivalent
        if isinstance(res_group.ix, numbers.Integral):
            val = self.values[res_group.atoms.ix]
            sd = np.zeros(6)
            sd[:3] = val[:, :3].sum(axis=0)
            sd[3:] = val[:, 3:].mean(axis=0)
            return sd
        else:
            return np.array([rg.surfdata for rg in res_group], dtype=np.float32)


class surfaceLayerDensity(AtomAttr):
    """
    Surface layer density per surface atom relative to bulk solvent, default 1
    [1x surface area, 1x surface volume, 3x area mean position]

    """
    attrname = 'surfdensity'
    singular = 'surfdensity'
    dtype = np.float32
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    @staticmethod
    def _gen_initial_values(n_atoms, n_residues, n_segments):
        # prepare zero shape array for later values
        return np.ones(n_atoms)

    def set_atoms(self, ag, values):
        if isinstance(values, str) and values == 'default':
            self.values[ag.ix] = 1.
        else:
            self.values[ag.ix] = values

    def get_residues(self, res_group):
        if isinstance(res_group.ix, numbers.Integral):
            return self.values[res_group.atoms.ix].mean()
        else:
            return np.array([rg.surfdensity for rg in res_group], dtype=np.float32)


class vanderWaalsRadii(AtomAttr):
    """
    van der Waals radii in units nm.

    """
    attrname = 'vdWradiinm'
    singular = 'vdWradiinm'
    dtype = np.float32
    target_classes = [Atom, Residue, AtomGroup, ResidueGroup]

    def get_residues(self, res_group):
        # equivalent radius for sum of vdW Volumes
        if isinstance(res_group.ix, numbers.Integral):
            return (self.values[res_group.atoms.ix]**3).sum()**(1/3)
        else:
            return np.array([rg.vdWradiinm for rg in res_group], dtype=np.float32)


def getSurfaceVolumePoints(objekt, point_density=5, probe_radius=0.13,
                           surfacename='1', vdwradii=None, shellThickness=0.3):
    r"""
    Calculates the solvent excluded volume (SES/SAS) for contrast calculation in all functions.

    It is **NOT** necessary to call this function.
    getSurfaceVolumePoints is called automatically from all scattering functions and determines the surface
    atoms and the objekt volume.

    Parameters
    ----------
    objekt : atom group
        Atom group.
    point_density : integer, default 5
        Point density on surface of each atom for rolling ball algorithm as n_points = 2**(2*point_density)+2
        On error it is automatically incremented
    probe_radius : float, default 0.13 nm for water
        Probe radius for SAS/SES calculation.
    shellThickness : float
        Shell thickness of the surface layer. The default is 0.3.
    surfacename : str
        Name for surface selection
    vdwradii : dict, default None
        Dictionary of van der Waals radii for rolling ball algorithm in units nm.
         - If None the vdW radii used in the object universe are used. See notes below.
         - I a defaultdict only these values are used. This is used e.g. for Calpha or coarse grain models
           to use only the given defaults like `vdwradii = defaultdict(lambda :0.38)` .

    Returns
    -------
        None

        Universe topology attributes *surface* and *surfdata* are populated
         - per surface atom with .surfdata = [surface area, SASvolume, shellVolume, surfmean position]
         - adds to objekt.universe .SASVolume volume SAS
         - adds to objekt.universe .SESVolume volume SES
         - surface area can be calculated universe.select_atoms('surface 1').surfdata[:,0].sum()
         - SASVolume is universe.select_atoms('surface 1').surfdata[:,1].sum()
         - dummy bead positions in surface layer universe.select_atoms('surface 1').surfdata[:,3:]


    Notes
    -----
    **SES/SAS** see `Accessible surface area <https://en.wikipedia.org/wiki/Accessible_surface_area>`_

    **SAS** area/volume (solvent-accessible surface) is the surface area of a  molecule that is accessible to a solvent
    center. SAS area is calculated by sasa.aVSPointsGradients.

    SAS area is here calculated using the *rolling ball* algorithm developed by Shrake & Rupley [1]_.
    It describes the surface of the center of a probe molecule (ball) with probe_radius
    rolling over the van der Waals surface.
    We use a probe_radius of 0.13 nm that represents the radius of a water molecule.

    **SES** area/volume (solvent excluded surface) is defined by the envelope excluding the volume occupied
    by the rolling ball probe. Also called Connolly surface [5]_ .

    **Method**

    - Shrake/Rupley rolling ball algorithm:
      For each atom a regular angular grid of :math:`N_{SAS}` points builds a surface S in a distance
      :math:`d=R_{vdW} +R_{probe}` of the atomic vdWaals surface. :math:`R_{probe}` represents the solvent size.
      The points in S are tested for overlap with the same surface of other neighboring atoms.
      The set of non overlapping points build the SAS surface enclosing the SAS volume of the atom group.
      The SAS points have a distance :math:`R_{probe}` from the van der Waals surface of the atoms.

    - The SESVolume as a kind of dry volume is :math:`V_{SES} = V_{SAS} - V_{surface layer}`.
      The surface layer volume :math:`V_{surface layer}` for each atom `i` may be estimated as the
      volume between previous determined SAS points `p` and the van der Waals surface with volume per SAS point
      :math:`V_{p,i} = 4/3\pi ((R_{vdW,i}+R_{probe})^3 - R_{vdW,i}^3) / N_{SAS}`.

      In each corner (touching atoms) the probe surface sphere describes a smooth surface not reaching into the corner.
      This missing volume can be approximated using the rolling ball algorithm with same
      number of points :math:`N_{SAS}` but reduced probe radius :math:`R_{probe}/2`.
      Each additional appearing point not in the original SAS surface contributes a volume
      :math:`V_{p,c} = 4/3\pi (R_{probe})^3 / N_{SAS}` as sector from the probe center located in the SAS corner.
      Also buried atoms (between non-touching atoms which are not in the SAS surface) contribute with the same amount.
      It should be mentioned that this is an approximation for the corner probe sphere volume
      as the points distributed around the original atoms show a small deviation compared to atoms distributed around
      probe spheres located in the corner. On the other hand most algorithms describe only an approximation.

      .. figure:: ../../examples/images/rollingball.png
        :align: center
        :width: 50 %
        :alt: rollingball

        red: atoms, green: probe, solid line: SAS, dashed: SES, dots: probe R/2 points,
        blue: additional layer volume corner with additional points and probe section per point

    A comparison to experimental determined protein densities is shown in :ref:`Protein density determination`.
    For a probe radius of 1.3 A we find excellent agreement. 1.3 A corresponds to the reduced oxygen vdW radius
    for proper protein density determination.

    As vdWaals radii we use for the atoms C, N, O the observed radii according to Fraser at al [2]_.
    For H we use 1.09 A according to the revised value of Rowland et al. [3]_.
    For other values we use vdWaals radii of Bondi et al. [4]_ which are rare for proteins.

    For the determination of the **hydration layer** contributing to the neutron/X-ray scattering
    usually a 0.3 nm hydration layer is assumed as e.g. in CRYSON/CRYSOL.
    To determine the respective hydration layer volume we use the same approach as above with
    the shellthickness parameter. By default, we use a thickness of 0.3 nm for the hydration layer
    if no other value is given.


    References
    ----------
    .. [1] Environment and exposure to solvent of protein atoms. Lysozyme and insulin
           Shrake, A; Rupley, JA. (1973). J Mol Biol. 79 (2): 351–71. doi:10.1016/0022-2836(73)90011-9.
    .. [2] An improved method for calculating the contribution of solvent to the X-ray diffraction pattern
           of biological molecules.
           Fraser, R. D. B., MacRae, T. P., & Suzuki, E. (1978).
           Journal of Applied Crystallography, 11(6), 693–694. https://doi.org/10.1107/S0021889878014296
    .. [3] Intermolecular Nonbonded Contact Distances in Organic Crystal Structures:
           Comparison with Distances Expected from van der Waals Radii.
           R. Scott Rowland, Robin Taylor
           The Journal of Physical Chemistry. Bd. 100, Nr. 18, 1996, S. 7384–7391, doi:10.1021/jp953141
    .. [4] van der Waals Volumes and Radii.
           A. Bondi
           The Journal of Physical Chemistry. Bd. 68, Nr. 3, 1964, S. 441–451, doi:10.1021/j100785a001
    .. [5] Analytical molecular surface calculation
           Connolly, M. L.
           J. Appl. Crystallogr. 16, 548–558 (1983). doi:10.1107/S0021889883010985.

    """

    if len(objekt.atoms) == 0:
        raise ValueError('no atoms in objekt found')

    objekt.universe.surfdata = 'default'
    objekt.universe.surface = ''
    if vdwradii is None:
        vdwradii = objekt.universe.vdWradiinm

    while True:
        if point_density>20:
            break
        try:
            # aVSPointsGradients returns (area, volume, sPAG), sPAG as dictionary with
            # surface atom:  [atom SAS exposed surface area,
            #                 list of points in the atom exposed surface,
            #                 gradient vector pointing outward from the atom]
            area, volume, sPAGpr = sasa.aVSPointsGradients(objekt, probe_radius,
                                                           point_density=point_density, vdwradii=vdwradii)
            # same but with smaller probe to get the corner additional points
            _, _, sPAG0 = sasa.aVSPointsGradients(objekt, probe_radius / 2.,
                                                            point_density=point_density, vdwradii=vdwradii)
            # same but with larger probe to get the corner seen from the shell
            _, _, sPAG2 = sasa.aVSPointsGradients(objekt, shellThickness,
                                                            point_density=point_density, vdwradii=vdwradii)

        except ZeroDivisionError:
            # increment number of points as sometimes there is an error with no points on surface for an atom
            point_density+=1
            print('incremented point_density to %i' %(2**(2*point_density) + 2))
        else:
            break

    # now add surface points of smaller surface to surface atoms
    # sPAG will be list of surface atoms with
    #       [points in surface , exposed surface area, gradient vector pointing outward,
    #        number of points in smaller and larger surface if present]
    sPAG = {satom: ((sPAGpr[satom][1], sPAGpr[satom][0], sPAGpr[satom][2]) if satom in sPAGpr else (None, 0, 0)) +
                   (len(sPAG0[satom][1]), len(sPAG2[satom][1]) if satom in sPAG2 else None) for satom in sPAG0}

    allSASlayerVolume = 0
    pointsonsphere = 2 ** (2 * point_density) + 2
    for atom, surf in sPAG.items():
        if surf[0] is None:
            # buried atoms in innermost surface contributing to r/2 but not to r; needed for SESVolume
            allSASlayerVolume += 4/3.*pi * probe_radius**3 * surf[3] / pointsonsphere
            continue

        # mean vector of surface points with length atom.vdW_radius+probe_radius is in the surface
        # center in surface
        v = (surf[0] - atom.posnm).mean(axis=0)
        # R is vdWradius + probe_radius and sync to vdW used in aVSPointsGradients
        R = la.norm(surf[0][0]-atom.posnm)
        normv = la.norm(v)
        if normv > 0:
            surfmean = atom.posnm + R * v/normv
        else:
            # it happens that 2 points on opposite site are found and norm(v) is nan
            # then we take just the first
            v = surf[0][0]-atom.posnm
            R = la.norm(surf[0][0]-atom.posnm)
            surfmean = atom.posnm + R * v/la.norm(v)

        # respective layer volume per point
        pointShellVolume = 4/3*pi* ((R - probe_radius + shellThickness)**3 - (R - probe_radius)**3) / pointsonsphere
        pointSASVolume = 4/3* pi * (R**3 - (R - probe_radius)**3) / pointsonsphere

        # difference in sphere volumes x fraction of points
        # SAS layer add overlap
        SASlayervolume = pointSASVolume * len(surf[0])  # full points
        # in corners the point difference approximates a probe sphere reaching into the corner
        SASlayervolume += 4/3.*pi * probe_radius**3 * (surf[3]-len(surf[0])) / pointsonsphere

        # same for hydration shell with shellThickness
        # the result is not much dependent on accuracy of these calculations
        # the more important  part is SES calculation
        # a second option would be to add SASlayervolume and use  pointShellVolume only outside SAS
        # The corner volume needs to be weighted half in this case
        if surf[4] is not None:
            shellVolume = pointShellVolume * surf[4]  # full points
            shellVolume += 4/3.*pi * shellThickness**3 * (len(surf[0])-surf[4]) / pointsonsphere
        else:
            # no full points
            shellVolume = 4/3.*pi * shellThickness**3 * len(surf[0]) / pointsonsphere

        # surface data = [surf area, SASlayervolume, shellVolume, surfmean]
        atom.surfdata = np.r_[surf[1], SASlayervolume, shellVolume, surfmean]
        atom.surface = surfacename
        allSASlayerVolume += SASlayervolume

    objekt.universe.SASVolume = volume
    objekt.universe.SESVolume = volume - allSASlayerVolume
    objekt.universe.SASArea = area

    return


def getNativeContacts(objekt, overlap=0.01, vdwradii=None):
    """
    Creates a native contact residue dict for a given object for Go-like protein modeling.

    A residue j is added as contact to residue i if any atom van der Waals radii overlap
     :math:`R_i^{vdW} + R_j^{wdW}-overlap < distance(i,j)`

    objekt :
        group of atoms
    overlap :
        Overlap of van der Waals radii to be counted as in contact in units nm.
    vdwradii : dictionary
        Van der Waals radii to use in units nm.

    Returns
    -------
        dict with {residue : list of residue in contact }
    or
        list of index pairs for bonds

    Examples
    --------
    ::

     import jscatter as js
     from collections import defaultdict

     # all atom universe with hydrogens
     uni=js.bio.scatteringUniverse('3pgk')
     u = uni.select_atoms("protein")
     NN1 = js.bio.getNativeContacts(u)

     # CA atom group
     u = uni.select_atoms("protein and name CA")
     # use a larger van der Waals radius for CA only with 3.8A as distance between CA along backbone
     NN2 = js.bio.getNativeContacts(u, vdwradii=defaultdict(lambda: 3.8, {'C':3.8}))



    References
    ----------
    .. [1] Prediction of hydrodynamic and other solution properties of partially
           disordered proteins with a simple, coarse-grained model.
           Amorós, D., Ortega, A., & De La Torre, J. G. (2013).
           Journal of Chemical Theory and Computation, 9(3), 1678–1685. https://doi.org/10.1021/ct300948u
    .. [2] Selection of Optimal Variants of Gō-Like Models of Proteins through Studies of Stretching
           Joanna I. Sułkowska Marek Cieplak
           Biophysical Journal 95,3174-3191 (2008) https://doi.org/10.1529/biophysj.107.127233

    """
    if vdwradii is None:
        # a default for proteins in nm
        vdwradii = data.vdwradii

    atoms = objekt.atoms

    # create atom data with position
    atom_data = [None] * len(atoms)
    for i, a in enumerate(atoms):
        pos1 = a.posnm
        atom_data[i] = (pos1[0], pos1[1], pos1[2], vdwradii[a.type.capitalize()])

    # index and d2 of neighbours
    nborslist = sasa.NeighborList(atoms, np.max(list(vdwradii.values())), atom_data)

    # a dictionary with items: atom : [neighbor atoms]
    nativecontacts ={}

    for i, atom in enumerate(atoms):
        ipos = atom_data[i]
        iresidue=atom.residue
        iwdWrad = ipos[3]
        nbors=nborslist[i]
        for j, d2 in nbors:
            atomj=atoms[j]
            jpos=atom_data[j]
            jwdWrad = jpos[3]
            if (iwdWrad+jwdWrad-overlap)**2 > d2:
                jresidue=atomj.residue
                if iresidue == jresidue:
                    continue
                if not iresidue in nativecontacts:
                    nativecontacts[iresidue] = []
                if jresidue not in nativecontacts[iresidue]:
                    nativecontacts[iresidue].append(jresidue)
                # print(iwdWrad, jwdWrad, d2**0.5, iresidue, jresidue)

    return nativecontacts


def getDistanceMatrix(objekt, cutoff=1):
    """
    Distance matrix for atoms in objekt.

    objekt migth be a selection to get e.g. distances between CA or H atoms

    Parameters
    ----------
    objekt : AtomGroup or residueGroup
        Objekt to get distance matrix.
    cutoff : float
        Cutoff radius. For larger distances 0 is returned.

    Returns
    -------
        Distance matrix NxN (upper triagonal) in units nm.

    Notes
    -----
    For larger matrices a faster neighbor search is used.

    Examples
    --------
    ::

     import jscatter as js

     uni=js.bio.scatteringUniverse('3pgk')
     u = uni.select_atoms("protein and type H")
     dd = js.bio.getDistanceMatrix(u)

     u = uni.select_atoms("protein and name CA")
     dd = js.bio.getDistanceMatrix(u,cutoff=2)


    """
    atoms = objekt.atoms

    if atoms.n_atoms < 3000:
        # faster for small number
        x = atoms.posnm
        ix, iy = np.triu_indices(atoms.n_atoms, k=1)
        distances = np.zeros((atoms.n_atoms,)*2)
        distances[ix, iy] = la.norm(x[ix, :3]-x[iy, :3], axis=1)
        distances[distances > cutoff] = 0
        return distances
    else:
        # create atom data with position
        atom_data = [None] * len(atoms)
        for i, a in enumerate(atoms):
            pos1 = a.posnm
            atom_data[i] = (pos1[0], pos1[1], pos1[2])

        # index and d2 of neighbours
        nborslist = sasa.NeighborList(atoms, cutoff/2, atom_data)
        # fill the matrix
        distances = np.zeros((atoms.n_atoms,)*2, dtype=np.float32)
        for i in range(len(nborslist)):
            nb = nborslist[i]
            for j, d in nb:
                distances[i, j] = d**0.5

        return distances


def assignTypes(pairs):
    """
    Assign unknown atom type values from known atom name.

    Some coordinate formats use non-chemical symbols, which need to be assigned some real atom types.
    We do this here to real atom types. If someone wants different things the new names can be added manually.

    Parameters
    ----------
    pairs : dict
        Dictionary of {'unknownname': 'existingname'} like {'mw': 'C'}

    Notes
    -----
    Adds corresponding dict entries to neutronFFgroup, xrayFFatomic, xrayFFatomicdummy, xrayFFgroupdummy, xrayFFgroup.

    For custom entries add new {key:values} pairs to the above dictionaries.


    """
    if isinstance(pairs, tuple):
        pairs = [pairs]

    for new, exists in pairs.items():
        for FF in [xrayFFatomic, xrayFFatomicdummy]:
            FF[new.capitalize()] = FF[exists.capitalize()]
        Nscatlength[new.lower()] = Nscatlength[exists.lower()]
        data.vdwradii[new.capitalize()] = data.vdwradii[exists.capitalize()]


def addNXAttributes(universe, vdwradiiA={}):
    """
    Add topology attributes as needed for Xray/neutron scattering to existing universe.

    Uses default values for a protein in D2O. See scatteringUniverse for details.

    Parameters
    ----------
    universe : MDAnalysis universe
        Universe
    vdwradiiA : dict, default data.vdWradii
        Dictionary of van der Waals radii to use.

    Returns
    -------
        None

    """
    # get universe
    u = universe

    u.temperature = 293.15
    u.solvent = ['1D2O1', '0H2O1']  # default D2O
    u.solventDensity = formel.waterdensity(u.solvent, T=u.temperature)
    u.qlist = np.r_[0.01, 0.1, 1.0, 2.]  # units 1/nm
    u.tlist = 10**np.r_[0:6]  # units ps
    u.error = 200
    u.amideHexFract = 0.9
    u.histidinExchange = 0.5

    # water radius
    u.probe_radius = 0.13  # unit nm
    u.shellThickness = 0.3  # nm
    u.calphaCoarseGrainRadius = 0.342  # unit nm
    u.iscalphamodel = False

    # register scattering length and other new properties needed for Xray and neutron scattering
    u.add_TopologyAttr("fax")
    u.add_TopologyAttr("faxdumys")
    u.add_TopologyAttr("fan")
    u.add_TopologyAttr("fi2ns")
    u.add_TopologyAttr("fi2xs")
    u.add_TopologyAttr("deuteration")
    u.add_TopologyAttr("hdexchange")
    u.add_TopologyAttr("posnm")
    u.add_TopologyAttr("surface")
    u.add_TopologyAttr("surfdata")
    u.add_TopologyAttr("surfdensity")
    u.vdWradiiA = vdwradiiA
    u.vdWradiinm = {k.capitalize(): v/10 for k, v in vdwradiiA.items()}
    vdwr = np.zeros_like(u.atoms)
    for t in list(set(u.atoms.types)):
        ag = u.select_atoms('type ' + t)
        vdwr[ag.ix] = u.vdWradiinm[t.capitalize()]
        # np.r_[[data.vdwradii[a.type.capitalize()] for a in u.atoms]]
    u.add_TopologyAttr('vdWradiinm', vdwr)

    if not u.bonds:
        # guess_bonds needs all atoms with vdW radii
        u.atoms.guess_bonds()

    # set default values for scattering length densities
    # u.atoms.deuteration = 0  # this is already the initial value
    u.atoms.hdexchange = 'default'
    if False:
        # in above hdexchange the following two lines are already called, we dont do it twice
        # these incorporate hdexchange and deuteration
        u.atoms.fans = 'types'
        u.atoms.fi2ns = 'types'
    u.atoms.faxs = 'types'
    u.atoms.fi2xs = 'types'
    u.atoms.faxdumys = 'types'
    u.atoms.surfdensity = 'default'

    # force explicit residue ff calculation
    u.explicitResidueFormFactorAmpl = False

    return


class scatteringUniverse(MDAnalysis.Universe):

    def __init__(self, *args, **kwargs):
        r"""
        Create MDAnalysis universe for neutron/Xray scattering.

        scatteringUniverse returns a MDAnalysis universe with
        `MDAnalysis <https://docs.mdanalysis.org/stable/index.html>`_ methods
        complemented by scattering specific attributes as atomic formfactors and methods.
        Parameters describe additional scattering parameters. Others are passed to MDAnalysis.universe.
        Atom type needs to be defined for all atoms. See Notes.

        Parameters
        ----------
        args : pdb structure file, universe or trajectories
            PDB files, PDB ID or path to trajectories to build the universe as described for MDAnalysis.universe.
            See `MDAnalysis <https://userguide.mdanalysis.org/stable/universe.html>`_ for different formats.
            Already existing local files are prefered.
        biounit : bool, default False
            If biounit is True or above args is a PDB biounit/assembly1 with ending *.pdb[biounit]*
            as e.g. ``.pdb1`` the biounit is downloaded, merged and used for the universe.
            See :py:func:`~mergePDBModel`.
        addHydrogen : bool, default True
            Add hydrogen to atomic coordinates for PDB files.

            - False: do not add hydrogens.
                If the pdb file contains hydrogens or contains only Cα atoms
                (e.g. using a different program) set to False.
            - True:
             - By default :py:func:`~pdb2pqr` is used to add hydrogen in a fast mode
               without debumping and position optimization, see :py:func:`~fastpdb2pqr`.
               The resulting ``_h.pdb`` file is used that contains also ligands.

               The '_h.pqr' file also contains charge information but no ligands by default.
               This file can be used to populate the charge attribute in a second universe and
               adding the ligands from the first universe using MERGE (but no ligand charge).
               For more complicated cases see pdb2pqr documentation.
             - For other formats as e.g. trajectories this option is ignored as these should contain hydrogens.
             - If PyMol is installed, it can be used to add hydrogens, addHydrogen='pymol'.
               Pymol is maybe bit faster and add hydrogens also to ligands.
               No charges are added.
        solvent : string or list of string default ['1D2O1','0H2O1']
            Description of solvent saved in attribut uni.solvent.
            :py:func:`~jscatter.formel.scatteringLengthDensityCalc` is used to calc solvent scattering length.

            A chemical formula with fraction+[lettercode+number]+.....
             - eg 'D2O1' or 'H2O1' for water and heavy water
             - ['0.6D2O1','0.4H2O1'] for a mixture of 0.6 hwater and 0.4 water
             - ['6D2O1','4H2O1']     for a mixture of 0.6 hwater and 0.4 water
             - default is h2o/d2o solvent according to setUnivProp
        solventDensity : float
            Density of the solvent for above calculation saved in attribute uni.solventDensity.
        surfdensity : float, optional
           Surface layer density relative to bulk solvent for later surface atoms.
            - 1, None : no layer included.
            - ≠ 1 :  lower or higher density
        refreshVolume : bool
            Refresh volume calculation (SES and SAS volume).
        point_density : int, default 5
            Point density on surface (per atom) for SES and SAS calculation as
            :math:`n_{points} = 2^{2 point_density}+2` . See :py:func:`~.bio.mda.getSurfaceVolumePoints` .
        vdwradii : dict
            Atomic van der Waals radii (units A) passed to universe are used to identify bonds between atoms using the
            universe.guess_bonds method and to calculate SES and SAS volume.
            Bonds between atoms are created, if the two atoms are within
            :math:`d < f \cdot (R_1 + R_2)` of each other, where :math:`R_{1,2}` are the VdW radii
            of the atoms and :math:`f` is an ad-hoc *fudge_factor*. This is the same algorithm that VMD uses.

            The default is for protein atoms  ``{'H': 1.09, 'C': 1.58, 'N': 0.84, 'O': 1.3, 'S': 1.68, 'P': 1.11}``
            These values are smaller than the vdW radii from Bondi but result in a correct SESVolume and scattering
            intensity. See :py:func:`~.bio.mda.getSurfaceVolumePoints`  .
        assignTypes : dict
            Assign unknown atom type values from known atom names if these are non-standard.

            Some coordinate formats use non-chemical symbols, which need to be assigned some real atom types.
            We do this here to real atom types. If someone wants different things the new names can be added manually.
            E.g. ``{'mw': 'O'}`` for unknown mw set to oxygen.

            For custom setting see :py:func:`jsatter.bio.mda.assignTypes`.

            We set according values for xrayFFatomic, xrayFFatomicdummy, Nscatlength, vdwradii.

        Notes
        -----
        **Biological unit**

        Use a biological unit for calculation. The PDB crystal structure is not always the biological unit
        in special for multimeric proteins.
        The biological assembly can be retrieved from PDB servers as eg https://www.ebi.ac.uk/pdbe/ .
        Look for biological unit or assembly. Check the structure in a PDB viewer as Pymol or VMD.

        If existent the biological unit can be downloaded with *.pdb1* or *.pdb2* file ending,
        see :py:func:`~.bio.mda.fetch_pdb`. The biological unit can then be merged into one model using
        see :py:func:`~.bio.mda.mergePDBModel`.

        The scattering universe has **additional attributes for scattering** of atoms/residues.
        All atoms need a defined type to be used as scattering amplitude.

        **Universe attributes to adjust** :

        - solvent : solvent see above Parameters section.
        - qlist : scattering vectors in unit 1/nm.
        - tlist : times in units *ps* for dynamics.
        - error : Determines how to calculate spherical averages (number of Fibonacci points on sphere).
        - amideHexFract : exchangable fraction of backbone amide -NH hydrogens

          - 0.9 for folded proteins
          - For intrinsically unfolded proteins this might be higher due to improved access to the backbone.
            (see hdexchange to change)

        - histidinExchange : exchangeable fraction histidine hydrogens (0.5) (see hdexchange to change)
        - temperature : temperature in K
        - probe_radius : radius of the probe for surface determination in the rolling ball algorithm,
          The default is 0.13 [nm] for water. This reduced value (often 0.14 nm) corresponds to the reduced
          vdwradii of oxygen that reproduces SESVolume and results in the best protein density determination.
        - shellThickness : hydration shell thickness as a surface layer thickness. Default is 0.3 nm.
        - solventDensity : from js.formel.waterdensity(u.solvent, T=u.temperature)
        - calphaCoarseGrainRadius : 0.342 [nm] vdwradii for Cα only structures for coarse grained calculations.
          The value gives an average good approximation for the protein densities.
        - iscalphamodel : False
        - explicitResidueFormFactorAmpl :

          - If ``True`` (default) the residue formfactor amplitude (fan/fax) is calculated
            explicit for each residue instead of using precalculated average values.
          - Precalculated residue formfactors are stored in the dict ``js.mda.xrayFFgroup`` and
            ``js.bio.neutronFFgroup``.
          - Additional residue or monomer types can be added to the dict
            for coarse grained calculations e.g. of polymer bead models. In this case  set
            ``explicitResidueFormFactorAmpl=False``

        **Atom attributes** can be changed for each atom. Predefined values are ok for most folded proteins.
        These attributes can be set for individual atoms or for groups like

        ``urn.select_atoms('resname HIS and type H').deuteration =1``.

        - deuteration : atomic deuteration, effective only for H atoms.
          Fractional values are interpreted as statistical deuteration e.g. of half the atoms in an ensemble.

          For residue calculation use with ``uni.explicitResidueFormFactorAmpl = True`` to get updated
          residue formfactors accordingly.

        - hdexchange:
          Fraction of hydrogens that exchange with solvent hydrogens .
          The default is for folded proteins, Intrinsically folded may be different e.g. for the backbone N-H.

          Set as  ``.hdexchange = (a,b,c)`` with
            - a : H bonded to O,S,sidechain N ; default 1, all exchange
            - b : backbone N-H : default uni.amideHexFract = 0.9
            - c : histidine -H : default u.histidinExchange = 0.5
            A single float sets a=b=c and keyword 'default' sets to universe defaults.

        - surfdensity : scattering length density relative to bulk for surface atoms.
           - Typically between 1.00 to 1.18 for proteins.
           - If equal 1 no surface is assumed.

        Example how to set for individual atoms/residues
        E.g. set according to residue type or residue numbers ::

            import jscatter as js
            uni = js.bio.scatteringUniverse('3CLN')
            uni.select_atoms('resname ARG HIS LYS ASP GLU').atoms.surfdensity = 1.1
            protein = uni.select_atoms('protein')

            # scatIntUniv uses prepScatGroups which uses getSurfaceVolumePoints to determine the surface
            Sx = js.bio.scatIntUniv(protein ,mode='xray')
            print('Mean universe atoms ', uni.atoms.surfdensity.mean())
            print('Mean in surface atoms', protein.select_atoms('surface 1').surfdensity.mean())

            # hydrophobicity scale [-4.5..4.5] dependent on residue type
            md = 0.09  # maximum density in layer 9% different from bulk
            for k, v in js.data.aaHydrophobicity.items():
                uni.select_atoms('resname '+k.upper()).atoms.surfdensity = 1 + md * v[0]/4.5
            print('Mean universe atoms ', uni.atoms.surfdensity.mean())
            print('Mean in surface atoms', protein.select_atoms('surface 1').surfdensity.mean())

            # set higher exchange for backbone NH in a segment (migth be unfolded at the surface)
            protein.select_atoms('resnum 33:44').atoms.hdexchange = (1, 0.7, 0.5)

            # use a partial deuteration of a small domain or even individual H atoms.
            # maybe partial deuteration is possible in the future
            protein.select_atoms('resnum 33:44').atoms.deuteration = 1
            # deuteration of 2 amino acids types
            protein.select_atoms('resname ARG LYS').atoms.deuteration = 1

        **Fixed attributes**

        Set according to other attributes or atom type for all atoms (residue values as appropriate averages)

        (singular/plural):

        - fax/faxs : atomic/residue xray formfactor amplitude, unit nm

          - atomic xray formfactor amplitudes according to REZ et al.[2]_.
          - residue formfactor amplitudes for coarse grained calculation
            are calculated using the Debye scattering equation with atomic formfactors :math:`f_j(Q)`
            and positions :math:`r_j` according to Yang et al. [4]_ if atoms are present:

            .. math:: F_a^{residue}(Q) = \big\langle \sum_{j.k} f_j(Q)f_k(Q)
                                \frac{sin(Q(r_j-r_k))}{Q(r_j-r_k)} \big\rangle^\frac{1}{2}

            This is obviously only valid for small scattering vectors where we can
            neglect the atomic details and interferences in a residue.
          - Precalculated amino acid residue formfactors are stored in the dict ``js.mda.xrayFFgroup`` and
            ``js.bio.neutronFFgroup``.
            Adding new ones for e.g. polymer monomers ::

             monomerfa = js.ff.sphere(q=np.r_[0:10:200j], radius=1.2)
             monomerfa.Y = (monomer.Y/monomer.I0)**0.5 * V**2 * x_contrast**2  # valid only for small q
             js.mda.xrayFFgroup['ETH'] = monomerfa

             # naming the specific residues to use the new defined formfactor
             # leads to automatic usage of the new formfactor amplitude.
             # use select mechanism of MDAnalysis to be specific
             uni.residues.resnames = 'ETH'

             # set corresponding incoherent if needed (just as example for C2H4 monomer)
             # here we assume one Cα atom per residue/monomer in coarse graining.
             uni.residues.atoms.fi2xs = js.data.xrayFFatomic['C'][2]*2 + js.data.xrayFFatomic['H'][2] * 4

        - faxdumy/faxdumys : Xray/neutron formfactor amplitude of dummy solvent atoms unit nm

          - Dummy atoms are represented by a Gaussian formfactor amplitude according to Fraser et al
            [5]_ as also implemented in CRYSOL

            .. math:: f_i(Q) = v_i\rho_s e^{-\pi v_i^{2/3} Q^2}

            with Gaussian spheres of volume :math:`v_i` equal to the van der Waals volume
            and solvent scattering length density :math:`\rho_s`.

        - fan/fans : atomic/residue neutron formfactor amplitude unit nm

          - atomic neutron formfactor amplitudes which are Q independent with a scattering length according to [1]_
            taken from https://www.ncnr.nist.gov/resources/n-lengths/list.html
          - residue scattering is calculated as for fax based on atomic scattering amplitudes..
        - fi2n/fi2ns : neutron incoherent scattering amplitude squared, unit nm². Same source as fan.
        - fi2x/fi2xs : xray incoherent scattering amplitude squared according to [3]_ (compton scattering), unit nm².
        - posnm : atom/residue center of geometry positions in unit nm. MDAnalysis uses Å in .position.
                  posnm is for convenience to get 1/nm wavevectors.
        - surface : name of surface, to test if atoms belong to surface atoms. (Maybe later different surfaces)
        - surfdata : surface atom data as [surface area, surface volume, shell volume, 3x surface area mean position]
        - vdWradiinm : vdWradii in nm as defined in js.data.vdwradii

        Set **default values** dependent on *.solvent* using
        `js.formel.scatteringLengthDensityCalc(u.solvent, u.solventDensity, T=u.temperature)`

        - xsld : solvent xray scattering length density, unit 1/nm²=nm/nm³
        - edensity : solvent electron density, unit e/nm³
        - bcDensitySol : solvent neutron scattering length density, unit 1/nm²=nm/nm³
        - b2_incSol : solvent neutron incoherent scattering length density squared, unit 1/nm=nm²/nm³
        - d2oFract : solvent d/h fraction


        Examples
        --------
        Some examples to show how to create a universe and calc the scattering and differences due to mode.
        The example shows the validity of residue coarse graining up to around 3/nm.
        With coarse graining in cubes (cubesize) the approximation seems best.
        This might be useful to speed up computations that take long (e.g.ISF at low Q)

        There is basically no difference between precalculated and averaged residue formfactors and explicit calculated
        residue formfactors for each residue (uni.explicitResidueFormFactorAmpl = True)
        The explicit ones include better deuteration of specific atoms.

        Cα models loose some precision in volume respectivly in forward scattering.
        C-alpha models need a .calphaCoarseGrainRadius = 0.342 nm because of the missing atoms.
        In addition, the mean residue position is not the C-alpha position.
        We use 0.342 nm as a good average to get same forward scattering over a bunch of proteins
        (see example_bio_proteinCoarseGrainRadius.py).
        ::

         import jscatter as js

         # first get and create the biological unit ('.pdb1') of alcohol dehydrogenase (tetramer, 144 kDa)
         adh = js.bio.fetch_pdb('4w6z.pdb1')
         # the 2 dimers in are in model 1 and 2 and need to be merged into one.
         adhmerged = js.bio.mergePDBModel(adh)

         # Ribonuclease A and Phosphoglycerate kinase are monomers and can be used without modifications.
         # 3pgk has a Mg atom that is misinterpreted (as M), to use it we add this
         vdwradii ={'M':js.data.vdwradii['Mg']*10}  # in A

         p = js.grace(1,1.4)
         p.multi(3,2,vgap=0,hgap=0)
         for c, pdbid in enumerate(['3rn3', '3pgk', adhmerged]):
             # load from pdb id, scatteringUniverse adds hydrogens automatically
             uni = js.bio.scatteringUniverse(pdbid, vdwradii=vdwradii)
             uni.qlist = js.loglist(0.1, 9.9, 200)
             u = uni.select_atoms("protein")
             ur = u.residues

             S = js.bio.nscatIntUniv(u)
             Sx = js.bio.xscatIntUniv(u)

             # use an averaging in cubes filled with the atoms, cubesize approximates residue size
             Scu = js.bio.nscatIntUniv(u, cubesize=0.6)
             Sxcu = js.bio.xscatIntUniv(u, cubesize=0.6)

             # use now the precalculated fomfactors on residue level coarse graining
             uni.explicitResidueFormFactorAmpl = False  # default
             Sr = js.bio.nscatIntUniv(ur)
             Sxr = js.bio.xscatIntUniv(ur)

             # calc residue fomfactors explicit (not precalculated)
             # useful for changes of residue deuteration or backbone N-H exchange of IDP
             uni.explicitResidueFormFactorAmpl = True
             Ser = js.bio.nscatIntUniv(ur)
             Sxer = js.bio.xscatIntUniv(ur)

             # create a C-alpha pdb file and then the Ca-only universe for calculation
             ca = uni.select_atoms('name CA')
             ca.write('pdb_ca.pdb')
             # addHydrogen=False prevents addition of 4H per C atom
             unica = js.bio.scatteringUniverse('pdb_ca.pdb', addHydrogen=False)
             unica.qlist = js.loglist(0.1, 10, 200)
             uca = unica.residues
             Sca = js.bio.nscatIntUniv(uca)
             Sxca = js.bio.xscatIntUniv(uca)

             p[2*c].plot(S, li=[1, 2, 1], sy=0, le='atomic')
             p[2*c].plot(Scu, li=[1, 2, 5], sy=0, le='atomic in cubes')
             p[2*c].plot(Sr, li=[1, 2, 2], sy=0, le='res pre')
             p[2*c].plot(Ser, li=[3, 2, 3], sy=0, le='res ex')
             p[2*c].plot(Sca, li=[1, 2, 4], sy=0, le='Ca model')
             p[2*c].legend(x=1, y=8e-3,charsize=0.8)
             p[2*c].text(x=0.15, y=1e-7,charsize=1,string=pdbid)

             p[2*c+1].plot(Sx, li=[1, 2, 1], sy=0, le='atomic')
             p[2*c+1].plot(Sxcu, li=[1, 2, 5], sy=0, le='atomic in cubes')
             p[2*c+1].plot(Sxr, li=[1, 2, 2], sy=0, le='res pre')
             p[2*c+1].plot(Sxer, li=[3, 2, 3], sy=0, le='res ex')
             p[2*c+1].plot(Sxca, li=[1, 2, 4], sy=0, le='Ca model')
             p[2*c+1].legend(x=1, y=8e-3,charsize=0.8)
             p[2*c+1].text(x=0.15, y=1e-7,charsize=1,string=pdbid)

             p[2*c].xaxis(label='', ticklabel=False, scale='log', min=1e-1, max=9.9)
             p[2*c+1].xaxis(label='', ticklabel=False, scale='log', min=1e-1, max=9.9)
             p[2*c].yaxis(label='F(Q)',ticklabel='power',scale='log', min=3e-8,max=8e-3)
             p[2*c+1].yaxis(ticklabel=False, scale='log', min=3e-8,max=8e-3)

         p[2*c].xaxis(label='Q / nm\S-1', scale='log', min=1e-1, max=9.9)
         p[2*c+1].xaxis(label='Q / nm\S-1', scale='log', min=1e-1, max=9.9)
         p[0].subtitle('neutron scattering')
         p[1].subtitle('Xray scattering')
         p[0].title(' '*30 + 'Comparison of formfactors with different resolution')
         #p.save(js.examples.imagepath+'/uniformfactors.jpg', size=(700/300, 1000/300))

        .. image:: ../../examples/images/uniformfactors.jpg
         :align: center
         :width: 50 %
         :alt: uniformfactors


        References
        ----------
        .. [1] Neutron scattering lengths and cross-sections
               V. F. Sears
               Neutron News, 3, 26-37 (1992) https://doi.org/10.1080/10448639208218
        .. [2] REZ et al.Acta Cryst.  A50, 481-497 (1994)
        .. [3] A new analytic approximation to atomic incoherent X-ray scattering intensities.
               J. THAKKAR and DOUGLAS C. CHAPMAN
               Acta Cryst. (1975). A31, 391
        .. [4] A Rapid Coarse Residue-Based Computational Method for X-Ray Solution Scattering
               Characterization of Protein Folds and Multiple Conformational States of Large Protein Complexes
               S. Yang, S. Park, L. Makowski, B. Roux
               Biophysical Journal 96, 4449–4463 (2009) doi: 10.1016/j.bpj.2009.03.036
        .. [5] An improved method for calculating the contribution of solvent
               to the X-ray diffraction pattern of biological molecules
               R. D. B. Fraser, T. P. MacRae and E. Suzuki
               J. Appl. Cryst. (1978). 11, 693-694  https://doi.org/10.1107/S0021889878014296

        """

        addHydrogen = kwargs.pop('addHydrogen', True)
        guess_bonds = kwargs.pop('guess_bonds', True)
        ph = kwargs.pop('ph', None)
        # add all vdW radii (in A) as defaults
        vdwradiiA = {k.upper(): v * 10 for k, v in data.vdwradii.items()}
        # add capitalized two letters
        vdwradiiA.update({k.capitalize(): v for k, v in vdwradiiA.items() if len(k)>1})
        vdwradiiA.update(kwargs.pop('vdwradii', {}))
        biounit = kwargs.pop('biounit', False)
        assig_Types = kwargs.pop('assignTypes', {})

        if assig_Types:
            assignTypes(assig_Types)

        # create universe, postphone bonds to end to have more control
        kwargs.update({'guess_bonds': False, 'vdwradii': vdwradiiA})

        if isinstance(args[0], str):
            # creating scattering universe from a file or PDB ID that will be downloaded and hydrogens added

            if os.path.exists(args[0]):
                # prefer existing files
                pass
            elif os.path.splitext(args[0])[1] in ['', '.pdb1', '.pdb2'] and \
                     re.match('^[0-9][a-z0-9]{3}$', os.path.splitext(args[0])[0].lower()):
                # download pdb id and requested biounit; pdb1,pdb2 is biounit, '' only PDB id
                if os.path.splitext(args[0])[1] in ['.pdb1', '.pdb2'] or biounit:
                    arg0 = fetch_pdb(id=args[0], biounit=True)
                    arg0 = mergePDBModel(arg0)
                else:
                    arg0 = fetch_pdb(id=args[0])
                args = (arg0,) + args[1:]

            if addHydrogen and (os.path.splitext(args[0])[1] == '.pdb' and isinstance(args[0], (str, os.PathLike))):
                if pymol2 and addHydrogen == 'pymol':
                    pdb_h = addH_Pymol(args[0])
                    print('Use PyMol to add hydrogens.')
                    args = (pdb_h,) + args[1:]
                else:
                    # add hydrogens using pdb2pqr and missing atoms
                    debump = kwargs.pop('debump', False)
                    opt = kwargs.pop('opt', False)
                    pqr_h, pdb_h = fastpdb2pqr(args[0], debump=debump, opt=opt, ph=ph)
                    print('Use pdb2pqr to add hydrogens.')
                    args = (pdb_h,) + args[1:]
                # except ValueError:
                #     Warning('No hydrogens added, maybe not an atomic structure but coarse grained as CA model?')

            # init universe with updated args
            super(scatteringUniverse, self).__init__(*args, **kwargs)

        elif isinstance(args[0], MDAnalysis.Universe):
            # create universe with topology from input
            # TODO we may need to add more to get the full input
            super(scatteringUniverse, self).__init__(args[0]._topology.copy(), addHydrogen=False, guess_bonds=False)
            self.trajectory = args[0].trajectory.copy()

        else:
            raise TypeError('Cannot create universe from input arguments')

        # try to add types (==elements)
        # e.g. psf fiels might contain numbers as types, but we need types for scattering
        # later we might add types from masses or something like
        try:
            # test if types are present otherwise determine from names
            if not set(self.atoms.types).issubset(vdwradiiA.keys()):
                self.atoms.types = guess_types(self.atoms.names)

        except AttributeError:
            # there was no type atribute, so we add types (im not sure if this is not always present)
            atomtypes = guess_types(self.atoms.names)
            self.add_TopologyAttr(Atomtypes(atomtypes, guessed=True))

        except MDAnalysis.exceptions.NoDataError:
            # was not initialised so we do it now
            self.atoms.types = guess_types(self.atoms.names)

        # now guess bonds with our vdw radii
        if guess_bonds:
            self.atoms.guess_bonds(vdwradiiA)

        # now add all Attributes for N+X scattering
        # prepare all needed scattering attributes
        addNXAttributes(self, vdwradiiA)

    def _updateattributes(self):
        # some attributes depend on solvent and get updated on access
        xsld, edensity, nsld, incsld, mass, massfullprotonated, massfulldeuterated, dhfraction = \
                formel.scatteringLengthDensityCalc(self.solvent, self.solventDensity, T=self.temperature, mode='a')
        self._bcDensitySol = nsld
        self._b2_incSol = incsld
        self._d2oFract = dhfraction
        self._xsldSolvent = xsld
        self._edensitySolvent = edensity

    @property
    def bcDensitySol(self):
        """
        Coherent neutron scattering length density solvent.

        """
        self._updateattributes()
        return self._bcDensitySol

    @property
    def b2_incSol(self):
        """
        Incoherent neutron scattering length density solvent.

        """
        self._updateattributes()
        return self._b2_incSol

    @property
    def d2oFract(self):
        """
        D2O fraction in solvent.
        """
        self._updateattributes()
        return self._d2oFract

    @property
    def xsldSolvent(self):
        """X-ray scattering length of solvent."""
        self._updateattributes()
        return self._xsldSolvent

    @property
    def edensitySolvent(self):
        """Electron density solvent in e/nm³"""
        self._updateattributes()
        return self._edensitySolvent

    def copy(self):
        """Return an independent copy of this Universe"""
        new = self.__class__(self._topology.copy(), addHydrogen=False, guess_bonds=False)
        new.trajectory = self.trajectory.copy()
        return new

    def view(self, select='all', frames=None, viewer=''):
        """
        View the actual configuration in a selected viewer.

        Parameters
        ----------
        select : string, default = 'all'
            Selection string as in select_atoms.
        frames : array-like or slice or FrameIteratorBase or str, optional
            An ensemble of frames to write. The ensemble can be a list or
            array of frame indices, a mask of booleans, an instance of
            :class:`slice`, or the value returned when a trajectory is indexed.
            By default, `frames` is set to ``None`` and only the current frame
            is written. If `frames` is set to "all", then all the frame from
            trajectory are written.
        viewer : 'pymol', 'vmd', 'chimera', full path
            Viewer to show pdb structure.
             - If the programm is in the PATH the short name is enough.
             - The full path can be specified
             - Empty string selects the standard program to open '.pdb' files.


        Examples
        --------
        ::

         import jscatter as js

         uni = js.bio.scatteringUniverse('3RN3.pdb')
         uni.view(select='protein')


        """
        with tempfile.TemporaryDirectory() as tdir:
            try:
                name = os.path.basename(self.filename)
            except TypeError:
                name = 'universetempfile'
            name = os.path.splitext(name)[0] + '.pdb'
            tfile = os.path.join(tdir, name)
            if viewer:
                viewerpath = shutil.which(viewer)
                if not viewerpath:
                    raise FileNotFoundError(f'The executable {viewer} is not found in PATH.')
                self.select_atoms(select).write(tfile, frames=frames)
                view_process = subprocess.run([viewerpath, tfile])
            else:
                # try default open dependent on system
                # TODO xdg-open fails on linux for chimera with file not found
                self.select_atoms(select).write(tfile, frames=frames)
                if sys.platform.startswith('linux'):
                    view_process = subprocess.run(['xdg-open', tfile])
                elif sys.platform.startswith('darwin'):
                    view_process = subprocess.run(['open', tfile])
                elif sys.platform == 'win32':
                    os.startfile(tfile)

        return


def fetch_pdb(id, path='./', biounit=False):
    """
    Fetch id from pdb databank at http://www.rcsb.org/

    id : string
        PDB id
        4 letter code of protein structure
    path : string
        path where to store the file
    biounit : bool, int
        Download biounit/assembly1 with ending *.pdb[biounit]* as e.g. *.pdb1*.

    Returns
    -------
    Saves gunziped file and returns corresponding path.

    Notes
    -----
    Biounit/assembly can be downloaded using file ending  *.pdb1* or *.pdb2*


    """
    ids = id.split('.')

    end = ''
    assembly = ''
    if len(ids)>1 and ids[1][-1] in ['1', '2', '3']:
        end = ids[1][-1]
        assembly = '_' + end
    elif isinstance(biounit, bool):
        if biounit:
            end = '1'
            assembly = '_' + end
    elif isinstance(biounit, int):
        end = str(biounit)
        assembly = '_' + end

    outfile = path + f'{ids[0]}{assembly}.pdb'

    url = f'http://www.rcsb.org/pdb/files/{ids[0]}.pdb{end}.gz'

    print('Try to download > ', url)
    print('save as ', outfile)
    try:
        with urllib.request.urlopen(url) as zfile:
            with gzip.GzipFile(fileobj=io.BytesIO(zfile.read())) as uncompressed:
                content = uncompressed.read()
        with open(outfile, 'wb') as f:
            f.write(content)
    except Exception as e:
        print(e)
        return 0
    return outfile


def mergePDBModel(pdb):
    """
    Merge models in PDB structure from biological assembly to single model.

    Biological units are saved as multi model PDB files. mergePDBmodel merges these multiple models
    into one model that can be read by MDAnalysis or other programs as multimeric protein.

    Parameters
    ----------
    pdb : string,filename
        PDB id or filename with models to merge.

    Returns
    -------
        merged filename

    Examples
    --------
    Fetch ferritin (24-mer) 1lb3 biological assembly and merge to one frame.
    The example needs some time
    ::

     import jscatter as js
     fer = js.bio.fetch_pdb('1lb3',biounit=True)
     merged_filename = js.bio.mergePDBModel(fer)

     # to show it
     uni = js.bio.scatteringUniverse(merged_filename, addHydrogen=False)
     uni.view(viewer='pymol')

    """
    u = MDAnalysis.Universe(pdb)
    segid = u.segments.segids
    models = []
    if u.trajectory.n_frames <=1:
        raise TypeError('Only a single model is in pdb.')
    for ts in range(u.trajectory.n_frames):
        u.trajectory[ts]
        models.append(u.copy())
        segid = [chr(ord(id) + len(np.unique(segid)) ) for id in segid]
        models[-1].segments.segids = np.array(segid, dtype=object)

    mergeduniverse = MDAnalysis.core.universe.Merge(*[m.atoms for m in models])
    pdb, end = os.path.splitext(pdb)
    new = pdb + '_merged' + end
    mergeduniverse.atoms.write(new)
    return new


def _getargs(input_pdb, output, *args, **kwargs):
    # transform args,kwargs tor arg for pdb2pqr as list of strings
    argdefault = ['nodebump', 'noopt']
    for default in argdefault:
        if default not in args:
            args = args + (default,)
    arg = [input_pdb, output] + ['--' + a.replace('_', '-') for a in args]
    if 'log-level' not in kwargs:
        kwargs.update({'log-level':'ERROR'})
    for k,v in kwargs.items():
        arg = arg + ['--' + k.replace('_', '-'), v]
    return arg


def pdb2pqr(input_pdb, output, *args, **kwargs):
    """
    Adds hydrogens to pdb structure, optional determines charges and repairs missing atoms.

    Interface to pdb2pqr in interactive shell. Original source is at [1]_, [2]_, Please cite [3]_,[4]_.
    From original documentation at [2]_ :

     Adding a limited number of missing heavy (non-hydrogen) atoms to biomolecular structures.
     Estimating titration states and protonating biomolecules in a manner consistent with favorable
     hydrogen bonding. Assigning charge and radius parameters from a variety of force fields.
     Generating “PQR” output compatible with several popular computational modeling and analysis packages.

    Parameters
    ----------
    input_pdb : string
        Path to input pdb file. If only the pdb ID the corresponding file is downloaded.
    output : string
        Path of output file.
    args : strings
        Positional arguments are prepended by --xxx to represent options without input parameter

        If '-' is in key exchange it by underscore '_'.
    kwargs : pairs key=value
        Keyword arguments for options with input value.
        passed as '--key value '

        If '-' is in key exchange it by underscore '_'.


    Notes
    -----
    The PDB2PQR tool prepares structures for further calculations (by APBS) by reconstructing
    missing atoms, **adding hydrogens**, assigning atomic charges and radii from specified
    force fields, and generating PQR files.
    `APBS <http://www.poissonboltzmann.org/>`_ solves the equations of continuum electrostatics for
    large biomolecular assemblies.

    Several programs use a modified PDB format called PQR, in which atomic partial charge (Q)
    and radius (R) fields follow the X,Y,Z coordinate fields in ATOM and HETATM records.

    See `PDB2PQR Server <http://nbcr-222.ucsd.edu/pdb2pqr_2.1.1/>`_
    or `PDB2PQR Homepage <http://www.poissonboltzmann.org/pdb2pqr/>`_

    There are other programs that allow addition of hydrogens:

    - `CHARMM GUI <http://www.charmm-gui.org/?doc=input/pdbreader>`_ provides a web-based graphical
      user interface to generate various molecular simulation systems and input files.
      The output of *Input Generator/PDB Reader* in the file *step1_pdbreader.pdb* contains hydrogen atoms.

    - PSFGEN is a tool (included in **VMD** or `NAMD <https://www.ks.uiuc.edu/Research/namd/>`_ )
      to generate a protein structure file (PSF) for MD Simulations from a PDB structure. It can be used from
      `VMD <https://www.ks.uiuc.edu/Research/vmd/>`_ using the *Automatic PSF Builder*
      or on the `command line <https://www.ks.uiuc.edu/Research/vmd/plugins/psfgen/>`_.

    - HAAD
      https://zhanglab.ccmb.med.umich.edu/HAAD/
      https://doi.org/10.1371/journal.pone.0006701



    **Original help from pdb2pqr30** ::

     PDB2PQR v3.1.0+15.g41d841a.dirty: biomolecular structure conversion software.

        positional arguments:
          input_path            Input PDB path or ID (to be retrieved from RCSB database
          output_pqr            Output PQR path

        optional arguments:
          -h, --help            show this help message and exit
          --log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}
                                Logging level (default: INFO)

        Mandatory options:
          One of the following options must be used

          --ff {AMBER,CHARMM,PARSE,TYL06,PEOEPB,SWANSON}
                                The forcefield to use. (default: PARSE)
          --userff USERFF       The user-created forcefield file to use. Requires --usernames and overrides --ff (default: None)
          --clean               Do no optimization, atom addition, or parameter assignment, just return the original PDB file in aligned format. Overrides
                                --ff and --userff (default: False)

        General options:
          --nodebump            Do not perform the debumping operation (default: True)
          --noopt               Do not perform hydrogen optimization (default: True)
          --keep-chain          Keep the chain ID in the output PQR file (default: False)
          --assign-only         Only assign charges and radii - do not add atoms, debump, or optimize. (default: False)
          --ffout {AMBER,CHARMM,PARSE,TYL06,PEOEPB,SWANSON}
                                Instead of using the standard canonical naming scheme for residue and atom names, use the names from the given forcefield
                                (default: None)
          --usernames USERNAMES
                                The user-created names file to use. Required if using --userff (default: None)
          --apbs-input APBS_INPUT
                                Create a template APBS input file based on the generated PQR file at the specified location. (default: None)
          --pdb-output PDB_OUTPUT
                                Create a PDB file based on input. This will be missing charges and radii (default: None)
          --ligand LIGAND       Calculate the parameters for the specified MOL2-format ligand at the path specified by this option. (default: None)
          --whitespace          Insert whitespaces between atom name and residue name, between x and y, and between y and z. (default: False)
          --neutraln            Make the N-terminus of a protein neutral (default is charged). Requires PARSE force field. (default: False)
          --neutralc            Make the C-terminus of a protein neutral (default is charged). Requires PARSE force field. (default: False)
          --drop-water          Drop waters before processing biomolecule. (default: False)
          --include-header      Include pdb header in pqr file. WARNING: The resulting PQR file will not work with APBS versions prior to 1.5 (default: False)

        pKa options:
          Options for titration calculations

          --titration-state-method {propka}
                                Method used to calculate titration states. If a titration state method is selected, titratable residue charge states will be
                                set by the pH value supplied by --with_ph (default: None)
          --with-ph PH          pH values to use when applying the results of the selected pH calculation method. (default: 7.0)

        PROPKA invocation options:
          -f FILENAMES, --file FILENAMES
                                read data from <filename>, i.e. <filename> is added to arguments (default: [])
          -r REFERENCE, --reference REFERENCE
                                setting which reference to use for stability calculations [neutral/low-pH] (default: neutral)
          -c CHAINS, --chain CHAINS
                                creating the protein with only a specified chain. Specify " " for chains without ID [all] (default: None)
          -i TITRATE_ONLY, --titrate_only TITRATE_ONLY
                                Treat only the specified residues as titratable. Value should be a comma-separated list of "chain:resnum" values; for example:
                                -i "A:10,A:11" (default: None)
          -t THERMOPHILES, --thermophile THERMOPHILES
                                defining a thermophile filename; usually used in 'alignment-mutations' (default: None)
          -a ALIGNMENT, --alignment ALIGNMENT
                                alignment file connecting <filename> and <thermophile> [<thermophile>.pir] (default: None)
          -m MUTATIONS, --mutation MUTATIONS
                                specifying mutation labels which is used to modify <filename> according to, e.g. N25R/N181D (default: None)
          --version             show program's version number and exit
          -p PARAMETERS, --parameters PARAMETERS
                                set the parameter file [{default:s}] (default: /home/biehl/local/lib/python3.9/site-packages/propka/propka.cfg)
          -o PH, --pH PH        setting pH-value used in e.g. stability calculations [7.0] (default: 7.0)
          -w WINDOW WINDOW WINDOW, --window WINDOW WINDOW WINDOW
                                setting the pH-window to show e.g. stability profiles [0.0, 14.0, 1.0] (default: (0.0, 14.0, 1.0))
          -g GRID GRID GRID, --grid GRID GRID GRID
                                setting the pH-grid to calculate e.g. stability related properties [0.0, 14.0, 0.1] (default: (0.0, 14.0, 0.1))
          --mutator MUTATOR     setting approach for mutating <filename> [alignment/scwrl/jackal] (default: None)
          --mutator-option MUTATOR_OPTIONS
                                setting property for mutator [e.g. type="side-chain"] (default: None)
          -d, --display-coupled-residues
                                Displays alternative pKa values due to coupling of titratable groups (default: False)
          -l, --reuse-ligand-mol2-files
                                Reuses the ligand mol2 files allowing the user to alter ligand bond orders (default: False)
          -k, --keep-protons    Keep protons in input file (default: False)
          -q, --quiet           suppress non-warning messages (default: None)
          --protonate-all       Protonate all atoms (will not influence pKa calculation) (default: False)


    References
    ----------
    .. [1] https://pdb2pqr.readthedocs.io/en/latest/
    .. [2] https://github.com/Electrostatics/electrostatics.github.io
    .. [3] Improvements to the APBS biomolecular solvation software suite.
           Jurrus E, et al.
           Protein Sci 27 112-128 (2018).
    .. [4] PDB2PQR: expanding and upgrading automated preparation of biomolecular structures for molecular simulations.
           Dolinsky TJ, et al.
           Nucleic Acids Res 35 W522-W525 (2007).

    """
    arglist = _getargs(input_pdb, output, *args, **kwargs)
    parser = build_main_parser()
    p2q_args = parser.parse_args(arglist)
    main_driver(p2q_args)


def fastpdb2pqr(input_pdb, debump=False, opt=False, drop_water=True, ph=None, whitespace=True):
    """
    A fast version of :py:func:`~.bio.mda.pdb2pqr`.

    Speedup is achieved by omitting optimization, debumping, minimized logging and reducing options.
    For full options use pdb2pqr.

    Parameters
    ----------
    input_pdb : str
        Input pdb file.
    debump : bool, default False
        Debump added atoms, ensure that new atoms are not rebuilt too close to existing atoms.
    opt : bool, default False
        Perform hydrogen optimization, default is not to do it,
        Adjusts hydrogen positions and flips certain side chains (His, Asn, Glu)
        as needed to optimize hydrogen bonds.
    drop_water : bool
        Drop water atoms.
    ph : float, default None
        pH value to use for assignment of charges.
        If None pH 7 is assumed but PROPKA is not used.
        Cite [5]_ [6]_ if using charge assignments by PROPKA.

    whitespace : bool
        Insert whitespaces between atom name and residue name, between x and y, and between y and z.
        This improves readability but breaks PDB file definition.

    Returns
    -------
        input_pdb.pqr, input_pdb_h.pdb (without previous suffix)

    Notes
    -----
    Uses default options of pdb2pqr except of these.
     - debump = False
     - opt = False
     - drop_water = True ; this reduces just te number of atoms not to get errors in mda
     - whitespace; mda has problems as somewhere split() is used instead of char numbers as defined for pqr files
     - pdb_output = input_pdb with prefix appended '_h'

    Examples
    --------
    Use fastpdb2pqr and combine the '_h.pdb' file including ligands but without charges with the '_h.pqr file'
    that cotains charges but no ligands.

    To get charge states of ligands please use the web services or programs mentioned in :py:func:`pdb2pqr` .

    Charges can be added manually for the ligands.
    ::

     import jscatter as js
     import MDAnalysis as mda

     # this adds hydrogens to uni with ligands  and adds charges in the corresponding '.pqr' file
     uligand = js.bio.scatteringUniverse('3pgk')
     uligand.add_TopologyAttr('charges')  # all charges are zero
     ucharge = js.bio.scatteringUniverse('3pgk_h.pqr')
     protein = ucharge.select_atoms('protein').atoms
     for l,c in zip(uligand.select_atoms('protein').residues, ucharge.select_atoms('protein').residues):
         try:
             # this throws an error if len(charges) is different; in that way same residues get correct charge
             l.atoms.charges =c.atoms.charges
         except:
             print('---',l.resnum,c.resnum)

     uligand.atoms.charges.sum()  # = -1

    References
    ----------
    .. [1] https://pdb2pqr.readthedocs.io/en/latest/
    .. [2] https://github.com/Electrostatics/electrostatics.github.io
    .. [3] Improvements to the APBS biomolecular solvation software suite.
           Jurrus E, et al.
           Protein Sci 27 112-128 (2018).
    .. [4] PDB2PQR: expanding and upgrading automated preparation of biomolecular structures for molecular simulations.
           Dolinsky TJ, et al.
           Nucleic Acids Res 35 W522-W525 (2007).
    .. [5] Improved Treatment of Ligands and Coupling Effects in Empirical Calculation and Rationalization of pKa Values
           Sondergaard, Chresten R., Mats HM Olsson, Michal Rostkowski, and Jan H. Jensen.
           Journal of Chemical Theory and Computation 7, (2011): 2284-2295.
    .. [6] PROPKA3: consistent treatment of internal and surface residues in empirical pKa predictions.
           Olsson, Mats HM, Chresten R. Sondergaard, Michal Rostkowski, and Jan H. Jensen.
           Journal of Chemical Theory and Computation 7, no. 2 (2011): 525-537.
    """
    # define fast arguments for adding H
    output_pqr = os.path.splitext(input_pdb)[0] + '_h.pqr'
    output_pdb = os.path.splitext(input_pdb)[0] + '_h.pdb'
    if ph:
        arglist = _getargs(input_pdb, output_pqr, with_ph=f'{ph:.1f}', titration_state_method='propka')
    else:
        arglist = _getargs(input_pdb, output_pqr)
    parser = build_main_parser()
    args = parser.parse_args(arglist)

    # set some args to get fast result
    args.debump = debump
    args.opt = opt
    args.assign_only = False
    args.clean = False
    args.userff = None
    args.ffout = None
    args.neutraln = False
    args.neutralc = False
    args.ligand = None
    args.keep_chain = True
    args.drop_water = drop_water
    args.whitespace = whitespace
    args.pdb_output = output_pdb

    definition = pdb2pqr_io.get_definitions()
    pdblist, is_cif = pdb2pqr_io.get_molecule(input_pdb)
    if args.drop_water:
        pdblist = pdb2pqr_drop_water(pdblist)

    biomolecule, definition, ligand = pdb2pqr_setup_molecule(pdblist, definition, args.ligand)
    biomolecule.set_termini(args.neutraln, args.neutralc)
    biomolecule.update_bonds()

    # do the magic
    results = pdb2pqr_non_trivial(args=args,
                                        biomolecule=biomolecule,
                                        ligand=ligand,
                                        definition=definition,
                                        is_cif=is_cif)
    # write output
    print('write ', output_pqr)
    pdb2pqr_print_pqr(args=args,
                          pqr_lines=results["lines"],
                          header_lines=results["header"],
                          missing_lines=results["missed_residues"],
                          is_cif=is_cif)
    print('write ', output_pdb)
    pdb_lines = pdb2pqr_io.print_biomolecule_atoms(biomolecule.atoms, chainflag=args.keep_chain, pdbfile=True)
    pdb2pqr_print_pdb(args=args,
                        pdb_lines=pdb_lines,
                        header_lines=results["header"],
                        missing_lines=results["missed_residues"],
                        is_cif=is_cif)

    return output_pqr, output_pdb


def addH_Pymol(pdbid):
    """
    Add hydrogens to pdb file using pymol if present.

    Parameters
    ----------
    pdbid : string
        PDB id or filename of PDB file

    Returns
    -------
        Filename of saved file.

    Notes
    -----
    From https://pymolwiki.org/index.php/H_Add ::

     PyMOL fills missing valences but does no optimization of hydroxyl rotamers.
     Also, many crystal structures have bogus or arbitrary ASN/GLN/HIS orientations.
     Getting the proper amide rotamers and imidazole tautomers & protonation states
     assigned is a nontrivial computational chemistry project involving
     electrostatic potential calculations and a combinatorial search.
     There's also the issue of solvent & counter-ions present in systems like
     aspartyl proteases with adjacent carboxylates .

    For higher accuracy (optimization) use :py:func:`~jscatter.bio.mda.pdb2pqr` .

    """

    # TODO simplify this ?
    if pymol2:
        p1 = pymol2.PyMOL()
        p1.start()
        if os.path.isfile(pdbid):
            pdb = pdbid
            p1.cmd.load(pdb)
            pdb, end = os.path.splitext(pdb)
        else:
            pdb = os.path.splitext(pdbid)[0].lower()
            p1.cmd.fetch(pdb)
            end = '.pdb'

        # remove alternate conformations
        # TODO select alternate location
        p1.cmd.remove('not alt ""+A')
        p1.cmd.alter('all', 'alt=""')
        p1.cmd.h_add()
        # save it
        p1.cmd.save(pdb+'_h'+end)
        p1.stop()
        return pdb+'_h'+end
    else:
        raise ModuleNotFoundError('pymol not installed. Use pdb2pqr.')

