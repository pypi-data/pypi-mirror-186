#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import os
from natf import utils
from natf import settings


def get_flux(line):
    """
    Get the power time from a line with FLUX.
    """
    # get power
    line_ele = line.strip().split()
    flux = float(line_ele[1])
    return flux


def get_power(line):
    """
    Get the power time from a line with FLUX.
    """
    # get power
    flux = get_flux(line)
    power = utils.neutron_intensity_to_power(flux)
    return power


def get_time(line, unit='s'):
    """
    Get the irradiation or cooling time from line.

    Parameters:
    -----------
    line: str
        The line to extract data.
    unit: str
        The output unit of time, default is [s].
    """
    line_ele = line.strip().split()
    time_s = utils.time_to_sec(line_ele[1], line_ele[2])
    time = utils.time_sec_to_unit(time_s, unit)
    return time


def get_total_power_time(irradiation_scenario):
    """
    Get the total power time [MWY] for a given irradiation scenario.
    """
    total_power_time = 0.0
    fin = open(irradiation_scenario, 'r')
    while True:
        line = fin.readline()
        if line == '':
            fin.close()
            raise ValueError(
                f"{irradiation_scenario} does not have a end (keywork: ZERO) of irradiation phase")
        if utils.is_comment(line, code='fispact'):
            continue
        if 'FLUX' in line.upper():
            power = get_power(line)
        if 'TIME' in line.upper():
            time = get_time(line, unit='a')
            total_power_time += power*time
        if 'ZERO' in line.upper():
            break
    fin.close()
    return total_power_time


def concate_irradiation_block(block, flux_line, time_line):
    """
    Concate the irradiation block.

    Parameters:
    -----------
    block: str
        Current irradiation block.
    flux_line: str
        The line contain 'FLUX' information, with '\n'.
    time_line: str
        The line contain 'TIME' information, with '\n'.

    Returns:
    block: str
        Updated block
    """

    flux_line = flux_line.strip()
    time_line = time_line.strip()
    if 'ZERO' in block and 'ZERO' in time_line:
        return block
    if len(block) > 0:
        block = f"{block}\n{flux_line}\n{time_line}"
    else:
        block = f"{flux_line}\n{time_line}"
    return block


def get_cooling_block(irradiation_scenario):
    """
    Get the cooling block of the irradiation scenario.
    """
    cooling_block = ''
    with open(irradiation_scenario, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if 'ZERO' in line.upper():
                while True:
                    line = fin.readline()
                    if line == '':
                        break
                    if utils.is_comment(line, code='fispact'):
                        continue
                    if 'TIME' in line.upper():
                        cooling_block = f"{cooling_block}{line}"
    return cooling_block


def create_sub_irradiation_scenario(irradiation_scenario, step, start_point):
    """
    Generate a sub irradiation scenario contains irradiation of power_time_step
    start from the given start_point.
    For example, total power time step 200, step 20, start 100 will generate a
    irradiation scenario start at 100 [MWY], and last for 20 [MWY].

    Parameters:
    -----------
    irradiation_scenario: str
        The irradiation scenario file 
    step: float
        The power_time_step [MWY]
    start_point: float
        The start power*time point of irradiation [MWY]
    """

    otext = ''
    irrad_count = 0.0
    current_point = 0.0
    with open(irradiation_scenario, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if utils.is_comment(line, code='fispact'):
                continue
            if 'FLUX' in line.upper():
                line1 = line
                power = get_power(line1)
                line2 = fin.readline()
                if 'ZERO' in line2.upper():  # flux 0.0
                    otext = f"{otext}\n{line1}\n{line2}"
                    fin.close()
                    return otext
                time = get_time(line2, unit='a')
                irrad_count += power*time
                if irrad_count > start_point and irrad_count <= start_point + step:
                    # keep the remain time of current flux
                    tmp_time = (
                        irrad_count - max(current_point, start_point)) / power
                    tmp_line = f"TIME {tmp_time} YEARS ATOMS\n"
                    current_point += power*tmp_time
                    otext = concate_irradiation_block(otext, line1, tmp_line)
                    # check the next flux, if it's cooling, use it, otherwise ignore
                    last_pos = fin.tell()
                    while True:
                        next_line = fin.readline()
                        if utils.is_comment(next_line, code='fispact'):
                            continue
                        if 'FLUX' in next_line:
                            next_power = get_power(next_line)
                            if next_power <= 0:
                                next_time_line = fin.readline()
                                otext = concate_irradiation_block(
                                    otext, next_line, next_time_line)
                                if irrad_count == start_point + step:
                                    otext = concate_irradiation_block(
                                        otext, "FLUX 0.0", "ZERO")
                                    return otext
                            else:
                                # next flux is not zero, rewind to previous line
                                fin.seek(last_pos)
                            break
                elif irrad_count > start_point + step:
                    # flux do not change, but time change to step/power
                    tmp_time = (step - current_point) / power
                    if tmp_time > 0:
                        tmp_line = f"TIME {tmp_time} YEARS ATOMS\n"
                        otext = concate_irradiation_block(
                            otext, line1, tmp_line)
                    otext = concate_irradiation_block(
                        otext, "FLUX 0.0", "ZERO")
                    fin.close()
                    return otext
    fin.close()
    return otext


def split_irradiation_scenario(irradiation_scenario, power_time_step):
    """
    Split the irradiation scenario according to the power time step.
    General rules for splitting the irradiation scenario:
        - split only when power_time larger than step, otherwise raise an ValueError
        - if there are [n] sub-irradiation scenarios, the 1 to n-1 only irradiates, the last one irradiate then cooling
        - there may cooling between two irradiates, the cooling can not be used separately, put it in irradiates after cooling

    Parameters:
    -----------
    irradiation_scenario: str
        The irradiation scenario file
    power_time_step: float    
        The step in unit of [MWY].

    Returns:
    --------
    irrad_scens: list of str
        The sub irradiation_scenario contents
    operation_times: list of float
        The operation time for each time step.
    """

    total_power_time = get_total_power_time(irradiation_scenario)
    sub_irrads = []
    operation_times = []
    fin = open(irradiation_scenario, 'r')
    if total_power_time <= power_time_step:
        text = fin.read()
        sub_irrads.append(text)
        fin.close()
        return sub_irrads, [total_power_time]
    else:
        current_point = 0.0
        remain_irrad = total_power_time
        while remain_irrad > 0:
            text = create_sub_irradiation_scenario(
                irradiation_scenario, power_time_step, current_point)
            sub_irrads.append(text)
            remain_irrad -= power_time_step
            current_point += power_time_step
            operation_times.append(min(current_point, total_power_time))

        # append the cooling block to the last irradiation scenario
        cooling_block = get_cooling_block(irradiation_scenario)
        sub_irrads[-1] = f"{sub_irrads[-1]}\n{cooling_block}"
        return sub_irrads, operation_times


def generate_sub_irradiation_files(irrad_blocks, dirname):
    """
    Generate sub-irradiation scenarios and put them info directories.

    Parameters:
    -----------
    irrad_blocks: list of str
        The sub-irradiation scenarios
    dirname: str
        The folder to store each sub irrads.
    """

    for i, irr in enumerate(irrad_blocks):
        subdir = os.path.join(dirname, f"step{i}")
        os.system(f"mkdir -pv {subdir}")
        ofname = os.path.join(subdir, "irradiation_scenario")
        with open(ofname, 'w') as fo:
            fo.write(irr+'\n')


def get_fispact_files_template(n_group_size=709):
    """Get the FISPACT FILES template"""
    thisdir = os.path.dirname(os.path.abspath(__file__))
    if n_group_size in (175, 709):
        filename = os.path.join(
            thisdir, 'data', 'fispact_files', f'FILES-{n_group_size}')
    else:
        raise ValueError(
            f"{n_group_size} not currently supported for automatically FISPACT run, remove FISPACT_DATA_DIR")
    return filename


def create_fispact_files(template_file, fispact_files_dir, fispact_data_dir):
    """Copy the template FILES to fispact_files_dir and replace the fispact_data_dir"""
    filename = os.path.join(fispact_files_dir, 'FILES')
    with open(filename, 'w') as fo:
        with open(template_file, 'r') as fin:
            while True:
                line = fin.readline()
                if line == '':
                    break
                if 'FISPACT_DATA_DIR' in line:
                    line = line.replace('FISPACT_DATA_DIR', fispact_data_dir)
                    fo.write(line)
                else:
                    fo.write(line)
    return filename


def write_fispact_file(material, irradiation_scenario, neutron_flux,
                       file_prefix,
                       aim=None,
                       model_degree=360.0,
                       tab4flag=False,
                       endf_lib_flag=False,
                       fispact_materials=[],
                       fispact_materials_paths=[],
                       stable_flag=False):
    """
    Write fispact input files: including the input .i the flux .flx files

    Parameters:
    -----------
    material : Material object, required
        The material to be irradiated
    irradiation_scenario : str, required
        The filename of the irradiation scenario
    neutron_flux : numpy array, required
        The neutron flux (with total)
    file_prefix : str, required
        The prefix (including the path) of the file
    model_degree : float, optional
        The degree of the model used in MCNP, default value: 360.0. Used to
        modify the neutron flux by a factor of model_degree/360.0
    tab4flag : bool, optional
        Whether to use TAB4 keyword
    endf_lib_flag : bool, optional
        Whether to use ENDF data library
    fispact_materials : list, optional
        The list of the materials that defined by user to use another one
    fispact_materials_paths : list, optional
        The list of the materials paths that need to use
    aim : str, optional
        The AIM of the workflow
    stable_flag : bool, optional
        Whether to show stable nuclides.
    """

    # write the input file
    file_name = f"{file_prefix}.i"
    fo = open(file_name, 'w', encoding='utf-8')
    fo.write('<< ---- get nuclear data ---- >>\n')
    fo.write('NOHEADER\n')
    n_group_size = len(neutron_flux) - 1
    if n_group_size in (709,):
        endf_lib_flag = True
    # endf lib used? ---------
    if endf_lib_flag:
        fo.write('EAFVERSION 8\n')
        fo.write('COVAR\n')
    # ------------------------
    fo.write(f"GETXS 1 {len(neutron_flux) - 1}\n")
    fo.write('GETDECAY 1\n')
    fo.write('FISPACT\n')
    fo.write('* Irradiation start\n')
    fo.write('<< ---- set initial conditions ---- >>\n')
    # material part start
    if aim in ['COOLANT_ACT_PRE']:
        if any(material in sublist for sublist in fispact_materials):
            material_path = settings.get_material_path(fispact_materials,
                                                       fispact_materials_paths, material)
            fo.write(
                '<< ---- material info. defined by user in the separate file below ---- >>\n')
            fo.write(f"<< ---- {material_path} ---->>\n")
            # read the files in fispact_material_list and write it here
            fin = open(material_path)
            for line in fin:
                if line.strip().split() == []:
                    continue
                fo.write(line)
    elif any(material.id in sublist for sublist in fispact_materials):
        material_path = settings.get_material_path(fispact_materials,
                                                   fispact_materials_paths, material.id)
        fo.write(
            '<< ---- material info. defined by user in the separate file below ---- >>\n')
        fo.write(f"<< ---- {material_path} ---- >>\n")
        # read the files in fispact_materials and write it here
        fin = open(material_path)
        for line in fin:
            if line.strip().split() == []:
                continue
            line = line.strip()
            fo.write(f"{line}\n")
    else:
        fo.write('<< ---- material info. converted from MCNP output file ---- >>\n')
        fo.write(f"DENSITY {material.density:.5E}\n")
        fo.write(f'FUEL {len(material.fispact_material_nuclide)}\n')
        for i in range(len(material.fispact_material_nuclide)):  # write nuclide information
            fo.write(
                f"{material.fispact_material_nuclide[i]} {material.fispact_material_atoms_kilogram[i]:.5E}\n")
    # material part end
    fo.write('MIND 1.E6\n')
    fo.write('HAZARDS\n')
    if n_group_size in (69, 315):  # fission mode
        fo.write('USEFISSION\n')
        fo.write("FISYIELD 4 Th233 U235 U238 Pu239\n")
    fo.write('CLEAR\n')
    if tab4flag:
        fo.write('TAB4 44\n')
    fo.write('ATWO\n')
    fo.write('HALF\n')
    if not stable_flag:
        fo.write('NOSTABLE\n')
    fo.write('UNCERT 2\n')
    fo.write('TOLERANCE 0 1E4 1.0E-6\n')
    fo.write('TOLERANCE 1 1E4 1.0E-6\n')
    # irradiation scenario part
    if aim == 'COOLANT_ACT_PRE':
        fo.write(irradiation_scenario)
    else:
        with open(irradiation_scenario, 'r', encoding='utf-8') as fin:
            while True:
                line = fin.readline()
                line_ele = line.split()
                if line == '':  # end of the file
                    break
                if utils.is_blank_line(line):
                    continue
                if 'FLUX' in line:  # this is the irradiation part that defines flux
                    try:
                        real_flux = float(
                            line_ele[1]) * model_degree / 360.0 * neutron_flux[n_group_size]
                        fo.write(f"FLUX {real_flux:.5E}\n")
                    except BaseException:
                        errmsg = f"Neutron flux length inconsistency."
                        raise ValueError(errmsg)
                else:
                    fo.write(line)
        # fin.close()
    fo.write('END\n')
    fo.write('*END of RUN \n')
    fo.close()

    # write .flx file
    filename = f"{file_prefix}.flx"
    write_fispact_flux_file(filename, neutron_flux)


def write_fispact_flux_file(filename, neutron_flux):
    """
    Write the FISPACT flux file.

    Parameters:
    -----------
    filename : str
        The flux filename .flx
    neutron_flux : list or np.array
        The neutron flux
    """
    n_group_size = len(neutron_flux) - 1
    with open(filename, 'w') as fo:
        for i in range(n_group_size):  # reverse the neutron flux
            fo.write(f"{neutron_flux[n_group_size -1 -i]:.5E}\n")
        fo.write('1.0\n')
        fo.write(
            f"Neutron energy group {n_group_size} G, TOT = {neutron_flux[-1]:.5E}")


def construct_irradiation_scenario(irr_time, cooling_times, irr_total_flux):
    """
    Construct FISPACT-II format irradiation scenario.
    """
    irr_snr = '<<-----------Irradiation Scenario--------------->>\n'
    irr_snr += 'FLUX ' + utils.format_single_output(irr_total_flux) + '\n'
    irr_snr += 'TIME ' + utils.format_single_output(irr_time) + ' SECS ATOMS\n'
    irr_snr += 'ZERO\n'
    irr_snr += '<<-----------End of Irradiation --------------->>\n'
    irr_snr += '<<-----------Cooling Times--------------->>\n'
    for i, ct in enumerate(cooling_times):
        irr_snr += 'TIME ' + utils.format_single_output(ct) + ' SECS ATOMS\n'
    return irr_snr
