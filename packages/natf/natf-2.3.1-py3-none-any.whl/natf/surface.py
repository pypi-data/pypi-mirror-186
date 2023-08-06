#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from natf import mcnp_input

# mcnp mnemonics from user's guide vol II, chap III, p. 3-13
mnemonics = {'P': 4, 'PX': 1, 'PY': 1, 'PZ': 1,
             'SO': 1, 'S': 4, 'SX': 2, 'SY': 2, 'SZ': 2,
             'C/X': 3, 'C/Y': 3, 'C/Z': 3, 'CX': 2, 'CY': 2, 'CZ': 2,
             'K/X': 5, 'K/Y': 5, 'K/Z': 5, 'KX': 3, 'KY': 3, 'KZ': 3,
             'SQ': 10, 'GQ': 10, 'TX': 6, 'TY': 6, 'TZ': 6}  # XYZP is not supported


class Surface(object):
    ''' class Surface'''

    def __init__(self, name=None, id=None, flag=None, mnemonic=None, card_entries=None):
        if name is not None:
            self._name = name
        if id is not None:
            self._id = id  # id
        if flag is not None:
            self._flag = flag  # * or + for boundaries
        if mnemonic is not None:
            self._mnemonic = mnemonic  # type
        if card_entries is not None:
            self._card_entries = card_entries  # parameters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be string')
        self._name = value

    # id setter and getter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError(f'surface id must be integer, given {value}')
        if value < 1 or value > 99999999:
            raise ValueError(
                f'surface id must between 1 and 99999999, given {value}')
        self._id = value

    @property
    def flag(self):
        return self._flag

    @flag.setter
    def flag(self, value):
        if not isinstance(value, str):
            raise ValueError('surface flag must be string')
        if value not in ('*', '+'):
            raise ValueError("surface flag does not support!",
                             "Supported flags: '*', '+'")
        self._flag = value

    @property
    def mnemonic(self):
        return self._mnemonic

    @mnemonic.setter
    def mnemonic(self, value):
        if not isinstance(value, str):
            raise ValueError('surface mnemonic must be string')
        if value.upper() not in mnemonics.keys():
            raise ValueError('surface mnemonic not supported')
        self._mnemonic = value.upper()

    @property
    def card_entries(self):
        return self._card_entries

    @card_entries.setter
    def card_entries(self, value):
        if not hasattr(self, 'mnemonic') or self.mnemonic is None:
            raise ValueError('mnemonic must be assigned before card entries')
        if not isinstance(value, list):
            raise ValueError('card_entries should be a list')
        if len(value) != mnemonics[self.mnemonic]:
            raise ValueError('wrong card entries number')
        self._card_entries = list(value)

    def __str__(self, indent=6):
        """Return the mcnp style surface card"""
        s = ''.join([self.flag, str(self.id), ' ', self.mnemonic])
        indent_str = ' '*indent
        for i, value in enumerate(self.card_entries):
            s = mcnp_input.mcnp_style_str_append(s, value, indent)
        s = ''.join([s, '\n'])
        return s
