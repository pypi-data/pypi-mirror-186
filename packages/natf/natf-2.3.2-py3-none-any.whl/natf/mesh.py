#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np
from natf.material import Material


class Mesh(object):
    """class Mesh"""

    def __init__(self):
        self._geom = ''  # xyz/cyl
        self._id = -1
        self._xmin = -1.0
        self._xmax = -1.0
        self._ymin = -1.0
        self._ymax = -1.0
        self._zmin = -1.0
        self._zmax = -1.0
        self._rmin = -1.0
        self._rmax = -1.0
        self._tmin = -1.0
        self._tmax = -1.0
        self._origin = [0.0, 0.0, 0.0]  # used only when geom is cyl
        self._axs = [0, 0, 0]  # used only when geom is cyl
        self._vec = [0, 0, 0]  # used only when geom is cyl
        self._vol = -1.0
        self._mass = -1.0
        self._density = -1.0
        self._mesh_cell_list = []  # cids, not cells
        self._mesh_cell_counts = []
        self._mesh_cell_vol_fraction = []  # float
        self._mesh_mat_list = []  # mat ids, not materials
        self._mesh_mat_counts = []
        self._mesh_mat_vol_fraction = []
        self._packing_factor = -1.0  # float
        # gammit emit rate of mesh, a 2D array
        self._gamma_emit_rate = np.zeros((0, 0), dtype=float, order='C')
        self._neutron_flux = []  # list of float, size 176 only
        self._neutron_flux_error = []  # list of float, size 176 only
        self._mat = Material()  # material of the mesh

    @property
    def geom(self):
        return self._geom

    @geom.setter
    def geom(self, value):
        if not isinstance(value, str):
            raise ValueError('geom of mesh must be string')
        if value != 'xyz' and value != 'cyl':
            raise ValueError('geom must be xyz or cyl. (in lower case)')
        self._geom = value

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int):
            raise ValueError('id must be integer')
        if value < 0:
            raise ValueError('id must larger than 0')
        self._id = value

    @property
    def xmin(self):
        return self._xmin

    @xmin.setter
    def xmin(self, value):
        if not isinstance(value, float):
            raise ValueError('xmin of mesh must be float')
        self._xmin = value

    @property
    def xmax(self):
        return self._xmax

    @xmax.setter
    def xmax(self, value):
        if not isinstance(value, float):
            raise ValueError('xmax of mesh must be float')
        self._xmax = value

    @property
    def ymin(self):
        return self._ymin

    @ymin.setter
    def ymin(self, value):
        if not isinstance(value, float):
            raise ValueError('ymin of mesh must be float')
        self._ymin = value

    @property
    def ymax(self):
        return self._ymax

    @ymax.setter
    def ymax(self, value):
        if not isinstance(value, float):
            raise ValueError('ymax of mesh must be float')
        self._ymax = value

    @property
    def zmin(self):
        return self._zmin

    @zmin.setter
    def zmin(self, value):
        if not isinstance(value, float):
            raise ValueError('zmin of mesh must be float')
        self._zmin = value

    @property
    def zmax(self):
        return self._zmax

    @zmax.setter
    def zmax(self, value):
        if not isinstance(value, float):
            raise ValueError('zmax of mesh must be float')
        self._zmax = value

    @property
    def rmin(self):
        return self._rmin

    @rmin.setter
    def rmin(self, value):
        if not isinstance(value, float):
            raise ValueError('rmin of mesh must be float')
        self._rmin = value

    @property
    def rmax(self):
        return self._rmax

    @rmax.setter
    def rmax(self, value):
        if not isinstance(value, float):
            raise ValueError('rmax of mesh must be float')
        self._rmax = value

    @property
    def tmin(self):
        return self._tmin

    @tmin.setter
    def tmin(self, value):
        if not isinstance(value, float):
            raise ValueError('tmin of mesh must be float')
        self._tmin = value

    @property
    def tmax(self):
        return self._tmax

    @tmax.setter
    def tmax(self, value):
        if not isinstance(value, float):
            raise ValueError('tmax of mesh must be float')
        self._tmax = value

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if not isinstance(value, list):
            raise ValueError('origin must be a list')
        if len(value) != 3:
            raise ValueError('origin must have a length of 3')
        for item in value:
            if not isinstance(item, float):
                raise ValueError('origin must be a list of float')
        self._origin = value

    @property
    def axs(self):
        return self._axs

    @axs.setter
    def axs(self, value):
        if not isinstance(value, list):
            raise ValueError('axs must be a list')
        if len(value) != 3:
            raise ValueError('axs must have a length of 3')
        for item in value:
            if not isinstance(item, int):
                raise ValueError('axs must be a list of int')
        self._axs = value

    @property
    def vec(self):
        return self._vec

    @vec.setter
    def vec(self, value):
        if not isinstance(value, list):
            raise ValueError('vec must be a list')
        if len(value) != 3:
            raise ValueError('vec must have a length of 3')
        for item in value:
            if not isinstance(item, int):
                raise ValueError('vec must be a list of int')
        self._vec = value

    @property
    def vol(self):
        return self._vol

    @vol.setter
    def vol(self, value):
        if not isinstance(value, float):
            raise ValueError('vol of mesh must be float')
        if value < 0.0:
            raise ValueError('vol must not smaller than 0.0')
        self._vol = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if not isinstance(value, float):
            raise ValueError('mass of mesh must be float')
        if value < 0.0:
            raise ValueError('mass must not smaller than 0.0')
        self._mass = value

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, value):
        if not isinstance(value, float):
            raise ValueError('density of mesh must be float')
        if value < 0.0:
            raise ValueError('density must not smaller than 0.0')
        self._density = value

    @property
    def mesh_cell_list(self):
        return self._mesh_cell_list

    @mesh_cell_list.setter
    def mesh_cell_list(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_cell_list must a list')
        for i in range(len(value)):
            if not isinstance(value[i], int):
                raise ValueError('mesh_cell_list of mesh must be int')
            if value[i] < 1 or value[i] > 100000:
                raise ValueError(
                    'mesh_cell_list of mesh should between 1 ~ 100000')
        self._mesh_cell_list = value

    @property
    def mesh_cell_counts(self):
        return self._mesh_cell_counts

    @mesh_cell_counts.setter
    def mesh_cell_counts(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_cell_counts must be a list')
        for item in value:
            if not isinstance(item, int):
                raise ValueError('mesh_cell_counts must be a list of int')
            if item < 0:
                raise ValueError('mesh_cell_counts must no smaller than 0')
        self._mesh_cell_counts = value

    @property
    def mesh_cell_vol_fraction(self):
        return self._mesh_cell_vol_fraction

    @mesh_cell_vol_fraction.setter
    def mesh_cell_vol_fraction(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_cell_vol_fraction must a list')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError(
                    'mesh_cell_vol_fraction of mesh must be float')
            if value[i] < 0.0 or value[i] > 1.0:
                raise ValueError(
                    'mesh_cell_vol_fraction of mesh should between 0 ~ 1')
        if abs(sum(value) - 1) > 1e-6:
            raise ValueError('sum of mesh_cell_vol_fraction must be 1.0')
        self._mesh_cell_vol_fraction = value

    @property
    def mesh_mat_list(self):
        return self._mesh_mat_list

    @mesh_mat_list.setter
    def mesh_mat_list(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_mat_list must a list')
        for i in range(len(value)):
            if not isinstance(value[i], int):
                raise ValueError('mesh_mat_list of mesh must be int')
            if value[i] < 0 or value[i] > 100000:
                raise ValueError(
                    'mesh_mat_list of mesh should between 0 ~ 100000')
        self._mesh_mat_list = value

    @property
    def mesh_mat_counts(self):
        return self._mesh_mat_counts

    @mesh_mat_counts.setter
    def mesh_mat_counts(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_mat_counts must be a list')
        for item in value:
            if not isinstance(item, int):
                raise ValueError('mesh_mat_counts must be a list of int')
            if item < 0:
                raise ValueError('mesh_mat_counts must no smaller than 0')
        self._mesh_mat_counts = value

    @property
    def mesh_mat_vol_fraction(self):
        return self._mesh_mat_vol_fraction

    @mesh_mat_vol_fraction.setter
    def mesh_mat_vol_fraction(self, value):
        if not isinstance(value, list):
            raise ValueError('mesh_mat_vol_fraction must a list')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError('mesh_mat_vol_fraction of mesh must be float')
            if value[i] < 0.0 or value[i] > 1.0:
                raise ValueError(
                    'mesh_mat_vol_fraction of mesh should between 0 ~ 1')
        if abs(sum(value) - 1) > 1e-6:
            raise ValueError('sum of mesh_mat_vol_fraction must be 1.0')
        self._mesh_mat_vol_fraction = value

    @property
    def packing_factor(self):
        return self._packing_factor

    @packing_factor.setter
    def packing_factor(self, value):
        if not isinstance(value, float):
            raise ValueError('packing_factor of mesh must be float')
        if value < 0.0:
            raise ValueError('packing_factor must not smaller than 0.0')
        self._packing_factor = value

    @property
    def neutron_flux(self):
        return self._neutron_flux

    @neutron_flux.setter
    def neutron_flux(self, value):
        if not isinstance(value, list):
            raise ValueError('neutron_flux of cell must be a list')
        if len(value) != 176:
            raise ValueError(
                'neutron flux should have data of 176, with the last of total data')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError(
                    'neutron_flux of mesh must be a list of float')
            if value[i] < 0:
                raise ValueError(
                    'neutron_flux of mesh must be a list that each element is no smaller than 0.0')
        self._neutron_flux = value

    @property
    def neutron_flux_error(self):
        return self._neutron_flux_error

    @neutron_flux_error.setter
    def neutron_flux_error(self, value):
        if not isinstance(value, list):
            raise ValueError('neutron_flux_error must be a list')
        if len(value) != 176:
            raise ValueError(
                'neutron flux error of mesh should have data of 176, with the last of total data')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError('neutron_flux_error must be a list of float')
            if value[i] < 0.0 or value[i] > 1:
                raise ValueError('neutron_flux_error must between 0 and 1')
        self._neutron_flux_error = value

    @property
    def gamma_emit_rate(self):
        return self._gamma_emit_rate

    @gamma_emit_rate.setter
    def gamma_emit_rate(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('gamma_emit_rate must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'gamma_emit_rate must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('gamma_emit_rate must composed of float')
        if value.min() < 0.0:
            raise ValueError('gamma_emit_rate must no smaller than 0.0')
        self._gamma_emit_rate = value

    @property
    def mat(self):
        return self._mat

    @mat.setter
    def mat(self, value):
        if not isinstance(value, Material):
            raise ValueError('mesh mat must be a "Material"')
        self._mat = value

    def cal_vol(self):
        if self._geom == 'xyz':
            self._vol = (self._xmax - self._xmin) * \
                (self._ymax - self._ymin) * (self._zmax - self._zmin)
        if self._geom == 'cyl':
            self._vol = 3.1415926 * (self._rmax ** 2 - self._rmin ** 2) * \
                (self._zmax - self._zmin) * (self._tmax - self._tmin)
        if self._vol < 0.0:
            raise ValueError(
                'there are mesh with vol smaller then 0.0, check the geometry')
