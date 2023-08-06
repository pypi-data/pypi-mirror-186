#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
from natf import utils, settings, material

''' class NucTreat.'''

thisdir = os.path.dirname(os.path.abspath(__file__))
SUPPORTED_UNITS = ('Bq/kg', 'Ci/m3', 'g/kg', 'atoms/kg')


class NucTreat(object):
    """
    class NucTreat, used to treat nuclide for cell.
    """

    def __init__(self):
        self._ids = []
        self._nuc = None
        self._operate = None
        self._bounds = None
        self._time = 0.0
        self._time_unit = 's'

    @property
    def ids(self):
        return self._ids

    @ids.setter
    def ids(self, value):
        if not isinstance(value, list):
            raise ValueError(f"ids of nuc_treat must be a list")
        self._ids = value

    @property
    def nuc(self):
        return self._nuc

    @nuc.setter
    def nuc(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a nuclide")
        self._nuc = value

    @property
    def operate(self):
        return self._operate

    @operate.setter
    def operate(self, value):
        if not isinstance(value, tuple):
            raise ValueError('Invalid operate: {value}')
        if len(value) != 3:
            raise ValueError('Wrong length of operate: {value}')
        self._operate = value

    @property
    def bounds(self):
        return self._bounds

    @bounds.setter
    def bounds(self, value):
        if not isinstance(value, tuple):
            raise ValueError(f"{value} not a tuple")
        if len(value) != 3:
            raise ValueError(f"Wrong lenghth of bounds: {value}")
        self._bounds = value

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError(f"{value} not a float")
        self._time = value

    @property
    def time_unit(self):
        return self._time_unit

    @time_unit.setter
    def time_unit(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a string")
        if value not in utils.TIME_UNITS:
            raise ValueError(
                f"time unit {value} not supported! Use {utils.TIME_UNITS}")
        self._time_unit = value


def compose_nuc_treat_from_line(line):
    """
    Compose NucTreat object from a line.
    """
    nuc_treat = NucTreat()
    ntd = parse_nuc_treat_from_line(line)
    nuc_treat.ids = ntd['ids']
    nuc_treat.nuc = ntd['nuc']
    nuc_treat.operate = ntd['operate']
    nuc_treat.bounds = ntd['bounds']
    return nuc_treat


def parse_nuc_operator(s):
    """
    Get the nuclide operator from string.
    The operator part have 3 kinds of forms:
        - operand: 1 float value. The operator is set to '*' (multiply)
        - operator operand: 1 char and 1 float value. Supported operator:
            - *: multiply. default unit: unity
            - +: addition. default unit: Bq/kg
            - -: subtraction. default unit: Bq/kg
        - operator operand operand_unit: 1 char, 1 float value and a string.
            Used when the operator in (+, -)
            Supported units:
            - Bq/kg
            - g/kg: gram nuc per kg material
    """
    supported_operators = ('*', '+', '-')
    supported_units = ('Bq/kg', 'g/kg')
    s = s.strip()
    tokens = s.split()
    # invalid entry
    if len(tokens) < 1:
        raise ValueError(f"invalid expression of nuclide operation: {s} ")

    # 1 entry
    if len(tokens) == 1:
        return '*', float(tokens[0]), None

    # 2 entries
    if len(tokens) == 2:
        operator = tokens[0].strip()
        if operator not in supported_operators:
            raise ValueError(f"operator {operator} in {s} not supported")
        return operator, float(tokens[1]), 'Bq/kg'

    # 3 entries
    if len(tokens) == 3:
        operator = tokens[0].strip()
        if operator not in supported_operators:
            raise ValueError(f"operator {operator} in {s} not supported")
        if tokens[0].strip() == '*':
            raise ValueError(f"Wrong unit in {s} when operator is '*'")
        unit = tokens[2].strip()
        if unit not in supported_units:
            raise ValueError(f"Unit in {s} not supported. Use ")
        return operator, float(tokens[1]), unit

    # invalid entries
    if len(tokens) > 3:
        raise ValueError(f"invalid operator expression: {s}")


def parse_nuc_bounds(s):
    """
    Parse the information of nuclide boundaries
    Possible entries:
        - lower_bound upper_bound: 2 float entries
        - lower_bound upper_bound unit: 2 float entries and 1 string

    Parameters:
    -----------
    s : string
        The string contains nuclide boundaries

    returns:
    --------
    bounds : list
        The lower and upper bounds
    """
    # keywords check
    if 'bounds:' not in s.lower():
        raise ValueError(f"Invalid nuc bounds: {s}")
    tokens = s.lower().strip().split('bounds:')[-1].strip().split()
    if len(tokens) < 2 or len(tokens) > 3:
        raise ValueError(f"Invalid bounds length: {s}")
    if len(tokens) == 2:
        return float(tokens[0]), float(tokens[1]), 'Bq/kg'
    if len(tokens) == 3:
        return float(tokens[0]), float(tokens[1]), tokens[2].strip().replace('bq', 'Bq')


def parse_nuc_treat_from_line(line):
    """
    Parse the NucTreat parameters from nuc_treatment file.

    Parameters:
    -----------
    line : str
        The line from nuc_treatment

    Returns:
    --------
    params: dictionary
        The dictionary contains key and paramerters:
            - ids
            - nuc
            - operate: (operator, operand, unit)
            - bounds: (lower_bound, upper_bound, unit)
    """
    # check the length of tokens
    tokens = line.split(',')
    if len(tokens) >= 3:
        # ids, nuc, operator
        item_ids = settings.get_item_ids(tokens[0].split())
        if len(tokens[1].strip().split()) > 1:
            raise ValueError(
                f"line {line} contains multipler nuclides. Only one is supported.")
        nuc = tokens[1].strip()
        # deal with operator
        operator, operand, operand_unit = parse_nuc_operator(tokens[2])
        lower_bound = 0
        upper_bound = float('inf')
        bounds_unit = 'Bq/kg'
    if len(tokens) == 4:
        # ids, nuc, operator, bounds
        lower_bound, upper_bound, bounds_unit = parse_nuc_bounds(tokens[3])
    if len(tokens) > 4:
        raise ValueError(f"Invalid expression: {line}")
    ntd = {}
    ntd['ids'] = item_ids
    ntd['nuc'] = nuc
    ntd['operate'] = (operator, operand, operand_unit)
    ntd['bounds'] = (lower_bound, upper_bound, bounds_unit)
    return ntd


def read_nuc_treatment(self, filename):

    if filename == '':
        return []
    nuc_treats = []
    fin = open(filename, 'r')
    line = ' '
    while line != '':
        try:
            line = fin.readline()
        except:
            line = fin.readline().encode('ISO-8859-1')
        if utils.is_blank_line(line):  # this is a empty line
            continue
        if utils.is_comment(line, code='#'):  # this is a comment line
            continue
        nuc_treat = parse_nuc_treat_from_line(line)
    fin.close()
    return nuc_treats


def calc_nuc_treat_factor(value, operate, bounds):
    """
    Calculate the treatment factor (convert to '*' operate).
    For different operates:
        - '*': calc the factor according to the bounds
        - '+' or '-': calc the factor according to the operate and bounds

    Parameters:
    -----------
    value : float
        The value to be treat
    operate : tuple
        The info of (operator, operand, operand_unit)
    bounds : tuple
        The info of (lower_bound, upper_bound, unit)

    Returns:
    --------
    factor : float
        The equivalent factor
    """
    if operate[0] == '*':
        # increment operation
        if operate[1] > 1.0:
            if value < bounds[1]:
                if value*operate[1] < bounds[1]:
                    return operate[1]
                else:
                    return bounds[1]/value
            else:  # value larger than bounds, not an allowed operation
                return 1.0
        else:  # decrement operation
            if value < bounds[0]:
                return 1.0  # not allowed
            else:
                if value*operate[1] < bounds[0]:
                    return bounds[0]/value
                else:
                    return operate[1]
    if operate[0] == '+':
        # increment operation
        if value < bounds[1]:
            if value+operate[1] < bounds[1]:
                return (value+operate[1])/value
            else:
                return bounds[1]/value
        else:  # value larger than bounds, not an allowed operation
            return 1.0
    if operate[0] == '-':
        # decrement operation
        if value < bounds[0]:
            return 1.0  # not allowed
        else:
            if value-operate[1] < bounds[0]:
                return bounds[0]/value
            else:
                return (value-operate[1])/value


def treat_cell_nuc_responses(c, nt):
    """
    # TODO: rename
    Treat the nuclide responses according to the NucTreat object.
    """
    nidx = c.nuclides.index(nt.nuc)  # find nuc index
    tidx = 0
    factor = 1
    # nuclide inventory
    if nt.bounds[2] == 'Bq/kg':
        factor = calc_nuc_treat_factor(
            c.act[tidx, nidx], nt.operate, nt.bounds)

    # nuclide responses
    for intv in range(len(c.act)):
        c.act[intv, nidx] = c.act[intv, nidx] * factor
        c.decay_heat[intv, nidx] = c.decay_heat[intv, nidx] * factor
        c.contact_dose[intv,
                       nidx] = c.contact_dose[intv, nidx] * factor
        c.ci[intv, nidx] = c.ci[intv, nidx] * factor
    return c


def treat_fispact_nuc_composition(mat, nt):
    """
    TODO: update the nuclide treatment factor
    Treat the composition of the material according to the NucTreat object.

    The density is assumed to be constant.
    Properties required to change:
        - atom_density
        - fispact_material_atoms_kilogram
        - fispact_material_grams_kilogram

    Returns:
    --------
    mat : Material object
        The treated material object
    purified_atoms : float
        Purified atoms per kg material.
    purified_grams : float
        Purified grams of nuc per kg material.
    """
    nidx = mat.fispact_material_nuclide.index(
        nt.nuc)  # find nuc index, material
    factor = nt.operate[1]
    # update fispact material composition
    purified_atoms = mat.fispact_material_atoms_kilogram[nidx] * (1-factor)
    mat.fispact_material_atoms_kilogram[nidx] *= factor
    purified_grams = mat.fispact_material_grams_kilogram[nidx] * (1-factor)
    mat.fispact_material_grams_kilogram[nidx] *= factor

    # update total_atoms
    total_atoms = 0.0
    for i, nuc in enumerate(mat.fispact_material_atoms_kilogram):
        total_atoms += mat.fispact_material_atoms_kilogram[i]
    # calculate atom density
    vol = 1e3 / mat.density  # [cm3]
    mat.atom_density = total_atoms * 1e-24 / vol
    return mat, purified_atoms, purified_grams
