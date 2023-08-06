#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
import re
from natf import utils

''' class NucTreat.'''

thisdir = os.path.dirname(os.path.abspath(__file__))
SUPPORTED_UNITS = ('Bq/kg', 'Ci/m3', 'g/kg', 'atoms/kg')


class NucTreat(object):
    """
    class NucTreat, used to treat nuclide for cell.
    """

    def __init__(self):
        self._id = -1
        self._cid = None
        self._nuc = None
        self._operator = None
        self._operand = None
        self._operand_unit = None
        self._bounds = [float('-inf'), float('inf')]
        self._bounds_unit = 'g/kg'
        self._time = 0.0
        self._time_unit = 's'

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{value} not an integer')
        self._id = value

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        if not isinstance(value, int):
            raise ValueError(f'{value} not an integer')
        self._cid = value
        if value < 1 or value > 99999999:
            raise ValueError('cid must between 1 and 99999999')
        self._cid = value

    @property
    def nuc(self):
        return self._nuc

    @nuc.setter
    def nuc(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a nuclide")
        self._nuc = value

    @property
    def operator(self):
        return self._operator

    @operator.setter
    def operator(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a string")
        if value not in ('*', '+', '-'):
            raise ValueError(f"{value} not supported! Use ('*', '+', '-')")

    @property
    def operand(self):
        return self._operand

    @operand.setter
    def operand(self, value):
        if not isinstance(value, float) and not isinstance(value, int):
            raise ValueError(f"{value} not a float")
        if value < 0:
            raise ValueError(f"{value} is negtive. Use positive number")
        self._operand = value

    @property
    def operand_unit(self):
        return self._operand_unit

    @operand_unit.setter
    def operand_unit(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a string")
        if value not in SUPPORTED_UNITS:
            raise ValueError(
                f"{value} not in supported units: {SUPPORTED_UNITS}")
        self._operand_unit = value

    @property
    def bounds(self):
        return self._bounds

    @bounds.setter
    def bounds(self, value):
        if not isinstance(value, list):
            raise ValueError(f"{value} not a list")
        for item in value:
            if not isinstance(item, float) and not isinstance(item, int):
                raise ValueError(f"{item} in bounds not a float")
        self._bounds = value

    @property
    def bounds_unit(self):
        return self._bounds_unit

    @bounds_unit.setter
    def bounds_unit(self, value):
        if not isinstance(value, str):
            raise ValueError(f"{value} not a string")
        if value not in SUPPORTED_UNITS:
            raise ValueError(
                f"{value} not in supported units: {SUPPORTED_UNITS}")
        self._bounds_unit = value

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
    # TODO
    pass


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
        nuc_treat = compose_nuc_treat_from_line(line)
    fin.close()
    return nuc_treats
