#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import numpy as np
from natf.surface import Surface


class HalfSpace(object):
    ''' class Surface'''

    def __init__(self, surf, sense):
        self.surf = surf
        self.sense = sense

    @property
    def surf(self):
        return self._surf

    @surf.setter
    def surf(self, value):
        if not isinstance(value, Surface):
            raise ValueError('given argument not a Surface instance')
        self._surf = value

    @property
    def sense(self):
        return self._sense

    @sense.setter
    def sense(self, value):
        if value not in ('+', '-', 'positive', 'negative'):
            raise ValueError('sense not supported')
        self._sense = value

    def __str__(self):
        """Return the mcnp style surface card"""
        if self.sense in ('+', 'positive'):
            return str(self.surf.id)
        else:
            return ''.join(['-', str(self.surf.id)])
