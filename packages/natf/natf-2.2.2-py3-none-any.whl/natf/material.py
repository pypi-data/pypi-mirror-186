#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
from natf import utils

''' class Material.'''

thisdir = os.path.dirname(os.path.abspath(__file__))
appendix16 = os.path.join(thisdir, "data", "appendix16")

start_id_for_created_mat = 10000
counts_of_created_mat = 0  # for material update (after irradiation)

fendl31c_xsdir = os.path.join(thisdir, "data", "fendl31c_nucs")
tendl19c_xsdir = os.path.join(thisdir, "data", "tendl19c_nucs")


class Material(object):
    """calsee Material, used to store material information"""

    def __init__(self):
        self._id = -1
        self._atom_density = -1.0
        self._density = -1.0
        self._mcnp_material_nuclide = []
        self._mcnp_material_atom_fraction = []  # atom fraction [%]
        self._mcnp_material_mass_fraction = []  # mass fraction [%]
        self._fispact_material_nuclide = []
        self._fispact_material_atoms_kilogram = []  # atoms per kilogram
        self._fispact_material_grams_kilogram = []  # grams per kilogram

    def __str__(self, card='mat', style='mcnp'):
        """Return definition for material"""
        if card == 'mat' and style == 'mcnp':
            m_str = f"M{self._id} "
            if len(self.mcnp_material_atom_fraction) > 0:
                for i, nuc in enumerate(self.mcnp_material_nuclide):
                    m_str = f"{m_str}\n      {nuc} {self.mcnp_material_atom_fraction[i]}"
            elif len(self.mcnp_material_mass_fraction) > 0:
                for i, nuc in enumerate(self.mcnp_material_nuclide):
                    m_str = f"{m_str}\n      {nuc} -{self.mcnp_material_mass_fraction[i]}"
            else:
                raise ValueError(
                    f"material {self.id} do not has nuclide composition")
            return m_str
        elif card == 'cell' and style == 'mcnp':
            # create material string in cell card
            m_str = ''
            if self.density > 0:
                m_str = f"{self.id} -{self.density}"
            elif self.atom_density > 0:
                m_str = f"{self.id} {self.atom_density}"
            else:
                raise ValueError(
                    f"material {self.id} does not assigned density/atom_density")
            return m_str
        else:
            raise ValueError(f"card: {card}, style: {style} not supported")

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'mat id must be an integer, given {value}')
        if value > 99999999 or value < 0:
            raise ValueError(
                f'mat id must between 1 ~ 99999999, given {value}')
        self._id = value

    @ property
    def atom_density(self):
        return self._atom_density

    @ atom_density.setter
    def atom_density(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError('atom_density must be a float')
        if value < 0:
            raise ValueError(
                f'atom_density should be larger than 0, given {value}')
        if value > 1:
            print(
                f'Warning: atom_density of material {self.id} is larger than 1.0, maybe nonphysical')
        self._atom_density = value

    @ property
    def density(self):
        return self._density

    @ density.setter
    def density(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError('density should be a float!')
        if value < 0:
            raise ValueError('density should be larger than 0!')
        if value > 30:
            print(
                f'Warning: density of material {self.id} exceed 30, maybe nonphysical')
        self._density = value

    @ property
    def mcnp_material_nuclide(self):
        return self._mcnp_material_nuclide

    @ mcnp_material_nuclide.setter
    def mcnp_material_nuclide(self, value):
        if not isinstance(value, list):
            raise ValueError('mcnp_material_nuclide should be a list')
        for i in range(len(value)):
            if not isinstance(value[i], str):
                raise ValueError(
                    'mcnp_material_nuclide should be a list of string')
            if not value[i].isdigit():
                raise ValueError(
                    'mcnp_material_nuclide should be a list of string that composed of digit')
            if len(value[i]) < 3 or len(value[i]) > 6:
                raise ValueError(
                    'mcnp_material_nuclide should be a list of string with length between 3~6')
        self._mcnp_material_nuclide = value

    @ property
    def mcnp_material_atom_fraction(self):
        return self._mcnp_material_atom_fraction

    @ mcnp_material_atom_fraction.setter
    def mcnp_material_atom_fraction(self, value):
        if not isinstance(value, list):
            raise ValueError('mcnp_material_atom_fraction should be a list')
        fraction_sum = 0.0
        for i in range(len(value)):
            if not isinstance(
                    value[i],
                    float) and not isinstance(
                    value[i],
                    int):
                raise ValueError(
                    'mcnp_material_atom_fraction should be a list of float/int')
            if value[i] < 0 or value[i] > 1:
                raise ValueError(
                    'mcnp_material_atom_fraction should be a list of float between 0 ~ 1')
            fraction_sum += value[i]
        if abs(fraction_sum - 1) > 1e-3:
            raise ValueError(
                'mcnp_material_atom_fraction should be a list that sum to be 1.0')
        if len(self._mcnp_material_nuclide) != 0 and len(
                value) != len(self._mcnp_material_nuclide):
            raise ValueError(
                'the length of mcnp_material_atom_fraction should equals to the length of mcnp_material_nuclide! check them')
        self._mcnp_material_atom_fraction = value

    @ property
    def mcnp_material_mass_fraction(self):
        return self._mcnp_material_mass_fraction

    @ mcnp_material_mass_fraction.setter
    def mcnp_material_mass_fraction(self, value):
        if not isinstance(value, list):
            raise ValueError('mcnp_material_mass_fraction should be a list')
        fraction_sum = 0.0
        for i in range(len(value)):
            if not isinstance(
                    value[i],
                    float) and not isinstance(
                    value[i],
                    int):
                raise ValueError(
                    'mcnp_material_mass_fraction should be a list of float/int')
            if value[i] < 0 or value[i] > 1:
                raise ValueError(
                    'mcnp_material_mass_fraction should be a list of float between 0 ~ 1')
            fraction_sum += value[i]
        if abs(fraction_sum - 1) > 1e-3:
            raise ValueError(
                'mcnp_material_mass_fraction should be a list that sum to be 1.0')
        if len(self._mcnp_material_nuclide) != 0 and len(
                value) != len(self._mcnp_material_nuclide):
            raise ValueError(
                'the length of mcnp_material_mass_fraction should equals to the length of mcnp_material_nuclide! check them')
        self._mcnp_material_mass_fraction = value

    # fispact_material_nuclide is a read only variable, so it doesn't have a
    # setter
    @ property
    def fispact_material_nuclide(self):
        return self._fispact_material_nuclide

    @ fispact_material_nuclide.setter
    def fispact_material_nuclide(self, value):
        if not isinstance(value, list):
            raise ValueError('fispact_material_nuclide should be a list')
        for i in range(len(value)):
            if not isinstance(value[i], str):
                raise ValueError(
                    'fispact_material_nuclide should be a list of string')
            if len(value[i]) < 2 or len(value[i]) > 6:
                raise ValueError(
                    'fispact_material_nuclide should be a list of string with length between 2~6')
        self._fispact_material_nuclide = value

    @ property
    def fispact_material_atoms_kilogram(self):
        return self._fispact_material_atoms_kilogram

    @ fispact_material_atoms_kilogram.setter
    def fispact_material_atoms_kilogram(self, value):
        if not isinstance(value, list):
            raise ValueError(
                'fispact_material_atoms_kilogram should be a list')
        for i in range(len(value)):
            if not isinstance(value[i], float) and not isinstance(value[i], int):
                raise ValueError(
                    'fispact_material_atoms_kilogram should be a list of float/int')
        if len(self._fispact_material_nuclide) != 0 and len(value) != len(self._fispact_material_nuclide):
            raise ValueError(
                'the length of fispact_material_atoms_kilogram should equals to the length of fispact_material_nuclide!')
        self._fispact_material_atoms_kilogram = value

    @ property
    def fispact_material_grams_kilogram(self):
        return self._fispact_material_grams_kilogram

    @ fispact_material_grams_kilogram.setter
    def fispact_material_grams_kilogram(self, value):
        if not isinstance(value, list):
            raise ValueError(
                'fispact_material_grams_kilogram should be a list')
        for i in range(len(value)):
            if not isinstance(value[i], float) and not isinstance(value[i], int):
                raise ValueError(
                    'fispact_material_grams_kilogram should be a list of float/int')
        if len(self._fispact_material_nuclide) != 0 and len(value) != len(self._fispact_material_nuclide):
            raise ValueError(
                'the length of fispact_material_grams_kilogram should equals to the length of fispact_material_nuclide!')
        self._fispact_material_grams_kilogram = value

    def mcnp2fispact(self):
        """
        Convert the mcnp material to fispact material

        Properties to be set:
            - fispact_material_nuclide
            - fispact_material_atoms_kilogram
        """
        if len(self._mcnp_material_nuclide) == 0:
            return
        if self._density < 0.0:
            raise Exception(
                'the density of the material should be set before convert')
        # convert the mcnp nuclide to fispact nuclide
        ELE_TABLE = utils.get_ele_table()
        for i in range(len(self._mcnp_material_nuclide)):
            nuc = self._mcnp_material_nuclide[i]
            z, a, m = decompose_mcnp_nuc(nuc)
            scale = self._atom_density * \
                self._mcnp_material_atom_fraction[i] * \
                1e24 * 1e3 / self._density  # atoms per kilogram
            if a != 0:
                self._fispact_material_nuclide.append(
                    compose_fispact_nuc(z, a, m))
                self._fispact_material_atoms_kilogram.append(scale)
            if a == 0:
                # open the abundance file
                fin = open(appendix16)
                for line in fin:
                    line_ele = line.split()
                    if int(line_ele[0]) == z:
                        if (line_ele[1]) == '0.0':
                            errormessage = ''.join(
                                ['Nuclide: ', nuc, ' has no natural isotopes\n'])
                            raise ValueError(errormessage)
                        # get the start number
                        start_a = int(line_ele[3])
                        abundance_list = [float(x) for x in line_ele[4:]]
                        a_list = [
                            x + start_a for x in range(len(abundance_list))]
                        isotopes = []
                        for item in a_list:
                            tempiso = ''.join([ELE_TABLE[z-1], str(item)])
                            isotopes.append(tempiso)
                        # treat the isotope that has 0.0 abundance
                        real_isotopes = []
                        real_abundance_list = []
                        for i in range(len(abundance_list)):
                            # this is a isotope with 0.0 abundance
                            if abundance_list[i] < 1e-6:
                                pass
                            else:
                                real_abundance_list.append(abundance_list[i])
                                real_isotopes.append(isotopes[i])
                        self._fispact_material_nuclide.extend(real_isotopes)
                        self._fispact_material_atoms_kilogram.extend(
                            map(lambda x: x * scale / 100.0, real_abundance_list))
                fin.close()

    def fispact2mcnp(self, ntrans_avail_nucs, record_drop=False,
                     record_file=None):
        """
        Convert the mcnp material to fispact material

        Parameters:
        -----------
        ntrans_avail_nucs : list of str
            The nuclides available in neutron transport. There are some
            activated nuclides absent in the nuclear library. Only nuclides
            exist in the specified library will be kept.
        record_drop : bool
            Record the dropped atoms/kg if the record_drop is True.
        record_file : str
            The detailed record of element dropped in each FISPACT -> MCNP converstion.

        Properties to be set:
            - atom_density
            - mcnp_material_nuclide
            - mcnp_material_atom_fraction
        """
        # compose mcnp_material_nuclide
        mcnp_nuclides = []
        mcnp_atom_fraction = []
        total_atoms = 0.0
        drop_atoms = 0.0
        drop_mass = 0.0
        for i, nuc in enumerate(self.fispact_material_nuclide):
            nuc_m = nuc_fispact2mcnp(nuc)
            if nuc_m in ntrans_avail_nucs:
                mcnp_nuclides.append(nuc_m)
                total_atoms += self.fispact_material_atoms_kilogram[i]
            else:
                drop_atoms += self.fispact_material_atoms_kilogram[i]
                drop_mass += self.fispact_material_grams_kilogram[i]
                if record_file and record_drop:
                    with open(record_file, 'a') as fo:
                        fo.write(
                            f"{nuc},"
                            f"{utils.format_single_output(self.fispact_material_atoms_kilogram[i])},"
                            f"{utils.format_single_output(self.fispact_material_grams_kilogram[i])}\n")
        # calculate atom density
        vol = 1e3 / self.density  # [cm3]
        self.atom_density = total_atoms * 1e-24 / vol
        for i, nuc_m in enumerate(mcnp_nuclides):
            nuc = nuc_mcnp2fispact(nuc_m)
            nidx = self.fispact_material_nuclide.index(nuc)
            mcnp_atom_fraction.append(
                self.fispact_material_atoms_kilogram[nidx]/total_atoms)
        # assign the value
        self.mcnp_material_nuclide = mcnp_nuclides
        self.mcnp_material_atom_fraction = mcnp_atom_fraction
        return drop_atoms, drop_mass

    def treat_fispact_nuc_composition(self, nuc, level):
        """
        Reset the composition of the [nuc] to specific [level].

        The density is assumed to be constant.
        Properties required to change:
            - atom_density
            - fispact_material_atoms_kilogram
            - fispact_material_grams_kilogram

        Returns:
        --------
        purified_atoms : float
            Purified atoms per kg material.
        purified_grams : float
            Purified grams of nuc per kg material.
        """
        nidx = self.fispact_material_nuclide.index(nuc)  # find nuc index
        # update fispact material composition
        purified_atoms = self.fispact_material_atoms_kilogram[nidx] * (1-level)
        self.fispact_material_atoms_kilogram[nidx] *= level
        purified_grams = self.fispact_material_grams_kilogram[nidx] * (1-level)
        self.fispact_material_grams_kilogram[nidx] *= level

        # update total_atoms
        total_atoms = 0.0
        for i, nuc in enumerate(self.fispact_material_atoms_kilogram):
            total_atoms += self.fispact_material_atoms_kilogram[i]
        # calculate atom density
        vol = 1e3 / self.density  # [cm3]
        self.atom_density = total_atoms * 1e-24 / vol
        return purified_atoms, purified_grams


def decompose_fispact_nuc(nuc):
    """
    Decompose the fispact nuclide.

    Parameters:
    -----------
    nuc: str
        A FISPACT nuclide.

    Returns:
    --------
    z: int
        The number of protons.
    a: int
        The number of protons + neutrons.
    m: int
        Metastable state. Only 0 or 1 is supported.
    """
    z, a, m = 0, 0, 0
    ELE_TABLE = utils.get_ele_table()

    # metastable state
    if nuc[-1] == 'm':
        m = 1
        nuc = nuc[:-1]

    sym_a = re.findall('(\d+|[A-Za-z]+)', nuc)
    z = ELE_TABLE.index(sym_a[0]) + 1
    a = int(sym_a[1])
    return z, a, m


def decompose_mcnp_nuc(nuc):
    """
    Decompose the mcnp nuclide.

    Parameters:
    -----------
    nuc: str
        A MCNP nuclide.

    Returns:
    --------
    z: int
        The number of protons.
    a: int
        The number of protons + neutrons.
    m: int
        Metastable state. Only 0 or 1 is supported.
    """
    z, a, m = 0, 0, 0
    ELE_TABLE = utils.get_ele_table()
    z = int(nuc[:-3])
    a = int(nuc[-3:])
    if a > 300:
        a = a - 300 - 100
        m = 1
    return z, a, m


def compose_mcnp_nuc(z, a, m):
    """
    Construct mcnp nuclide.
    """
    if m > 0:
        nuc = f"{z}{a+300+m*100:03d}"
    else:
        nuc = f"{z}{a:03d}"
    return nuc


def compose_fispact_nuc(z, a, m):
    if m > 0:
        m = 'm'
    else:
        m = ''

    ELE_TABLE = utils.get_ele_table()
    sym = ELE_TABLE[z-1]
    nuc = f"{sym}{a}{m}"
    return nuc


def nuc_fispact2mcnp(nuc):
    """
    Convert fispact format nuclides to mcnp format.
    """
    z, a, m = decompose_fispact_nuc(nuc)
    nuc = compose_mcnp_nuc(z, a, m)
    return nuc


def nuc_mcnp2fispact(nuc):
    """
    Convert fispact format nuclides to mcnp format.
    """
    z, a, m = decompose_mcnp_nuc(nuc)
    nuc = compose_fispact_nuc(z, a, m)
    return nuc


def create_pseudo_mat(mid=1, den=1.0):
    """
    Create a pseudo-material.
    """
    mat = Material()
    mat.id = mid
    mat.density = den
    mat.mcnp_material_nuclide = ['1001']
    mat.mcnp_material_mass_fraction = [1.0]
    return mat


def is_mat_used(materials, mid):
    """
    Check whether a mid used in the mcnp problem.
    """
    for i in range(len(materials)):
        if materials[i].id == mid:
            return True
    return False


def get_nucs_from_xsdir(filename):
    """
    Get the nuclides in specified file.
    """
    nucs = []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            # continue line
            if line[0:6] == '      ' or utils.is_blank_line(line):
                continue
            line_ele = line.strip().split()
            nuc = line_ele[0].split('.')[0]
            nucs.append(nuc)
    return nucs


def get_neutron_library_nuclides(nuclide_sets=['FENDL3', 'TENDL2019'],
                                 filenames=None):
    """
    Get the available nuclides in specified nuclear library.

    Parameters:
    -----------
    nuclide_sets : list
        The nuclide libraries to use in MCNP transport.
    filenames : list
        The user defined library xsdir file for test.
    """

    if filenames is None:
        filenames = []
        if 'FENDL3' in nuclide_sets:
            filenames.append(fendl31c_xsdir)
        if 'TENDL2019' in nuclide_sets:
            filenames.append(tendl19c_xsdir)

    nuclides = []
    # read nuclides
    for i, filename in enumerate(filenames):
        # get nucs
        nucs = get_nucs_from_xsdir(filename)
        # combine nuclides list
        for nuc in nucs:
            if nuc not in nuclides:
                nuclides.append(nuc)
    return nuclides
