#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import re
import numpy as np
import pandas as pd
from natf.cell import Cell
from natf import mcnp_input, utils

gamma_energy_upper_bounds = [0.01, 0.02, 0.05, 0.10, 0.20, 0.30, 0.40, 0.60,
                             0.80, 1.00, 1.22, 1.44, 1.66, 2.00, 2.50, 3.00,
                             4.00, 5.00, 6.50, 8.00, 10.00, 12.00, 14.00, 20.00]


class Part(object):
    '''class Part'''

    def __init__(self, id=''):
        self._id = id  # id, or name of the part
        self._dirname = None  # directory for output files
        self._cell_ids = []  # list of cell ids
        self._removed_cids = []  # removed invalid cell ids
        self._subpart_ids = []
        self._part_cell_list = []  # a lis of Cell
        self._part_subpart_list = []  # list of sub parts
        self._mass_flow_rate = 0.0  # mass flow rate of this part
        self._node_part_count = []  # number of BLK modules merge into this node

    def __str__(self):
        p_str = f"Part id: {self.id}"
        p_str = f"{p_str}\npart_cell_list:"
        for c in self.part_cell_list:
            p_str = f"{p_str} {c.id}"
        return p_str

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, str):
            raise ValueError('part id must be string')
        self._id = value

    @property
    def dirname(self):
        return self._dirname

    @dirname.setter
    def dirname(self, value):
        if not isinstance(value, str):
            raise ValueError('dirname of the part must be string')
        self._dirname = value

    @property
    def cell_ids(self):
        return self._cell_ids

    @cell_ids.setter
    def cell_ids(self, value):
        if not isinstance(value, list):
            raise ValueError('cell_ids must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], int):
                raise ValueError('cell_ids must be a list of int')
        self._cell_ids = value

    @property
    def removed_cids(self):
        return self._removed_cids

    @removed_cids.setter
    def removed_cids(self, value):
        if not isinstance(value, list):
            raise ValueError('removed_cids must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], int):
                raise ValueError('removed_cids must be a list of int')
        self._removed_cids = value

    @property
    def subpart_ids(self):
        return self._subpart_ids

    @subpart_ids.setter
    def subpart_ids(self, value):
        if not isinstance(value, list):
            raise ValueError('subpart_ids must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], str):
                raise ValueError('subpart_ids must be a list of string')
        self._subpart_ids = value

    @property
    def part_cell_list(self):
        return self._part_cell_list

    @part_cell_list.setter
    def part_cell_list(self, value):
        if not isinstance(value, list):
            raise ValueError('part_cell_list must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], Cell):
                raise ValueError('part_cell_ist must be a list of Cell')
        self._part_cell_list = value

    @property
    def part_subpart_list(self):
        return self._part_cell_list

    @part_subpart_list.setter
    def part_subpart_list(self, value):
        if not isinstance(value, list):
            raise ValueError('part_subpart_list must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], Part):
                raise ValueError('part_subpart_ist must be a list of Cell')
        self._part_subpart_list = value

    @property
    def mass_flow_rate(self):
        return self._mass_flow_rate

    @mass_flow_rate.setter
    def mass_flow_rate(self, value):
        if not isinstance(value, float):
            raise ValueError('mass flow rate of the part must be float')
        if value < 0.0:
            raise ValueError('mass flow rate must >= 0.0')
        self._mass_flow_rate = value

    @property
    def node_part_count(self):
        return self._node_part_count

    @node_part_count.setter
    def node_part_count(self, value):
        if not isinstance(value, list) and not isinstance(value, np.ndarray):
            raise ValueError('node_part_count must be a list')
        for i in range(len(value)):
            if not isinstance(value[i], int) and not isinstance(value[i], np.int64):
                raise ValueError('node_part_count must be a list of int')
        self._node_part_count = value

    @property
    def equal_cell(self):
        return self._equal_cell

    def init_equal_cell(self):
        """
        Calculate the equal_cell:
        - id (use part name)
        - vol (sum)
        - mass (sum) 
        - density (average)
        - neutron flux (vol average)
        """
        self._equal_cell = Cell()
        self._equal_cell.id = self.id
        # check part_cell_list
        if len(self.part_cell_list) >= 1:
            # merge basic info. vol, mass and density
            for c in self.part_cell_list:  # vol and mass
                self.equal_cell.vol += c.vol
                self.equal_cell.mass += c.mass
            self.equal_cell.density = self.equal_cell.mass / self.equal_cell.vol  # density
            # neutron flux
            ave_flux = [0.0] * len(self.part_cell_list[0].neutron_flux)
            for i, c in enumerate(self.part_cell_list):
                for j in range(len(ave_flux)):
                    ave_flux[j] += c.vol / \
                        self.equal_cell.vol * c.neutron_flux[j]
            self.equal_cell.neutron_flux = ave_flux

    def merge_cell(self, aim):
        """merge_cell: a method of class Part
        function: merge the part_cell_list to make a equivalent cell
        data need to merge: basic: vol, mass, density
                            result data: nuclides, half_lives, act, decay_heat, ...
                            contact_dose, ci, dpa, He_production, H_production"""
        # check aim
        if aim not in ('CELL_ACT_POST', 'CELL_DPA_POST'):
            raise ValueError(
                'Part.merge_cell() can only be called when the aim is CELL_ACT/DPA_POST')
        if aim == 'CELL_ACT_POST':
            # treat nuclides and half_lives
            for c in self._part_cell_list:
                for i, nuc in enumerate(c.nuclides):
                    if nuc in self._equal_cell.nuclides:
                        pass
                    if nuc not in self._equal_cell.nuclides:
                        self._equal_cell.nuclides.append(nuc)
                        self._equal_cell.half_lives.append(c.half_lives[i])
            # treat act, decay_heat, contact_dose and ci
            # first, resize the act, decay_heat, contact_dose and ci
            NUC = len(self._equal_cell.nuclides)
            INTV = self._part_cell_list[0].act.shape[0]
            self._equal_cell.act = np.resize(self._equal_cell.act, (INTV, NUC))
            self._equal_cell.total_alpha_act = np.resize(
                self._equal_cell.total_alpha_act, (INTV))
            self._equal_cell.decay_heat = np.resize(
                self._equal_cell.decay_heat, (INTV, NUC))
            self._equal_cell.contact_dose = np.resize(
                self._equal_cell.contact_dose, (INTV, NUC))
            self._equal_cell.ci = np.resize(self._equal_cell.ci, (INTV, NUC))
            # merge the data
            for c in self._part_cell_list:
                for i, nuc in enumerate(c.nuclides):
                    nid = self._equal_cell._nuclides.index(nuc)
                    for intv in range(INTV):
                        self._equal_cell.act[intv][nid] += c.act[intv][i] * (
                            c.mass / self._equal_cell.mass)  # unit: Bq/kg
                        self._equal_cell.decay_heat[intv][nid] += c.decay_heat[intv][i] * (
                            c.mass / self._equal_cell.mass)  # kW/kg
                        self._equal_cell.contact_dose[intv][nid] += c.contact_dose[intv][i] * (
                            c.mass / self._equal_cell.mass)  # unit: Sv/h
                        self._equal_cell.ci[intv][nid] += c.ci[intv][i] * \
                            (c.mass / self._equal_cell.mass)
                for intv in range(INTV):
                    self._equal_cell.total_alpha_act[intv] += c.total_alpha_act[intv] * (
                        c.mass / self._equal_cell.mass)
        if aim == 'CELL_DPA_POST':
            # dpa and gas production
            dpa, He_production, H_production = 0.0, 0.0, 0.0
            for c in self._part_cell_list:
                dpa += c.dpa * (c.mass / self._equal_cell.mass)
                He_production += c.He_production * \
                    (c.mass / self._equal_cell.mass)
                H_production += c.H_production * \
                    (c.mass / self._equal_cell.mass)
            self._equal_cell.dpa = dpa
            self._equal_cell.He_production = He_production
            self._equal_cell.H_production = H_production

    def part_act_analysis(self, aim, rwss=[]):
        """
        Analysis the:
        - activity,
        - contact_dose,
        - decay_heat,
        - ci,
        - radwaste class (optional),
        of the Part, using the method the Cell.

        Parameters:
        -----------
        aim: aim, must be 'CELL_ACT_POST'
        rwss: list of RadwasteStandard, optional
            The standards used.
            Supported standards are: CHN2018, UK, USNRC, USNRC_FETTER.
        """

        # aim check
        if aim not in ['CELL_ACT_POST']:
            raise ValueError(
                'method act_analysis() of a Part should be called only when the aim is CELL_ACT_POST')
        # data prepare check
        if self._equal_cell.act.shape[0] < 1:
            raise ValueError(
                'method act_analysis() should be called after filling the data of act')
        # analysis the act info.
        # calculate the act_max_nuc, act_max_act and act_max_ratio
        self._equal_cell.analysis_act()
        # analysis the decay_heat
        self._equal_cell.analysis_decay_heat()
        # analysis the contact_dose
        self._equal_cell.analysis_contact_dose()
        # analysis the ci
        self._equal_cell.analysis_ci()
        # analysis radwaste classification
        for rws in rwss:
            self._equal_cell.analysis_radwaste(rws=rws)

    def generate_directory(self, work_dir):
        """
        Generate directory name for output files.
        """
        self.dirname = os.path.join(work_dir, self._id)
        if not os.path.isdir(self.dirname):
            os.mkdir(self.dirname)

    def generate_output_filename(self, item):
        """
        Create output filename for specific file.
        """
        filename = os.path.join(self.dirname, ''.join([self._id, '.', item]))
        return filename

    def generate_output_title_line(self, item):
        """
        Generate output file title line for each item.
        """
        title_line = None
        # input item check
        if item == 'basicinfo':
            title_line = utils.data_to_line_1d(
                key=self._id, value='basic_information')
        if item == 'nuc':
            title_line = utils.data_to_line_1d(
                key='Nuclide', value=['Half_life(s)', 'Half_life'])
        if item in ['acts', 'act', 'dhv', 'dh', 'cd', 'ci', 'ci_chn2018', 'llw_chn2018']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.nuclides)
        if item in ['act_st_t']:
            value = ['total_specific_act(Bq/kg)', 'total_activity(Bq)']
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=value)
        if item in ['acts_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.act_max_contri_nuc)
        if item in ['acts_max']:
            title_line = utils.data_to_line_1d(key='Cooling_time(s)', value=[
                                               'Total'] + self._equal_cell.act_max_contri_nuc)
        if item in ['dh_vt_t']:
            value = ['total_decay_heat_vol(kW/m3)',
                     'total_decay_heat(kW)']
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=value)
        if item in ['dhv_max']:
            title_line = utils.data_to_line_1d(key='Cooling_time(s)', value=[
                                               'Total'] + self._equal_cell.decay_heat_max_contri_nuc)
        if item in ['dhv_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.decay_heat_max_contri_nuc)
        if item in ['cdt']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value='total_contact_dose(Sv/hr)')
        if item in ['cd_max']:
            title_line = utils.data_to_line_1d(key='Cooling_time(s)', value=[
                                               'Total'] + self._equal_cell.contact_dose_max_contri_nuc)
        if item in ['cd_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.contact_dose_max_contri_nuc)
        if item in ['cit']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=['total_ci'])
        if item == 'cit_chn2018':
            title_line = utils.data_to_line_1d(
                key='Cooling_times(s)', value=['total_ci_chn2018'])
        if item == 'llwt_chn2018':
            title_line = utils.data_to_line_1d(
                key='Cooling_times(s)', value=['total_llw_chn2018'])
        if item in ['ci_max']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=['Total'] + self._equal_cell.ci_max_contri_nuc)
        if item in ['ci_chn2018_max']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=['Total'] + self._equal_cell.ci_chn2018_max_contri_nuc)
        if item in ['llw_chn2018_max']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=['Total'] + self._equal_cell.llw_chn2018_max_contri_nuc)
        if item in ['ci_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.ci_max_contri_nuc)
        if item in ['ci_chn2018_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.ci_chn2018_max_contri_nuc)
        if item in ['llw_chn2018_max_ratio']:
            title_line = utils.data_to_line_1d(
                key='Cooling_time(s)', value=self._equal_cell.llw_chn2018_max_contri_nuc)
        if item in ['gamma_emit_rate']:
            title_line = utils.data_to_line_1d(key='Energy upper boundary (MeV)', value=[
                                               'Gamma emit rate (g/cc/s)'])
        if title_line is None:  # check
            raise ValueError("item {0} is not supported".format(item))
        return title_line

    def output_item(self, item, key, value):
        """
        Output item.

        Parameters:
        -----------
        item: string
            The postfix of the file.
        key: string, list or numpy array
            The key first column of the of the data.
        value: float, list or numpy array
            The data of the content to print.
        """
        filename = self.generate_output_filename(item)
        fo = open(filename, 'w')
        title_line = self.generate_output_title_line(item)
        fo.write(title_line)
        if isinstance(key, list) or isinstance(key, np.ndarray):
            for i in range(len(key)):
                line = utils.data_to_line_1d(key=key[i], value=value[i])
                fo.write(line)
        else:
            line = utils.data_to_line_1d(key=key, value=value)
            fo.write(line)
        fo.close()

    def output_basicinfo(self, model_degree):
        """
        Output basic infomation.
        """
        item = 'basicinfo'
        key = ["volume(cm3)", "mass(g)", "density(g/cm3)", "cell_ids"]
        value = [self._equal_cell.vol * 360.0 / model_degree,
                 self._equal_cell.mass * 360.0 / model_degree,
                 self._equal_cell.density]
        # cell ids
        cids_str = '['
        if len(self.cell_ids) > 1:
            for i, cid in enumerate(self.cell_ids):
                if i == 0:
                    cids_str = f"{cids_str}{cid} "
                elif i < len(self.cell_ids)-1:
                    cids_str = mcnp_input.mcnp_style_str_append(
                        cids_str, f"{cid} ")
                elif i == len(self.cell_ids)-1:
                    cids_str = mcnp_input.mcnp_style_str_append(
                        cids_str, f"{cid}")
            cids_str = f"{cids_str}]"
        if len(self.cell_ids) == 1:
            cids_str = f"[{self.cell_ids[0]}]"
        value.append(cids_str)
        self.output_item(item=item, key=key, value=value)

    def output_flux(self):
        """Output flux"""
        # write .flx file
        filename = self.generate_output_filename('flx')
        fo = open(filename, 'w')
        for i in range(len(self.equal_cell.neutron_flux) - 1):
            flux = self.equal_cell.neutron_flux[len(
                self.equal_cell.neutron_flux)-2-i]
            fo.write(
                f"{utils.format_single_output(flux)}\n")
        fo.write("1.0\n")
        fo.write(
            f"Neutron energy group 175 G, TOT = {self.equal_cell.neutron_flux[-1]}")
        fo.close()

        # write .flux file
        filename = self.generate_output_filename('flux')
        fo = open(filename, 'w')
        for i in range(len(self.equal_cell.neutron_flux) - 1):
            fo.write(
                f"{utils.format_single_output(self.equal_cell.neutron_flux[i])}\n")
        fo.close()

    def output_nuc(self):
        # output nuclides & half_lives
        item = 'nuc'
        key = self._equal_cell.nuclides
        half_lives = self._equal_cell.half_lives
        value = []
        for i in range(len(key)):
            if half_lives[i] < float('inf'):
                time, unit = utils.proper_time_unit(half_lives[i])
                time_prop = f"{utils.format_single_output(time)} {unit}"
                value.append([half_lives[i], time_prop])
            else:
                value.append(['Stable', 'Stable'])
        self.output_item(item=item, key=key, value=value)

    def output_acts(self, cooling_times_cul):
        # output specific activity info. unit Bq/kg
        item = 'acts'
        key = cooling_times_cul
        value = self._equal_cell.act
        self.output_item(item=item, key=key, value=value)

    def output_act(self, model_degree, cooling_times_cul):
        item = 'act'
        key = cooling_times_cul
        value = np.multiply(self._equal_cell.act, 360.0 /
                            model_degree*self._equal_cell.mass/1e3)
        self.output_item(item=item, key=key, value=value)

    def output_act_st_t(self, model_degree, cooling_times_cul):
        item = 'act_st_t'
        key = cooling_times_cul
        value = np.array([self._equal_cell.total_act,
                          np.multiply(np.array(self._equal_cell.total_act),
                                      self._equal_cell.mass / 1e3 * 360.0 / model_degree)
                          ])
        value = value.transpose().copy()
        self.output_item(item, key=key, value=value)

    def output_acts_max(self, cooling_times_cul):
        item = 'acts_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_act]).transpose(),
                                self._equal_cell.act_max_contri_act), axis=1)
        self.output_item(item=item, key=key, value=value)

    def output_acts_max_ratio(self, cooling_times_cul):
        item = 'acts_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.act_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_dhv(self, cooling_times_cul, factor):
        item = 'dhv'
        key = cooling_times_cul
        value = np.multiply(self._equal_cell.decay_heat, factor)
        self.output_item(item=item, key=key, value=value)

    def output_dh(self, cooling_times_cul, factor):
        item = 'dh'
        key = cooling_times_cul
        value = np.multiply(self._equal_cell.decay_heat, factor)
        self.output_item(item=item, key=key, value=value)

    def output_dh_vt_t(self, cooling_times_cul, factor1, factor2):
        item = 'dh_vt_t'
        key = cooling_times_cul
        value = np.array([np.multiply(self._equal_cell.total_decay_heat, factor1),
                          np.multiply(
                              np.array(self._equal_cell.total_decay_heat), factor2)
                          ])
        value = value.transpose().copy()
        self.output_item(item=item, key=key, value=value)

    def output_dhv_max(self, cooling_times_cul, factor):
        item = 'dhv_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_decay_heat]).transpose(),
                                self._equal_cell.decay_heat_max_contri_dh), axis=1)
        value = np.multiply(value, factor)
        self.output_item(item=item, key=key, value=value)

    def output_dhv_max_ratio(self, cooling_times_cul):
        item = 'dhv_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.decay_heat_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_cdt(self, cooling_times_cul):
        item = 'cdt'
        key = cooling_times_cul
        value = self._equal_cell.total_contact_dose
        self.output_item(item=item, key=key, value=value)

    def output_cd(self, cooling_times_cul):
        item = 'cd'
        key = cooling_times_cul
        value = self._equal_cell.contact_dose
        self.output_item(item=item, key=key, value=value)

    def output_cd_max(self, cooling_times_cul):
        item = 'cd_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_contact_dose]).transpose(),
                                self._equal_cell.contact_dose_max_contri_cd), axis=1)
        self.output_item(item=item, key=key, value=value)

    def output_cd_max_ratio(self, cooling_times_cul):
        item = 'cd_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.contact_dose_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_ci(self, cooling_times_cul):
        item = 'ci'
        key = cooling_times_cul
        value = self._equal_cell.ci
        self.output_item(item=item, key=key, value=value)

    def output_cit(self, cooling_times_cul):
        item = 'cit'
        key = cooling_times_cul
        value = np.array([self._equal_cell.total_ci])
        value = value.transpose().copy()
        self.output_item(item=item, key=key, value=value)

    def output_ci_max(self, cooling_times_cul):
        item = 'ci_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_ci]).transpose(),
                                self._equal_cell.ci_max_contri_ci), axis=1)
        self.output_item(item=item, key=key, value=value)

    def output_ci_max_ratio(self, cooling_times_cul):
        item = 'ci_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.ci_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_ci_chn2018(self, cooling_times_cul):
        item = 'ci_chn2018'
        key = cooling_times_cul
        value = self._equal_cell.ci_chn2018
        self.output_item(item=item, key=key, value=value)

    def output_cit_chn2018(self, cooling_times_cul):
        item = 'cit_chn2018'
        key = cooling_times_cul
        value = np.array([self._equal_cell.total_ci_chn2018])
        value = value.transpose().copy()
        self.output_item(item=item, key=key, value=value)

    def output_ci_chn2018_max(self, cooling_times_cul):
        item = 'ci_chn2018_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_ci_chn2018]).transpose(),
                                self._equal_cell.ci_chn2018_max_contri_ci), axis=1)
        self.output_item(item=item, key=key, value=value)

    def output_ci_chn2018_max_ratio(self, cooling_times_cul):
        item = 'ci_chn2018_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.ci_chn2018_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_llw_chn2018(self, cooling_times_cul):
        item = 'llw_chn2018'
        key = cooling_times_cul
        value = self._equal_cell.llw_chn2018
        self.output_item(item=item, key=key, value=value)

    def output_llwt_chn2018(self, cooling_times_cul):
        item = 'llwt_chn2018'
        key = cooling_times_cul
        value = np.array([self._equal_cell.total_llw_chn2018])
        value = value.transpose().copy()
        self.output_item(item=item, key=key, value=value)

    def output_llw_chn2018_max(self, cooling_times_cul):
        item = 'llw_chn2018_max'
        key = cooling_times_cul
        value = np.concatenate((np.array([self._equal_cell.total_llw_chn2018]).transpose(),
                                self._equal_cell.llw_chn2018_max_contri_llw), axis=1)
        self.output_item(item=item, key=key, value=value)

    def output_llw_chn2018_max_ratio(self, cooling_times_cul):
        item = 'llw_chn2018_max_ratio'
        key = cooling_times_cul
        value = self._equal_cell.llw_chn2018_max_contri_ratio
        self.output_item(item=item, key=key, value=value)

    def output_gamma_emit_rate(self, gamma_energy_upper_bounds):
        item = 'gamma_emit_rate'
        key = gamma_energy_upper_bounds
        value = self.equal_cell.gamma_emit_rate[0]
        self.output_item(item=item, key=key, value=value)

    def output_data(self, work_dir, model_degree, aim, cooling_times_cul=None,
                    rwss=[]):
        """
        Output data: output corresponding information according to the aim and model_degree
        case 1: aim = CELL_ACT_POST
            - output basic info. :vol, mass, density
            - nuclides info. : nuclides, half_lives
            - act info. :nuclide, act
            - act_max_contri_nuc & act_max_contri_act
            - act_max_contri_nuc & act_max_contri_ratio
            - nuclide & decay_heat
            - decay_heat_max_contri_nuc & decay_heat_max_contri_dh
            - decay_heat_max_contri_nuc & decay_heat_max_contri_ratio
            - total_decay_heat
            - nuclide & contact_dose
            - contact_dose_max_contri_nuc & contact_dose_max_contri_cd
            - contact_dose_max_contri_nuc & contact_dose_max_contri_ratio
            - nuclide & ci
            - ci_max_contri_nuc & ci_max_contri_ci
            - ci_max_contri_nuc & ci_max_contri_ratio
            - nuclide & ci_chn2018
            - ci_chn2018_max_contri_nuc & ci_chn2018_max_contri_ci
            - ci_chn2018_max_contri_nuc & ci_chn2018_max_contri_ratio
            - nuclide & llw_chn2018
            - llw_chn2018_max_contri_nuc & llw_chn2018_max_contri_llw
            - llw_chn2018_max_contri_nuc & llw_chn2018_max_contri_ratio
            - radwaste classification, optional if rws is not None
        case 2: aim = CELL_DPA_POST.
            - output basic info. : vol, mass, density
            - dpa,
            - He_production
            - H_production
        """

        # generate directory for this part
        self.generate_directory(work_dir)
        # case 1: aim == CELL_ACT_POST
        if aim == 'CELL_ACT_POST':
            # check cooling_times_cul
            if cooling_times_cul is None:
                raise ValueError(
                    "cooling_times_cul must be provided in CELL_ACT_POST mode")
            # output basic info.
            self.output_basicinfo(model_degree)
            # output nuclides & half_lives
            self.output_nuc()
            # output flux
            self.output_flux()

            # -------------------activity part--------------------------------
            # output specific activity info. unit Bq/kg
            self.output_acts(cooling_times_cul)
            # output activity info. unit Bq
            self.output_act(model_degree, cooling_times_cul)
            # total_specific activity and total activity
            self.output_act_st_t(model_degree, cooling_times_cul)
            # output act_max_contri_nuc & act_max_contri_act, unit Bq/kg
            self.output_acts_max(cooling_times_cul)
            # output act_max_contri_nuc & act_max_contri_ratio, unit 1
            self.output_acts_max_ratio(cooling_times_cul)

            # --------------------decay_heat----------------------------------
            # output decay_heat info., unit kW/m3, origin kW/kg
            # unit change factor from kW/kg -> kW/m3
            factor = self._equal_cell.mass / 1.0e3 / \
                (self._equal_cell.vol / 1.0e6)

            def f(x):
                return x * factor
            # decay heat kW/m3
            self.output_dhv(cooling_times_cul, factor)
            # output decay_heat of 360 degree model info. unit kW
            self.output_dh(cooling_times_cul, factor*self._equal_cell.vol/1e6)
            # total decay_heat
            self.output_dh_vt_t(cooling_times_cul, factor,
                                factor*self._equal_cell.vol/1e6)
            # output decay_heat_max_contri_nuc & decay_heat_max_contri_dh,
            # unit : kW/m3
            self.output_dhv_max(cooling_times_cul, factor)
            # output decay_heat_max_contri_nuc & decay_heat_max_contri_ratio,
            # unit 1
            self.output_dhv_max_ratio(cooling_times_cul)

            # ---------------------contact_dose-------------------------------
            # total contact_dose
            self.output_cdt(cooling_times_cul)
            # contact_dose of each nuc
            self.output_cd(cooling_times_cul)
            # contact_dose_max
            self.output_cd_max(cooling_times_cul)
            # contact_dose_max_ratio
            self.output_cd_max_ratio(cooling_times_cul)

            # ------------------------ci part---------------------------------
            self.output_ci(cooling_times_cul)
            # total ci
            self.output_cit(cooling_times_cul)
            # ci_max
            self.output_ci_max(cooling_times_cul)
            # ci_max_ratio
            self.output_ci_max_ratio(cooling_times_cul)
            # ------------------------ci_chn2018------------------------------
            for rws in rwss:
                if rws.standard == 'CHN2018':
                    self.output_ci_chn2018(cooling_times_cul)
                    self.output_cit_chn2018(cooling_times_cul)
                    self.output_ci_chn2018_max(cooling_times_cul)
                    self.output_ci_chn2018_max_ratio(cooling_times_cul)
                    self.output_llw_chn2018(cooling_times_cul)
                    self.output_llwt_chn2018(cooling_times_cul)
                    self.output_llw_chn2018_max(cooling_times_cul)
                    self.output_llw_chn2018_max_ratio(cooling_times_cul)

            # --------------------Radwaste part-------------------------------
            #  radwaste classification chn2018
            for rws in rwss:
                # radwaste classification results
                if rws.standard == 'CHN2018':
                    filename = self.generate_output_filename('rwc_chn2018')
                    line = ','.join(['Cooling_time(s)', 'Radwaste_Class', 'Decay_heat(kW/m3)',
                                     'Clearance', 'VLLW', 'LLW', 'ILW', 'Limit'])
                    fo = open(filename, 'w')
                    fo.write(line+'\n')
                    for intv in range(len(cooling_times_cul)):
                        line = ','.join([utils.format_single_output(cooling_times_cul[intv]),  # cooling time
                                         # rwc
                                         self._equal_cell.radwaste_class_chn2018[intv],
                                         utils.format_single_output(
                                             self._equal_cell.total_decay_heat[intv] * factor),  # decay heat, (kW/m3)
                                         utils.data_to_line_1d(
                                             key=None, value=self._equal_cell.rw_chn2018_index_sum[intv], postfix=''),  # indices
                                         utils.format_single_output(1.0)])  # limit
                        fo.write(line+'\n')
                    fo.close
                elif rws.standard == 'USNRC':
                    filename = self.generate_output_filename('rwc_usnrc')
                    line = ','.join(['Cooling_time(s)', 'Radwaste_Class', 'CI', 'LLWA_LL',
                                     'LLWB_LL', 'LLWC_LL', 'LLWA_SL', 'LLWB_SL', 'LLWC_SL', 'Limit'])
                    fo = open(filename, 'w')
                    fo.write(line+'\n')
                    for intv in range(len(cooling_times_cul)):
                        line = ','.join([utils.format_single_output(cooling_times_cul[intv]),  # cooling time
                                         # rwc
                                         self._equal_cell.radwaste_class_usnrc[intv],
                                         utils.format_single_output(
                                             self._equal_cell.total_ci_usnrc[intv]),
                                         utils.data_to_line_1d(
                                             key=None, value=self._equal_cell.rw_usnrc_index_sum_ll[intv], postfix=''),
                                         utils.data_to_line_1d(
                                             key=None, value=self._equal_cell.rw_usnrc_index_sum_sl[intv], postfix=''),
                                         utils.format_single_output(1.0)])  # limit
                        fo.write(line+'\n')
                    fo.close
                elif rws.standard == 'USNRC_FETTER':
                    filename = self.generate_output_filename(
                        'rwc_usnrc_fetter')
                    line = ','.join(['Cooling_time(s)', 'Radwaste_Class', 'CI', 'LLWA',
                                     'LLWB', 'LLWC', 'Limit'])
                    fo = open(filename, 'w')
                    fo.write(line+'\n')
                    for intv in range(len(cooling_times_cul)):
                        line = ','.join([utils.format_single_output(cooling_times_cul[intv]),  # cooling time
                                         # rwc
                                         self._equal_cell.radwaste_class_usnrc_fetter[intv],
                                         utils.format_single_output(
                                             self._equal_cell.total_ci_usnrc[intv]),
                                         utils.data_to_line_1d(
                                             key=None, value=self._equal_cell.rw_usnrc_fetter_index_sum[intv], postfix=''),
                                         utils.format_single_output(1.0)])  # limit
                        fo.write(line+'\n')
                    fo.close
                elif rws.standard == 'UK':
                    filename = self.generate_output_filename('rwc_uk')
                    line = ','.join(['Cooling_time(s)', 'Radwaste_Class', 'CI', 'Decay_heat(kW/m3)',
                                     'Alpha_act(Bq/kg)', 'Act(Bq/kg)', 'Limit'])
                    fo = open(filename, 'w')
                    fo.write(line+'\n')
                    for intv in range(len(cooling_times_cul)):
                        line = ','.join([utils.format_single_output(cooling_times_cul[intv]),  # cooling time
                                         # rwc
                                         self._equal_cell.radwaste_class_uk[intv],
                                         utils.format_single_output(
                                             self._equal_cell.total_ci[intv]),
                                         utils.format_single_output(
                                             self._equal_cell.total_decay_heat[intv] * factor),  # decay heat, (kW/m3)
                                         utils.format_single_output(
                                             self._equal_cell._total_alpha_act[intv]),  # alpha act
                                         utils.format_single_output(
                                             self._equal_cell._total_act[intv]),  # total act
                                         utils.format_single_output(1.0)])  # limit
                        fo.write(line+'\n')
                    fo.close
                elif rws.standard == 'RUSSIAN':
                    filename = self.generate_output_filename('rwc_russian')
                    line = ','.join(['Cooling_time(s)', 'Radwaste_Class', 'Decay_heat(kW/m3)',
                                     'LLW', 'Limit'])
                    fo = open(filename, 'w')
                    fo.write(line+'\n')
                    for intv in range(len(cooling_times_cul)):
                        line = ','.join([utils.format_single_output(cooling_times_cul[intv]),  # cooling time
                                         # rwc
                                         self._equal_cell.radwaste_class_russian[intv],
                                         utils.format_single_output(
                                             self._equal_cell.total_decay_heat[intv] * factor),  # decay heat, (kW/m3)
                                         utils.data_to_line_1d(
                                             key=None, value=self._equal_cell.rw_russian_index_sum[intv], postfix=''),  # indices
                                         utils.format_single_output(1.0)])  # limit
                        fo.write(line+'\n')
                    fo.close

        # case 2: aim == CELL_DPA_POST
        # output the dpa information
        if aim == 'CELL_DPA_POST':
            # output the DPA information
            filename = self.generate_output_filename('dpa')
            fo = open(filename, 'w')
            line = ' '.join(['DPA:', str(self._equal_cell.dpa), 'DPA/FPY\n'])
            fo.write(line)
            line = ' '.join(['He_production:', str(
                self._equal_cell.He_production), 'appm/FPY\n'])
            fo.write(line)
            line = ' '.join(['H_production:', str(
                self._equal_cell.H_production), 'appm/FPY\n'])
            fo.write(line)
            fo.close()

        # case 3: aim == COOLANT_ACT_POST
        if aim == 'COOLANT_ACT_POST':
            # output the act, decay_heat, contact_dose
            filename = self.generate_output_filename('coolant_response')
            fo = open(filename, 'w')
            line = utils.data_to_line_1d(
                key='Nuclide', value=self.equal_cell.nuclides)
            fo.write(line)
            line = utils.data_to_line_1d(
                key='Specific act (Bq/kg)', value=self.equal_cell.act[0])
            fo.write(line)
            line = utils.data_to_line_1d(
                key='Decay heat (kW/kg)', value=self.equal_cell.decay_heat[0])
            fo.write(line)
            line = utils.data_to_line_1d(
                key='Contact dose (Sv/h)', value=self.equal_cell.contact_dose[0])
            fo.write(line)
            fo.close()
            # output gamma_emit_rate
            self.output_gamma_emit_rate(gamma_energy_upper_bounds)
            # output neutron_emit_rate
            filename = self.generate_output_filename('neutron_emit_rate')
            fo = open(filename, 'w')
            line = ','.join(['Energy (MeV)', 'Neutron emit rate (n/kg/s)'])
            fo.write(line+'\n')
            nid = self.equal_cell.nuclides.index('N17')
            line = ','.join(['0.848', utils.format_single_output(
                self.equal_cell.act[0][nid]*0.95)])
            fo.write(line+'\n')
            fo.close()

    def output_photon_source(self, cooling_times_cul):
        """
        Out the photon source information for the part.
        The file has three blocks:
        block 1: basic information
            - [num_cells] [num_e_groups] [has_bounding_box]
        block 2: upper energy bins photon energy structure (in MeV) (usually 24 bins)
            - [e1] [e2] ... [e24]
        block 3: information for each cell, there are [num_cells] lines, each line has
            - [cid] [vol, cm3] [emit_rate, g/cm3/s] [pr1] [pr2] ... [pr24] [xmin] [xmax] [ymin] [ymax] [zmin] [zmax]
        """
        filename = self.generate_output_filename('phtn_src')
        fo = open(filename, 'w')
        # block 1
        line = f"{len(self.part_cell_list)} 24 0\n"
        fo.write(line)
        # block 2
        line = f""
        fo.write(line)
        fo.close()

    def remove_invalid_cids(self, invalid_cids=[]):
        """
        Remove invalid cells from part.
        NOTICE: the cids in subparts will not removed by this function.

        Parameters:
        -----------
        invalid_cids : list of int
            The cids of invalid cells 
        """
        if len(invalid_cids) == 0:
            return
        for j, cid in enumerate(invalid_cids):
            if cid in self.cell_ids:
                self.cell_ids.remove(cid)
                self.removed_cids.append(cid)


def is_cell_id_in_parts(parts, cid):
    """check whether a cell id is in parts"""
    for i, p in enumerate(parts):
        if cid in p.cell_ids:
            return True
    return False


def is_item_part(item, parts=None):
    """
    Check whether the item means a part.
    The item is a string and exist in Parts.

    Parameters:
    -----------
    item : str
    """
    if not isinstance(item, str):
        return False
    if item.strip() == '':
        return False

    if parts is None:
        return True
    else:
        try:  # check whether item in part list
            pidx = utils.find_index_by_property(item, parts)
            return True
        except:
            return False


def get_subpart_cell_ids_sub(value):
    """get_subpart_cell_id_sub, used to interpret a string of subpart/cell list to int list of subpart/cell ids"""
    cell_ids_sub = []
    subpart_ids_sub = []
    if '~' in value:  # this string need to expand
        cell_ele = value.split('~')
        pre_cell, post_cell = int(cell_ele[0]), int(cell_ele[-1])
        for i in range(pre_cell, post_cell + 1, 1):
            cell_ids_sub.append(i)
    else:
        value.strip()
        try:
            cell_ids_sub.append(int(value))
        except:
            # not a string, it should be a part id
            # check whether it is a regex
            try:
                re.compile(value)
            except:
                raise ValueError(f"{value} is not a valid regular expression")
            subpart_ids_sub.append(value)
    return subpart_ids_sub, cell_ids_sub


def get_subpart_cell_ids(value):
    """get_cell_ids, used to get cell ids from the context read from part_cell_list
    input: value, this is a list of string, that need to interpret to cell ids
    return: a list of int that represent the cell ids"""
    subpart_ids = []
    cell_ids = []
    for item in value:
        subpart_ids_sub, cell_ids_sub = get_subpart_cell_ids_sub(item)
        subpart_ids.extend(subpart_ids_sub)
        cell_ids.extend(cell_ids_sub)
    return subpart_ids, cell_ids


def get_part_cell_subpart_ids(part_cell_list):
    """
    Get the cell ids and subpart ids of parts from part_cell_list.

    Parameters:
    -----------
    part_cell_list : string
        The part cell list file

    Returns:
    parts : list of Part
        parts
    """

    parts = []
    part_id = ''
    pid = -1
    if part_cell_list == '':  # part_cell_list not given
        return parts
    fin = open(part_cell_list, 'r')
    line = ' '
    while line != '':
        try:
            line = fin.readline()
        except:
            line = fin.readline().encode('ISO-8859-1')
        line_ele = line.split()
        if utils.is_blank_line(line):  # this is a empty line
            continue
        if utils.is_comment(line, code='#'):  # this is a comment line
            continue
        # otherwise, this is a line that contains information
        if line[:5] == '     ':  # this is a continue line
            subpart_ids, cell_ids = get_subpart_cell_ids(line_ele)
            parts[pid].cell_ids.extend(cell_ids)
            parts[pid].subpart_ids.extend(subpart_ids)
        else:  # this line contains a part id
            part_id = line_ele[0]
            part = Part()
            part.id = part_id
            parts.append(part)
            subpart_ids, cell_ids = get_subpart_cell_ids(line_ele[1:])
            pid = utils.find_index_by_property(part.id, parts)
            parts[pid].cell_ids.extend(cell_ids)
            parts[pid].subpart_ids.extend(subpart_ids)
    fin.close()
    return parts


@utils.log
def get_part(cells, part_cell_list, coolant_flow_parameters=None,
             create_equal_cell=True):
    """get_part, read part_cell_list and form the parts

    Parameters:
    -----------
    cells : list of Cell
        The list of cells
    part_cell_list : str
        The filename of the part cell list
    coolant_flow_parameters: str
        The filename of the coolant flow parameters
    create_equal_cell : bool
        Whether to create the equivalent cell
    """
    parts = get_part_cell_subpart_ids(part_cell_list=part_cell_list)

    # match cell part
    for p in parts:
        p = match_cell_part(p, cells, parts=parts)

    # print all parts for user to check
    info_str = f"    parts read from {part_cell_list} are:"
    for i, p in enumerate(parts):
        info_str = f"{info_str} {p.id},"
    info_str = utils.length_control(info_str, indent=4)
    print(info_str)

    # init equal_cell for each part
    if create_equal_cell:
        for i, p in enumerate(parts):
            p.init_equal_cell()

    # read part mass flow rate if coolant_flow_parameters is provided
    if coolant_flow_parameters is not None:
        df = pd.read_csv(coolant_flow_parameters)
        for i, p in enumerate(parts):
            part_info = np.array(df.loc[df['Parts'] == p.id]).flatten()
            p.mass_flow_rate = float(part_info[1])
    return parts


def find_matched_subparts(sp, parts):
    """
    Find the indexes of matched subparts

    Parameters:
    -----------
    sp : string
        id of the subpart
    parts : list
        List of the Parts

    Returns:
    --------
    indexes : list
        List of part index.
    """

    pattern = re.compile(sp)
    pidxes = []
    for i, part in enumerate(parts):
        if re.fullmatch(pattern, part.id):
            pidxes.append(i)
    return pidxes


def part_merge_subpart(part, subpart, cells, parts):
    """
    Merge a subpart into a part.

    Parameters:
    -----------
    part : Part
        The part.
    subpart : Part
        The subpart
    cells : list of Cell
        The list of cells
    parts : list of Part
        The parts

    Returns:
    --------
    part : Part
        The updated part
    """

    if len(subpart.part_cell_list) == 0:  # this part not matched
        subpart = match_cell_part(subpart, cells, parts)
    for c in subpart.part_cell_list:
        if c in part.part_cell_list:
            raise ValueError(
                f"Duplicate cell {c.id} in part {part.id}")
        else:
            part.cell_ids.append(c.id)
            part.part_cell_list.append(c)
    return part


def match_cell_part(part, cells, parts=[]):
    """put the cells defined in the cell_ids to the part"""
    if len(part.part_cell_list) > 0:  # already matched
        return part
    for item in part.cell_ids:
        cidx = utils.find_index_by_property(item, cells)
        part.part_cell_list.append(cells[cidx])
    # if subpart provided
    self_id = utils.find_index_by_property(part.id, parts)
    for sp in part.subpart_ids:
        # if sp is a regex
        pidxes = find_matched_subparts(sp, parts)
        if len(pidxes) > 1:
            for i, pidx in enumerate(pidxes):
                if pidx != self_id:
                    part = part_merge_subpart(part, parts[pidx], cells, parts)
        else:  # not a regex or only one matched subpart
            pidx = utils.find_index_by_property(sp, parts)
            part = part_merge_subpart(part, parts[pidx], cells, parts)
    return part


def replace_cids_with_split(cell_ids, cid_old2new):
    """
    Replace old cids with new split cids
    """
    new_cell_ids = []
    for i, cid in enumerate(cell_ids):
        new_cids = cid_old2new[cid]
        new_cell_ids.extend(new_cids)
    return new_cell_ids


def compose_part_line(part_id, subpart_ids, cell_ids):
    """
    Compose part description in part_cell_list file.

    Parameters:
    -----------
    part_id : str
        The id of the part
    subpart_ids : list of str
        The list of ids of subparts
    cell_ids : list of int
        The list of cell ids

    Returns:
    --------
    s : str
        The composed part line
    """
    s = part_id
    for i, p in enumerate(subpart_ids):
        s = f"{s} {p}"
    cell_str = utils.proper_str_list_of_ints(cell_ids)
    s = f"{s} {cell_str}"
    return s


def update_part_cell_list(part_cell_list, cid_old2new, output="part_cell_list.new"):
    """
    update the part cell list file. A new file will be write

    Parameters:
    -----------
    part_cell_list : str
        The part cell list file
    cid_old2new : dict
        The dict of old cid to new cids
    output : str
        The updated part_cell_list
    """
    # read the part cell list
    fo = open(output, 'w')
    fin = open(part_cell_list, 'r')
    line = ' '
    counter = 0
    pcell_ids = []
    while line != '':
        try:
            line = fin.readline()
        except:
            line = fin.readline().encode('ISO-8859-1')
        line_ele = line.split()
        if utils.is_blank_line(line):  # this is a empty line
            fo.write(line)
            continue
        if utils.is_comment(line, code='#'):  # this is a comment line
            fo.write(line)
            continue
        # otherwise, this is a line that contains information
        if line[:5] == '     ':  # this is a continue line
            subpart_ids, cell_ids = get_subpart_cell_ids(line_ele)
            cell_ids = replace_cids_with_split(cell_ids, cid_old2new)
            pcell_ids.extend(cell_ids)
        else:  # this line contains a part id
            counter += 1
            # write previous line
            if counter > 1:
                new_line = compose_part_line(
                    part_id, subpart_ids, pcell_ids)
                fo.write(new_line+'\n')
                pcell_ids = []
            part_id = line_ele[0]
            part = Part()
            part.id = part_id
            subpart_ids, cell_ids = get_subpart_cell_ids(line_ele[1:])
            cell_ids = replace_cids_with_split(cell_ids, cid_old2new)
            pcell_ids.extend(cell_ids)

    new_line = compose_part_line(
        part_id, subpart_ids, pcell_ids)
    fo.write(new_line+'\n')
    fo.close()


def has_valid_cells(p, parts):
    """
    Check wether a part contains valid cells.

    Parameters:
    -----------
    p : Part
        The part to check
    parts : list of Parts
        List of the parts

    Returns:
    --------
    True : if it has valid cells
    False : it it does not have valid cells
    """
    if len(p.cell_ids) > 0:  # has cells
        return True
    if len(p.subpart_ids) == 0:  # no cell_ids, no subpart_ids
        return False
    # no cell_ids, has subparts
    for i, sp_id in enumerate(p.subpart_ids):
        pidx = utils.find_index_by_property(sp_id, parts)
        flag = has_valid_cells(parts[pidx], parts)  # check subparts
        if flag:
            return True
    return False


def part_cell_list_remove_invalid_cids(part_cell_list, invalid_cids=[],
                                       output="part_cell_list.new"):
    """
    Remove invalid cids from the part cell list file.

    Parameters:
    -----------
    part_cell_list : str
        The part cell list file
    invalid_cids : list of ints
        The list of ids of invalid cells
    output : str
        The updated part_cell_list
    """

    if len(invalid_cids) == 0:
        return

    parts = get_part_cell_subpart_ids(part_cell_list=part_cell_list)
    for i, p in enumerate(parts):
        for j, cid in enumerate(invalid_cids):
            if cid in p.cell_ids:
                p.cell_ids.remove(cid)
                p.removed_cids.append(cid)

    # read the part cell list
    with open(output, 'w') as fo:
        # write comment lines
        fo.write(
            "# Be careful about the content, do not enter any characters except ASCII.\n")
        fo.write("# Regular expression is supported\n")
        fo.write("#     - Only fullmatch mode is supported\n")
        fo.write(
            "#     - Nested define of parts is supported, but do not use multiple level regex\n")
        fo.write("#     - The subparts should not contain identical cell\n")
        fo.write(
            "# This file is generated by part_cell_list_remove_invalid_cids, do not modify the content\n")

        # write removed cids information as comment
        line = f"IMPORTANT WARNING MESSAGE! Removed {len(invalid_cids)} invalid cids: {utils.proper_str_list_of_ints(invalid_cids)}"
        block = utils.length_control(line)
        block = utils.comment_a_block(block, symbol='#')
        fo.write(block)

        # write parts
        for i, p in enumerate(parts):
            if len(p.removed_cids) > 0:
                line = f"part: {p.id} removed {len(p.removed_cids)}/{len(p.cell_ids)+len(p.removed_cids)} cids: {utils.proper_str_list_of_ints(p.removed_cids)}"
                block = utils.length_control(line)
                fo.write(utils.comment_a_block(block, symbol='#'))
            if has_valid_cells(p, parts=parts) > 0:  # there are still valid cells
                line = f"{p.id} {' '.join(p.subpart_ids)} {utils.proper_str_list_of_ints(p.cell_ids)}"
                block = utils.length_control(line)
                fo.write(block+'\n')
