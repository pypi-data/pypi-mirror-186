#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import math
import numpy as np
from natf import utils
from natf import mcnp_input
from natf.material import Material


class Cell(object):
    '''class Cell'''
    # count the number of cells and record the cell ids
    counter = 0
    cells_ids = []

    def __init__(self, id=None):
        self._name = ''
        self._icl = None
        self._id = id
        if self._id is None:
            self.assign_default_id()
        Cell.cells_ids.append(self._id)
        Cell.counter += 1
        self._mid = None
        self._mat = Material()
        self._geom = []  # list of dict of {Boolean:surf_list}
        self._imp_n = 1.0
        self._imp_p = None
        self._fill = None
        self._u = None
        self._vol = 0.0  # cm3
        self._mass = 0.0  # g
        self._density = 0.0  # g/cm3
        self._neutron_flux = np.zeros(0, dtype=float)
        self._neutron_flux_error = np.zeros(0, dtype=float)
        self._gamma_emit_rate = np.zeros(shape=(0, 0), dtype=float, order='C')
        self._nuclides = []  # fispact output data nuclides
        self._half_lives = []
        self._points = np.zeros(shape=(0, 3), dtype=np.float64, order='C')
        self._aabb_bounds = [float('inf'), float('-inf'),  # x-dim
                             float('inf'), float('-inf'),  # y-dim
                             float('inf'), float('-inf')]  # z-dim
        # activity part, unit: Bq/kg
        # specific activity of nuclides at different interval, shape=(INTV, NUC)
        self._act = np.zeros(shape=(0, 0), dtype=float, order='C')
        self._act_max_contri_nuc = []  # read only
        # specific activity of max contribution nuclide
        self._act_max_contri_act = np.zeros(shape=(0, 0), dtype=float,
                                            order='C')
        self._act_max_contri_ratio = np.zeros(shape=(0, 0), dtype=float)
        self._total_act = np.zeros(0, dtype=float)
        self._total_alpha_act = np.zeros(shape=(0), dtype=float)
        # decay heat part, unit: kW/kg
        self._decay_heat = np.zeros(shape=(0, 0), dtype=float)
        self._decay_heat_max_contri_nuc = []
        self._decay_heat_max_contri_dh = np.zeros(shape=(0, 0), dtype=float)
        self._decay_heat_max_contri_ratio = np.zeros(shape=(0, 0), dtype=float)
        self._total_decay_heat = np.zeros(0, dtype=float)
        # contact dose part,
        self._contact_dose = np.zeros(shape=(0, 0), dtype=float)
        self._contact_dose_max_contri_nuc = []
        self._contact_dose_max_contri_cd = np.zeros(shape=(0, 0), dtype=float)
        self._contact_dose_max_contri_ratio = np.zeros(
            shape=(0, 0), dtype=float)
        self._total_contact_dose = []
        # Clear Index part
        self._ci = np.zeros(shape=(0, 0), dtype=float)
        self._ci_max_contri_nuc = []
        self._ci_max_contri_ci = np.zeros(shape=(0, 0), dtype=float)
        self._ci_max_contri_ratio = np.zeros(shape=(0, 0), dtype=float)
        self._total_ci = np.zeros(0, dtype=float)
        # irradiation damage part
        self._dpa = None
        self._He_production = None
        self._H_production = None
        # radwaste part
        # CHN2018
        self._rw_chn2018_index_sum = None
        self._radwaste_class_chn2018 = []
        self._ci_chn2018 = np.zeros(shape=(0, 0), dtype=float)
        self._ci_chn2018_max_contri_nuc = []
        self._ci_chn2018_max_contri_ci = np.zeros(shape=(0, 0), dtype=float)
        self._ci_chn2018_max_contri_ratio = np.zeros(shape=(0, 0), dtype=float)
        self._total_ci_chn2018 = np.zeros(0, dtype=float)
        self._llw_chn2018 = np.zeros(shape=(0, 0), dtype=float)
        self._llw_chn2018_max_contri_nuc = []
        self._llw_chn2018_max_contri_llw = np.zeros(shape=(0, 0), dtype=float)
        self._llw_chn2018_max_contri_ratio = np.zeros(
            shape=(0, 0), dtype=float)
        self._total_llw_chn2018 = np.zeros(0, dtype=float)
        # USNRC
        self._rw_usnrc_index_sum_ll = None
        self._rw_usnrc_index_sum_sl = None
        self._radwaste_class_usnrc = []
        self._ci_usnrc = np.zeros(shape=(0, 0), dtype=float)
        self._total_ci_usnrc = np.zeros(0, dtype=float)
        # USNRC_FETTER
        self._rw_usnrc_fetter_index_sum = None
        self._radwaste_class_usnrc_fetter = []
        # UK
        self._radwaste_class_uk = []
        # RUSSIAN
        self._rw_russian_index_sum = None
        self._radwaste_class_russian = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError('name must be string')
        self._name = value

    # icl getter and setter
    @property
    def icl(self):
        return self._icl

    @icl.setter
    def icl(self, value):
        if not isinstance(value, int):
            raise ValueError('icl must be integer')
        if value < 1 or value > 99999999:
            raise ValueError('icl must between 1 and 99999999')
        self._icl = value

    # id setter and getter
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) and not isinstance(value, str):
            raise ValueError(f'id must be integer or string, given {value}')
        if isinstance(value, int):
            if value < 1 or value > 99999999:
                raise ValueError(
                    f'cell id must between 1 and 99999999, given {value}')
        self._id = value

    def assign_default_id(self):
        """Assign default cell id if it is not provided"""
        if Cell.cells_ids:
            self._id = max(Cell.cells_ids) + 1
        else:
            self._id = 1

    # mid setter and getter
    @property
    def mid(self):
        return self._mid

    @mid.setter
    def mid(self, value):
        if not isinstance(value, int):
            raise ValueError('mid must be integer')
        if value < 0 or value > 100000:
            raise ValueError('mid must between 0 and 100000')
        self._mid = value

    @property
    def mat(self):
        return self._mat

    @mat.setter
    def mat(self, value):
        if not isinstance(value, Material):
            raise ValueError('mat must be a object of class Material')
        self._mat = value

    @property
    def surf_list(self):
        return self._surf_list

    @surf_list.setter
    def self_list(self, value):
        if not isinstance(value, list):
            raise ValueError('surf_list of cell must be a list')
        for i, surf in value:
            if not isinstance(value, int):
                raise ValueError('surf_list should be a list of int')
        self._surf_list = value

    @property
    def surf_sign(self):
        return self._surf_sign

    @surf_sign.setter
    def self_sign(self, value):
        if not isinstance(value, list):
            raise ValueError('surf_sign of cell must be a list')
        for i, surf in value:
            if not isinstance(value, str):
                raise ValueError('surf_sign should be a list of string')
            if value not in ('*', '+', ''):
                raise ValueError('surf sign {0} not support'.format(value))
        self._surf_sign = value

    @property
    def imp_n(self):
        return self._imp_n

    @imp_n.setter
    def imp_n(self, value):
        if value < 0:
            raise ValueError('imp_n must be a number that no smaller than 0')
        self._imp_n = value

    @property
    def imp_p(self):
        return self._imp_p

    @imp_p.setter
    def imp_p(self, value):
        if value < 0:
            raise ValueError('imp_p must be a number that no smaller than 0')
        self._imp_p = value

    @property
    def fill(self):
        return self._fill

    @fill.setter
    def fill(self, value):
        if not isinstance(value, tuple):
            raise ValueError('fill must be a tuple')
        if len(value) != 3:
            raise ValueError(
                'fill must be a tuple with three elements: (fill_number, star_flag, rotation_matrix)')
        self._fill = value

    @property
    def u(self):
        return self._u

    @u.setter
    def u(self, value):
        if not isinstance(value, int):
            raise ValueError('universe must be an integer')
        if value < 0:
            raise ValueError(
                'universe must be a number that no smaller than 0')
        self._u = value

    @property
    def vol(self):
        return self._vol

    @vol.setter
    def vol(self, value):
        if not isinstance(value, float):
            raise ValueError('vol of cell must be a float')
        if value < 0:
            raise ValueError('vol must be a float that no smaller than 0')
        self._vol = value

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, value):
        if not isinstance(value, float):
            raise ValueError('mass of cell must be a float')
        if value < 0:
            raise ValueError('mass of cell must be a float no smaller than 0')
        self._mass = value

    @property
    def density(self):
        return self._density

    @density.setter
    def density(self, value):
        if not isinstance(value, float):
            raise ValueError('density of cell must be a float')
        if value < 0:
            raise ValueError('density of cell must between 0 and 30')
        if value > 30:
            print(
                f'Warning: density of cell {self.id} exceed 30, maybe nonphysical')
        self._density = value

    @property
    def neutron_flux(self):
        return self._neutron_flux

    @neutron_flux.setter
    def neutron_flux(self, value):
        if not isinstance(value, list):
            raise ValueError('neutron_flux of cell must be a list')
        if len(value) not in [70, 176, 316, 710]:
            raise ValueError('neutron flux should have data of 70/176/316/710, \
                    with the last of total data')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError(
                    'neutron_flux of cell must be a list of float')
            if value[i] < 0:
                raise ValueError('neutron_flux must be a list that each element\
                        is no smaller than 0.0')
        self._neutron_flux = value

    @property
    def neutron_flux_error(self):
        return self._neutron_flux_error

    @neutron_flux_error.setter
    def neutron_flux_error(self, value):
        if not isinstance(value, list):
            raise ValueError('neutron_flux_error must be a list')
        if len(value) not in [70, 176, 316, 710]:
            raise ValueError('neutron flux should have data of 70/176/316/710, \
                    the last of total data')
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
            raise ValueError('gamma_emit_rate must be a two-dimensional\
                    ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('gamma_emit_rate must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('gamma_emit_rate must no smaller than 0.0')
        except:
            pass
        self._gamma_emit_rate = value

    @property
    def nuclides(self):
        return self._nuclides

    @nuclides.setter
    def nuclides(self, value):
        if not isinstance(value, list):
            raise ValueError('nuclides of cell must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], str):
                raise ValueError('nuclides of cell should be a list of string')
        self._nuclides = value

    @property
    def half_lives(self):
        return self._half_lives

    @half_lives.setter
    def half_lives(self, value):
        if not isinstance(value, list):
            raise ValueError('half_lives must a list')
        for i in range(len(value)):
            if not isinstance(value[i], float):
                raise ValueError('half_lives of nuclides must be float')
            if value[i] < 0:
                raise ValueError('half_lives of nuclides should be no smaller\
                        than 0.0')
        self._half_lives = value

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, value):
        if not isinstance(value, np.ndarray):
            raise ValueError('points must a np.ndarray')
        self._points = value

    @property
    def aabb_bounds(self):
        return self._aabb_bounds

    @aabb_bounds.setter
    def aabb_bounds(self, value):
        if not isinstance(value, list):
            raise ValueError('aabb_bounds must a list')
        if len(self._aabb_bounds) != 6:
            raise ValueError('size of aabb_bounds must be 6')
        for i in range(len(value)):
            if not (isinstance(value[i], int) or isinstance(value[i], float)):
                raise ValueError('aabb_bounds of must be float')
        self._aabb_bounds = value

    @property
    def act(self):
        return self._act

    @act.setter
    def act(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('act must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('act must be a two-dimensional ndarray')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    f'act must no smaller than 0.0, error data {value.min()}')
        except:
            pass
        self._act = value.astype(np.float)

    @property
    def act_max_contri_nuc(self):
        return self._act_max_contri_nuc

    @property
    def act_max_contri_act(self):
        return self._act_max_contri_act

    @property
    def act_max_contri_ratio(self):
        return self._act_max_contri_ratio

    @property
    def total_act(self):
        return self._total_act

    @property
    def total_alpha_act(self):
        return self._total_alpha_act

    @total_alpha_act.setter
    def total_alpha_act(self, value):
        if not isinstance(value, type(np.ndarray((0)))):
            raise ValueError('total_alpha_act must be ndarray')
        if len(value.shape) != 1:
            raise ValueError(
                'total_alpha_act must be a one-dimensional ndarray')
        for i in range(value.shape[0]):
            if not isinstance(value[i], float):
                raise ValueError('total_alpha_act must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('total_alpha_act must no smaller than 0.0')
        except:
            pass
        self._total_alpha_act = value

    @property
    def decay_heat(self):
        return self._decay_heat

    @decay_heat.setter
    def decay_heat(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('decay heat must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('decay heat must be a two-dimensional ndarray')
        try:
            if value.min() < 0.0:
                raise ValueError('act must no smaller than 0.0')
        except:
            pass
        self._decay_heat = value.astype(np.float)

    @property
    def decay_heat_max_contri_nuc(self):
        return self._decay_heat_max_contri_nuc

    @property
    def decay_heat_max_contri_dh(self):
        return self._decay_heat_max_contri_dh

    @property
    def decay_heat_max_contri_ratio(self):
        return self._decay_heat_max_contri_ratio

    @property
    def total_decay_heat(self):
        return self._total_decay_heat

    @property
    def contact_dose(self):
        return self._contact_dose

    @contact_dose.setter
    def contact_dose(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('contact_dose must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('contact_dose must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('contact_dose must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('contact_dose must no smaller than 0.0')
        except:
            pass
        self._contact_dose = value.astype(np.float)

    @property
    def contact_dose_max_contri_nuc(self):
        return self._contact_dose_max_contri_nuc

    @property
    def contact_dose_max_contri_cd(self):
        return self._contact_dose_max_contri_cd

    @property
    def contact_dose_max_contri_ratio(self):
        return self._contact_dose_max_contri_ratio

    @property
    def total_contact_dose(self):
        return self._total_contact_dose

    @property
    def ci(self):
        return self._ci

    @ci.setter
    def ci(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('ci must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('ci must be a two-dimensional ndarray')
        try:
            if value.min() < 0.0:
                raise ValueError('ci must no smaller than 0.0')
        except:
            pass
        self._ci = value.astype(np.float)

    @property
    def ci_max_contri_nuc(self):
        return self._ci_max_contri_nuc

    @property
    def ci_max_contri_ci(self):
        return self._ci_max_contri_ci

    @property
    def ci_max_contri_ratio(self):
        return self._ci_max_contri_ratio

    @property
    def total_ci(self):
        return self._total_ci

    @property
    def ci_usnrc(self):
        return self._ci_usnrc

    @ci_usnrc.setter
    def ci_usnrc(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('ci_usnrc must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('ci_usnrc must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('ci_usnrc must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('ci_usnrc must no smaller than 0.0')
        except:
            pass
        self._ci_usnrc = value

    @property
    def total_ci_usnrc(self):
        return self._total_ci_usnrc

    @property
    def dpa(self):
        return self._dpa

    @dpa.setter
    def dpa(self, value):
        if not isinstance(value, float):
            raise ValueError('dpa value must be a float number')
        if value < 0:
            raise ValueError('dpa value must no smaller than 0.0')
        self._dpa = value

    @property
    def He_production(self):
        return self._He_production

    @He_production.setter
    def He_production(self, value):
        if not isinstance(value, float):
            raise ValueError('He_production value must be a float number')
        if value < 0:
            raise ValueError('He_production value must no smaller than 0.0')
        self._He_production = value

    @property
    def H_production(self):
        return self._H_production

    @H_production.setter
    def H_production(self, value):
        if not isinstance(value, float):
            raise ValueError('H_production value must be a float number')
        if value < 0:
            raise ValueError('H_production value must no smaller than 0.0')
        self._H_production = value

    @property
    def rw_chn2018_index_sum(self):
        return self._rw_chn2018_index_sum

    @rw_chn2018_index_sum.setter
    def rw_chn2018_index_sum(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('rw_chn2018_index_sum must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'rw_chn2018_index_sum must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError(
                        'rw_chn2018_index_sum must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    'rw_chn2018_index_sum must no smaller than 0.0')
        except:
            pass
        self._rw_chn2018_index_sum = value

    @property
    def ci_chn2018(self):
        return self._ci_chn2018

    @ci_chn2018.setter
    def ci_chn2018(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('ci_chn2018 must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('ci_chn2018 must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('ci_chn2018 must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('ci_chn2018 must no smaller than 0.0')
        except:
            pass
        self._ci_chn2018 = value

    @property
    def ci_chn2018_max_contri_nuc(self):
        return self._ci_chn2018_max_contri_nuc

    @property
    def ci_chn2018_max_contri_ci(self):
        return self._ci_chn2018_max_contri_ci

    @property
    def ci_chn2018_max_contri_ratio(self):
        return self._ci_chn2018_max_contri_ratio

    @property
    def total_ci_chn2018(self):
        return self._total_ci_chn2018

    @property
    def rw_usnrc_index_sum_ll(self):
        return self._rw_usnrc_index_sum_ll

    @property
    def llw_chn2018(self):
        return self._llw_chn2018

    @llw_chn2018.setter
    def llw_chn2018(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('llw_chn2018 must be ndarray')
        if len(value.shape) != 2:
            raise ValueError('llw_chn2018 must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError('llw_chn2018 must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError('llw_chn2018 must no smaller than 0.0')
        except:
            pass
        self._llw_chn2018 = value

    @property
    def llw_chn2018_max_contri_nuc(self):
        return self._llw_chn2018_max_contri_nuc

    @property
    def llw_chn2018_max_contri_llw(self):
        return self._llw_chn2018_max_contri_llw

    @property
    def llw_chn2018_max_contri_ratio(self):
        return self._llw_chn2018_max_contri_ratio

    @property
    def total_llw_chn2018(self):
        return self._total_llw_chn2018

    @rw_usnrc_index_sum_ll.setter
    def rw_usnrc_index_sum_ll(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('rw_usnrc_index_sum_ll must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'rw_usnrc_index_sum_ll must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError(
                        'rw_usnrc_index_sum_ll must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    'rw_usnrc_index_sum_ll must no smaller than 0.0')
        except:
            pass
        self._rw_usnrc_index_sum_ll = value

    @property
    def rw_usnrc_index_sum_sl(self):
        return self._rw_usnrc_index_sum_sl

    @rw_usnrc_index_sum_sl.setter
    def rw_usnrc_index_sum_sl(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('rw_usnrc_index_sum_sl must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'rw_usnrc_index_sum_sl must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError(
                        'rw_usnrc_index_sum_sl must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    'rw_usnrc_index_sum_sl must no smaller than 0.0')
        except:
            pass
        self._rw_usnrc_index_sum_sl = value

    @property
    def rw_usnrc_fetter_index_sum(self):
        return self._rw_usnrc_fetter_index_sum

    @rw_usnrc_fetter_index_sum.setter
    def rw_usnrc_fetter_index_sum(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('rw_usnrc_fetter_index_sum must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'rw_usnrc_fetter_index_sum must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError(
                        'rw_usnrc_fetter_index_sum must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    'rw_usnrc_fetter_index_sum must no smaller than 0.0')
        except:
            pass
        self._rw_usnrc_fetter_index_sum = value

    @property
    def rw_russian_index_sum(self):
        return self._rw_russian_index_sum

    @rw_russian_index_sum.setter
    def rw_russian_index_sum(self, value):
        if not isinstance(value, type(np.ndarray((0, 0)))):
            raise ValueError('rw_russian_index_sum must be ndarray')
        if len(value.shape) != 2:
            raise ValueError(
                'rw_russian_index_sum must be a two-dimensional ndarray')
        for i in range(value.shape[0]):
            for j in range(value.shape[1]):
                if not isinstance(value[i, j], float):
                    raise ValueError(
                        'rw_russian_index_sum must composed of float')
        try:
            if value.min() < 0.0:
                raise ValueError(
                    'rw_russian_index_sum must no smaller than 0.0')
        except:
            pass
        self._rw_russian_index_sum = value

    def update_material(self, mat):
        """
        Update material information from given material.
        The mid, mat, density will be updated.
        """
        self._mat = mat
        self._mid = mat.id
        self._density = mat.density
        return

    def treat_nuc_responses(self, nuc, level):
        """
        Reset the property of the [nuc] to specific [level]. And adjust the
        corresponding total values.
        """
        nidx = self.nuclides.index(nuc)  # find nuc index
        for intv in range(len(self.act)):
            self.act[intv, nidx] = self.act[intv, nidx] * level
            self.decay_heat[intv, nidx] = self.decay_heat[intv, nidx] * level
            self.contact_dose[intv,
                              nidx] = self.contact_dose[intv, nidx] * level
            self.ci[intv, nidx] = self.ci[intv, nidx] * level

    def analysis_act(self):
        """get the act_max_contri_nuc, act_max_contri_act and
        act_max_contri_ratio"""
        # input check for nuclides, a
        if self._act.size == 0:
            raise ValueError('act not set before using')
        self._total_act = self.act.sum(axis=1)  # calculate the a_total
        # get the max nuclide
        indexes = get_max_contri_indexes(self.act)
        for idx in indexes:
            self._act_max_contri_nuc.append(self.nuclides[idx])
        self._act_max_contri_act = self.act[:, indexes]
        # cal the act_max_contri_ratio
        self._act_max_contri_ratio = contri_to_ratio(
            self.act_max_contri_act, self.total_act)

    def analysis_decay_heat(self):
        # input check for nuclides,
        if self._decay_heat.size == 0:
            raise ValueError('decay_heat not set before using')
        # calculate the a_total
        self._total_decay_heat = self.decay_heat.sum(axis=1)
        # get the max nuclides
        indexes = get_max_contri_indexes(self.decay_heat)
        for idx in indexes:
            self._decay_heat_max_contri_nuc.append(self.nuclides[idx])
        self._decay_heat_max_contri_dh = self.decay_heat[:, indexes]
        # cal the act_max_contri_ratio
        self._decay_heat_max_contri_ratio = contri_to_ratio(
            self.decay_heat_max_contri_dh, self.total_decay_heat)

    def analysis_contact_dose(self):
        # input check for nuclides
        if self._contact_dose.size == 0:
            raise ValueError('contact_dose not set before using')
        # calculate the a_total
        self._total_contact_dose = self._contact_dose.sum(axis=1)
        # get the max nuclides
        indexes = get_max_contri_indexes(self.contact_dose)
        for idx in indexes:
            self._contact_dose_max_contri_nuc.append(self.nuclides[idx])
        self._contact_dose_max_contri_cd = self.contact_dose[:, indexes]
        # cal the act_max_contri_ratio
        self._contact_dose_max_contri_ratio = contri_to_ratio(
            self.contact_dose_max_contri_cd, self.total_contact_dose)

    def analysis_ci(self):
        # input check for nuclides, a
        if self._ci.size == 0:
            raise ValueError('ci not set before using')
        self._total_ci = self.ci.sum(axis=1)  # calculate the a_total
        # get the max nuclides
        indexes = get_max_contri_indexes(self.ci)
        for idx in indexes:
            self._ci_max_contri_nuc.append(self.nuclides[idx])
        self._ci_max_contri_ci = self.ci[:, indexes]
        # cal the ci_max_contri_ratio
        self._ci_max_contri_ratio = contri_to_ratio(
            self.ci_max_contri_ci, self._total_ci)

    def analysis_ci_chn2018(self):
        # input check for nuclides, a
        if self._ci_chn2018.size == 0:
            raise ValueError('ci_chn2018 not set before using')
        self._total_ci_chn2018 = self.ci_chn2018.sum(
            axis=1)  # calculate the a_total
        # get the max nuclides
        indexes = get_max_contri_indexes(self.ci_chn2018)
        for idx in indexes:
            self._ci_chn2018_max_contri_nuc.append(self.nuclides[idx])
        self._ci_chn2018_max_contri_ci = self.ci_chn2018[:, indexes]
        # cal the ci_max_contri_ratio
        self._ci_chn2018_max_contri_ratio = contri_to_ratio(
            self.ci_chn2018_max_contri_ci, self._total_ci_chn2018)

    def analysis_llw_chn2018(self):
        # input check for nuclides, a
        if self._llw_chn2018.size == 0:
            raise ValueError('llw_chn2018 not set before using')
        self._total_llw_chn2018 = self.llw_chn2018.sum(
            axis=1)  # calculate the a_total
        # get the max nuclides
        indexes = get_max_contri_indexes(self.llw_chn2018)
        for idx in indexes:
            self._llw_chn2018_max_contri_nuc.append(self.nuclides[idx])
        self._llw_chn2018_max_contri_llw = self.llw_chn2018[:, indexes]
        # cal the llw_max_contri_ratio
        self._llw_chn2018_max_contri_ratio = contri_to_ratio(
            self.llw_chn2018_max_contri_llw, self._total_llw_chn2018)

    def analysis_radwaste(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            The standard used.
            Supported standards are: CHN2018, UK, USNRC, USNRC_FETTER, RUSSIAN.
        """
        if rws.standard == 'CHN2018':
            self.analysis_radwaste_chn2018(rws)
        elif rws.standard == 'USNRC':
            self.analysis_radwaste_usnrc(rws)
        elif rws.standard == 'USNRC_FETTER':
            self.analysis_radwaste_usnrc_fetter(rws)
        elif rws.standard == 'UK':
            self.analysis_radwaste_uk(rws)
        elif rws.standard == 'RUSSIAN':
            self.analysis_radwaste_russian(rws)
        else:
            raise ValueError("rws {0} not supported!".format(rws.standard))

    def analysis_radwaste_chn2018(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            The standard used, must be CHN2018.
        """

        # init rw_index with shape of (INTV, NUC, class)
        rw_index = np.zeros(shape=(len(self.act),
                                   len(self.act[0]), len(rws.classes)), dtype=float)

        # calculate radwaste index for each nuclides
        for nid, nuc in enumerate(self.nuclides):
            # get the limits for the nuclides
            limits = rws.get_nuc_limits(nuc=nuc)
            # loop over the interval
            for intv in range(len(self.act)):
                # calculate the index for each class
                rw_index[intv, nid, :] = np.divide(self.act[intv, nid], limits)

        # assign the ci_chn2018
        self.ci_chn2018 = rw_index[:, :, 0]
        self.analysis_ci_chn2018()
        self.llw_chn2018 = rw_index[:, :, 2]
        self.analysis_llw_chn2018()

        # sum up the index for each nuclide, shape=(INTV, class)
        rw_index_sum = np.sum(rw_index, axis=1)

        # get the radwaste classification according to the indices for each class
        rw_class = []
        for intv in range(len(self.act)):
            # CHN2018 use rw_index_sum and decay heat to classify radwaste
            # convert decay heat from kW/kg to kW/m3
            decay_heat = self.total_decay_heat[intv]  # kW/kg
            decay_heat = decay_heat * self.density * 1000.0  # kW/m3
            rw_class.append(rws.determine_class_chn2018(rw_index_sum[intv],
                                                        decay_heat))

        self.rw_chn2018_index_sum = rw_index_sum.copy()
        self.radwaste_class_chn2018 = rw_class

    def analysis_radwaste_usnrc(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            Supported standards is: USNRC.
        """

        # init rw_index with shape of (INTV, NUC, class)
        rw_index_sl = np.zeros(shape=(len(self.act),
                                      len(self.act[0]), len(rws.classes)), dtype=float)
        rw_index_ll = np.zeros(shape=(len(self.act),
                                      len(self.act[0]), len(rws.classes)), dtype=float)

        # calculate radwaste index for each nuclide
        for nid, nuc in enumerate(self.nuclides):
            # get the limits for the nuclides
            limits = rws.get_nuc_limits(nuc=nuc, half_life=self.half_lives[nid],
                                        density=self.density)
            # loop over the interval
            for intv in range(len(self.act)):
                # calculate the index for each class
                if nuc in ('Pu241', 'Cm242') or (not utils.is_short_live(self.half_lives[nid])):
                    rw_index_ll[intv, nid, :] = np.divide(
                        self.act[intv, nid], limits)
                else:
                    rw_index_sl[intv, nid, :] = np.divide(
                        self.act[intv, nid], limits)

        rw_usnrc_index_sum_ll = np.sum(rw_index_ll, axis=1)
        rw_usnrc_index_sum_sl = np.sum(rw_index_sl, axis=1)

        # calculate the clearance index for each nuclide
        ci_usnrc = np.zeros(
            shape=(len(self.act), len(self.act[0])), dtype=float)
        for nid, nuc in enumerate(self.nuclides):
            # get the ci limit for the nuclides
            limit = rws.get_nuc_limit_usnrc_clearance(nuc=nuc)
            for intv in range(len(self.act)):
                ci_usnrc[intv, nid] = self.act[intv, nid] / limit
        total_ci_usnrc = np.sum(ci_usnrc, axis=1)

        # get the radwaste classification according to the indices for each class
        rw_class = []
        for intv in range(len(self.act)):
            # USNRC use rw_usnrc_index_sum_sl and rw_usnrc_index_sum_ll to classify radwaste
            rw_cls = rws.determine_class_usnrc(rw_usnrc_index_sum_ll[intv],
                                               rw_usnrc_index_sum_sl[intv], total_ci_usnrc[intv])
            rw_class.append(rw_cls)

        self.rw_usnrc_index_sum_ll = rw_usnrc_index_sum_ll.copy()
        self.rw_usnrc_index_sum_sl = rw_usnrc_index_sum_sl.copy()
        self.ci_usnrc = ci_usnrc.copy()
        self._total_ci_usnrc = total_ci_usnrc.copy()
        self.radwaste_class_usnrc = rw_class

    def analysis_radwaste_usnrc_fetter(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            Supported standards is: USNRC_FETTER.
        """

        # init rw_index with shape of (INTV, NUC, class)
        rw_index = np.zeros(shape=(len(self.act),
                                   len(self.act[0]), len(rws.classes)), dtype=float)

        # calculate radwaste index for each nuclide
        for nid, nuc in enumerate(self.nuclides):
            # get the limits for the nuclides
            limits = rws.get_nuc_limits(nuc=nuc, half_life=self.half_lives[nid],
                                        density=self.density)
            # loop over the interval
            for intv in range(len(self.act)):
                # calculate the index for each class
                rw_index[intv, nid, :] = np.divide(self.act[intv, nid], limits)

        rw_index_sum = np.sum(rw_index, axis=1)

        # calculate the clearance index for each nuclide
        ci_usnrc = np.zeros(
            shape=(len(self.act), len(self.act[0])), dtype=float)
        for nid, nuc in enumerate(self.nuclides):
            # get the ci limits for the nuclides
            limit = rws.get_nuc_limit_usnrc_clearance(nuc=nuc)
            for intv in range(len(self.act)):
                ci_usnrc[intv, nid] = self.act[intv, nid] / limit
        total_ci_usnrc = np.sum(ci_usnrc, axis=1)

        # get the radwaste classification according to the indices for each class
        rw_class = []
        for intv in range(len(self.act)):
            # USNRC use rw_usnrc_index_sum_sl and rw_usnrc_index_sum_ll to classify radwaste
            rw_cls = rws.determine_class_usnrc_fetter(
                rw_index_sum[intv], total_ci_usnrc[intv])
            rw_class.append(rw_cls)

        self.rw_usnrc_fetter_index_sum = rw_index_sum.copy()
        self.ci_usnrc = ci_usnrc.copy()
        self._total_ci_usnrc = total_ci_usnrc.copy()
        self.radwaste_class_usnrc_fetter = rw_class

    def analysis_radwaste_uk(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            The standard used, must be UK.
        """

        # get the radwaste classification according to the:
        # alpha activity, activity and decay heat
        rw_class = []
        for intv in range(len(self.total_act)):
            # convert decay heat from kW/kg to kW/m3
            decay_heat = self.total_decay_heat[intv]  # kW/kg
            decay_heat = decay_heat * self.density * 1000.0  # kW/m3
            rw_class.append(rws.determine_class_uk(self.total_alpha_act[intv],
                                                   self.total_act[intv], decay_heat, self.total_ci[intv]))
        self.radwaste_class_uk = rw_class

    def analysis_radwaste_russian(self, rws=None):
        """
        Analysis the radwaste classification.

        Parameters:
        -----------
        rws: RadwasteStandard
            The standard used, must be RUSSIAN.
        """

        # init rw_index with shape of (INTV, NUC, class)
        rw_index = np.zeros(shape=(len(self.act),
                                   len(self.act[0]), 1), dtype=float)

        # calculate radwaste index for each nuclide
        for nid, nuc in enumerate(self.nuclides):
            # get the limits for the nuclides
            limits = rws.get_nuc_limits(nuc=nuc)
            # loop over the interval
            for intv in range(len(self.act)):
                # calculate the index for each class
                rw_index[intv, nid, :] = np.divide(self.act[intv, nid], limits)

        # sum up the index for each nuclide, shape=(INTV, class)
        rw_index_sum = np.sum(rw_index, axis=1)

        # get the radwaste classification according to the indices for each class
        rw_class = []
        for intv in range(len(self.act)):
            rw_class.append(rws.determine_class_russian(rw_index_sum[intv]))
        self.rw_russian_index_sum = rw_index_sum.copy()
        self.radwaste_class_russian = rw_class

    def __str__(self):
        """print mcnp style cell card"""
        s = ''.join([str(self.id), '     ', str(self.mat.id),
                    ' ', '-', str(self.mat.density)])
        indent_length = len(s)
        for key, value in self.geom:
            if key == 'intersection':
                bool_mark = ''
            elif key == 'union':
                bool_mark = ':'
            elif key == 'complement':
                bool_mark = '#'
            for j, hs in enumerate(value):
                if hs.sense == '-':
                    hs_sense_str = hs.sense
                else:
                    hs_sense_str = ''
                hs_str = ''.join([bool_mark, hs_sense_str, str(hs.surf.id)])
                s = mcnp_input.mcnp_style_str_append(s, hs_str, indent_length)
        s = mcnp_input.mcnp_style_str_append(
            s, ''.join(['imp:n=', str(self.imp_n)]))
        if self.imp_p is not None:
            s = mcnp_input.mcnp_style_str_append(
                s, ''.join(['imp:p=', str(self.imp_p)]))
        return s

    def calc_aabb_bounds(self):
        """
        Update the AABB bounds of the cell.
        """

        self.aabb_bounds[0] = min(self.points[:, 0])
        self.aabb_bounds[1] = max(self.points[:, 0])
        self.aabb_bounds[2] = min(self.points[:, 1])
        self.aabb_bounds[3] = max(self.points[:, 1])
        self.aabb_bounds[4] = min(self.points[:, 2])
        self.aabb_bounds[5] = max(self.points[:, 2])

    def has_valid_aabb_bounds(self):
        """Check whether the aabb bounds are valid"""
        if self.imp_n == 0:
            return True  # ignore if the cell has 0 importance
        if abs(min(self.aabb_bounds)) == float('inf') or abs(max(self.aabb_bounds)) == float('inf'):
            return False
        else:
            return True

    def calc_cutting_coords(self, coords, direction='X'):
        """
        Calculate the coordinates of the cutting plane
        """
        idx_dir = ord(direction.upper()) - ord('X')
        # determine the cut planes according to aabb
        cutting_coords = []
        for i in range(len(coords)):
            if coords[i] > self.aabb_bounds[idx_dir*2] and coords[i] < self.aabb_bounds[idx_dir*2+1]:
                cutting_coords.append(coords[i])
        # remove the coords when the cell are separated -> there is no points between two plane
        bins = [float('-inf')]
        for coord in coords:
            bins.append(coord)
        bins.append(float('inf'))
        inds = np.digitize(self.points[:, idx_dir], bins=bins)
        inds = sorted(list(set(inds)))
        cutting_coords = []
        for idx in inds[:-1]:
            cutting_coords.append(bins[idx])
        return cutting_coords

    def calc_divide_planes(self, distance=10.0):
        """
        Split the cell if it is too large (length > distance) on either one dimension.

        Parameters:
        -----------
        distance: float
            The distance to split the cell.

        Returns:
        --------
        x_coords : list of floats
            The x-coords of the plane
        y_coords : list of floats
            The y-coords of the plane
        z_coords : list of floats
            The z-coords of the plane
        """
        x_coords, y_coords, z_coords = [], [], []
        # do not split if it's graveyard or filled by universe
        if self.imp_n == 0 or self.fill or not self.has_valid_aabb_bounds():
            return x_coords, y_coords, z_coords
        for i in range(math.floor(self.aabb_bounds[0]), math.ceil(self.aabb_bounds[1]), distance):
            if i > self.aabb_bounds[0]:
                x_coords.append(i)
        for i in range(math.floor(self.aabb_bounds[2]), math.ceil(self.aabb_bounds[3]), distance):
            if i > self.aabb_bounds[2]:
                y_coords.append(i)
        for i in range(math.floor(self.aabb_bounds[4]), math.ceil(self.aabb_bounds[5]), distance):
            if i > self.aabb_bounds[4]:
                z_coords.append(i)
        return x_coords, y_coords, z_coords


def is_item_cell(item, cells=None):
    """
    Check whether the item means a cell.
    The item can be converted to a int number existing in Cells list.

    Parameters:
    -----------
    item : int or str
    """
    if isinstance(item, str):
        try:
            cid = int(item)
        except:  # can not convert to int
            return False
    elif isinstance(item, int):
        cid = item
    else:  # wrong type
        return False

    if cells is None:
        return True
    else:  # check whether item in cell list if cells provided
        try:
            cidx = utils.find_index_by_property(cid, cells, 'id')
            return True
        except:
            return False


def get_max_contri_indexes(values):
    """
    Get the indexes of nuclides take max contribution for each interval.

    Parameters:
    -----------
    values : numpy array (2D)
        The values to compare

    Returns:
    --------
    indexes : list of int
        The ordered indexes.
    """

    indexes = []
    for i in range(len(values)):
        # find the index of max value (could be more than one value)
        idx = np.where(values[i] == np.max(values[i]))[0]
        for j in idx:
            if j not in indexes and values[i][j] > 0:
                indexes.append(j)
    return indexes


def contri_to_ratio(values, total_value):
    results = values.copy()
    for i in range(values.shape[0]):
        for j in range(values.shape[1]):
            if total_value[i] > 0:
                results[i][j] = results[i][j] / total_value[i]
            else:
                results[i][j] = 0.0
    return results


def split_cell(c, coords, distance=10, geom='xyz', direction='x',
               cell_id_start=10000):
    """
    Split a cell.

    Parameters:
    -----------
    c : Cell
        The cell to split
    coords : list of floats
        The coordinates of the surfaces to divide the cell
    distance : float
        The distance between cutting surfaces
    geom : string
        The geometry representation used.
        Currently supports: 'xyz'
    direction : string
        The direction to split
    cell_id_start : int
        The start id of the new cells

    Returns:
    --------
    cells : list
        The split smaller cells geometry information
    start : int
        The index of the start of the coords that cut the cell
    end : int
        The index of the last coords cutting the cell
    """
    if len(coords) == 0:  # do not split if the cell is small
        return [c], []

    idx_dir = ord(direction.upper()) - ord('X')
    # do not cut if cell length is small in the direction
    if (c.aabb_bounds[idx_dir*2+1] - c.aabb_bounds[idx_dir*2]) <= distance:
        return [c], []

    # determine the cut planes
    cutting_coords = c.calc_cutting_coords(coords, direction=direction)

    # split cells
    counter = 0
    cells = []
    for i in range(len(cutting_coords)+1):
        c_ = Cell(id=cell_id_start+counter)
        c_.mid = c.mid
        c_.density = c.density
        c_.imp_n = c.imp_n
        if c.imp_p is not None:
            c_.imp_p = c.imp_p
        if c.u is not None:
            c_.u = c.u
        if c.fill is not None:
            c_.fill = c.fill
        cells.append(c_)
        counter += 1
    return cells, cutting_coords
