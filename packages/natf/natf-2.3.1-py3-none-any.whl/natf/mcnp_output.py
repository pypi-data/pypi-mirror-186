#!/usr/bin/env python3
# -*- coding:utf-8 -*- import numpy as np import re
import argparse
import re
import os
from natf.cell import Cell
from natf import utils
from natf import mcnp_input
from natf import part
import tables
import struct


def is_tally_result_start(line, tally_num=None):
    """
    Check whether a line is the tally result start.

    Parameters:
    -----------
    line: str
        The line to be checked.
    tally_num: int or None
        None: Check this is the start of any tally
        int: Check for the specific tally number.
    """
    tally_start_pattern = re.compile("^1tally .*nps =", re.IGNORECASE)
    if re.match(tally_start_pattern, line):
        # check tally id
        if tally_num is None:
            return True
        else:
            return get_tally_id(line) == tally_num
    else:
        return False


def is_tally_result_end(line):
    tally_end_pattern1 = re.compile(".*tfc bin check", re.IGNORECASE)
    tally_end_pattern2 = re.compile(".*===", re.IGNORECASE)
    if re.match(tally_end_pattern1, line) or re.match(tally_end_pattern2, line):
        return True
    else:
        return False


def get_tally_id(line):
    if not is_tally_result_start(line):
        raise ValueError(f"line: {line} is not tally result start")
    line_ele = line.strip().split()
    return int(line_ele[1])


def has_tally_result(filename, tally_num=[4]):
    """Check whether the file contain specific tally result"""
    if filename is None or filename == '':
        return False
    if not os.path.isfile(filename):
        return False
    if isinstance(tally_num, int):
        tally_num = [tally_num]
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                return False
            if is_tally_result_start(line):
                if get_tally_id(line) in tally_num:
                    return True
    return False


def get_tally_file(mcnp_output, continue_output, tally_number):
    """
    Check which file to use when both mcnp_output and continue_output are provided.
    """
    # check tally results
    if has_tally_result(mcnp_output, tally_number) and \
            not has_tally_result(continue_output, tally_number):
        return mcnp_output
    if has_tally_result(continue_output, tally_number):
        print(f"Tally {tally_number} results in {continue_output} will be used")
        return continue_output
    if not has_tally_result(mcnp_output, tally_number) and \
            not has_tally_result(continue_output, tally_number):
        raise ValueError(
            f"ERROR: {mcnp_output} and {continue_output} do not have tally result")


def get_cell_names_from_line(line):
    """
    """
    cell_names = []
    ls = line.strip().split()
    for i in range(1, len(ls)):
        cell_names.append(int(ls[i]))
    return cell_names


def read_tally_result_single_cell_single_group(filename, tally_num=4, with_fm=False):
    """
    Get the result for a tally that has only single cell, single energy group and with FM card.
    This can be used for the tbr calculation for new tallies.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    """
    cids, results, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                if is_tally_result_end(line1):
                    break
                if " cell " in line1:
                    cid = get_cell_names_from_line(line1)
                    cids.extend(cid)
                    line = fin.readline()
                    if with_fm:
                        line = fin.readline()
                    line_ele = line.split()
                    for j in range(len(cid)):
                        results.append(float(line_ele[2 * j]))
                        errs.append(float(line_ele[2 * j + 1]))
            break
    fin.close()
    return cids, results, errs


def read_tally_result_single_group(filename, tally_num=4):
    """
    Get the single group neutron flux for a tally.
    This is used for the volume calculation.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    """
    cids, results, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                if is_tally_result_end(line1):
                    break
                if " cell " in line1:
                    cid = get_cell_names_from_line(line1)
                    cids.extend(cid)
                    line = fin.readline()
                    if 'multiplier' in line:
                        line = fin.readline()
                    line_ele = line.split()
                    for j in range(len(cid)):
                        results.append(float(line_ele[2 * j]))
                        errs.append(float(line_ele[2 * j + 1]))
            break
    fin.close()
    return cids, results, errs


def get_dumped_nps(filename):
    """
    Get the dumped nps.

    Parameters:
    -----------
    filename : str
        The mcnp output file

    Returns:
    --------
    dumped_nps : list
        The list of dumped nps
    """
    dumped_nps = []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '' or 'computer time =' in line:
                break
            if is_tally_result_start(line):
                nps = float(line.strip().split()[-1])
                if nps not in dumped_nps:
                    dumped_nps.append(nps)
            else:
                continue
    if len(dumped_nps) == 0:
        raise ValueError(f"file {filename} does not have valid dumped nps")
    print(f"    the dumped nps in {filename} are {dumped_nps}")
    return dumped_nps


def read_cell_neutron_flux_single_tally(filename, tally_num=4, n_group_size=175):
    """
    Get the neutron flux for a single tally.

    Parameters:
    -----------
    filename: str
        the mcnp output file to be read
    tally_number: int
        tally number
    n_group_size: int
        Number of group size, 69, 175, 315 or 709.
    """
    cids, fluxes, errs = [], [], []
    dumped_nps = get_dumped_nps(filename)
    fin = open(filename)
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError(
                f'1tally {tally_num} not found in the file, wrong file!')
        if not is_tally_result_start(line):
            continue
        # check nps
        nps = float(line.strip().split()[-1])
        if nps < dumped_nps[-1]:
            continue
        if get_tally_id(line) == tally_num:
            while True:
                line1 = fin.readline()
                line_ele1 = line1.split()
                if utils.is_blank_line(line1):
                    continue
                # end of the cell neutron flux information part
                if is_tally_result_end(line1):
                    break
                if 'cell' in line1:
                    line2 = fin.readline()
                    if 'energy' in line2:  # the following 176/710 lines are neutron flux information
                        cid = get_cell_names_from_line(line1)
                        cids.extend(cid)
                        cell_flux = []
                        cell_error = []
                        if n_group_size >= 2:
                            num_data = n_group_size + 1
                        else:
                            raise ValueError(
                                f"Wrong n_group_size:{n_group_size}")
                        for i in range(num_data):
                            line = fin.readline()
                            # check the neutron energy group
                            if i == n_group_size:
                                if 'total' not in line:
                                    errormessage = ''.join(
                                        [
                                            'ERROR in reading cell neutron flux\n',
                                            'Neutron energy group is ',
                                            str(n_group_size),
                                            ' in input file\n',
                                            'But keyword: \'total\' not found in the end!\n',
                                            'Check the neutron energy group in the output file\n'])
                                    raise ValueError(errormessage)
                            line_ele = line.split()
                            erg_flux = []
                            erg_error = []
                            for j in range(len(cid)):
                                erg_flux.append(float(line_ele[2 * j + 1]))
                                erg_error.append(float(line_ele[2 * j + 2]))
                            cell_flux.append(erg_flux)
                            cell_error.append(erg_error)
                        for i in range(len(cid)):
                            temp_flux = []
                            temp_error = []
                            for j in range(num_data):
                                temp_flux.append(cell_flux[j][i])
                                temp_error.append(cell_error[j][i])
                            fluxes.append(temp_flux)
                            errs.append(temp_error)
            break
    fin.close()
    print(
        f"    finish reading neutron flux from {filename} tally {tally_num} at nps of {nps:.5E}")
    return cids, fluxes, errs


def tallied_vol_to_tally(inp="outp", output="tally_card.txt", n_group_size=175,
                         part_cell_list=None):
    """
    Read the f4 tally for volume, get the cids, vols, errs info and write
    tally card.
    """
    parser = argparse.ArgumentParser(
        description="""Read the tallied cell volumes from MCNP output file and write as tally (SD) card""")
    parser.add_argument("-i", "--input", required=False, default="outp",
                        help="output of the vol tally file path, default: outp")
    parser.add_argument("-o", "--output", required=False, default="tally_card.txt",
                        help="save the tally_card to output file, default: tally_card.txt")
    parser.add_argument("-t", "--tally_num", required=False, default=4, type=int,
                        help="the tally number of volume info, default: 4")
    parser.add_argument("-g", "--group", required=False, default=175, type=int,
                        help="the neutron energy group used in tally, default: 175")
    parser.add_argument("-p", "--part_cell_list", required=False,
                        help="the part_cell_list will be automatically updated if provided by removing cells with invalid (ZERO) volume.")

    args = vars(parser.parse_args())

    # red cis/vols/errs from mcnp outp
    outp_file = args['input']
    tally_num = int(args['tally_num'])
    e_group_size = 175
    if args['group'] is not None:
        e_group_size = int(args['group'])
    e_groups = utils.get_e_group(e_group_size, reverse=False)
    if args['part_cell_list'] is not None:
        part_cell_list = args['part_cell_list']

    cids, vols, errs = read_tally_result_single_group(
        outp_file, tally_num=tally_num)

    # check calculated vol
    zero_vol_cids = []
    large_err_cids = []
    for i in range(len(cids)):
        if vols[i] <= 0.0:
            zero_vol_cids.append(cids[i])
        if errs[i] >= 0.05:
            large_err_cids.append(cids[i])

    # remove zero vol from tally card
    if len(zero_vol_cids) > 0:
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=f'  WARNING: {len(zero_vol_cids)} cells have invalid (0.0) vols:', cids=zero_vol_cids)
        print(warn_str)
        new_cids = []
        new_vols = []
        new_errs = []
        for i in range(len(cids)):
            if vols[i] > 0.0:
                new_cids.append(cids[i])
                new_vols.append(vols[i])
                new_errs.append(errs[i])
        cids = new_cids
        vols = new_vols
        errs = new_errs
    if len(large_err_cids) > 0:
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=f"  warning: {len(large_err_cids)} cells have large relative error:", cids=large_err_cids)

    # save valid data into a tally style card
    output = "tally_card.txt"
    if args['output'] is not None:
        output = args['output']
    mcnp_input.mcnp_tally_style(
        cids, sds=vols, output=output, e_group_size=e_group_size)

    # update part_cell_list
    if part_cell_list is not None:
        part.part_cell_list_remove_invalid_cids(
            part_cell_list=part_cell_list, invalid_cids=zero_vol_cids)


def update_cell_flux(cells, cids, fluxes, dict_cid_idx=None):
    """
    Update the cell volume according to the given cids and volumes.
    """
    for i in range(len(cids)):
        if dict_cid_idx:
            cidx = dict_cid_idx[cids[i]]
        else:
            cidx = utils.find_index_by_property(cids[i], cells, 'id')
        cells[cidx].neutron_flux = fluxes[i]
    return cells


@utils.log
def get_cell_neutron_flux(mcnp_output, cells, tally_number, n_group_size, continue_output=None, dict_cid_idx=None):
    """get_cell_neutron_flux: read the mcnp output file and get the neutron flux of the cell

    Parameters:
    -----------
    mcnp_output: str
        the mcnp output file
    cells: list
        the list of Cell
    tally_number: int
        tally number
    n_group_size: int
        Number of group size, 69, 175, 315 or 709.
    continue_output: str, optional
       The output file of continue run, contains neutron flux info. Used when
       the mcnp_output file does not contain neutron flux info.

    Returns:
    --------
    cells: list
        cells that have the neutron flux information in it
    """
    tally_file = get_tally_file(mcnp_output, continue_output, tally_number)
    if isinstance(tally_number, int):
        cids, fluxes, errs = read_cell_neutron_flux_single_tally(
            tally_file, tally_number, n_group_size)
        cells = update_cell_flux(
            cells, cids, fluxes, dict_cid_idx=dict_cid_idx)
    elif isinstance(tally_number, list):
        for i in range(len(tally_number)):
            cids, fluxes, errs = read_cell_neutron_flux_single_tally(
                tally_file, tally_number[i], n_group_size)
            cells = update_cell_flux(
                cells, cids, fluxes, dict_cid_idx=dict_cid_idx)
    print('    read cell neutron flux completed')
    return cells


def read_cell_vol_single_tally(filename, tally_num):
    """
    Read the cell, volume and mass information for specific tally.
    """
    cids, vols = [], []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                raise ValueError(
                    f'tally result not found in the file, wrong file!')
            if is_tally_result_start(line, tally_num):
                # read the following line
                line = fin.readline()
                line = fin.readline()
                line = fin.readline()
                line = fin.readline()
                while True:
                    line = fin.readline()
                    line_ele = line.split()
                    if len(line_ele) == 0:  # end of the volumes
                        break
                    # otherwise, there are volume information
                    if line_ele[0] == 'cell:':  # this line contains cell names
                        cell_names = get_cell_names_from_line(line)
                        line = fin.readline()  # this is the volume information
                        line_ele = line.split()
                        cell_vols = get_cell_vols_from_line(line)
                        cids.extend(cell_names)
                        vols.extend(cell_vols)
                break
    return cids, vols


def update_cell_vol(cells, cids, vols, dict_cid_idx=None):
    """
    Update the cell volume according to the given cids and volumes.
    """
    for i in range(len(cids)):
        if dict_cid_idx:
            cidx = dict_cid_idx[cids[i]]
        else:
            cidx = utils.find_index_by_property(cids[i], cells, 'id')
        cells[cidx].vol = vols[i]
    return cells


@utils.log
def get_cell_vol_mass(mcnp_output, cells, tally_number, continue_output=None,
                      dict_cid_idx=None, verbose=True):
    """
    Read the mcnp output file and get the volumes and masses defined in SD cards.

    Parameters:
    -----------
    mcnp_output : string
        The mcnp output file
    cells : list of Cell
        The cells list
    tally_number : int or list of int
        The tally numbers
    continue_output : string
        The output filename of continue run
    dict_cid_idx: dict
        The cell id index dict
    verbose: bool
        Whether to print warning messages

    Returns:
    --------
    cells : list of Cell
        The cells with updated volume and mass
    """

    # open the mcnp output file
    tally_file = get_tally_file(mcnp_output, continue_output, tally_number)
    if isinstance(tally_number, int):
        cids, vols = read_cell_vol_single_tally(tally_file, tally_number)
        cells = update_cell_vol(cells, cids, vols, dict_cid_idx=dict_cid_idx)
    elif isinstance(tally_number, list):
        for i in range(len(tally_number)):
            cids, vols = read_cell_vol_single_tally(
                tally_file, tally_number[i])
            cells = update_cell_vol(
                cells, cids, vols, dict_cid_idx=dict_cid_idx)

    # update the mass of the cells
    cids_invalid_vol = []
    for c in cells:
        if c.vol > 0:
            c.mass = c.density * c.vol
        else:
            cids_invalid_vol.append(c.id)
    if verbose:
        warn_title = '    warning: cells without valid vol/mass:'
        warn_str = utils.compose_warning_message_for_cids(
            warn_title=warn_title, cids=cids_invalid_vol)
        print(warn_str)
    return cells


@utils.log
def get_cell_tally_info(mcnp_output, cells, tally_number, n_group_size,
                        continue_output=None, dict_cid_idx=None):
    """get_cell_tally_info: run this only for the cell tally condition"""
    cells = get_cell_vol_mass(mcnp_output, cells, tally_number,
                              continue_output=continue_output, dict_cid_idx=dict_cid_idx)
    cells = get_cell_neutron_flux(mcnp_output, cells, tally_number,
                                  n_group_size, continue_output=continue_output, dict_cid_idx=dict_cid_idx)
    return cells


def get_cell_vols_from_line(line):
    cell_vols = []
    ls = line.strip().split()
    for i in range(len(ls)):
        cell_vols.append(float(ls[i]))
    return cell_vols


def is_cell_info_start(line):
    """
    Check if this line is the cells info start.
    """
    # This check works for MCNP5 1.2
    if "cells" in line and "print table 60" in line:
        return True
    else:
        return False


@utils.log
def get_cell_basic_info(mcnp_output):
    """
    Get the basic information of cells.
    The basic info include:
        - icl : the problem number (index) of the cell
        - id : the id (named by user in input file) of the cell
        - mid : material id (named by user) of the cell
        - gram density : the material density in [g/cm3]
        - vol : the volume calculated by mcnp
        - mass : the mass calculated by mcnp
        - imp_n : the neutron importance

    Parameters:
    -----------
    mcnp_output : string
        The mcnp outp file. It contains '1cells' info

    Returns:
    --------
    cells : list of Cell
        The list of cells in the problem.
    """

    cells = []
    fin = open(mcnp_output, 'r')
    while True:
        line = fin.readline()
        if line == '':
            raise ValueError('1cells not found in the file, wrong file!')
        if is_cell_info_start(line):  # read 1cells
            # read the following line
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            line = fin.readline()
            while True:
                temp_c = Cell()
                line = fin.readline()
                if ' total' in line:  # end of the cell information part
                    break
                # check data
                line_ele = line.split()
                if len(line_ele) == 0:  # skip the blank line
                    continue
                if str(line_ele[0]).isdigit():  # the first element is int number
                    temp_c.icl = int(line_ele[0])
                    temp_c.id = int(line_ele[1])
                    temp_c.mid = int(line_ele[2])
                    temp_c.density = float(line_ele[4])
                    temp_c.vol = float(line_ele[5])
                    temp_c.mass = float(line_ele[6])
                    temp_c.imp_n = float(line_ele[8])
                    if len(line_ele) >= 10:
                        temp_c.imp_p = float(line_ele[9])
                cells.append(temp_c)
            break
    fin.close()
    return cells


def get_mid_nucs_fracs(line):
    """
    Get the material id, nuclide list and fraction.
    """
    tokens = line.strip().split()
    mid = int(tokens[0])
    nucs, fracs = [], []
    for i in range(1, len(tokens), 2):
        nucs.append(tokens[i][:-1])
        fracs.append(float(tokens[i+1]))
    return mid, nucs, fracs


def get_nucs_fracs(line):
    """
    Get the material nuclide list and fraction.
    """
    tokens = line.strip().split()
    nucs, fracs = [], []
    for i in range(0, len(tokens), 2):
        nucs.append(tokens[i][:-1])
        fracs.append(float(tokens[i+1]))
    return nucs, fracs


def get_material_basic_info(mcnp_output):
    """
    Get the basic information of the material.
    - mat_number
    - density
    - nuc_vec: dict of nuclide/mass_fraction pair
    """
    cells = get_cell_basic_info(mcnp_output)
    # get used materials ids
    mids, densities, nuc_vecs = [], [], []
    mid = 0
    # read material composition
    with open(mcnp_output, 'r', encoding='utf-8') as fin:
        while True:
            line = fin.readline()
            if line == '':
                raise ValueError("material composition not found in the file")
            if 'number     component nuclide, mass fraction' in line:  # start of material composition
                while True:
                    line = fin.readline()
                    if 'cell volumes and masses' in line:  # end of material composition
                        # save the last material
                        mids.append(mid)
                        cidx = utils.find_index_by_property(mid, cells, 'mid')
                        densities.append(cells[cidx].density)
                        nuc_vecs.append(nuc_vec)
                        break
                    if utils.is_blank_line(line) or 'warning' in line:
                        continue
                    tokens = line.strip().split()
                    if len(tokens) % 2 != 0:  # this line contain mid
                        if mid > 0:  # not the first material, save the previous one
                            mids.append(mid)
                            cidx = utils.find_index_by_property(
                                mid, cells, 'mid')
                            densities.append(cells[cidx].density)
                            nuc_vecs.append(nuc_vec)
                        nuc_vec = {}
                        mid, nucs, fracs = get_mid_nucs_fracs(line)
                    else:  # this line do not have mid
                        nucs, fracs = get_nucs_fracs(line)
                    # update the nuc_vec
                    for i, nuc in enumerate(nucs):
                        if nuc not in nuc_vec.keys():
                            nuc_vec[nuc] = fracs[i]
                        else:
                            nuc_vec[nuc] += fracs[i]
                break
    return mids, densities, nuc_vecs


def get_tbr_from_mcnp_output(filename, tallies):
    """
    Read the MCNP output file to get the tbr.
    The TBR for each breeder cells may distributed in difference tallies.

    Parameters:
    -----------
    filename: str
        The MCNP output file.
    tallies: list of int
        The tally number that contains TBR information.
    """
    tbr_total = 0.0
    for tid in tallies:
        cids, tbr_tmps, errs = read_tally_result_single_cell_single_group(
            filename, tally_num=tid, with_fm=True)
        tbr_total += tbr_tmps[0]
    return tbr_total


def read_cpu_time(filename):
    """
    read the mcnp output file to get the cpu time

    Returns:
    cpu_time : float
        The CPU time in [minutes]
    """
    with open(filename, 'r') as f:
        for line in f:
            line = line.rstrip()
            # start read data
            if "computer time =" in line:
                row = line.split('=')
                cpu_time = float(row[-1].split()[0])
                break
    return cpu_time


class PtracEvent(tables.IsDescription):
    """This class holds one Ptrac event and serves as a table definition
    for saving Ptrac data to a HDF5 file.
    """

    event_type = tables.Int32Col()
    node = tables.Float32Col()
    nsr = tables.Float32Col()
    nsf = tables.Float32Col()
    nxs = tables.Float32Col()
    ntyn = tables.Float32Col()
    ipt = tables.Float32Col()
    ncl = tables.Float32Col()
    mat = tables.Float32Col()
    ncp = tables.Float32Col()
    xxx = tables.Float32Col()
    yyy = tables.Float32Col()
    zzz = tables.Float32Col()
    uuu = tables.Float32Col()
    vvv = tables.Float32Col()
    www = tables.Float32Col()
    erg = tables.Float32Col()
    wgt = tables.Float32Col()
    tme = tables.Float32Col()


class PtracReader(object):
    """Class to read _binary_ PTRAC files generated by MCNP."""

    def __init__(self, filename):
        """Construct a new Ptrac reader for a given filename, determine the
        number format and read the file's headers.
        """

        self.variable_mappings = {
            1: "nps",
            3: "ncl",
            4: "nsf",  # surface id
            8: "node",
            9: "nsr",
            10: "nxs",
            11: "ntyn",
            12: "nsf",
            16: "ipt",
            17: "ncl",
            18: "mat",
            19: "ncp",
            20: "xxx",  # position x
            21: "yyy",  # position y
            22: "zzz",  # position z
            23: "uuu",  # cos(x-direction)
            24: "vvv",  # cos(y-direction)
            25: "www",  # cos(z-direction)
            26: "erg",  # energy
            27: "wgt",  # weight
            28: "tme",
        }

        self.eightbytes = False

        self.f = open(filename, "rb")
        self.determine_endianness()
        self.read_headers()
        self.read_variable_ids()

        self.next_event = 0

    def __del__(self):
        """Destructor. The only thing to do is close the Ptrac file."""
        self.f.close()

    def determine_endianness(self):
        """Determine the number format (endianness) used in the Ptrac file.
        For this, the file's first entry is used. It is always minus one
        and has a length of 4 bytes, unless compiled with 8-byte ints.
        """

        # read and unpack first 4 bytes
        b = self.f.read(4)
        should_be_4 = struct.unpack("<i", b)[0]
        if should_be_4 == 4:
            self.endianness = "<"
        else:
            self.endianness = ">"

        # discard the next 8 bytes (the value -1 and another 4)
        c = self.f.read(8)
        assert c[4:8] == b, (
            "8 byte integers compilation flag " "not supported for MCNP6"
        )

    def read_next(self, format, number=1, auto=False, raw_format=False):
        """Helper method for reading records from the Ptrac file.
        All binary records consist of the record content's length in bytes,
        the content itself and then the length again.
        format can be one of the struct module's format characters (i.e. i
        for an int, f for a float, s for a string).
        The length of the record can either be hard-coded by setting the
        number parameter (e.g. to read 10 floats) or determined automatically
        by setting auto=True.
        Setting the parameter raw_format to True means that the format string
        will not be expanded by number, but will be used directly.
        """

        if self.eightbytes and (not raw_format) and format == "f":
            format = "d"
        if self.eightbytes and (not raw_format) and format == "i":
            format = "q"

        # how long is one field of the read values
        format_length = 1
        if format in ["h", "H"] and not raw_format:
            format_length = 2
        elif format in ["i", "I", "l", "L", "f"] and not raw_format:
            format_length = 4
        elif format in ["d", "q", "Q"] and not raw_format:
            format_length = 8

        if auto and not raw_format:
            b = self.f.read(4)

            if b == b"":
                raise EOFError

            length = struct.unpack(self.endianness.encode() + b"i", b)[0]
            number = length // format_length

            b = self.f.read(length + 4)
            tmp = struct.unpack(
                b"".join([self.endianness.encode(),
                         (format * number).encode(), b"i"]),
                b,
            )
            length2 = tmp[-1]
            tmp = tmp[:-1]
        else:
            bytes_to_read = number * format_length + 8
            b = self.f.read(bytes_to_read)
            if b == b"":
                raise EOFError

            fmt_string = self.endianness + "i"
            if raw_format:
                fmt_string += format + "i"
            else:
                fmt_string += format * number + "i"

            tmp = struct.unpack(fmt_string.encode(), b)
            length = tmp[0]
            length2 = tmp[-1]
            tmp = tmp[1:-1]

        assert length == length2

        if format == "s":
            # return just one string
            return b"".join(tmp).decode()
        elif number == 1:
            # just return the number and not a tuple containing just the number
            return tmp[0]
        else:
            # convert tuple to list
            return list(tmp)

    def read_headers(self):
        """Read and save the MCNP version and problem description from the
        Ptrac file.
        """

        # mcnp version info
        self.mcnp_version_info = self.read_next("s", auto=True)
        # problem title
        self.problem_title = self.read_next("s", auto=True).strip()

        # ptrac input data. can be omitted for now,
        # but has to be parsed, because it has variable length.
        # Also, this is the first difference between a file generated
        # with 4-byte and 8-byte numbers.
        line = self.read_next("f", auto=True)
        # if this line doesn't consist of 10 floats, then we've read them with
        # the wrong byte length and re have to re-read them (and every
        # following float) with 8 bytes length.
        if len(line) != 10:
            self.eightbytes = True
            tmp = struct.pack(self.endianness + "f" * 20, *line)
            line = list(struct.unpack(self.endianness + "d" * 10, tmp))

        # the first item is 13 in MCNP5, 14 in MCNP6. afterwards, there is
        # that times the following scheme:
        # n x_0 ... x_n,
        # where n is the number of values for the current input variable and
        # the x_i are its n values.
        num_variables = int(line[0])  # should always be 13 or 14.
        current_pos = 1
        current_variable = 1

        while current_variable <= num_variables:
            n = int(line[current_pos])
            if current_variable < num_variables and (current_pos + n + 1) >= len(line):
                line += self.read_next("f", 10)
            current_pos += n + 1
            current_variable += 1

    def read_variable_ids(self):
        """Read the list of variable IDs that each record type in the Ptrac
        file is comprised of. The variables can vary for different problems.
        Consult the MCNP manual for details.
        """

        variable_nums = dict()
        variable_ids = dict()

        if self.eightbytes:
            mcnp_version = self.mcnp_version_info[8:13]
            if mcnp_version in ["6    ", "6.mpi"]:
                variable_info = self.read_next(
                    "iqqqqqqqqqqiiiiiiiii", 120, raw_format=True
                )
            else:  # Not sure about MCNPX
                variable_info = self.read_next(
                    "qqqqqqqqqqqiiiiiiiii", 124, raw_format=True
                )
        else:
            variable_info = self.read_next("i", 20)

        variable_nums["nps"] = variable_info[0]
        variable_nums["src"] = variable_info[1] + variable_info[2]
        variable_nums["bnk"] = variable_info[3] + variable_info[4]
        variable_nums["sur"] = variable_info[5] + variable_info[6]
        variable_nums["col"] = variable_info[7] + variable_info[8]
        variable_nums["ter"] = variable_info[9] + variable_info[10]

        num_vars_total = sum(variable_info[:11])

        if self.eightbytes:
            # only the NPS vars are in 8 byte, the other ones are still 4
            fmt_string = "q" * variable_info[0] + \
                "i" * sum(variable_info[1:11])
            fmt_length = 8 * variable_info[0] + 4 * sum(variable_info[1:11])
            all_var_ids = self.read_next(
                fmt_string, fmt_length, raw_format=True)
        else:
            all_var_ids = self.read_next("i", num_vars_total)

        for l in ["nps", "src", "bnk", "sur", "col", "ter"]:
            variable_ids[l] = all_var_ids[: variable_nums[l]]
            all_var_ids = all_var_ids[variable_nums[l]:]

        self.variable_nums = variable_nums
        self.variable_ids = variable_ids

    def read_nps_line(self):
        """Read an NPS record and save the type of the next event."""
        nps_line = self.read_next("i", self.variable_nums["nps"])
        self.next_event = nps_line[1]

    def read_event_line(self, ptrac_event):
        """Read an event record and save it to a given PtracParticle instance."""

        # save for current event, because this record
        # contains only the next event's type
        event_type = self.next_event

        if event_type == 1000:
            e = "src"
        elif event_type == 3000:
            e = "sur"
        elif event_type == 4000:
            e = "col"
        elif event_type == 5000:
            e = "ter"
        else:
            e = "bnk"

        evt_line = self.read_next("f", self.variable_nums[e])

        self.next_event = evt_line[0]

        for i, j in enumerate(self.variable_ids[e][1:]):
            if j in self.variable_mappings:
                ptrac_event[self.variable_mappings[j]] = evt_line[i + 1]
        ptrac_event["event_type"] = event_type

    def write_to_hdf5_table(self, hdf5_table, print_progress=0):
        """Writes the events contained in this Ptrac file to a given HDF5
        table. The table must already exist and have rows that match the
        PtracEvent definition.
        If desired, the number of processed events can be printed to the
        console each N events by passing the print_progress=N parameter.
        """

        ptrac_event = hdf5_table.row
        counter = 0

        while True:
            try:
                self.read_nps_line()
            except EOFError:
                break  # no more entries

            while self.next_event != 9000:
                self.read_event_line(ptrac_event)
                ptrac_event.append()

                counter += 1
                if print_progress > 0 and counter % print_progress == 0:
                    print("processing event {0}".format(counter))


def ptrac_to_hdf5(ptrac_filename):
    """
    Convert binary ptrac file to hdf5 format.
    """
    ptrac = PtracReader(ptrac_filename)
    hdf5_filename = f"{ptrac_filename}.h5"

    # open HDF5 file and create table if it doesn't exist yet
    h5file = tables.open_file(hdf5_filename, mode="a",
                              title=ptrac.problem_title)
    table_name = 'ptrac'
    table_title = 'Ptrac data'
    table_path = "/" + table_name
    if table_path in h5file:
        table = h5file.get_node(table_path)
    else:
        table = h5file.create_table(
            "/", table_name, PtracEvent, table_title)

    print("Writing ptrac.h5 ...")
    ptrac.write_to_hdf5_table(table, print_progress=1000000)

    table.flush()
    h5file.close()
