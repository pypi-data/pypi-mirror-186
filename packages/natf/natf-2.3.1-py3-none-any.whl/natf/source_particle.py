#!/usr/bin/env python3
# -*- coding:utf-8 -*-

class SourceParticle(object):
    ''' class Source particle'''

    def __init__(self):
        self._xxx = -1.0
        self._yyy = -1.0
        self._zzz = -1.0
        self._cid = -1
        self._mid = -1
        self._mesh_id = -1

    @property
    def xxx(self):
        return self._xxx

    @xxx.setter
    def xxx(self, value):
        if not isinstance(value, float):
            raise ValueError('xxx must be float')
        self._xxx = value

    @property
    def yyy(self):
        return self._yyy

    @yyy.setter
    def yyy(self, value):
        if not isinstance(value, float):
            raise ValueError('yyy must be float')
        self._yyy = value

    @property
    def zzz(self):
        return self._zzz

    @zzz.setter
    def zzz(self, value):
        if not isinstance(value, float):
            raise ValueError('zzz must be float')
        self._zzz = value

    @property
    def cid(self):
        return self._cid

    @cid.setter
    def cid(self, value):
        if not isinstance(value, int):
            raise ValueError('cid of source particle must be int')
        if value > 100000 or value < 1:
            raise ValueError(
                'cid of source particle must in the range of 1 ~ 100000')
        self._cid = value

    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        if not isinstance(value, int):
            raise ValueError('mid of source particle must be integer')
        if value > 100000 or value < 0:
            raise ValueError(
                'mid of source particle must in the range of 0 ~ 100000')
        self._mid = value

    @property
    def mesh_id(self):
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, value):
        if not isinstance(value, int):
            raise ValueError('mesh_id of source particle must be integer')
        if value != -1 and value < 0:
            raise ValueError(
                'mesh_id of source particle must no smaller than 0 (except -1)')
        self._mesh_id = value


######################################################################
######################################################################
def get_source_particles(MCNP_PTRAC):
    """get source particle information form ptrac file in ascii
    input: MCNP_PTRAC, this is the file name of the patrc.
    return: SourceParticles, this is a list of SourceParticle"""

    source_particles = []
    # open the ptrac file
    fin = open(MCNP_PTRAC)
    for line in fin:
        line_ele = line.split()
        sp = SourceParticle()
        if len(line_ele) == 6:
            sp.cid = int(line_ele[3])
            sp.mid = int(line_ele[4])
            source_particles.append(sp)
        if len(line_ele) == 9:
            source_particles[-1].xxx = float(line_ele[0])
            source_particles[-1].yyy = float(line_ele[1])
            source_particles[-1].zzz = float(line_ele[2])

    fin.close()
    return source_particles
