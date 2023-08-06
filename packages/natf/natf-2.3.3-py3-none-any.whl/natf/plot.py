#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from __future__ import print_function
import os
import numpy as np
import pandas as pd
from matplotlib.pylab import plt  # load plot library
from matplotlib import rc, rcParams
import seaborn as sns
from natf import utils
from natf import radwaste_standard as radstd

rcParams['font.weight'] = 'bold'
# set color and markers
sns.set_palette(sns.color_palette("hls", 10))
prop_cycle = plt.rcParams['axes.prop_cycle']
colors = prop_cycle.by_key()['color']
markers = ['o', 's', 'v', '^', 'P', '*', 'X', 'd', 'x', 'D', 'H']
# default savefig parameters
savefig_kwargs = {'dpi': 600, 'bbox_inches': 'tight',
                  'format': 'tiff', 'pil_kwargs': {"compression": "tiff_lzw"}}


def get_labels(items, filename=None):
    """
    Get the labesl for all the parts.
    """
    if filename is not None and items == ['All']:
        # part with multiple nuc 'All'
        df = pd.read_csv(filename)
        items = list(df.columns)[1:]
    labels = []
    for i, p in enumerate(items):
        if p.upper() == ('CP', 'COOLANT PLATE'):
            labels.append('CP')
        elif p.upper() in ['', 'PFC', 'PLASMA FACING COMPONENT']:
            labels.append('PFC')
        elif p in ['Divertor_W_layer']:
            labels.append('Divertor W layer')
        elif p == 'Divertor_structure':
            labels.append("Divertor structure using SS316")
        elif p == 'Divertor_structure_eurofer':
            labels.append("Divertor structure using Eurofer")
        elif p == 'FirstWall':
            labels.append('FW')
        elif p == 'Be_U_0':
            labels.append('Be w/o U')
        elif p.upper() in ('BLK', 'BLANKET'):
            labels.append('BLK')
        elif p.upper() in ('DIV', 'DIVERTOR'):
            labels.append('DIV')
        elif p.upper() in ('VV', 'VACUUM VESSEL'):
            labels.append('VV')
        elif p.upper() == 'PF':
            labels.append('PFC')
        elif p.upper() == 'TF':
            labels.append('TFC')
        elif p.upper() == 'CS':
            labels.append('CS')
        elif p.upper() == 'TS':
            labels.append('TS')
        elif p.upper() == 'CRYOSTAT':
            labels.append('cryostat')
        elif p.upper() == 'ALL':
            labels.append('Overall')
        else:
            labels.append(p)
    return labels


def rwc_to_label(key, level=0):
    """
    Convert key to label.
    """
    if key == 'rwc_chn2018':
        labels = ['EW', 'VLLW', 'LLW', 'ILW', 'HLW']
    if key == 'rwc_russian':
        labels = ['EW', 'LLW', 'ILW', 'HLW']
    if key in ['rwc_usnrc_fetter', 'rwc_usnrc']:
        labels = ['EW', 'LLW', 'ILW', 'HLW']
    if key == 'rwc_uk':
        labels = ['EW', 'LLW', 'ILW', 'HLW']
    return labels[level]


def rwc_to_color(level):
    """
    Define the color used in plot for Radwaste.
    """
    color_map = {0: 'green',  # EW
                 1: 'blue',  # VLLW
                 2: 'yellow',  # LLW
                 3: 'brown',  # ILW
                 4: 'red'}  # HLW
    return color_map[level]


def get_part_flux(filename, n_group_size=175, reverse=True):
    """
    Read the neutron flux (part.flx) of a part.

    Parameters:
    -----------
    reverse : bool
        True for .flx file (energy group high to low)
        False for .flux file (energy group low to high)

    Returns:
    --------
    flux : np.array
        Neutron flux from lower energy to higher energy
    """
    flux = np.zeros(n_group_size, dtype=np.float)
    with open(filename, 'r') as fin:
        count = 0
        while True:
            line = fin.readline()
            if line == '':
                break
            flux[count] = float(line.strip().split()[0])
            count += 1
            if count == n_group_size:
                break
    if reverse:
        flux = flux[::-1]
    return flux


def get_filename(part, key, work_dir=None):
    """
    Get the filename for specific part and key.
    Eg. Get the act of A -> A.act
    """
    filename = os.path.join(work_dir, part, part + '.' + key)
    return filename


def get_value(filename, nucs=None, item=None):
    """
    Get the value for specific file.
    """
    df = pd.read_csv(filename)
    if nucs == ['All']:
        nucs = list(df.columns)[1:]
    if item is not None:
        # return specific item but not all
        idx = list(df['Nuclide']).index(item)
        value = np.array(df[nucs]).flatten()[idx]
    else:
        value = df[nucs]
    return value


def get_cooling_times(filename):
    "Get the cooling time."
    df = pd.read_csv(filename)
    value = df['Cooling_time(s)']
    return value


def get_values(parts, key, item=None, nucs=None, work_dir=None):
    """
    Get the value of parts for given key.
    The key could be 'act', 'acts', 'ci', ...

    Parameters:
    nucs: list
        If nucs is ['Total'], then get total value.
        If nucs is a list of specific nuc, then them.
        if nucs is ['all'], then get all the nucs
    """
    if len(parts) > 1 and len(nucs) > 1:
        raise ValueError(
            "Multiple nucs and multiple parts mode is not supported")
    values = []
    cooling_times = []
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        value = get_value(filename, nucs=nucs, item=item)
        if item is None:
            if i == 0:
                cooling_times = get_cooling_times(filename)
        values.append(value)
    return values, cooling_times


def plot_example():
    """
    Example.
    """
    # create figure
    fig, ax = plt.subplots(figsize=(8, 6))
    # example data
    a = np.arange(1, 5)
    b = a**2
    c = a**3
    ax.plot(a, b)
    ax.plot(a, c)
    ax.legend()
    # show figure
    # save figure
    fig.savefig(fname="example.tiff", **savefig_kwargs)


def get_ylabel(key):
    """
    Set ylabel according to key.
    """
    if key in ['act']:
        return 'Total activity (Bq)'
    if key in ['act_st_t']:
        return 'Specific activity (Bq/kg)'
    if key in ['cdt']:
        return 'Contact dose rate (Sv/h)'
    if key == 'flx':
        return r'Nuetron flux (n/cm$^2\cdot$s)'


def plot_parts_flux(parts, work_dir=None, figname="example.tiff",
                    multiplier=1.0, labels=None, figsize=None, ylim=None):
    """
    Plot the fluxes of parts.
    """
    # set color palette
    sns.set_palette(sns.color_palette("hls", len(parts)))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    # label and value
    key = 'flx'
    if labels is None:
        labels = get_labels(parts)
    ylabel = get_ylabel(key='flx')
    # plots
    fig, ax = plt.subplots(figsize=figsize)
    for i, p in enumerate(parts):
        filename = get_filename(p, work_dir=work_dir, key=key)
        flux = get_part_flux(filename)
        flux = np.multiply(flux, multiplier)
        ax.step(utils.get_e_group(175, with_lowest_bin=False, reverse=False), flux,
                label=labels[i], color=colors[i], marker=None)
    ax.legend()
    # style definition
    #rc('text', usetex=True)
    rc('font', family='serif', weight='bold')
    ax.set_xscale('log')
    ax.set_yscale('log')
    if ylim is not None:
        ax.set_ylim(ylim)
    ax.set_xlabel(xlabel='Neutron energy (MeV)',
                  fontsize='x-large', fontweight='bold')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large', fontweight='bold')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='both', axis='both')
    # save file
    fig.savefig(fname=figname, **savefig_kwargs)


def plot_parts(parts, key=None, nucs=None, work_dir=None,
               figname='example.tiff', figtitle=None,
               xlabel='Time after shutdown (years)', ylabel=None, labels=None):
    """
    Plot specific act of given parts.
    """
    # set color palette
    sns.set_palette(sns.color_palette("hls", len(parts)))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    # label and value
    if labels is None:
        labels = get_labels(parts)
    if ylabel is None:
        ylabel = get_ylabel(key)
    values, cooling_times = get_values(
        parts, key=key, nucs=nucs, work_dir=work_dir)
    # convert time from sec to year.
    for i, ct in enumerate(cooling_times):
        cooling_times[i] = utils.time_sec_to_unit(ct, 'a')
    # plots parts
    fig, ax = plt.subplots()
    for i, p in enumerate(parts):
        ax.plot(cooling_times, values[i][nucs[0]], label=labels[i],
                color=colors[i], marker=markers[i])
    ax.legend()
    # style definition
    #rc('text', usetex=True)
    rc('font', family='serif', weight='bold')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large', fontweight='bold')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large', fontweight='bold')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    # save file
    fig.savefig(fname=figname, **savefig_kwargs)


def plot_wap_distribute(parts, key=None, nucs=None, work_dir=None,
                        figname='example.tiff', figtitle=None,
                        xlabel='Distance from BLK to PHTS components (m)',
                        ylabel=r'Specific Activity (Bq/kg$_{H2O}$)',
                        x_values=None):
    """
    Plot specific activity of given nuclide in PHTS.
    """
    # set color palette
    sns.set_palette(sns.color_palette("hls", len(nucs)))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    # label and value
    labels = get_labels(parts)
    # plots parts
    fig, ax = plt.subplots()
    if x_values is None:
        x_values = range(0, len(parts))
    for i, nuc in enumerate(nucs):
        values, cooling_times = get_values(
            parts, key=key, nucs=[nucs[i]], work_dir=work_dir, item='Specific act (Bq/kg)')
        ax.plot(x_values, values, label=nuc,
                color=colors[i], marker=markers[i])
    ax.legend()
    # style definition
    #rc('text', usetex=True)
    rc('font', family='serif', weight='bold')
    ax.set_xlim([20, 200])
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large', fontweight='bold')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large', fontweight='bold')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    ax.set_xticks(x_values)
    ax.set_xticklabels(parts, rotation=75)
    ax2 = ax.twiny()
    ax2.set_xlim([20, 200])
    ax2.set_xticks(x_values)
    ax2.set_xticklabels(x_values, rotation=75)
    plt.tight_layout()
    # save file
    fig.savefig(fname=figname, **savefig_kwargs)


def plot_wap_power_cmp(powers, cs, parts, key=None, nucs=None, work_dir=None,
                       figname='example.tiff', figtitle=None,
                       xlabel='Distance from BLK to PHTS components (m)',
                       ylabel=r'Specific Activity (Bq/kg$_{H2O}$)',
                       x_values=None):
    """
    Plot specific activity of given nuclide in PHTS.
    Only one nuc is allowed.
    """
    # set color palette
    sns.set_palette(sns.color_palette("hls", len(powers)))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    # label and value
    labels = get_labels(parts)
    # plots parts
    fig, ax = plt.subplots()
    if x_values is None:
        x_values = range(0, len(parts))
    for i, power in enumerate(powers):
        folder_name = os.path.join(
            work_dir, 'natf_coolant_' + cs + '_' + power)
        values, cooling_times = get_values(
            parts, key=key, nucs=nucs, work_dir=folder_name, item='Specific act (Bq/kg)')
        ax.plot(x_values, values, label=power,
                color=colors[i], marker=markers[i])
    ax.legend()
    # style definition
    #rc('text', usetex=True)
    rc('font', family='serif', weight='bold')
    ax.set_xlim([20, 200])
    ax.set_xscale('linear')
    ax.set_yscale('log')
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    ax.set_xticks(x_values)
    ax.set_xticklabels(parts, rotation=75)
    ax2 = ax.twiny()
    ax2.set_xlim([20, 200])
    ax2.set_xticks(x_values)
    ax2.set_xticklabels(x_values, rotation=75)
    plt.tight_layout()
    # save file
    fig.savefig(fname=figname, **savefig_kwargs)


def plot_nucs(parts, key, nucs, labels=None, work_dir=None,
              figname='example.tiff', figtitle=None,
              xlabel='Time after shutdown (years)', ylabel=None, yscale='log'):
    """
    Plot the different nucs or item in the same part.
    """
    filename = get_filename(part=parts[0], key=key, work_dir=work_dir)
    # label and value
    if labels is None:
        labels = get_labels(nucs, filename=filename)
    if ylabel is None:
        ylabel = get_ylabel(key)
    values, cooling_times = get_values(
        parts, key=key, nucs=nucs, work_dir=work_dir)
    # convert time from sec to year.
    for i, ct in enumerate(cooling_times):
        cooling_times[i] = utils.time_sec_to_unit(ct, 'a')
    # plots parts
    ratio_fix = 0
    if 'ratio' in key:
        ratio_fix = 1

    # set color palette
    sns.set_palette(sns.color_palette("hls", len(labels)+ratio_fix))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']
    fig, ax = plt.subplots()
    for i, item in enumerate(labels):
        ax.plot(cooling_times, values[0][item], label=labels[i],
                color=colors[i+ratio_fix], marker=markers[i+ratio_fix])
    ax.legend()
    # style definition
    #rc('text', usetex=True)
    rc('font', family='serif', weight='bold')
    ax.set_xscale('log')
    ax.set_yscale(yscale)
    ax.set_xlabel(xlabel=xlabel, fontsize='x-large', fontweight='bold')
    ax.set_ylabel(ylabel=ylabel, fontsize='x-large', fontweight='bold')
    ax.tick_params(axis='both', tick1On=True, tick2On=True)
    ax.grid(which='major', axis='both')
    # save file
    fig.savefig(fname=figname, **savefig_kwargs)
    plt.close()


def get_part_mass(part, work_dir=None):
    """
    Get part mass from part name.
    """
    key = 'basicinfo'
    filename = get_filename(part, key, work_dir=work_dir)
    df = pd.read_csv(filename)
    mass_info = np.array(df.loc[df[part] == 'mass(g)']).flatten()
    return float(mass_info[1])


def get_part_vol(part, work_dir=None):
    """
    Get part volume from part name.
    """
    key = 'basicinfo'
    filename = get_filename(part, key, work_dir=work_dir)
    df = pd.read_csv(filename)
    vol_info = np.array(df.loc[df[part] == 'volume(cm3)']).flatten()
    return float(vol_info[1])


def write_part_basicinfo(parts, work_dir=None, ofname='cfetr_parts_vol_mass.csv'):
    """
    Write part basic information as a csv table.
    """
    vols = [0.0]*len(parts)
    masses = [0.0]*len(parts)
    for i, p in enumerate(parts):
        vols[i] = get_part_vol(p, work_dir=work_dir)
        masses[i] = get_part_mass(p, work_dir=work_dir)
    # save the ctrs into csv
    fo = open(ofname, 'w')
    title_line = utils.data_to_line_1d(
        key='Components', value=['Volumes (m3)', 'Masses (ton)'])
    fo.write(title_line)
    for i, p in enumerate(parts):
        line = utils.data_to_line_1d(
            key=p, value=[vols[i]/1e6, masses[i]/1e6], decimals=1)
        fo.write(line)
    fo.close()


def calc_rwcs_masses(parts, key, cooling_time_str=None, cooling_time=None, work_dir=None):
    """
    Calculate the mass of HLW, ILW and LLW.
    """
    rwc2int = radstd.rwc2int
    masses = np.array([0.0]*5)
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        rwc = get_rwc(filename, cooling_time_str=cooling_time_str,
                      cooling_time=cooling_time)
        masses[rwc2int[rwc]-1] += get_part_mass(p, work_dir=work_dir)
    return masses


def calc_rwcs_vols(parts, key, cooling_time_str=None, cooling_time=None, work_dir=None):
    """
    Calculate the mass of HLW, ILW and LLW.
    """
    rwc2int = radstd.rwc2int
    vols = np.array([0.0]*5)
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        rwc = get_rwc(filename, cooling_time_str=cooling_time_str,
                      cooling_time=cooling_time)
        vols[rwc2int[rwc]-1] += get_part_vol(p, work_dir=work_dir)
    return vols


def calc_recycle_masses(parts, cooling_time_str=None, cooling_time=None, work_dir=None):
    """
    Calculate the mass of recycling using CRH and ARH.
    """
    recycle_dict = {'CRH': 0, 'ARH': 1}
    masses = np.array([0.0, 0.0])
    for i, p in enumerate(parts):
        filename = get_filename(p, key='cdt', work_dir=work_dir)
        cd = get_cd(filename, cooling_time_str=cooling_time_str,
                    cooling_time=cooling_time)
        if cd <= 1e-2:
            masses[0] += get_part_mass(p, work_dir=work_dir)
            masses[1] += get_part_mass(p, work_dir=work_dir)
        if cd > 1e-2 and cd <= 1e4:
            masses[1] += get_part_mass(p, work_dir=work_dir)
    return masses


def calc_recycle_vols(parts, cooling_time_str=None, cooling_time=None, work_dir=None):
    """
    Calculate the volumes of recycling using CRH and ARH.
    """
    recycle_dict = {'CRH': 0, 'ARH': 1}
    vols = np.array([0.0, 0.0])
    for i, p in enumerate(parts):
        filename = get_filename(p, key='cdt', work_dir=work_dir)
        cd = get_cd(filename, cooling_time_str=cooling_time_str,
                    cooling_time=cooling_time)
        if cd <= 1e-2:
            vols[0] += get_part_vol(p, work_dir=work_dir)
            vols[1] += get_part_vol(p, work_dir=work_dir)
        if cd > 1e-2 and cd <= 1e4:
            vols[1] += get_part_vol(p, work_dir=work_dir)
    return vols


def plot_rwcs_time_evo(parts, key='rwc_chn2018', work_dir=None,
                       ofname='rwc_time_evo_mass.tiff', labels=None):
    """
    Plot the time dependent radwaste masses.
    """
    rc('font', family='serif', weight='bold')
    # get the cooling times
    filename = get_filename(parts[0], key, work_dir)
    cooling_times = get_cooling_times(filename)
    #
    fig, ax = plt.subplots()
    ax.set_xlabel('Cooling time (years)',
                  fontsize='x-large', fontweight='bold')
    ax.set_ylabel(r'Mass ($\times 10^{3}$ kg)',
                  fontsize='x-large', fontweight='bold')
    # get the mass
    masses = np.zeros(shape=(len(cooling_times), 5), dtype=float)
    for i, ct in enumerate(cooling_times):
        masses[i] = calc_rwcs_masses(
            parts, key, cooling_time=ct, work_dir=work_dir)
    # convert unit from s to a
    for i in range(len(cooling_times)):
        cooling_times[i] = cooling_times[i]/(365.25*24*3600)
    rwcis = []
    if key == 'rwc_chn2018':
        rwcis = [0, 1, 2, 3]  # EW, VLLW, LLW, ILW
    else:
        rwcis = [1, 2]  # LLW, ILW

    # set color palette
    sns.set_palette(sns.color_palette("hls", len(rwcis)))
    prop_cycle = plt.rcParams['axes.prop_cycle']

    # choose proper plot region
    plot_start_idx = 0
    plot_end_idx = len(cooling_times)
    if cooling_times[len(cooling_times)-1] < 100:
        plot_start_idx = 0
    else:
        for i, item in enumerate(cooling_times):
            if item > 0.1:  # start from 1 month
                plot_start_idx = i
                break

    for i, rwci in enumerate(rwcis):
        # do not plot constant zero 0.0
        if max(masses[:, rwci][plot_start_idx:plot_end_idx]) == 0.0:
            continue
        sns.lineplot(x=cooling_times[plot_start_idx:plot_end_idx],
                     y=np.divide(masses[:, rwci]
                                 [plot_start_idx:plot_end_idx], 1e6),
                     label=rwc_to_label(key, level=rwci),
                     color=rwc_to_color(rwci),
                     marker=markers[i])
    ax.legend(loc='best')
    ax.set_xscale('log')
    fig.tight_layout()
    fig.savefig(fname=ofname, **savefig_kwargs)
    plt.close()


def plot_rwcs_compare(parts, keys=['rwc_chn2018', 'rwc_usnrc', 'rwc_usnrc_fetter', 'rwc_uk'],
                      cooling_time_str='1 s', work_dir=None,
                      ofname='rwc_compare_1s.tiff', labels=None):
    """
    Plot the compare result of different radwaste standards.

    Parameters:
    -----------
    parts: list
        List of part names.
    keys: list
        List of keys. Eg. ['rwc_chn2018', 'rwc_usnrc']
    cooling_time: string
        The cooling time to plot.
    work_dir: string
        The working directory.
    ofname: string
        Output figure name.
    """
    rc('font', family='serif', weight='bold')
    rwcs_masses = np.zeros(shape=(len(keys), 5), dtype=float)
    for i, key in enumerate(keys):
        # get mass of Clearance, VLLW, LLW, ILW and HLW
        rwcs_masses[i][:] = calc_rwcs_masses(
            parts, key, cooling_time_str, work_dir=work_dir)
    # convert to unit t
    rwcs_masses = np.divide(rwcs_masses, 1.0e6)

    # determin plot classes and xtick_labels
    # do not plot if it is all zero for EW, ILW
    xtick_labels = ['EW', 'VLLW', 'LLW', 'ILW']
    start_idx = 0
    end_idx = 4
    # check start idx
    max_ew = 0.0
    for i in range(len(keys)):
        max_ew = max(max_ew, rwcs_masses[i][0])
    if max_ew == 0.0:
        xtick_labels.remove('EW')
        start_idx = 1
        max_vllw = 0.0
        for i in range(len(keys)):
            max_vllw = max(max_vllw, rwcs_masses[i][1])
        if max_vllw == 0.0:
            xtick_labels.remove('VLLW')
            start_idx = 2

    max_ilw = 0.0
    for i in range(len(keys)):
        max_ilw = max(max_ilw, rwcs_masses[i][3])
    if max_ilw == 0:
        xtick_labels.remove('ILW')
        end_idx = 3
        max_llw = 0.0
        for i in range(len(keys)):
            max_llw = max(max_llw, rwcs_masses[i][2])
        if max_llw == 0.0:
            xtick_labels.remove('LLW')
            end_idx == 2

    if len(xtick_labels) < 1:
        raise ValueError(f"no valid rwcs_masses")

    # plot
    x = np.arange(len(xtick_labels)) * 2
    width = 0.35
    fig, ax = plt.subplots()
    if labels is None:
        labels = ['China', 'USNRC', 'USNRC_FETTER', 'UK']

    # set color palette
    sns.set_palette(sns.color_palette("hls", len(labels)))
    prop_cycle = plt.rcParams['axes.prop_cycle']
    colors = prop_cycle.by_key()['color']

    rects0 = ax.bar(x - 1.5 * width, rwcs_masses[:][0][start_idx:end_idx], width,
                    label=labels[0], color=colors[0], hatch='//')  # CHN2018
    rects1 = ax.bar(
        x - 0.5 * width, rwcs_masses[:][1][start_idx:end_idx], width, label=labels[1], color=colors[1], hatch='--')
    rects2 = ax.bar(
        x + 0.5 * width, rwcs_masses[:][2][start_idx:end_idx], width, label=labels[2], color=colors[2], hatch='xx')
    rects3 = ax.bar(
        x + 1.5 * width, rwcs_masses[:][3][start_idx:end_idx], width, label=labels[3], color=colors[3], hatch='++')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel(r'Mass (tonnes)', fontsize='x-large', fontweight='bold')
    ax.set_xlabel('Radioactive class', fontsize='x-large', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(xtick_labels)
    ax.legend(loc='best')

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(round(height, 1)),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom', size=5)

    autolabel(rects0)
    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)
    fig.tight_layout()
    fig.savefig(fname=ofname, **savefig_kwargs)


def calc_recycle_cooling_requirement(parts, key='cdt', rh='CRH', work_dir=None, out_unit='a', ofname=None):
    """
    Calculate the cooling time requirement for CRH (conservative remote handling,
    0.01 Sv/h) and ARH (advanced remote handling, 10000 Sv/h).
    """
    ctrs = []
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir)
        cooling_times = get_cooling_times(filename)
        cds = list(get_value(filename, nucs='total_contact_dose(Sv/hr)'))
        cds = list([float(item) for item in cds])
        ctr = utils.calc_recycle_ctr(cooling_times, cds, rh=rh, out_unit='a')
        ctrs.append(ctr)
    return ctrs


def calc_rwc_cooling_requirement(parts, key, classes, standard='CHN2018',
                                 work_dir=None, out_unit='a', ofname=None):
    """
    Calculate the cooling time requirement for specific classes.
    """
    ctrs = []
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir)
        cooling_times = get_cooling_times(filename)
        rwcs = list(get_value(filename, nucs='Radwaste_Class'))
        ctr = utils.calc_ctr(cooling_times, rwcs, classes,
                             out_unit=out_unit, standard=standard)
        ctrs.append(ctr)
    # save the ctrs into csv
    if ofname is not None:
        fo = open(ofname, 'w')
        title_line = utils.data_to_line_1d(key='Components', value=list(
            c + ' (' + out_unit+')' for c in classes))
        fo.write(title_line)
        for i, p in enumerate(parts):
            line = utils.data_to_line_1d(key=p, value=ctrs[i])
            fo.write(line)
        fo.close()
    return ctrs


def cooling_time_str_to_float(cooling_time_str):
    tokens = cooling_time_str.strip().split()
    value = tokens[0]
    unit = tokens[1]
    ct = utils.time_to_sec(value, unit)
    return ct


def get_rwc(filename, cooling_time_str=None, cooling_time=None):
    """
    Get the rwc from specific filename and cooling time.

    Parameters:
    -----------
    cooling_time_str: str
        cooling time in string format, eg. '1 s'
    cooling_time: float
        cooling time in unit [s].
    """
    if cooling_time_str is not None and cooling_time is not None:
        raise ValueError("only one cooling time input is supported")
    if cooling_time_str is not None:
        ct = cooling_time_str_to_float(cooling_time_str)
    if cooling_time is not None:
        ct = cooling_time
    df = pd.read_csv(filename)
    cooling_times = np.array(df['Cooling_time(s)']).flatten()
    index = utils.get_ct_index(ct, cooling_times)
    rwc = np.array(df['Radwaste_Class']).flatten()[index]
    return rwc


def get_cd(filename, cooling_time_str=None, cooling_time=None):
    """
    Get the contact dose from specific filename and cooling time.

    Parameters:
    -----------
    cooling_time_str: str
        cooling time in string format, eg. '1 s'
    cooling_time: float
        cooling time in unit [s].
    """
    if cooling_time_str is not None and cooling_time is not None:
        raise ValueError("only one cooling time input is supported")
    if cooling_time_str is not None:
        ct = cooling_time_str_to_float(cooling_time_str)
    if cooling_time is not None:
        ct = cooling_time
    df = pd.read_csv(filename)
    cooling_times = np.array(df['Cooling_time(s)']).flatten()
    index = utils.get_ct_index(ct, cooling_times)
    cd = float(np.array(df['total_contact_dose(Sv/hr)']).flatten()[index])
    return cd


def get_rwcs_by_cooling_times(parts, cooling_times_str=['1 s', '1 a', '10 a', '100 a'],
                              cooling_times=[], key='rwc_chn2018', work_dir=None, ofname='cfetr_all_rwc_chn2018.csv'):
    """
    Get the radwaste classification of different cooling times.

    Parameters:
    -----------
    parts: list of string
        List of part names.
    cooling_times_str: list of string
        List of cooling times.
    cooling_times: list of float
    key: string
        Standard name. Supported standards: 'rwc_chn2018', 'usnrc', 'usnrc_fetter', 'uk'
    work_dir: string
        Working directory.
    ofname: string
        Output csv file name.
    """

    if len(cooling_times) == 0:
        cooling_times = [0.0] * len(cooling_times_str)
        # convert cooling_times from string to float
        for i, ct in enumerate(cooling_times_str):
            cooling_times[i] = cooling_time_str_to_float(ct)

    rwcs = np.array([['']*len(cooling_times)]*len(parts), dtype='<U16')
    for i, p in enumerate(parts):
        filename = get_filename(p, key, work_dir=work_dir)
        df = pd.read_csv(filename)
        cts = np.array(df['Cooling_time(s)']).flatten()
        for j, ct in enumerate(cooling_times):
            rwc = get_rwc(filename, cooling_time=ct)
            rwcs[i][j] = rwc

    if ofname is not None:
        # save the rwcs into csv
        fo = open(ofname, 'w')
        title_line = utils.data_to_line_1d(
            key='Components', value=cooling_times_str)
        fo.write(title_line)
        for i, p in enumerate(parts):
            line = utils.data_to_line_1d(key=p, value=rwcs[i])
            fo.write(line)
        fo.close()
    return rwcs
