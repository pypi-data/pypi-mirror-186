#
# Copyright 2000 by Peter McCluskey (pcm@rahul.net).
# You may do anything you want with it, provided this notice is kept intact.
#
# Changed to python 3 compatibility and usage of MdAnalysis Ralf Biehl 2021
# You may do anything you want with it, provided this notice is kept intact.

"""
_surface_atoms(atoms, solvent_radius = 0., point_density = 258, ret_fmt = 0)

point_density must be 2**(2*N) + 2, where N > 1 (258 and 1026 seem best).
Returns a dictionary with an item for each input atom.
These choices for ret_fmt specify what the dictionary will hold for each atom:
 1: area
 2: (area, volume)
 3: (area, volume, points)
 4: (area, volume, points, dir_tuple)

 points is a list of 3-tuples describing coordinates of points on a
solvent-accessible surface (zero to point_density points per atom).

 dir_tuple is a 3-tuple giving crude estimate of the direction which is
locally "up", i.e. normal to the surface. It is calculated by comparing
the atom's position with the average position of an atom's accessible surface
points.

 The algorithm used is based on the method described in this paper:
 Eisenhaber, Frank, et al. "The Double Cubic Lattice Method: Efficient
Approaches to Numerical Integration of Surface Area and Volume and to
Dot Surface Contouring of Molecular Assemblies", Journal of Computational
Chemistry, Vol. 16, pp 273-284 (1995).
 I have taken a few shortcuts which probably make it a bit less accurate
than what the paper describes (in particular, I used a simple tesselation
algorithm without fully understanding the one described in the paper).

"""

import sys
import math
import numpy as np
from collections import defaultdict

from .. import formel

try:
    from ..libs import surface
    useC=True
except:
    print('use python in SASAsurface.py')
    useC = False


"""
Surface related functions

"""


def aVSPointsGradients(objekt, probe_radius=0.13, point_density=4, vdwradii=None):
    """
    Calcs the solvent accessible surface by the rolling ball algorithm.

    Parameters
    ----------
    objekt :
        Object with atoms. Atoms need method .type or .name to get key in vdwradii (capital letters like 'C')
    probe_radius : float
        Distance from the vdW-radii of the atoms at which the surface is computed.
    point_density : int
        Density of points that describe the surface.
        The point density is finally 2**(2*point_density)+2 => (4 -> 258; 5 -> 1026)
    vdwradii : dict, default None
        Dictionary of {element symbol : van der Waals radii in nm}
        as {'C': 0.17,'H': 0.12,'N': 0.155,'O': 0.152,'S':0.18}

    Returns
    -------
        [total surface area, total surface layer volume, surface atom dict]
        The surface atom dict maps surface atoms to a tuple containing three surface-related quantities per surface atom:
         - SAS exposed surface area
         - list of points in the exposed surface
         - gradient vector pointing outward from the surface.

    """
    atoms = objekt.atoms
    smap = _surface_atoms(atoms,
                          probe_radius,
                          ret_fmt=4,
                          point_density=2 ** (2 * point_density) + 2,
                          vdwradii=vdwradii)
    surface_data = {}
    tot_a = 0
    tot_v = 0
    for a in atoms:
        (area, volume, points1, grad) = smap[a]
        if area > 0.:
            # we have a surface atom
            surface_data[a] = (area, points1, grad)
            tot_a = tot_a + area
            tot_v = tot_v + volume
    return tot_a, tot_v, surface_data


def _get_atom_data(atoms, solvent_radius, vdwradii):
    """
    Returns tuple with max vdW radii, atom_data, geometric center.

    Parameters
    ----------
    atoms : atom objects
        atoms with positionattribut. For mda use posnm as position in nm
    vdwradii : vdW radii in units nm
    solvent_radius : in units nm

    Returns
    -------

    """
    atom_data = [None] * len(atoms)
    maxvdWrad = 0
    sumx = 0
    sumy = 0
    sumz = 0
    for i, a in enumerate(atoms):
        try:
            vdw = vdwradii[a.type.capitalize()]
        except KeyError:
            vdw = vdwradii[a.name.capitalize()]
        pos1 = a.posnm  # conversion to nm from mda in A
        atom_data[i] = (pos1[0], pos1[1], pos1[2], vdw + solvent_radius)
        sumx = sumx + atom_data[i][0]
        sumy = sumy + atom_data[i][1]
        sumz = sumz + atom_data[i][2]
        maxvdWrad = max(maxvdWrad, atom_data[i][3])

    return maxvdWrad, atom_data, (sumx/len(atoms), sumy/len(atoms), sumz/len(atoms))


def _surface_atoms(atoms, solvent_radius=0., point_density=258, ret_fmt=0, vdwradii=None):

    # maxrad and atom_data[:,3] include +solvent_radius
    (maxrad, atom_data, cent) = _get_atom_data(atoms, solvent_radius, vdwradii)

    if not useC:
        # only needed for python in _atom_surf; do it here once
        tess1 = formel.rphitheta2xyz(formel.fibonacciLatticePointsOnSphere(point_density))
    else: tess1 = None

    # create neighbor list for fast search
    nbors = NeighborList(atoms,  maxrad + solvent_radius, atom_data)

    # create list of surface points for each surface atom
    surf_points = {}
    for i in range(len(atoms)):
        a1 = atoms[i]
        pos1 = atom_data[i]
        tot_rad = pos1[3]
        (points1, points_unit) = _atom_surf(nbors, i, atom_data, pos1, tot_rad, point_density, tess1, ret_fmt >= 2)
        surf_points[a1] = _xlate_results(points1, points_unit, point_density, tot_rad, pos1, ret_fmt, cent)

    return surf_points


def _atom_surf(nbors, i, atom_data, pos1, tot_rad, point_density, tess1, ret_unit_points=1):
    if useC:
        return surface.surface1atom(nbors, i, atom_data, pos1, tot_rad, point_density, ret_unit_points)

    else:
        # the slow python version of the C code
        rad1sq = tot_rad*tot_rad
        rad1_2 = 2*tot_rad
        data = []
        for (index, d2) in nbors[i]:
            apos = atom_data[index]
            vaax = apos[0] - pos1[0]
            vaay = apos[1] - pos1[1]
            vaaz = apos[2] - pos1[2]
            thresh = (d2 + rad1sq - (apos[3]**2)) / rad1_2
            data.append((vaax, vaay, vaaz, thresh))
        points_unit = []
        points1 = []
        for pt1 in tess1:
            buried = 0
            for (vx, vy, vz, thresh) in data:
                if vx*pt1[0] + vy*pt1[1] + vz*pt1[2] > thresh:
                    buried = 1
                    break
            if buried == 0:
                points1.append((tot_rad*pt1[0] + pos1[0],
                                tot_rad*pt1[1] + pos1[1],
                                tot_rad*pt1[2] + pos1[2]))
                points_unit.append(pt1)
        return points1, points_unit


class NeighborList:

    """
    This class is designed to efficiently find lists of atoms which are
    within a distance "radius" of each other.

    Constructor: NeighborList(|atoms|, |radius|, |atom_data|)

    Arguments:

    |atoms| - list of MMTKnp Atom
    |radius| - max distance between neighboring atoms
    |atom_data| - data returned from _get_atom_data
    """

    def __init__(self, atoms, radius, atom_data):
        boxes = {}
        self.box_size = 2*radius
        for i in range(len(atoms)):
            f = self.box_size
            pos = atom_data[i]
            key = '%d %d %d' % (int(math.floor(pos[0]/f)),
                                int(math.floor(pos[1]/f)),
                                int(math.floor(pos[2]/f)))
            if key in boxes:
                boxes[key].append(i)
            else:
                boxes[key] = [i]
        self.boxes = boxes
        self.atoms = atoms
        self.atom_data = atom_data

    def __len__(self):
        return len(self.atoms)

    def __getitem__(self, i):
        """
        Returns a list of tuples describing the neighbors of the ith atom
        in the atom list. Each tuple has the index of the atom which neighbors
        atom i, followed by the square of the distance between atoms.
        """
        boxes = self.boxes
        if useC:
            return surface.FindNeighborsOfAtom(self.atoms, i, boxes, self.box_size, self.atom_data)

        max_dist_2 = self.box_size**2
        pos1 = self.atom_data[i]
        f = self.box_size
        key_tup = (int(math.floor(pos1[0]/f)),
                   int(math.floor(pos1[1]/f)),
                   int(math.floor(pos1[2]/f)))
        nlist = []
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                for z in (-1, 0, 1):
                    key2 = '%d %d %d' % (key_tup[0]+x, key_tup[1]+y, key_tup[2]+z)
                    if key2 in boxes:
                        for i2 in boxes[key2]:
                            if i2 != i:
                                apos = self.atom_data[i2]
                                vaax = apos[0] - pos1[0]
                                vaay = apos[1] - pos1[1]
                                vaaz = apos[2] - pos1[2]
                                d2 = vaax*vaax + vaay*vaay + vaaz*vaaz
                                if d2 > max_dist_2:
                                    continue
                                nlist.append((i2, d2))
        return nlist


def _xlate_results(surfpoints, points_unit, point_density, tot_rad, pos1, ret_fmt, cent):
    area = 4 * math.pi * (tot_rad**2) * len(surfpoints) / point_density

    if ret_fmt < 2:
        return area

    sumx = 0
    sumy = 0
    sumz = 0
    for p in points_unit:
        sumx = sumx + p[0]
        sumy = sumy + p[1]
        sumz = sumz + p[2]
    n = max(1, len(surfpoints))
    vconst = 4/3.0*math.pi/point_density
    dotp1 = (pos1[0] - cent[0])*sumx + (pos1[1] - cent[1])*sumy + (pos1[2] - cent[2])*sumz
    volume = vconst*((tot_rad**2) * dotp1 + (tot_rad**3) * len(surfpoints))

    if ret_fmt == 2:
        return area, volume
    elif ret_fmt == 4:
        grad = (sumx/n, sumy/n, sumz/n)
        return area, volume, np.array(surfpoints, dtype=np.float32), grad
    else:
        return area, volume, np.array(surfpoints, dtype=np.float32)


