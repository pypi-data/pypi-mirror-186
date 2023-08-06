#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import with_statement, print_function
import configparser
import os
import numpy as np
from traceback import format_list
from progress.bar import Bar
import datetime
from natf import cell
from natf import material
from natf import part
from natf.radwaste_standard import rwc_to_int, ctr_to_int
from natf import utils
from natf import nuc_treat
from natf import mcnp_input
from natf import mcnp_output
from natf.plot import get_rwcs_by_cooling_times, calc_rwc_cooling_requirement, \
    calc_recycle_cooling_requirement
from natf import fispact_input
from natf.fispact_output import read_fispact_out_act, \
    read_fispact_out_gamma_emit_rate, read_fispact_out_dpa, \
    get_material_after_irradiation
from natf import settings
import natf
import tables


def create_cell_idx_dict(cells):
    dict_cid_idx = {}
    for i, c in enumerate(cells):
        dict_cid_idx[c.id] = i
    return dict_cid_idx


@utils.log
def get_material_info(mcnp_outp):
    """get_material_info, read the mcnp_outp file and returns the materials"""

    materials = []
    # read the mcnp_outp first time to get the numbers of material
    mat_list = []
    fin = open(mcnp_outp)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError('1cells not found in the file, wrong file!')
        if '1cells' in line:  # read 1cells
            # read the following line
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            while True:
                line = fin.readline()
                if ' total' in line:  # end of the cell information part
                    break
                line_ele = line.split()
                if len(line_ele) == 0:
                    continue
                mid, atom_density, gram_density = int(
                    line_ele[2]), float(
                    line_ele[3]), float(
                    line_ele[4])
                mat_list.append((mid, atom_density, gram_density))
            break
    fin.close()
    mat_list = list(set(mat_list))

    # initial the materials
    for i in range(len(mat_list)):
        m = material.Material()
        m.id = mat_list[i][0]
        m.atom_density = mat_list[i][1]
        m.density = mat_list[i][2]
        materials.append(m)

    # get the nuclide of the mcnp material
    fin = open(mcnp_outp)
    mid = -1
    nuc_list = []
    atom_fraction_list = []
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                "'component nuclide, atom fraction' not found in the file, wrong file! Check PRINT keyword")
        if 'component nuclide, atom fraction' in line:  # read atom fraction
            # read the following line
            line = fin.readline()
            mat_flag = False
            while True:
                line = fin.readline()
                if 'material' in line:  # end of the material atom fraction part
                    # some materials used only for a perturbation or tally, do not add here
                    if material.is_mat_used(materials, mid):
                        midx = utils.find_index_by_property(mid, materials)
                        materials[midx].mcnp_material_nuclide = list(nuc_list)
                        materials[midx].mcnp_material_atom_fraction = utils.scale_list(
                            atom_fraction_list)
                    break
                line_ele = line.split()
                if len(line_ele) == 0:
                    continue
                if len(line_ele) % 2 == 1:  # this line contains material id
                    if mat_flag:
                        if material.is_mat_used(materials, mid):
                            midx = utils.find_index_by_property(mid, materials)
                            materials[midx].mcnp_material_nuclide = list(
                                nuc_list)
                            materials[midx].mcnp_material_atom_fraction = utils.scale_list(
                                atom_fraction_list)
                        nuc_list = []  # reset
                        atom_fraction_list = []  # reset
                    mid = int(line_ele[0])
                    mat_flag = True
                    for i in range(len(line_ele) // 2):
                        nuc, atom_fraction = line_ele[2 * i +
                                                      1][:-1], float(line_ele[2 * i + 2])
                        if nuc not in nuc_list:
                            nuc_list.append(nuc)
                            atom_fraction_list.append(atom_fraction)
                            continue
                        if nuc in nuc_list:
                            nuc_index = nuc_list.index(nuc)
                            atom_fraction_list[nuc_index] += atom_fraction
                if len(line_ele) % 2 == 0:
                    for i in range(len(line_ele) // 2):
                        nuc, atom_fraction = line_ele[2 *
                                                      i][:-1], float(line_ele[2 * i + 1])
                        if nuc not in nuc_list:
                            nuc_list.append(nuc)
                            atom_fraction_list.append(atom_fraction)
                            continue
                        if nuc in nuc_list:
                            nuc_index = nuc_list.index(nuc)
                            atom_fraction_list[nuc_index] += atom_fraction
            break
    fin.close()

    # get the mass fraction of the nuclides
    fin = open(mcnp_outp)
    mid = -1
    nuc_list = []
    mass_fraction_list = []
    while True:
        line = fin.readline()
        if 'component nuclide, mass fraction' in line:  # read mass fraction
            # read the following line
            line = fin.readline()
            mat_flag = False
            while True:
                line = fin.readline()
                if ' warning.' in line or '1cell' in line:  # end of the material atom fraction part
                    if material.is_mat_used(materials, mid):
                        midx = utils.find_index_by_property(mid, materials)
                        materials[midx].mcnp_material_nuclide = list(nuc_list)
                        materials[midx].mcnp_material_mass_fraction = utils.scale_list(
                            mass_fraction_list)
                    break
                line_ele = line.split()
                if len(line_ele) == 0:
                    continue
                if len(line_ele) % 2 == 1:  # this line contains material id
                    if mat_flag:
                        if material.is_mat_used(materials, mid):
                            midx = utils.find_index_by_property(mid, materials)
                            materials[midx].mcnp_material_nuclide = list(
                                nuc_list)
                            materials[midx].mcnp_material_mass_fraction = utils.scale_list(
                                mass_fraction_list)
                        nuc_list = []  # reset
                        mass_fraction_list = []  # reset
                    mid = int(line_ele[0])
                    mat_flag = True
                    for i in range(len(line_ele) // 2):
                        nuc, mass_fraction = line_ele[2 * i +
                                                      1][:-1], float(line_ele[2 * i + 2])
                        if nuc not in nuc_list:
                            nuc_list.append(nuc)
                            mass_fraction_list.append(mass_fraction)
                            continue
                        if nuc in nuc_list:
                            nuc_index = nuc_list.index(nuc)
                            mass_fraction_list[nuc_index] += mass_fraction
                if len(line_ele) % 2 == 0:
                    for i in range(len(line_ele) // 2):
                        nuc, mass_fraction = line_ele[2 *
                                                      i][:-1], float(line_ele[2 * i + 1])
                        if nuc not in nuc_list:
                            nuc_list.append(nuc)
                            mass_fraction_list.append(mass_fraction)
                            continue
                        if nuc in nuc_list:
                            nuc_index = nuc_list.index(nuc)
                            mass_fraction_list[nuc_index] += mass_fraction
            break
    fin.close()
    return materials


@utils.log
def match_cells_materials(cells, materials):
    """match the cells and materials"""
    for c in cells:
        mid = utils.find_index_by_property(c.mid, materials)
        c.mat = materials[mid]
    return cells


def get_energy_index(energy, energy_group):
    """return energy index according to the energy and energy_group"""
    e_index = -1
    if energy == 'Total':
        return len(energy_group)
    else:
        energy = float(energy)
    for i in range(len(energy_group)):
        if abs(energy - energy_group[i]) / energy_group[i] < 1e-3:
            e_index = i
    if e_index == -1:
        raise ValueError(
            'energy not found in the energy group! Only 175/709 group supported!')
    return e_index


@utils.log
def cell_fispact_cal_pre(
        aim,
        work_dir,
        cells_need_cal,
        model_degree,
        irradiation_scenario,
        fispact_materials,
        fispact_materials_paths,
        fispact_files_dir='',
        fispact_data_dir=None):
    """
    Prepare FISPACT-II input files and FILES

    Parameters:
    -----------
    aim : str
        The AIM of the workflow
    work_dir : str
        The working directory
    cells_need_cal : list of Cell
        The cells need activation calculation
    model_degree : float
        The degree of the model used in MCNP. Used to modify the neutron flux by
        a factor of model_degree/360.0
    irradiation_scenario : str
        The filename of the irradiation scenario
    fispact_materials : list
        The list of the materials that defined by user to use another one
    fispact_materials_paths : list
        The list of the materials paths that need to use
    fispact_files_dir : str
        The directory to story fispact files
    fispact_data_dir : str
        The directory of FISPACT-II data libraries
    """

    if aim not in ('CELL_ACT_PRE', 'CELL_ACT_POST', 'CELL_DPA_PRE', 'CELL_DPA_POST', 'CELL_MAT_EVO'):
        raise RuntimeError('cell_fispact_cal_pre can only called in CELL MODE')
    tab4flag = False
    # endf libaries used, then need keyword EAFVERSION 8
    if aim in ('CELL_DPA_PRE', 'CELL_DPA_POST'):
        endf_lib_flag = True
    else:
        endf_lib_flag = False

    if aim in ('CELL_MAT_EVO'):
        stable_flag = True
    else:
        stable_flag = False

    # create fispact FILES
    if fispact_data_dir:
        n_group_size = len(cells_need_cal[0].neutron_flux) - 1
        tmp_file = fispact_input.get_fispact_files_template(n_group_size)
        filename = fispact_input.create_fispact_files(
            tmp_file, fispact_files_dir=fispact_files_dir, fispact_data_dir=fispact_data_dir)

    for c in cells_need_cal:
        file_prefix = settings.get_fispact_file_prefix(work_dir, c.id,
                                                       fispact_files_dir=fispact_files_dir)
        material = c.mat
        neutron_flux = c.neutron_flux
        try:
            fispact_input.write_fispact_file(
                material,
                irradiation_scenario,
                neutron_flux,
                file_prefix,
                aim=aim,
                model_degree=model_degree,
                tab4flag=tab4flag,
                endf_lib_flag=endf_lib_flag,
                fispact_materials=fispact_materials,
                fispact_materials_paths=fispact_materials_paths,
                stable_flag=stable_flag)
        except BaseException:
            errmsg = f"Encounter error when writing fispact file of cell {c.id}"
            raise ValueError(errmsg)


def calc_part_irradiation_scenario(part_name, coolant_flow_parameters,
                                   flux_multiplier, n_total_flux, model_degree=360.0):
    """
    Calculate the irradiation scenario according to the coolant flow parameters.

    Parameters:
    -----------
    part_name: str
        The name of the part.
    coolant_flow_parameters: str
        The file path of the coolant flow parameters.
    flux_multiplier: float
        The total neutron emitting rate of the fusion device.
        Eg: for CFETR 200 MW case, the value is 7.09e19.
    n_total_flux: float
        Total flux of the part.equal_cell.
    model_degree: float
        Default 360.

    Returns:
    --------
    irradiation_scenario: str
    """
    irr_time, cooling_times = settings.get_irr_and_cooling_times(
        part_name, coolant_flow_parameters)
    irr_total_flux = model_degree / 360.0 * flux_multiplier * n_total_flux
    irradiation_scenario = fispact_input.construct_irradiation_scenario(
        irr_time, cooling_times, irr_total_flux)
    return irradiation_scenario


@utils.log
def parts_fispact_cal_pre(aim, work_dir, parts, model_degree,
                          fispact_materials, fispact_materials_paths, coolant_flow_parameters,
                          flux_multiplier, fispact_files_dir=''):
    """fispact_cal_pre, write .flx and .i files for fispact according to the aim"""
    tab4flag = False
    endf_lib_flag = False
    # endf libraries used, then need keyword EAFVERSION 8 for p in parts:
    for p in parts:
        file_prefix = settings.get_fispact_file_prefix(work_dir, ele_id=p.id,
                                                       ele_type='p', fispact_files_dir=fispact_files_dir)
        neutron_flux = p.equal_cell.neutron_flux
        material = p.equal_cell.id
        irradiation_scenario = calc_part_irradiation_scenario(p.id,
                                                              coolant_flow_parameters, flux_multiplier, p.equal_cell.neutron_flux[-1], model_degree)
        try:
            fispact_input.write_fispact_file(material,
                                             irradiation_scenario,
                                             neutron_flux,
                                             file_prefix,
                                             model_degree=model_degree,
                                             tab4flag=tab4flag,
                                             endf_lib_flag=endf_lib_flag,
                                             fispact_materials=fispact_materials,
                                             fispact_materials_paths=fispact_materials_paths,
                                             aim=aim)
        except BaseException:
            errmsg = f"Error when writing fispact file of part {p.id}"
            raise ValueError(errmsg)


@utils.log
def read_fispact_output_cell(cells_need_cal, work_dir, aim,
                             fispact_files_dir='', n_group_size=175, out_phtn_src=False):
    """read_fispact_output_act: read the fispact output file to get activation information of cells
    input: cells_need_cal, list a cells that need to calculate and analysis
    input: work_dir, the working director
    return: cells_need_cal, changed list of cells"""
    interval_list = settings.check_interval_list(
        cells_need_cal, work_dir, fispact_files_dir=fispact_files_dir)
    print('     the intervals need to read are {0}'.format(interval_list))
    bar = Bar("reading fispact output files", max=len(
        cells_need_cal), suffix='%(percent).1f%% - %(eta)ds')
    for c in cells_need_cal:
        file_prefix = settings.get_fispact_file_prefix(work_dir, ele_id=c.id,
                                                       ele_type='c', fispact_files_dir=fispact_files_dir)
        filename = f"{file_prefix}.out"
        if aim in ('CELL_ACT_POST'):  # read output information
            read_fispact_out_act(c, filename, interval_list)
            if out_phtn_src:
                read_fispact_out_gamma_emit_rate(c, filename, interval_list)
        if aim == 'CELL_DPA_POST':  # read DPA information
            read_fispact_out_act(c, filename, interval_list)
            read_fispact_out_dpa(c, filename, interval_list)
        bar.next()
    bar.finish()


@utils.log
def read_fispact_output_part(parts, work_dir, aim, fispact_files_dir=''):
    """read_fispact_output_part: read the fispact output file to get
    activation information of parts in PHTS.

    Parameters:
    -----------
    parts:  list of parts
        parts that need to calculate and analysis
    work_dir: string
        The working director

    Returns:
    --------
    parts:
        Changed list of parts
    """
    interval_list = settings.check_interval_list(
        parts, work_dir, fispact_files_dir=fispact_files_dir)
    print('     the intervals need to read are {0}'.format(interval_list))
    for i, p in enumerate(parts):
        print('       reading part {0} start'.format(p.id))
        if aim == 'COOLANT_ACT_POST':  # read output information
            file_prefix = settings.get_fispact_file_prefix(work_dir, ele_id=p.id,
                                                           ele_type='p', fispact_files_dir=fispact_files_dir)
            filename = f"{file_prefix}.out"
            read_fispact_out_act(p.equal_cell, filename, interval_list)
            read_fispact_out_gamma_emit_rate(
                p.equal_cell, filename, interval_list)


@utils.log
def cell_act_post_process(parts, work_dir, model_degree, aim,
                          cooling_times_cul, rwss=[], out_phtn_src=False,
                          with_bounding_box=False):
    """
    cell_act_post_process: treat the parts, analysis the data and output results

    Parameters:
    -----------
    ...
    rwss : list of RadwasteStandard, optional
        Radwaste standards used.
    out_phtn_src : bool
        Whether output the photon source information for cell-based R2S
    """
    # first, merge the cells in the part to get the equal_cell
    if aim in ('CELL_ACT_POST', 'CELL_DPA_POST'):
        bar = Bar(f"merging cells of each part", max=len(
            parts), suffix='%(percent).1f%% - %(eta)ds')
        for p in parts:
            p.merge_cell(aim)
            bar.next()
        bar.finish()

    # if the aim is CELL_ACT_POST, then there should perform analysis
    if aim == 'CELL_ACT_POST':
        bar = Bar(f"analysis radwaste of parts", max=len(
            parts), suffix='%(percent).1f%% - %(eta)ds')
        for p in parts:
            p.part_act_analysis(aim, rwss=rwss)
            bar.next()
        bar.finish()

    # if the aim is CELL_DPA_POST, don't do anything
    # output the data
    bar = Bar(f"output results", max=len(parts),
              suffix='%(percent).1f%% - %(eta)ds')
    for p in parts:
        p.output_data(work_dir, model_degree, aim,
                      cooling_times_cul=cooling_times_cul, rwss=rwss)
        bar.next()
    bar.finish()

    # output the photon source information
    if out_phtn_src:
        bar = Bar(f"output photon source information", max=len(
            parts), suffix='%(percent).1f%% - %(eta)ds')
        for p in parts:
            output_part_photon_source(
                part=p,
                with_bounding_box=with_bounding_box)
            bar.next()
        bar.finish()


def output_part_photon_source(part, with_bounding_box=False):
    """
    Out the photon source information for the part.
    The file has three blocks:
    block 1: basic information
        - [num_cells] [num_e_groups] [has_bounding_box]
    block 2: total photon emit rate
        - [total_photon_emit, g/cm3/s]
    block 3: cell ids
        - [cid1] [cid2] ...
    block 4: upper energy bins photon energy structure (in MeV) (usually 24 bins)
        - [e1] [e2] ... [e24]
    block 5: information for each cell, there are [num_cells] lines, each line has
        - [vol, cm3] [emit_ratio] [pr1] [pr2] ... [pr24] [xmin] [xmax] [ymin] [ymax] [zmin] [zmax]
    """
    for ct in range(len(part.part_cell_list[0].gamma_emit_rate)):
        filename = part.generate_output_filename(f'phtn_src_ct{ct+1}')
        fo = open(filename, 'w')
        # block 1
        line = f"{len(part.cell_ids)} 24 {int(with_bounding_box)}\n"
        fo.write(line)
        part_total = 0.0
        for i, c in enumerate(part.part_cell_list):
            tol = sum(c.gamma_emit_rate[ct][:]) * c.vol
            part_total += tol
        line = f"{utils.format_single_output(part_total)}\n"
        fo.write(line)
        # block 3
        line = ''
        for i, c in enumerate(part.part_cell_list):
            if i == 0:
                line = f"{c.id}"
            else:
                line = f"{line} {c.id}"
        fo.write(line+'\n')
        # block 4
        e_groups = utils.get_e_group(e_group_size=24, unit='MeV',
                                     reverse=False, with_lowest_bin=False)
        line = ''
        for i, e in enumerate(e_groups):
            if i == 0:
                line = f"{utils.format_single_output(e)}"
            else:
                line = f"{line} {utils.format_single_output(e)}"
        fo.write(line+'\n')

        # block 5
        for i, c in enumerate(part.part_cell_list):
            line = f"{utils.format_single_output(c.vol)}"
            # normalization
            c_tol = sum(c.gamma_emit_rate[ct][:]) * c.vol
            cell_gamma_ratio = 0.0
            if part_total > 0:
                cell_gamma_ratio = c_tol/part_total
            line = f"{line} {utils.format_single_output(cell_gamma_ratio)}"

            ger_norm = [0]*len(c.gamma_emit_rate[0])
            if c_tol > 0:
                for j, ger in enumerate(c.gamma_emit_rate[ct][:]):
                    ger_norm[j] = c.gamma_emit_rate[0][j] / \
                        sum(c.gamma_emit_rate[0])
            # output
            cul_ger_norm = 0.0
            for j, ger in enumerate(ger_norm):
                cul_ger_norm += ger_norm[j]
                line = f"{line} {utils.format_single_output(cul_ger_norm)}"
            if with_bounding_box:
                for k in range(6):
                    line = f"{line} {utils.format_single_output(c.aabb_bounds[k])}"
            fo.write(line+'\n')
        fo.close()


def coolant_act_post_process(parts, nodes, work_dir, model_degree, aim):
    """
    coolant_act_post_process: treat the parts and coolant, analysis the data
    and output results
    """
    # merge nodes data
    for i, node in enumerate(nodes):
        settings.merge_node_parts(node, parts, i)

    # output the data
    for p in parts:
        p.output_data(work_dir, model_degree, aim)
    for node in nodes:
        node.output_data(work_dir, model_degree, aim)


@utils.log
def treat_nuc_responses(cells, parts, nuc_treatment, dict_cid_idx=None):
    """
    Treat the nuclide in cells. Such as extract the H3 by a factor of 99.9%.
    """
    if nuc_treatment == '':
        return cells
    nuc_trts = settings.get_nuc_treatments_new(nuc_treatment)
    nt_count = 0
    for i, nt in enumerate(nuc_trts):
        nuc_trts[i] = settings.expand_nuc_treatment_ids_new(nt, cells, parts)
        nt_count += len(nt.ids)
    bar = Bar("treating nuclides responses", max=nt_count,
              suffix='%(percent).1f%% - %(eta)ds')
    for i, nt in enumerate(nuc_trts):
        for j, cid in enumerate(nt.ids):
            if dict_cid_idx:
                cidx = dict_cid_idx[cid]
            else:
                cidx = utils.find_index_by_property(cid, cells, 'id')
            cells[cidx] = nuc_treat.treat_cell_nuc_responses(cells[cidx], nt)
            bar.next()
    bar.finish()
    return cells


def cells_aabb_from_ptrac(cells, ptrac_filename, dict_cid_idx):
    """
    Calculate cells aabb using ptrac file (binary).

    Parameters:
    -----------
    cells : list of Cell
        The cells list
    ptrac_filename : string
        The filename of ptrac file
    dict_cid_idx : dict
        The cell id to idx dict
    """
    aabb = [float('inf'), float('-inf'), float('inf'),
            float('-inf'), float('inf'), float('-inf')]
    ptrac_h5_filename = f"{ptrac_filename}.h5"
    if not os.path.isfile(ptrac_h5_filename):
        #        os.system(f"ptrac_to_hdf5 {ptrac_file} {ptrac_file}.h5")
        mcnp_output.ptrac_to_hdf5(ptrac_filename)
    # match pos and ves
    ptrac_h5f = tables.open_file(ptrac_h5_filename)
    table = ptrac_h5f.root.ptrac
    num_points = len(table)
    points = np.zeros(shape=(num_points, 3), dtype=float)
    cell_hits = [0]*len(cells)
    dict_p2cidx = {}  # point index to cell index
    bar = utils.IfBar("Get src sites information",  max=num_points,
                      suffix='%(percent).1f%% - %(eta)ds')
    counter = 0
    void_mode = True
    for row in table.iterrows():
        ncl = int(row['ncl'])
        r = [row['xxx'], row['yyy'], row['zzz']]
        cidx = dict_cid_idx[ncl]
        points[counter] = r
        cell_hits[cidx] += 1
        dict_p2cidx[counter] = cidx
        if cells[cidx].mid > 0:
            void_mode = False
            aabb[0] = min(aabb[0], r[0])
            aabb[1] = max(aabb[1], r[0])
            aabb[2] = min(aabb[2], r[1])
            aabb[3] = max(aabb[3], r[1])
            aabb[4] = min(aabb[4], r[2])
            aabb[5] = max(aabb[5], r[2])
        counter += 1
        bar.next()
    bar.finish()
    ptrac_h5f.close()
    if void_mode:
        raise ValueError(
            f" ERROR: all particles in ptrac file {ptrac_filename} are in VOID, DO NOT USE VOID MODE!!!")
    # put src sites into cells
    # It will takes much longer time if np.append is used
    # init the cell points
    for i, c in enumerate(cells):
        c.points = np.zeros(
            shape=(cell_hits[dict_cid_idx[c.id]], 3), dtype=float)
    cp_counter = [0]*len(cells)
    bar = utils.IfBar("Matching src sites and cells",  max=num_points,
                      suffix='%(percent).1f%% - %(eta)ds')
    for i, p in enumerate(points):
        cidx = dict_p2cidx[i]
        cells[cidx].points[cp_counter[cidx]] = p
        cp_counter[cidx] += 1
        bar.next()
    bar.finish()
    # calc aabb_bounds for cells
    for c in cells:
        if len(c.points) > 0:
            c.calc_aabb_bounds()

    # check whether all cells has valid aabb bounds
    cells_to_split = []
    cells_not_covered = []
    cells_fill = []
    cells_zero_importance = []
    for i, c in enumerate(cells):
        if c.fill:
            cells_fill.append(c.id)
        elif c.imp_n == 0:
            cells_zero_importance.append(c.id)
        elif not c.has_valid_aabb_bounds():
            cells_not_covered.append(c.id)
        else:
            cells_to_split.append(c.id)
    print(f"  there are {len(cells_to_split)} cells has valid ptrac sites")
    if len(cells_not_covered) == 0:
        warn_str = f"  all cells are covered by ptrac"
    else:
        warn_title = f'  {len(cells_not_covered)} cells not covered by ptrac:'
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=warn_title, cids=cells_not_covered)
    print(warn_str)
    return cells, aabb


def natf_cell_rwc_vis(config):
    """
    Modify the mcnp_input for visualization.
    """
    # ------ READ input -------
    aim = 'CELL_RWC_VIS'
    work_dir = config.get('general', 'work_dir', fallback='.')
    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)
    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')
    cells = mcnp_output.get_cell_basic_info(mcnp_outp)
    dict_cid_idx = create_cell_idx_dict(cells)
    cells = mcnp_output.get_cell_tally_info(mcnp_outp, cells, tally_number, n_group_size,
                                            continue_output=continue_output)
    # [model], required
    part_cell_list = os.path.join(
        work_dir, config.get('model', 'part_cell_list'))
    parts = part.get_part(cells, part_cell_list)
    # [fispact]
    irradiation_scenario = os.path.join(work_dir,
                                        config.get('fispact', 'irradiation_scenario'))
    cooling_times = settings.get_cooling_times(irradiation_scenario, aim)
    cooling_times_cul = settings.get_cooling_times_cul(cooling_times)
    # [radwaste] standard
    rwss = settings.get_radwaste_standards(config)

    # get RWC CHN2018 for each cooling_time
    rwc_vis_dir = os.path.join(work_dir, 'RWC_VIS')
    os.system(f"mkdir -pv {rwc_vis_dir}")
    names = []
    for p in parts:
        names.append(p.id)
    # rewrite mcnp_inp for each cooling_time
    bar = Bar("writing RWC VIS files", max=len(rwss) *
              len(cooling_times_cul), suffix='%(percent).1f%% - %(eta)ds')
    for rws in rwss:
        key = f'rwc_{rws.standard.lower()}'
        rwcs = get_rwcs_by_cooling_times(names, cooling_times=cooling_times_cul,
                                         key=key, work_dir=work_dir)
        if rws.standard in ['CHN2018']:
            classes = ['LLW', 'Clearance']
        else:
            classes = ['LLW']

        ctrs = calc_rwc_cooling_requirement(names, key=key,
                                            classes=classes, standard=rws.standard, work_dir=work_dir,
                                            out_unit='a', ofname=None)
        for i, ct in enumerate(cooling_times_cul):
            filename = os.path.join(
                rwc_vis_dir, f"{rws.standard.lower()}_ct{i}.txt")
            fo = open(filename, 'w')
            # rewrite cell card
            with open(mcnp_inp, 'r', encoding='gb18030') as fin:
                cell_start, surf_start = False, False
                cell_end, surf_end = False, False
                while True:
                    line = fin.readline()
                    if line == '':
                        break
                    # end of cell card
                    if utils.is_blank_line(line) and cell_start and not surf_start:
                        cell_end = True
                        surf_start = True
                        fo.write(line)
                        continue
                    if utils.is_comment(line):
                        fo.write(line)
                        continue
                    if mcnp_input.is_cell_title(line) and not cell_end:
                        cell_start = True
                        cid, mid, den = mcnp_input.get_cell_cid_mid_den(line)
                        if part.is_cell_id_in_parts(parts, cid):
                            pidx = utils.find_index_by_property(cid,
                                                                parts, prop='cell_ids', find_last=True)
                            rwc = rwcs[pidx][i]
                            rwci = rwc_to_int(rwc, standard=rws.standard)
                            new_line = mcnp_input.cell_title_change_mat(
                                line, mid_new=rwci, den_new=1.0)
                            fo.write(new_line+'\n')
                        else:  # this cell do not belong to activated parts, set to void
                            new_line = mcnp_input.cell_title_change_mat(
                                line, mid_new=0, den_new=None)
                            fo.write(new_line+'\n')
                        continue
                    if utils.is_blank_line(line) and surf_start and not surf_end:
                        surf_end = True
                        fo.write(line)
                        # append pseudo-mat here
                        fo.write(f"C ---- pseudo-mat for RWC VIS--------\n")
                        fo.write(material.create_pseudo_mat(
                            mid=1).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=2).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=3).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=4).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=5).__str__()+'\n')
                        continue
                    fo.write(line)  # other lines
            fo.write('\n')  # new line at the end
            fo.close()
            bar.next()
        # rewrite mcnp_inp for Time-to-Clearance and Time-to-LLW
        for i, cls in enumerate(classes):
            filename = os.path.join(
                rwc_vis_dir, f"{rws.standard.lower()}_to_{cls}.txt")
            fo = open(filename, 'w')
            # rewrite cell card
            with open(mcnp_inp, 'r', encoding='gb18030') as fin:
                cell_start, surf_start = False, False
                cell_end, surf_end = False, False
                while True:
                    line = fin.readline()
                    if line == '':
                        break
                    # end of cell card
                    if utils.is_blank_line(line) and cell_start and not surf_start:
                        cell_end = True
                        surf_start = True
                        fo.write(line)
                        continue
                    if utils.is_comment(line):
                        fo.write(line)
                        continue
                    if mcnp_input.is_cell_title(line) and not cell_end:
                        cell_start = True
                        cid, mid, den = mcnp_input.get_cell_cid_mid_den(line)
                        if part.is_cell_id_in_parts(parts, cid):
                            pidx = utils.find_index_by_property(cid,
                                                                parts, prop='cell_ids', find_last=True)
                            ctr = ctrs[pidx][i]
                            ctri = ctr_to_int(ctr)
                            new_line = mcnp_input.cell_title_change_mat(
                                line, mid_new=ctri, den_new=1.0)
                            fo.write(new_line+'\n')
                            continue
                        else:  # this cell do not belong to activated parts, set to void
                            new_line = mcnp_input.cell_title_change_mat(
                                line, mid_new=0, den_new=None)
                            fo.write(new_line+'\n')
                            continue
                    if utils.is_blank_line(line) and surf_start and not surf_end:
                        surf_end = True
                        fo.write(line)
                        # append pseudo-mat here
                        fo.write(f"C ---- pseudo-mat for RWC VIS--------\n")
                        fo.write(material.create_pseudo_mat(
                            mid=1).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=2).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=3).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=4).__str__()+'\n')
                        fo.write(material.create_pseudo_mat(
                            mid=5).__str__()+'\n')
                        continue
                    fo.write(line)  # other lines
            fo.write('\n')  # new line at the end
            fo.close()
    bar.finish()
    # rewrite mcnp_inp for Recycling
    ctrs = [[], []]  # CRH, ARH
    ctrs[0] = calc_recycle_cooling_requirement(
        names, key='cdt', rh='CRH', work_dir=work_dir, out_unit='a')
    ctrs[1] = calc_recycle_cooling_requirement(
        names, key='cdt', rh='ARH', work_dir=work_dir, out_unit='a')
    for i in range(0, 2):
        if i == 0:
            filename = os.path.join(rwc_vis_dir, f"to_recycle_crh.txt")
        else:
            filename = os.path.join(rwc_vis_dir, f"to_recycle_arh.txt")
        fo = open(filename, 'w')
        # rewrite cell card
        with open(mcnp_inp, 'r', encoding='gb18030') as fin:
            cell_start, surf_start = False, False
            cell_end, surf_end = False, False
            while True:
                line = fin.readline()
                if line == '':
                    break
                # end of cell card
                if utils.is_blank_line(line) and cell_start and not surf_start:
                    cell_end = True
                    surf_start = True
                    fo.write(line)
                    continue
                if utils.is_comment(line):
                    fo.write(line)
                    continue
                if mcnp_input.is_cell_title(line) and not cell_end:
                    cell_start = True
                    cid, mid, den = mcnp_input.get_cell_cid_mid_den(line)
                    if part.is_cell_id_in_parts(parts, cid):
                        pidx = utils.find_index_by_property(cid,
                                                            parts, prop='cell_ids', find_last=True)
                        ctr = ctrs[i][pidx]
                        ctri = ctr_to_int(ctr)
                        new_line = mcnp_input.cell_title_change_mat(
                            line, mid_new=ctri, den_new=1.0)
                        fo.write(new_line+'\n')
                        continue
                    else:  # this cell do not belong to activated parts, set to void
                        new_line = mcnp_input.cell_title_change_mat(
                            line, mid_new=0, den_new=None)
                        fo.write(new_line+'\n')
                        continue
                if utils.is_blank_line(line) and surf_start and not surf_end:
                    surf_end = True
                    fo.write(line)
                    # append pseudo-mat here
                    fo.write(f"C ---- pseudo-mat for RWC VIS--------\n")
                    fo.write(material.create_pseudo_mat(mid=1).__str__()+'\n')
                    fo.write(material.create_pseudo_mat(mid=2).__str__()+'\n')
                    fo.write(material.create_pseudo_mat(mid=3).__str__()+'\n')
                    fo.write(material.create_pseudo_mat(mid=4).__str__()+'\n')
                    fo.write(material.create_pseudo_mat(mid=5).__str__()+'\n')
                    continue
                fo.write(line)  # other lines
        fo.write('\n')  # new line at the end
        fo.close()
    print(f'NATF: {aim} completed!\n')


def natf_cell_act_pre(config):
    # general
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')
    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)
    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')

    # [fispact]
    # fispact.fispact_materials, optional
    fispact_material_list = config.get(
        'fispact', 'fispact_material_list', fallback='')
    if fispact_material_list != '':
        FISPACT_MATERIAL_LIST = os.path.join(
            work_dir, fispact_material_list)
    # fispact.irradiation_scenario
    irradiation_scenario = os.path.join(
        work_dir, config.get('fispact', 'irradiation_scenario'))
    # fispact.fispact_files_dir, optional
    fispact_files_dir = config.get('fispact', 'fispact_files_dir', fallback='')
    if fispact_files_dir != '':
        fispact_files_dir = os.path.join(work_dir, fispact_files_dir)
    fispact_data_dir = settings.get_fispact_data_dir(config, verbose=False)

    # [model], required
    part_cell_list = os.path.join(
        work_dir, config.get('model', 'part_cell_list'))
    # model.model_degree, optional
    model_degree = float(config.get('model', 'model_degree', fallback=360.0))

    # read the fispact material list
    fispact_materials, fispact_materials_paths = settings.get_fispact_materials(
        fispact_material_list, aim)
    cooling_times = settings.get_cooling_times(irradiation_scenario, aim)
    cooling_times_cul = settings.get_cooling_times_cul(cooling_times)
    # read mcnp output file, get cell information:
    # icl, cid, mid, vol (cm3), mass (g)
    cells = mcnp_output.get_cell_basic_info(mcnp_outp)
    dict_cid_idx = create_cell_idx_dict(cells)
    cells = mcnp_output.get_cell_tally_info(mcnp_outp, cells, tally_number, n_group_size,
                                            continue_output=continue_output)
    materials = get_material_info(mcnp_outp)
    for mat in materials:
        mat.mcnp2fispact()
    cells = match_cells_materials(cells, materials)
    parts = part.get_part(cells, part_cell_list)
    cells_need_cal = settings.get_cell_need_cal(aim, parts, cells)
    cell_fispact_cal_pre(aim, work_dir, cells_need_cal, model_degree,
                         irradiation_scenario, fispact_materials,
                         fispact_materials_paths,
                         fispact_files_dir=fispact_files_dir,
                         fispact_data_dir=fispact_data_dir)
    # generate FISPACT FILES and fisprun.sh

    print(f'NATF: {aim} completed!\n')


def natf_cell_act_post(config):
    # general
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')
    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)
    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')
    with_bounding_box = False
    mcnp_ptrac = config.get('mcnp', 'mcnp_ptrac', fallback='')
    if mcnp_ptrac:
        with_bounding_box = True

    # [fispact]
    # fispact.irradiation_scenario
    irradiation_scenario = os.path.join(
        work_dir, config.get('fispact', 'irradiation_scenario'))
    # nuc treatment
    nuc_treatment = config.get('fispact', 'nuc_treatment', fallback='')
    # fispact.fispact_files_dir, optional
    fispact_files_dir = config.get('fispact', 'fispact_files_dir', fallback='')
    if fispact_files_dir != '':
        fispact_files_dir = os.path.join(work_dir, fispact_files_dir)

    # [model], required
    part_cell_list = os.path.join(
        work_dir, config.get('model', 'part_cell_list'))
    # model.model_degree, optional
    model_degree = float(config.get('model', 'model_degree', fallback=360.0))

    # [radwaste] standard
    rwss = settings.get_radwaste_standards(config)

    # [photon_source], optional
    out_phtn_src = config.getboolean(
        'photon_source', 'out_phtn_src', fallback=False)

    # get the cooling times
    cooling_times = settings.get_cooling_times(irradiation_scenario, aim)
    cooling_times_cul = settings.get_cooling_times_cul(cooling_times)

    # read mcnp output file, get cell information:
    # icl, cid, mid, vol (cm3), mass (g)
    cells = mcnp_output.get_cell_basic_info(mcnp_outp)
    dict_cid_idx = create_cell_idx_dict(cells)
    if mcnp_ptrac:
        cells, aabb = cells_aabb_from_ptrac(
            cells=cells, ptrac_filename=mcnp_ptrac, dict_cid_idx=dict_cid_idx)
    cells = mcnp_output.get_cell_tally_info(mcnp_outp, cells, tally_number, n_group_size,
                                            continue_output=continue_output)
    materials = get_material_info(mcnp_outp)
    for mat in materials:
        mat.mcnp2fispact()
    cells = match_cells_materials(cells, materials)
    parts = part.get_part(cells, part_cell_list)
    cells_need_cal = settings.get_cell_need_cal(aim, parts, cells)
    dict_cid_idx_calc = create_cell_idx_dict(cells_need_cal)

    # deal with the fispact output and data analysis
    # first, check whether all the fispact output files are available
    settings.check_fispact_output_files(
        cells_need_cal, work_dir, aim, fispact_files_dir=fispact_files_dir)
    # then read the output information
    read_fispact_output_cell(cells_need_cal, work_dir, aim,
                             fispact_files_dir=fispact_files_dir,
                             n_group_size=n_group_size, out_phtn_src=out_phtn_src)
    treat_nuc_responses(cells_need_cal, parts,
                        nuc_treatment, dict_cid_idx_calc)
    cell_act_post_process(parts, work_dir, model_degree,
                          aim, cooling_times_cul, rwss=rwss,
                          out_phtn_src=out_phtn_src,
                          with_bounding_box=with_bounding_box)
    print(f'NATF: {aim} completed!\n')


def natf_coolant_act_pre(config):
    # [general]
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')
    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)

    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')

    # [coolant_flow]
    coolant_flow_parameters = os.path.join(work_dir,
                                           config.get('coolant_flow', 'coolant_flow_parameters'))
    flux_multiplier = float(config.get('coolant_flow', 'flux_multiplier'))

    # [fispact]
    # fispact.fispact_material_list, optional
    fispact_material_list = config.get(
        'fispact', 'fispact_material_list', fallback='')
    if fispact_material_list != '':
        fispact_material_list = os.path.join(work_dir, fispact_material_list)

    # fispact.fispact_files_dir, optional
    fispact_files_dir = config.get('fispact', 'fispact_files_dir', fallback='')
    if fispact_files_dir != '':
        fispact_files_dir = os.path.join(work_dir, fispact_files_dir)

    # [model], required
    part_cell_list = os.path.join(work_dir,
                                  config.get('model', 'part_cell_list'))
    # model.model_degree, optional
    model_degree = float(config.get('model', 'model_degree', fallback=360.0))

    # read the fispact material list
    fispact_materials, fispact_materials_paths = settings.get_fispact_materials(
        fispact_material_list, aim)

    cells = mcnp_output.get_cell_basic_info(mcnp_outp)
    dict_cid_idx = create_cell_idx_dict(cells)
    cells = mcnp_output.get_cell_tally_info(
        mcnp_outp, cells, tally_number, n_group_size)
    parts = part.get_part(cells, part_cell_list, coolant_flow_parameters)
    nodes = settings.get_nodes(coolant_flow_parameters)
    parts_fispact_cal_pre(aim, work_dir, parts, model_degree,
                          fispact_materials, fispact_materials_paths,
                          coolant_flow_parameters, flux_multiplier)
    print(f'NATF: {aim} completed!\n')


def natf_coolant_act_post(config):
    # general
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')

    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)
    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')

    # [coolant_flow]
    coolant_flow_parameters = os.path.join(work_dir,
                                           config.get('coolant_flow', 'coolant_flow_parameters'))
    flux_multiplier = float(config.get('coolant_flow', 'flux_multiplier'))

    # [fispact]
    # fispact.fispact_material_list, optional
    fispact_material_list = config.get(
        'fispact', 'fispact_material_list', fallback='')
    if fispact_material_list != '':
        FISPACT_MATERIAL_LIST = os.path.join(
            work_dir, fispact_material_list)

    # fispact.fispact_files_dir, optional
    fispact_files_dir = config.get('fispact', 'fispact_files_dir', fallback='')
    if fispact_files_dir != '':
        fispact_files_dir = os.path.join(work_dir, fispact_files_dir)

    # [model], required
    part_cell_list = os.path.join(work_dir,
                                  config.get('model', 'part_cell_list'))
    # model.model_degree, optional
    model_degree = float(config.get('model', 'model_degree', fallback=360.0))

    # read the fispact material list
    fispact_materials, fispact_materials_paths = settings.get_fispact_materials(
        fispact_material_list, aim)

    cells = mcnp_output.get_cell_basic_info(mcnp_outp)

    dict_cid_idx = create_cell_idx_dict(cells)
    cells = mcnp_output.get_cell_tally_info(
        mcnp_outp, cells, tally_number, n_group_size)
    parts = part.get_part(cells, part_cell_list, coolant_flow_parameters)
    nodes = settings.get_nodes(coolant_flow_parameters)

    # check whether all the fispact output files are available
    settings.check_fispact_output_files(
        parts, work_dir, aim, fispact_files_dir=fispact_files_dir)
    read_fispact_output_part(parts, work_dir, aim,
                             fispact_files_dir=fispact_files_dir)
    coolant_act_post_process(parts, nodes, work_dir, model_degree, aim)
    print(f'NATF: {aim} completed!\n')


def natf_cell_mat_evo(config):
    """
    Monte Carlo and activation coupling calculation. The material will be
    updated at each time step.

    Required inputs:
        - mcnp_inp: mcnp input file
        - mcnp_outp: mcnp output file

    workflow:
        1. generate fispact input file from information provide in mcnp
           input/output and irradiation history/time step.
           Only irradiation is performed if it's not the last time step.
           Both irradiation and cooling is performed if it's last time step.
        2. read fispact output file and get the updated material composition,
           write a new mcnp input file
        3. goto step 1 if the time step is not finished, or goto step 4 if
           it's last time step
        4. perform CELL_ACT_POST with the mcnp output and fispact output.
    """

    # ============= reading parameters from input
    # [general]
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')

    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    continue_output = config.get('mcnp', 'continue_output', fallback='')
    if continue_output:
        continue_output = os.path.join(work_dir, continue_output)
    # mcnp.tally_number
    tally_number = settings.get_tally_number(config)
    # mcnp.n_group_size
    n_group_size = config.getint('mcnp', 'n_group_size')
    # mcnp.nuclide_sets
    nuclide_sets = settings.get_nuclide_sets(config)
    wwinp = settings.get_wwinp(config)

    # [fispact]
    # fispact.irradiation_scenario, required in CELL_ACT and CELL_DPA mode
    irradiation_scenario = config.get('fispact', 'irradiation_scenario')
    # fispact.fispact_files_dir
    # required because large amount of files will be generated for each time step
    fispact_files_dir = config.get('fispact', 'fispact_files_dir')
    if fispact_files_dir != '':
        fispact_files_dir = os.path.join(work_dir, fispact_files_dir)
    fispact_data_dir = settings.get_fispact_data_dir(config)
    # fispact.nuc_treatment, optional
    try:
        nuc_treatment = config.get('fispact', 'nuc_treatment')
        if nuc_treatment != '':
            nuc_treatment = os.path.join(work_dir, nuc_treatment)
    except:
        nuc_treatment = ''
    # fispact.time_step, required, unit: MWY
    power_time_step = float(config.get('fispact', 'power_time_step'))
    # create folder to store temporary files for each step
    dump_dir = 'DUMP_FILES'
    dump_dir = os.path.join(work_dir, dump_dir)
    if not os.path.isdir(dump_dir):
        os.system(f"mkdir -pv {dump_dir}")

    # [model], required
    part_cell_list = os.path.join(
        work_dir, config.get('model', 'part_cell_list'))
    # model.model_degree, optional
    model_degree = float(config.get('model', 'model_degree', fallback=360.0))

    # [debug], optional
    monitor_cells = settings.get_monitor_cells(config)
    print(f"    cell: {monitor_cells} are monitored for dropped nuclides")
    monitor_nucs = settings.get_monitor_nucs(config)
    print(
        f"    nucs: {monitor_nucs} are monitored for inventory vs. iteration")

    # ============= PREPARE start ================
    # check and update status of the workflow
    status_file = 'status.ini'
    irrad_blocks, operation_times = fispact_input.split_irradiation_scenario(
        irradiation_scenario, power_time_step)
    total_steps = len(irrad_blocks)
    current_step = 0
    stat = 'PRE'
    if os.path.isfile(status_file):
        total_steps, current_step, stat = settings.read_mat_evo_status(
            status_file)
    else:  # it is step0 pre if the status file does not exist
        # split irradiation scenario
        fispact_input.generate_sub_irradiation_files(irrad_blocks, dump_dir)
        settings.update_mat_evo_status(
            status_file, total_steps, current_step, stat)

    # Record important parameters and values along with iteration
    # general records
    gr_file = 'general_records.csv'
    if current_step == 0:
        with open(gr_file, 'w') as fo:
            fo.write(
                f"Operation time (MWY),"
                f"Total atoms (atoms),Total mass (grams),"
                f"Dropped atoms (atoms),Dropped mass (grams)"
                "\n")
    # init tbr.csv
    tbr_file = 'tbr.csv'
    if current_step == 0:
        with open(tbr_file, 'w') as fo:
            fo.write("Operation time (MWY),TBR\n")
    # dropped nuclides
    record_file_total = None
    record_file_total = f"monitored_cells_nuc_drop.csv"
    if monitor_cells and current_step == 0:
        with open(record_file_total, 'w') as fo:
            fo.write(
                "Iteration step,Dropped atoms (atoms),Dropped mass (grams)\n")
    # inventory of specific nuclide
    monitor_nucs_file = f"monitored_nucs_inventory.csv"
    if monitor_nucs and current_step == 0:
        cnt = 'Iteration step'
        for nuc in monitor_nucs:
            cnt = f"{cnt},{nuc}(atoms),{nuc}(grams)"
        with open(monitor_nucs_file, 'w') as fo:
            fo.write(f"{cnt}\n")
    # ============= PREPARE end ================

    # ============= step 1 start ===============
    if current_step > 0:
        mcnp_outp = os.path.join(dump_dir, f"step{current_step}", "outp")
        continue_output = os.path.join(dump_dir, f"step{current_step}", "outq")
    step_dir = os.path.join(dump_dir, f"step{current_step}")
    fispact_files_dir = os.path.join(
        step_dir, fispact_files_dir.split("/")[-1])
    if not os.path.exists(fispact_files_dir):
        os.system(f"mkdir -pv {fispact_files_dir}")
    irradiation_scenario = os.path.join(step_dir, "irradiation_scenario")

    if stat == 'PRE':
        # redirect some file to STEP i
        # read the fispact material list
        # mat replacement is not allowed in CELL_MAT_EVO mode
        fispact_materials, fispact_materials_paths = [], []
        # read mcnp output file, get cell information:
        # icl, cid, mid, vol (cm3), mass (g)
        cells = mcnp_output.get_cell_basic_info(mcnp_outp)
        dict_cid_idx = create_cell_idx_dict(cells)
        cells = mcnp_output.get_cell_tally_info(mcnp_outp, cells, tally_number, n_group_size,
                                                continue_output=continue_output, dict_cid_idx=dict_cid_idx)
        materials = get_material_info(mcnp_outp)
        for mat in materials:
            mat.mcnp2fispact()
        cells = match_cells_materials(cells, materials)
        parts = part.get_part(cells, part_cell_list)
        cells_need_cal = settings.get_cell_need_cal(aim, parts, cells)
        cell_fispact_cal_pre(aim, work_dir, cells_need_cal, model_degree,
                             irradiation_scenario, fispact_materials,
                             fispact_materials_paths,
                             fispact_files_dir=fispact_files_dir,
                             fispact_data_dir=fispact_data_dir)
        if current_step > 0:
            tally_numbers = mcnp_input.get_tally_numbers(mcnp_inp)
            tbr_tallies = mcnp_input.update_mcnp_input_tallies(
                mcnp_inp, cells_need_cal, tid_start=max(tally_numbers), write_file=False)
            tbr = mcnp_output.get_tbr_from_mcnp_output(mcnp_outp, tbr_tallies)
            settings.update_tbr_file(
                tbr_file, operation_times[current_step-1], tbr)
        settings.update_mat_evo_status(
            status_file, total_steps, current_step, 'POST')
        print(f"End of NATF {aim}, step {current_step}, {stat}")
    # ============= step 1 end   ===============

    # ============= step 2 start ================
    if stat == 'POST':
        # read mcnp output file, get cell information:
        # icl, cid, mid, vol (cm3), mass (g)
        cells = mcnp_output.get_cell_basic_info(mcnp_outp)
        dict_cid_idx = create_cell_idx_dict(cells)
        cells = mcnp_output.get_cell_tally_info(mcnp_outp, cells, tally_number, n_group_size,
                                                continue_output=continue_output)
        parts = part.get_part(cells, part_cell_list)
        cells_need_cal = settings.get_cell_need_cal(aim, parts, cells)
        # check whether all the fispact output files are available
        settings.check_fispact_output_files(
            cells_need_cal, work_dir, aim, fispact_files_dir=fispact_files_dir)

        # update the material after irradiation
        mids = []
        for c in cells:
            mids.append(c.mid)
        mid_max = max(mids)
        current_mid = max(mid_max, 10000) + 1
        ntrans_avail_nucs = material.get_neutron_library_nuclides(
            nuclide_sets=nuclide_sets)
        nuc_trts = settings.get_nuc_treatments_new(nuc_treatment)
        nt_count = 0
        for i, nt in enumerate(nuc_trts):
            nuc_trts[i] = settings.expand_nuc_treatment_ids_new(
                nt, cells, parts)
            nt_count += len(nt.ids)
        nucs_to_treat = nuc_treat.get_nucs_to_treat_new(nuc_trts)
        total_atoms = 0.0
        total_mass = 0.0
        total_dropped_atoms = 0.0
        total_dropped_mass = 0.0
        monitor_cells_dropped_atoms = 0.0
        monitor_cells_dropped_mass = 0.0
        monitor_nucs_atoms = [0.0]*len(monitor_nucs)
        monitor_nucs_grams = [0.0]*len(monitor_nucs)
        purified_atoms = [0.0]*len(nucs_to_treat)
        purified_grams = [0.0]*len(nucs_to_treat)
        for c in cells_need_cal:
            c_ofname = os.path.join(fispact_files_dir, f"c{c.id}.out")
            mat = get_material_after_irradiation(c_ofname, current_mid)
            # treat the fispact output nuc composition
            # TODO: update material nuclide treat part
            for i, nt in enumerate(nuc_trts):
                for j, cid in enumerate(nt.ids):
                    if cid == c.id:
                        mat, pur_atoms, pur_grams = nuc_treat.treat_fispact_nuc_composition(
                            mat, nt)
                        nidx = nucs_to_treat.index(nt.nuc)
                        purified_atoms[nidx] += pur_atoms * c.mass/1e3
                        purified_grams[nidx] += pur_grams * c.mass/1e3

            # monitor nucs
            for i, nuc in enumerate(monitor_nucs):
                nidx = mat.fispact_material_nuclide.index(nuc)
                nuc_atoms = mat.fispact_material_atoms_kilogram[nidx] * c.mass/1e3
                monitor_nucs_atoms[i] += nuc_atoms
                nuc_grams = mat.fispact_material_grams_kilogram[nidx]*c.mass/1e3
                monitor_nucs_grams[i] += nuc_grams
            # monitor cells
            record_drop = False
            record_file = None
            if c.id in monitor_cells:
                record_drop = True
                record_file = os.path.join(
                    step_dir, f"c{c.id}_drop_ele.csv")
                with open(record_file, 'w') as fo:
                    fo.write("Nuclide,Atoms(atoms/kg),Mass(grams/kg)\n")
            # convert to mcnp material
            drop_atoms, drop_mass = mat.fispact2mcnp(ntrans_avail_nucs,
                                                     record_drop=record_drop,
                                                     record_file=record_file)
            if c.id in monitor_cells:
                monitor_cells_dropped_atoms += drop_atoms * c.mass/1e3
                monitor_cells_dropped_mass += drop_mass * c.mass/1e3
            total_dropped_atoms += drop_atoms * c.mass/1e3
            total_dropped_mass += drop_mass * c.mass/1e3
            c.update_material(mat)
            current_mid += 1
            # update total mass and atoms
            total_atoms += sum(mat.fispact_material_atoms_kilogram) * \
                c.mass/1e3
            total_mass += sum(mat.fispact_material_grams_kilogram) * c.mass/1e3
        # record purified nuclides
        if nuc_treatment:
            purified_nucs_file = f"purified_nucs.csv"
            if current_step == 0:
                # init the purified nucs file
                cnt = 'Iteration step'
                for nuc in nucs_to_treat:
                    cnt = f"{cnt},{nuc}(atoms),{nuc}(grams)"
                with open(purified_nucs_file, 'w') as fo:
                    fo.write(f"{cnt}\n")
            # update the purified nucs file
            cnt = f'{current_step}'
            for i, nuc in enumerate(nucs_to_treat):
                cnt = (f"{cnt},{utils.format_single_output(purified_atoms[i])},"
                       f"{utils.format_single_output(purified_grams[i])}")
            with open(purified_nucs_file, 'a') as fo:
                fo.write(f"{cnt}\n")
        # record dropped atoms of monitored cells
        if monitor_cells:
            with open(record_file_total, 'a') as fo:
                fo.write(
                    f"{current_step},"
                    f"{utils.format_single_output(monitor_cells_dropped_atoms)},"
                    f"{utils.format_single_output(monitor_cells_dropped_mass)}\n")
        # monitor nucs
        if monitor_nucs:
            cnt = f'{current_step}'
            for i, nuc in enumerate(monitor_nucs):
                cnt = (f"{cnt},{utils.format_single_output(monitor_nucs_atoms[i])},"
                       f"{utils.format_single_output(monitor_nucs_grams[i])}")
            with open(monitor_nucs_file, 'a') as fo:
                fo.write(f"{cnt}\n")
        # general records
        with open(gr_file, 'a') as fo:
            fo.write(f"{utils.format_single_output(operation_times[current_step])},"
                     f"{utils.format_single_output(total_atoms)},"
                     f"{utils.format_single_output(total_mass)},"
                     f"{utils.format_single_output(total_dropped_atoms)},"
                     f"{utils.format_single_output(total_dropped_mass)}"
                     f"\n")
        cnt = f"{operation_times[current_step]}"
        if current_step < total_steps - 1:
            # update mcnp input file
            next_step = current_step + 1
            step_dir = os.path.join(dump_dir, f"step{next_step}")
            ofname = os.path.join(step_dir, f"mcnp_input_step{next_step}")
            mcnp_input.update_mcnp_input_materials(
                mcnp_inp, cells_need_cal, ofname, dict_cid_idx=dict_cid_idx)
            tally_numbers = mcnp_input.get_tally_numbers(mcnp_inp)
            mcnp_input.update_mcnp_input_tallies(
                ofname, cells_need_cal, tid_start=max(tally_numbers))
            # copy the wwinp to step dir
            if wwinp:
                os.system(f"cp {wwinp} {os.path.join(step_dir, wwinp)}")
            # update status
            settings.update_mat_evo_status(
                status_file, total_steps, next_step, 'PRE')
            print(f"End of NATF {aim}, step {current_step}, {stat}")
        if current_step == total_steps - 1:
            # deal with the fispact output and data analysis
            # the finial post processing, perform CELL_ACT_POST
            aim = 'CELL_ACT_POST'
            # [radwaste] standard
            rwss = settings.get_radwaste_standards(config)
            # get the cooling times
            cooling_times = settings.get_cooling_times(irradiation_scenario)
            cooling_times_cul = settings.get_cooling_times_cul(cooling_times)

            # read the activation responses
            read_fispact_output_cell(cells_need_cal, work_dir, aim,
                                     fispact_files_dir=fispact_files_dir,
                                     n_group_size=n_group_size)
            treat_nuc_responses(cells_need_cal, parts, nuc_treatment)
            cell_act_post_process(parts, step_dir, model_degree,
                                  aim, cooling_times_cul, rwss=rwss)
            # update status
            settings.update_mat_evo_status(
                status_file, total_steps, total_steps-1, 'FIN')
            print(
                f"End of NATF CELL_MAT_EVO and CELL_ACT_POST, step {current_step}, {stat}")
            print(f'NATF: CELL_MAT_EVO completed!\n')


def natf_cell_split(config):
    # general
    work_dir = config.get('general', 'work_dir', fallback='.')
    aim = config.get('general', 'aim')
    # [mcnp]
    mcnp_inp = os.path.join(work_dir, config.get('mcnp', 'mcnp_input'))
    mcnp_outp = os.path.join(work_dir, config.get('mcnp', 'mcnp_output'))
    mcnp_ptrac = os.path.join(work_dir, config.get('mcnp', 'mcnp_ptrac'))

    # [geometry]
    geom = config.get('geometry', 'geom', fallback='XYZ')
    direction = config.get('geometry', 'direction', fallback='X')
    distance = int(config.get('geometry', 'distance', fallback='10'))
    bounds_str = config.get('geometry', 'bounds')
    bounds = []
    if bounds_str:
        if len(bounds_str) != 2:
            raise ValueError(f"only two values are supported")
        bounds[0] = float(bounds_str[0])
        bounds[1] = float(bounds_str[1])
        if bounds[0] >= bounds[1]:
            raise ValueError(f"invalid input of bounds: {bounds_str}")

    # [model], optional
    part_cell_list = config.get('model', 'part_cell_list', fallback='')
    if part_cell_list:
        part_cell_list = os.path.join(work_dir, part_cell_list)
    reset_cell_id = config.getboolean(
        'model', 'reset_cell_id', fallback='True')
    split_void = config.getboolean('model', 'split_void', fallback=False)
    cell_id_start = config.getint('model', 'cell_id_start', fallback=10000)
    surf_id_start = config.getint('model', 'surf_id_start', fallback=10000)
    keep_old_cells = config.getboolean(
        'model', 'keep_old_cells', fallback=True)

    # read mcnp output file, get cell information:
    cells = mcnp_output.get_cell_basic_info(mcnp_outp)
    parts = part.get_part(cells, part_cell_list, create_equal_cell=False)
    dict_cid_idx = {}
    for i, c in enumerate(cells):
        dict_cid_idx[c.id] = i
    cells_info, u_info, fill_info = mcnp_input.read_cells_geom(mcnp_inp)
    max_cell_id = max(cells_info.keys())
    for i in range(len(cells)):
        if u_info[cells[i].id] is not None:
            cells[i].u = u_info[cells[i].id]
        if fill_info[cells[i].id][0] is not None:
            cells[i].fill = fill_info[cells[i].id]
    cells, aabb = cells_aabb_from_ptrac(cells, mcnp_ptrac, dict_cid_idx)
    print("aabb:", aabb)
    coords = mcnp_input.calc_divide_planes(
        aabb, distance=distance, direction=direction)
    print("coords:", coords)

    new_cells = []
    new_cell_counter = 0
    cid_old2new = {}
    if reset_cell_id:
        cell_id_start = 1
    else:
        cell_id_start = max(max_cell_id + 1, cell_id_start)

    #  surfaces
    new_surf_counter = 0
    max_surf_id = mcnp_input.get_max_surf_id(mcnp_inp)
    surf_id_start = max(surf_id_start, max_surf_id + 1)
    surfs_lines = []
    for i in range(len(coords)):
        tmp_surf_id = i + surf_id_start
        surfs_lines.append(f"{tmp_surf_id} P{direction.upper()} {coords[i]}")
    tmp_surf_id = None
    new_surfs = []
    fo = open(f"new_input.txt", 'w')

    need_split = False
    # write cell part
    with open(mcnp_inp, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if utils.is_blank_line(line):
                break
            if utils.is_comment(line):
                fo.write(line)
            elif mcnp_input.is_cell_title(line):
                # get the cell id
                cid, mid, den = mcnp_input.get_cell_cid_mid_den(line)
                cidx = dict_cid_idx[cid]
                c = cells[cidx]
                # split the cell
                tmp_cells, cutting_coords = cell.split_cell(c, coords=coords, distance=distance, direction=direction,
                                                            cell_id_start=new_cell_counter+cell_id_start)
                # create cid map from old to new
                new_cids = []
                for i in range(len(tmp_cells)):
                    new_cids.append(new_cell_counter+1+i)
                cid_old2new[cid] = new_cids

                # do not split a cell when:
                #     - it is small on the direction
                #     - it is void and user do not want to split void
                need_split = not (len(tmp_cells) == 1 or (
                    mid == 0 and not split_void))

                if need_split:
                    # update cell id counts
                    new_cell_counter += len(tmp_cells)
                    # write new cells
                    for i in range(len(tmp_cells)):
                        geom_str = mcnp_input.proper_cell_geom(cells_info[cid])
                        if i == 0:
                            rsurf_id = coords.index(
                                cutting_coords[i]) + surf_id_start
                            geom_str = f"{geom_str} -{rsurf_id}"
                        elif i > 0 and i < len(tmp_cells)-1:
                            lsurf_id = coords.index(
                                cutting_coords[i-1]) + surf_id_start
                            rsurf_id = coords.index(
                                cutting_coords[i]) + surf_id_start
                            geom_str = f"{geom_str} {lsurf_id} -{rsurf_id}"
                        else:
                            lsurf_id = coords.index(
                                cutting_coords[-1]) + surf_id_start
                            geom_str = f"{geom_str} {lsurf_id}"
                        oline = mcnp_input.compose_cell_block(
                            cid=tmp_cells[i].id, mid=mid, density=den,
                            geom_str=geom_str,
                            imp_n=tmp_cells[i].imp_n, imp_p=tmp_cells[i].imp_p,
                            u=tmp_cells[i].u,
                            fill=tmp_cells[i].fill)
                        fo.write(mcnp_input.mcnp_style_line(oline)+'\n')
                else:  # do not need split
                    # rearrange the cid
                    new_cid = new_cell_counter + cell_id_start
                    oline = mcnp_input.compose_cell_block(
                        cid=new_cid, mid=mid, density=den,
                        geom_str=mcnp_input.proper_cell_geom(cells_info[cid]),
                        imp_n=c.imp_n, imp_p=c.imp_p,
                        u=c.u, fill=c.fill)
                    fo.write(mcnp_input.mcnp_style_line(oline)+'\n')
                    new_cell_counter += 1
                # comment origin cell title line
                if keep_old_cells:
                    fo.write(f"C {line}")
            else:  # continue line
                if keep_old_cells:
                    fo.write(f"C {line}")  # comment continue line

    # write surface part
    surf_card_start = False
    surf_card_end = False
    blank_count = 0
    with open(mcnp_inp, 'r', encoding='gb18030') as fin:
        while not surf_card_start:
            line = fin.readline()
            if utils.is_blank_line(line):
                blank_count += 1
                if blank_count == 1:
                    fo.write('\n')
                    surf_card_start = True
                    # read the rest file
                    while not surf_card_end:
                        line = fin.readline()
                        if utils.is_blank_line(line):
                            blank_count += 1
                            if blank_count == 2:
                                surf_card_end = True
                        if not utils.is_blank_line(line):
                            fo.write(line)
                    # origin surf end
                    # write new surfs for split
                    fo.write('C surfaces for split\n')
                    for i in range(len(surfs_lines)):
                        fo.write(surfs_lines[i]+'\n')
                    fo.write('\n')
                    # write rest line
                    while True:
                        line = fin.readline()
                        if line != '':
                            fo.write(line)
                        else:
                            break

    # update part cell list
    print("Updating the part cell list")
    part.update_part_cell_list(part_cell_list, cid_old2new)
    print(f'NATF: {aim} completed!\n')


def natf_run():
    # first check the configure file to get running information
    config_filename = "config.ini"
    config = configparser.ConfigParser()
    print(
        f"NATF version: {natf.__version__} start time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    config.read(config_filename)
    settings.check_config(filename=config_filename)

    # general
    aim = config.get('general', 'aim')
    print(f'Starting NATF: {aim}')
    if aim == 'CELL_RWC_VIS':
        natf_cell_rwc_vis(config)
    if aim in ('CELL_ACT_PRE', 'CELL_DPA_PRE'):
        natf_cell_act_pre(config)
    if aim in ('CELL_ACT_POST', 'CELL_DPA_POST'):
        natf_cell_act_post(config)
    if aim == 'COOLANT_ACT_PRE':
        natf_coolant_act_pre(config)
    if aim == 'COOLANT_ACT_POST':
        natf_coolant_act_post(config)
    if aim == 'CELL_MAT_EVO':
        natf_cell_mat_evo(config)
    if aim == 'CELL_SPLIT':
        natf_cell_split(config)
    return


# codes for test functions
if __name__ == '__main__':
    pass
