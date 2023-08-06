#!/usr/bin/env python3
# -*- coding:utf-8 -*- import numpy as np import re
import argparse
import collections
import re
from natf import utils
from natf import cell
from natf import surface
import math

# patterns
cont_pattern = re.compile("^      ")
comp_pattern = re.compile("^C *Component", re.IGNORECASE)
cell_range_pattern = re.compile("^C *Cell Range", re.IGNORECASE)
group_name_pattern = re.compile("^C *Group", re.IGNORECASE)
from_to_pattern = re.compile("^C.*From.*to", re.IGNORECASE)
new_comp_name_pattern = re.compile("^newcomp", re.IGNORECASE)
new_group_name_pattern = re.compile("^newgroup", re.IGNORECASE)
mat_title_pattern = re.compile("^M[1-9]", re.IGNORECASE)
# default values
MCNP_LINE_MAX_LENGTH = 80
MCNP_INDENT = 6


def is_cell_title(line):
    """Check whether this line is the first line of a cell card"""
    line_ele = line.split()
    if len(line_ele) == 0:  # blank line
        return False
    # not surf title
    try:
        int(line_ele[1])
    except:
        return False
    # continue line
    if str(line_ele[0]).isdigit() and (not re.match(cont_pattern, line)):
        return True
    return False


def is_surf_title(line):
    """Check whether this line is the first line of a surf card"""
    line_ele = line.split()
    if len(line_ele) < 3:  # surf title has cid, mnemonics, data at least 3 parameters
        return False
    if line_ele[1].upper() in surface.mnemonics:
        return True
    else:
        return False


def is_mat_title(line):
    """Check whether this line is the first line of a material card"""
    if re.match(mat_title_pattern, line):
        return True
    else:
        return False


def is_fn_tally_title(line):
    """
    Check whether this line is the title of Fn tally card.
    """
    fn_pattern = re.compile("^F[1-9]", re.IGNORECASE)
    if re.match(fn_pattern, line):
        return True
    else:
        return False


def is_fmeshn_tally_title(line):
    """
    Check whether this line is the title of FMESHn tally card.
    """
    fmeshn_pattern = re.compile("^FMESH[1-9]", re.IGNORECASE)
    if re.match(fmeshn_pattern, line):
        return True
    else:
        return False


def is_tally_title(line):
    """
    Check whether this line is the title of tally card
    """
    if is_fn_tally_title(line) or is_fmeshn_tally_title(line):
        return True
    else:
        return False


def get_cell_cid_mid_den(line):
    """Get the cell id, mid and density information"""
    line_ele = line.split()
    cid = int(line_ele[0])
    mid = int(line_ele[1])
    den = None
    if mid > 0:
        if '(' in line_ele[2]:
            tokens = line_ele[2].split('(')
            den = float(tokens[0])
        else:
            den = float(line_ele[2])
    elif mid == 0:
        pass
    else:
        raise ValueError(f"Wrong cell title line: {line}")
    return cid, mid, den


def cell_title_change_mat(cell_title, mid_new=0, den_new=0.0, atom_den_new=0.0):
    """Change the material in cell title"""
    line_ele = cell_title.split()
    cid = int(line_ele[0])
    mid = int(line_ele[1])
    rest = []
    if mid > 0:
        if '(' in line_ele[2]:
            tokens = line_ele[2].split('(')
            rest.append('('+tokens[1])
            rest.extend(line_ele[3:])
        else:
            rest.extend(line_ele[3:])
    elif mid == 0:
        rest.extend(line_ele[2:])
    else:
        raise ValueError(f"Wrong cell title line: {cell_title}")

    if mid_new == 0:
        return f"{cid} 0 {' '.join(rest)}"
    if mid_new > 0:
        if den_new > 0:
            return f"{cid} {mid_new} {-den_new} {' '.join(rest)}"
        elif atom_den_new > 0:
            return f"{cid} {mid_new} {atom_den_new} {' '.join(rest)}"
        else:
            raise ValueError(
                f"Wrong den_new:{den_new} and atom_den_new:{atom_den_new}")
    raise ValueError(f"Wrong mid_new:{mid_new}")


def has_comp_name(line):
    """Check whether this line contains component name"""
    if not utils.is_comment(line):
        return False
    if re.match(comp_pattern, line):
        return True
    else:
        return False


def get_comp_name(line, new_comp_count=0):
    """Get the component name"""
    line_ele = line.split()
    if line_ele[-1].lower() == "component:":
        return f"newcomp{new_comp_count+1}"
    else:
        return line_ele[-1]


def has_cell_range(line):
    """Check whether this line contains cell range info"""
    if not utils.is_comment(line):
        return False
    if re.match(cell_range_pattern, line):
        return True
    else:
        return False


def get_cell_range(line):
    """Get the cell range"""
    line_ele = line.split()
    cids = [range(int(line_ele[-3]), int(line_ele[-1]) + 1)]
    return cids


def has_group_name(line):
    """Check whether this line contains group name"""
    if re.match(group_name_pattern, line):
        return True
    else:
        return False


def get_group_name(line, new_group_count=0):
    line_ele = line.split()
    if line_ele[-1].lower() == "group:":
        return f"newcomp{new_group_count+1}"
    else:
        return line_ele[-1]


def has_from_to(line):
    if re.match(from_to_pattern, line):
        return True
    else:
        return False


def get_nonvoid_cells(inp="input"):
    """
    Read the MCNP input file generated by cosVMPT and output a list of all
    non-void cells"
    """
    nonvoid_cells = []
    with open(inp, 'r') as fin:
        cell_card_end = False
        while not cell_card_end:
            line = fin.readline()
            if utils.is_blank_line(line):  # end of cell card
                cell_card_end = True
                break
            if is_cell_title(line):
                line_ele = line.split()
                mid = int(line_ele[1])
                if mid > 0:
                    nonvoid_cells.append(int(line_ele[0]))
    return nonvoid_cells


def mcnp_tally_style(cids, tally_num=4, particle='n', sds=None, e_group_size=None,
                     output="tally_card.txt"):
    """
    Convert the cell number list to a mcnp style tally description.

    Parameters:
    -----------
    cids : list of int
        List of cell ids
    tally_num : int
        The tally number
    particle : str
        Particle type, 'n' or 'p'
    sds : list of floats
        The SD values
    e_group_size : int
        The energy group size, eg. 69/175/315/709/1102
    output : str
        The file name to write.
    """

    tally_card = f'C tallied cell numbers: {len(cids)}'
    if e_group_size:
        e_groups = utils.get_e_group(e_group_size, reverse=False)
        tally_card = f"{tally_card}\nC The cut:{particle} should smaller than {utils.format_single_output(e_groups[0])}"
    tally_card = f'{tally_card}\nFC{tally_num} tally card generated via natf:mcnp_tally_style'
    tally_card = f'{tally_card}\nF{tally_num}:{particle} '
    sub_cids = utils.consecutive_split(cids)
    for sc in sub_cids:
        if len(sc) > 3:
            tally_card = mcnp_style_str_append(
                tally_card, f"{sc[0]} {len(sc)-2}i {sc[-1]}")
        else:
            for i, cid in enumerate(sc):
                tally_card = mcnp_style_str_append(tally_card, str(cid))
    # SD card
    if sds is not None:
        tally_card = f"{tally_card}\nSD{tally_num}  "
        for i, sd in enumerate(sds):
            tally_card = mcnp_style_str_append(
                tally_card, utils.format_single_output(sd))
    # energy group
    if e_group_size:
        tally_card = f"{tally_card}\nE{tally_num}   "
        for i, e in enumerate(e_groups[1:]):
            tally_card = mcnp_style_str_append(
                tally_card, utils.format_single_output(e))
    with open(output, 'w') as fo:
        fo.write(tally_card+'\n')


def cell_vol_err_reader(inp="input"):
    """Read the cell-vol-err info file"""
    cids, vols, errs = [], [], []
    # Opening file and read data
    fin = open(inp, 'r')
    for line in fin:
        if utils.is_blank_line(line):
            break
        line_ele = line.split()
        cids.append(int(line_ele[0]))
        vols.append(float(line_ele[1]))
        errs.append(float(line_ele[2]))
    fin.close()
    return cids, vols, errs


def cell_vol_to_tally(inp="input", output="tally_card.txt", e_group_size=175):
    """
    Write the cell, vol, err info to tally card.
    """
    cell_vol_to_tally_help = ('This script read a cell-vol-err info file and\n'
                              'return a tally style string.\n')

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False,
                        help="cell-vol-err in file path")
    parser.add_argument("-o", "--output", required=False,
                        help="save the tally_card to output file")
    parser.add_argument("-g", "--group", required=False,
                        help="the energy group size to tally. 69/175/315/709/1102 are supported")
    args = vars(parser.parse_args())

    input_file = "input"
    if args['input'] is not None:
        input_file = args['input']
    cids, vols, errs = cell_vol_err_reader(input_file)
    # save data into a tally style card
    output = "tally_card.txt"
    if args['output'] is not None:
        output = args['output']
    # e_group_size
    e_group_size = 175
    if args['group'] is not None:
        e_group_size = int(args['group'])
    mcnp_tally_style(cids, sds=vols, output=output, e_group_size=e_group_size)


def nonvoid_cells_to_tally():
    nonvoid_cells_help = ('This script read a mcnp input file and return a tally style\n'
                          'string of all non-void cells.\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False,
                        help="mcnp input file path")
    parser.add_argument("-o", "--output", required=False,
                        help="save the string to output file")
    args = vars(parser.parse_args())

    input_file = "input"
    if args['input'] is not None:
        input_file = args['input']
    nonvoid_cells = get_nonvoid_cells(input_file)

    output = "output.txt"
    if args['output'] is not None:
        output = args['output']
    mcnp_tally_style(nonvoid_cells, output=output)


def get_part_cell_list(inp):
    """Read the components and groups input file generated by cosVMPT."""
    parts = collections.OrderedDict()
    # comps = collections.OrderedDict()  # {'name':[{group1:cids}, {group2:cids}, ...]}
    # group = collections.OrderedDict() # {'name':[cids]}
    current_comp, current_group, current_cell = None, None, None
    new_comp_count, new_group_count = 0, 0

    # read the file
    with open(inp, 'r') as fin:
        cell_card_end = False
        while not cell_card_end:
            line = fin.readline()
            if utils.is_blank_line(line):  # end of cell card
                cell_card_end = True
                break
            if has_comp_name(line):
                current_comp = get_comp_name(
                    line, new_comp_count=new_comp_count)
                if re.match(new_comp_name_pattern, current_comp):
                    new_comp_count += 1
                #comps[current_comp] = []
                parts[current_comp] = []
                continue
            if has_group_name(line):
                current_group = get_group_name(line, new_group_count)
                if re.match(new_group_name_pattern, current_group):
                    new_group_count += 1
                #group[current_group] = []
                current_part = f"{current_comp}-{current_group}"
                parts[current_part] = []
                #comps[current_comp][current_group] = []
                continue
            if is_cell_title(line):
                line_ele = line.split()
                mid = int(line_ele[1])
                if mid > 0:  # nonvoid cell
                    #    comps[current_comp].append(int(line_ele[0]))
                    parts[current_comp].append(int(line_ele[0]))
                    parts[current_part].append(int(line_ele[0]))
    return parts


def format_cell_list(name, cids):
    """Format the cell list to part_cell_list style"""
    cnt = name
    for i, cid in enumerate(cids):
        cnt = mcnp_style_str_append(cnt, str(cid))
    return cnt


def save_part_cell_list(parts, output):
    """Write the components and groups cells in format of part_cell_list"""
    cnt = f"# Be careful about the content, do not enter any characters except ASCII."
    cnt = f"{cnt}\n# Syntax of defing parts: part_name cell_list"
    cnt = f"{cnt}\n# Refer to 'NATF manual` for more details about defining parts."
    cnt = f"{cnt}\n# Generated by natf:part_cell_list"
    for key, value in parts.items():
        if len(value) > 0:  # void, do not print
            cnt = f"{cnt}\n{format_cell_list(key, value)}"
    with open(output, 'w') as fo:
        fo.write(cnt)


def part_cell_list(inp="input", output="part_cell_list.txt"):
    """
    Read the components and groups input file generated by cosVMPT, and
    write a part_cell_list file for NATF.
    """
    list_comp_group_help = ('This script read a mcnp input file and return a\n'
                            'part_cell_list file.\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=False,
                        help="mcnp input file path, default: input")
    parser.add_argument("-o", "--output", required=False,
                        help="name of the part_cell_list file, default: part_cell_list.txt")
    args = vars(parser.parse_args())

    # read the file
    if args['input'] is not None:
        inp = args['input']
    parts = get_part_cell_list(inp)

    # save the content
    if args['output'] is not None:
        output = args['output']
    save_part_cell_list(parts, output=output)


def update_mcnp_input_materials(filename, cells, ofname, dict_cid_idx=None):
    """
    Update the materials of the mcnp input file.
    """
    fo = open(ofname, 'w')
    mat_written = False
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if is_cell_title(line):
                # get the cell id
                cid, mid, den = get_cell_cid_mid_den(line)
                # whether in cells
                if cell.is_item_cell(cid, cells):
                    #                    cidx = cell.get_cell_index(cid, cells)
                    cidx = utils.find_index_by_property(cid, cells, 'id')
                    # get info of new material
                    mid_new = cells[cidx].mid
                    # replace with new material
                    new_line = cell_title_change_mat(
                        line, mid_new, atom_den_new=cells[cidx].mat.atom_density)
                    fo.write(new_line+"\n")
                    continue
            if is_mat_title(line) and not mat_written:
                # write all new materials before previous materials
                for c in cells:
                    fo.write(c.mat.__str__()+"\n")
                mat_written = True
                # write the original materials and the rest contents
                fo.write(line)
                while True:
                    line = fin.readline()
                    if line == '':
                        return
                    fo.write(line)
            # other lines
            fo.write(line)


def get_tally_id(line):
    """
    Get the tally number (int) from tally title.
    """
    tokens = line.strip().split()
    item = tokens[0].split(":")[0]
    if is_fn_tally_title(line):
        tid = item[1:]
    else:
        tid = item[5:]
    return int(tid)


def get_tally_numbers(filename):
    """
    Get all the used tally numbers.
    """
    tally_nums = []
    with open(filename, 'r') as fin:
        while True:
            line = fin.readline()
            if line == '':
                break
            if is_tally_title(line):
                # get the cell id
                tid = get_tally_id(line)
                tally_nums.append(tid)
    return tally_nums


def calc_next_tid(tid, postfix=4):
    """
    Calculate the next available tally id for different type.
    """
    last_digit = tid % 10
    if last_digit < postfix:
        tid = (tid//10) * 10 + postfix
    else:
        tid = (tid//10 + 1) * 10 + postfix
    return tid


def compose_fn_tally_single(tid, cid, mid=None, particle='N', sd=1.0, mt=None):
    """
    Compose a tally string. 
    """
    s = f"F{tid}:{particle} {cid}"
    if mid is not None and mt is not None:
        s = f"{s}\nFM{tid} -1 {mid} {mt}"
    s = f"{s}\nSD{tid} {sd}\n"
    #s = f"{s}\nFQ{tid} f e\n"
    return s


def update_mcnp_input_tallies(filename, cells, tid_start=10000, write_file=True):
    """
    Update the tallies of the mcnp input file.
    The TBR for cells will be added to tallies.
    """
    current_tid = tid_start
    new_tallies = []
    fo = open(filename, 'a')
    for i, cell in enumerate(cells):
        current_tid = calc_next_tid(current_tid)
        new_tallies.append(current_tid)
        tally_string = compose_fn_tally_single(
            tid=current_tid, cid=cell.id, mid=cell.mid, mt=205)
        if write_file:
            fo.write(tally_string)
    fo.close()
    return new_tallies


def mcnp_style_str_append(s, value, indent=MCNP_INDENT, max_len=MCNP_LINE_MAX_LENGTH):
    """append lines as mcnp style, line length <= max_len"""
    indent_str = ' '*indent
    s_tmp = ''.join([s, ' ', utils.format_single_output(value, decimals=None)])
    if len(s_tmp.split('\n')[-1]) >= max_len:
        s_tmp = ''.join([s, '\n', indent_str,
                        utils.format_single_output(value, decimals=None)])
    s = s_tmp
    return s


def proper_comment(s):
    # a blank between '$' and the following letter, and make it lower
    if '$' in s:
        cnt = s.split('$')[0]
        comment = s.split('$')[-1]
        s = f"{cnt.lower()}$ {comment.lstrip()}"
    else:
        s = s.lower()
    return s


def proper_blank(s):
    # remove extra blank space
    if '  ' in s:
        tokens = s.split()
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = f"{cnt} {tokens[i]}"
        s = cnt
        return s
    else:
        return s


def proper_geom_union(s):
    # remove space between ':' and '('
    if ': ' in s:
        tokens = s.split(': ')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = f"{cnt}:{tokens[i]}"
        s = cnt

    # add a space between '(' and ':'
    if '):' in s:
        tokens = s.split('):')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = f"{cnt}) :{tokens[i]}"
        s = cnt
    return s


def proper_geom_subtract(s):
   # remove space between '#' and '('
    if '# ' in s:
        tokens = s.split('# ')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = f"{cnt}#{tokens[i]}"
        s = cnt
    # add a space between ')' and '#'
    if ')#' in s:
        tokens = s.split(')#')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = f"{cnt}) #{tokens[i]}"
        s = cnt
    return s


def proper_cell_title_line(s):
    """
    Proper the cell title line. Add a space between '(' and mat density
    """
    # add a space between '(' and mat density
    if '(' in s:
        cid, mid, den = get_cell_cid_mid_den(s)
        tokens = s.split()
        if mid > 0 and '(' in tokens[2]:
            idx = tokens[2].index('(')
            tokens[2] = f"{tokens[2][0:idx]} {tokens[2][idx:]}"
        s = ' '.join(tokens)

    s = proper_comment(s)
    s = proper_blank(s)
    s = proper_geom_union(s)
    s = proper_geom_subtract(s)
    return s


def mcnp_style_line(s, indent=MCNP_INDENT, max_len=MCNP_LINE_MAX_LENGTH):
    """
    Convert a string into mcnp style line:
        - The length of a line is less then max_len
        - specified indent for continue line default indent: 6
        - split a '$' if it is the comment cause the long line
        - keep () in the same line as possible
        - split at ':', '#' if there is
    """
    indent_str = ' '*indent
    s = proper_comment(s)
    s = proper_blank(s)
    s = proper_geom_union(s)
    s = proper_geom_subtract(s)

    # return if the original line less than 80 col
    if len(s) < max_len:
        return s

    # when the line >= 80 col
    if ':' in s:
        tokens = s.split(':')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{mcnp_style_line(tokens[i].lstrip())}"
            if i > 0:
                if 'imp' in tokens[i-1]:
                    sub_tokens = tokens[i].split()
                    tmp_cnt = f"{cnt}:{sub_tokens[0]}"
                    if len(tmp_cnt.split('\n')[-1]) >= max_len:
                        # break it at last blank
                        last_blank = tmp_cnt[::-1].find(' ')
                        cnt = f"{tmp_cnt[:-last_blank-1]}\n{indent_str}{tmp_cnt[-last_blank:]}"
                    else:
                        cnt = f"{cnt}:{sub_tokens[0]}"
                    for item in sub_tokens[1:]:
                        cnt = mcnp_style_str_append(cnt, item)
                else:
                    cnt = f"{cnt.rstrip()}\n{indent_str}:{mcnp_style_line(tokens[i].lstrip(), max_len=80-indent)}"
        s = cnt
    if '#' in s:
        tokens = s.split('#')
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{mcnp_style_line(tokens[i].lstrip())}"
            if i > 0:
                cnt = f"{cnt.rstrip()}\n{indent_str}#{mcnp_style_line(tokens[i].lstrip(), max_len=80-indent)}"
        s = cnt
    if '$' in s:
        cnt = s.split('$')[0].rstrip()
        comment = s.split('$')[-1].lstrip()
        if len(cnt.split('\n')[-1]) + len(comment) < max_len-2:
            s = f"{cnt} $ {comment}"
        else:
            s = f"{mcnp_style_line(cnt)}\n{indent_str}$ {comment}"
    if '$' not in s and ':' not in s and '#' not in s:
        tokens = s.split()
        cnt = ''
        for i in range(len(tokens)):
            if i == 0:
                cnt = f"{tokens[i]}"
            else:
                cnt = mcnp_style_str_append(cnt, tokens[i])
        s = cnt
    return s


def get_surf_str_slice_end_from_line(line):
    """
    Get the index of the last block of a cell line.
    """
    # find the end index
    line_ele = line.strip().split()
    end = len(line_ele)
    keywords = ('$', 'IMP', 'U', 'FILL')
    for kw in keywords:
        if kw in line.upper():
            for i in range(len(line_ele)):
                if kw in line_ele[i].upper():
                    end = min(end, i)
                    break
    return end


def get_surf_str_from_cell_title_line(line):
    """
    Get the surface part from the cell title line.

    Parameters:
    -----------
    line : string
        The cell title line.

    Returns:
    --------
    surf_str : string
        The surface string part
    """
    line = proper_cell_title_line(line)
    line_ele = line.strip().split()
    # find the start index
    if line_ele[1] == '0':  # void material
        start = 2
    else:
        start = 3
    end = get_surf_str_slice_end_from_line(line)
    surf_str = ' '.join(line_ele[start:end])
    return surf_str


def get_surf_str_from_cell_cont_line(line):
    """
    Get the surface part from the cell continue line.

    Parameters:
    -----------
    line : string
        The cell continue line.

    Returns:
    --------
    surf_str : string
        The surface string part
    """
    line_ele = line.strip().split()
    start = 0
    end = get_surf_str_slice_end_from_line(line)
    surf_str = ' '.join(line_ele[start:end])
    return surf_str


def get_universe_from_cell_line(line):
    """Get the universe number from line"""
    line = line.upper().strip().split('$')[0]  # strip out comment
    universe = None
    if 'U' in line and '=' in line:
        line_ele = line.split('U')
        universe = int(line_ele[-1].split()[0].split('=')[-1])
    return universe


def get_fill_from_cell_line(line):
    """Get the fill info number

    Parameters:
    -----------
    line : str
        The line from mcnp input file

    Returns:
    --------
    fill_number : int
        The fill number
    star_flag : str
        The star flag. Could be '' or '*'. If the star flag is '*', means the rotation matrix is in degree
    rotation_matrix : list
        The rotation matrix of the cell.
    """
    line = line.upper().strip().split('$')[0]  # strip out comment
    star_flag = ''
    rotation_matrix = []
    fill = None
    if '*FILL' in line:
        star_flag = '*'
    if 'FILL' in line and '=' in line:
        line_ele = line.split('FILL')
        fill = int(line_ele[-1].split('=')[-1].split('(')[0])
        # check whether there is rotation matrix
        if '(' not in line_ele[-1]:
            return fill, star_flag, []
        else:
            rotation_ele = line_ele[-1].split(
                '=')[-1].split('(')[-1].split(')')[0].split()
            for i, item in enumerate(rotation_ele):
                rotation_matrix.append(float(item))
    return fill, star_flag, rotation_matrix


def compose_cell_block(cid, mid, density, geom_str, imp_n=1, imp_p=None, u=None,
                       fill=None):
    """
    Compose cell block (single or multiple lines) of mcnp input.

    Parameters:
    -----------
    cid : int
        Cell id
    mid : int
        Material id
    density : float
        Density of the material. Could be 0, positive (atom density) or negative (mass density)
    geom_str : str
        Geometry definition
    imp_n : float
        Neutron importance
    imp_p : float
        Photon importance
    u : int
        Universe number
    fill : dict
        Fill parameters. [fill_number, star_flag, rotation_matrix]

    Returns:
    --------
    s : str
        Composed cell block
    """
    s = f"{cid} {mid}"
    if mid > 0:
        s = f"{s} {density}"
    s = f"{s} {geom_str}"
    # write imp and comments
    if imp_n is not None:
        if isinstance(imp_n, int) or (float.is_integer(imp_n)):
            s = f"{s} imp:n={int(imp_n)}"
        else:
            s = f"{s} imp:n={imp_n}"
    if imp_p is not None:
        if isinstance(imp_p, int) or (float.is_integer(imp_p)):
            s = f"{s} imp:p={int(imp_p)}"
        else:
            s = f"{s} imp:p={imp_p}"
    if u is not None:
        s = f"{s} u={u}"
    if fill is not None:
        rotation_str = ''
        if len(fill[2]) > 0:
            rotation_str = f"({str(fill[2][0])}"
            for i, item in enumerate(fill[2][1:]):
                rotation_str = f"{rotation_str} {str(item)}"
            rotation_str = f"{rotation_str})"
            s = f"{s} {fill[1]}fill={fill[0]} {rotation_str}"
        else:
            s = f"{s} {fill[1]}fill={fill[0]}"
    return s


def decompose_cell_block(s):
    """
    Decompose cell block (consisting of 1 or more than 1 lines)

    Parameters:
    -----------
    s : str
        The line(s) of a cell block

    Returns:
    --------
    surf_str : str
        surface string
    u : int or None
        The universe number
    fill : tuple
        The fill information (fill, star_flag, rotation_matrix)
    """
    # cleanup the block and make it in one line
    line = ' '.join(s.replace('\n', ' ').split()).strip()
    line_ele = line.split()
    cid = int(line_ele[0])
    surf_str = get_surf_str_from_cell_title_line(line)
    u = get_universe_from_cell_line(line)
    fill_number, star_flag, rotation_matrix = get_fill_from_cell_line(
        line)
    return surf_str, u, (fill_number, star_flag, rotation_matrix)


def read_cells_geom(filename):
    """
    Read the cell geometry.

    Parameters:
    -----------
    filename : string
        The filename of the mcnp input

    Returns:
    --------
    cells_info : dict
        The dictionary of the cells {cid: surf_string}
    u_info : dict
        The dictionary of the universe information {cid: u}
    fill_info : dict
        The dictionary of the fill information {cid: fill}
    """
    cells_info = {}
    cid = None
    cell_block = ''
    surf_str = ''
    u_info = {}
    fill_info = {}
    line_counter = 0
    with open(filename, 'r') as fin:
        cell_card_end = False
        while not cell_card_end:
            line = fin.readline()
            line_counter += 1
            if utils.is_blank_line(line):  # end of cell card
                cell_card_end = True
                break
            if utils.is_comment(line):
                continue
            if is_cell_title(line):
                # deal with previous
                if cid is not None:
                    surf_str, u, fill = decompose_cell_block(
                        cell_block)
                    cells_info[cid] = surf_str
                    surf_str = ''
                    u_info[cid] = u
                    fill_info[cid] = fill
                # deal with new cell block
                cell_block = line
                line_ele = line.split()
                cid = int(line_ele[0])
                surf_str = get_surf_str_from_cell_title_line(line)
                u = get_universe_from_cell_line(line)
                fill_number, star_flag, rotation_matrix = get_fill_from_cell_line(
                    line)
            elif line_counter > 1:  # continue line
                cell_block = f"{cell_block}{line}"
                surf_str = mcnp_style_str_append(
                    surf_str, get_surf_str_from_cell_cont_line(line))
                u = get_universe_from_cell_line(line)
                fill_number, star_flag, rotation_matrix = get_fill_from_cell_line(
                    line)
        # deal with last cell
        cells_info[cid] = surf_str
        u_info[cid] = u
        fill_info[cid] = (fill_number, star_flag, rotation_matrix)
    return cells_info, u_info, fill_info


def read_surfs_geom(filename):
    """
    Read the surface geometry.

    Parameters:
    -----------
    filename : string
        The filename of the mcnp input

    Returns:
    --------
    surfs_info : dict
        The dictionary of the cells {surf_id: surf_string}
    """
    surfs_info = {}
    surf_id = None
    surf_str = ''
    surf_card_start = False
    surf_card_end = False
    blank_count = 0
    with open(filename, 'r') as fin:
        while not surf_card_start:
            line = fin.readline()
            if utils.is_blank_line(line):
                blank_count += 1
                if blank_count == 1:
                    surf_card_start = True
                    # read the rest file
                    while not surf_card_end:
                        line = fin.readline()
                        if utils.is_blank_line(line):
                            blank_count += 1
                            if blank_count == 2:
                                surf_card_end = True
                        if utils.is_comment(line):
                            continue
                        if is_surf_title(line):
                            # deal with previous
                            if surf_id is not None:
                                surfs_info[surf_id] = surf_str
                                surf_str = ''
                            line_ele = line.split()
                            if '*' in line_ele[0]:
                                surf_id = int(line_ele[0][1:])
                            else:
                                surf_id = int(line_ele[0])
                            surf_str = ' '.join(line_ele[1:])
                        else:  # continue line
                            line_ele = line.strip().split()
                            surf_str = mcnp_style_str_append(
                                surf_str, ' '.join(line_ele))
                    # deal with last cell
                    surfs_info[surf_id] = surf_str
    return surfs_info


def get_max_surf_id(filename):
    """
    Read the surface geometry.

    Parameters:
    -----------
    filename : string
        The filename of the mcnp input

    Returns:
    --------
    max_surf_id : int
        The maximum surface id used in the file.
    """
    surf_id = None
    surf_card_start = False
    surf_card_end = False
    max_surf_id = 0
    blank_count = 0
    with open(filename, 'r') as fin:
        while not surf_card_start:
            line = fin.readline()
            if utils.is_blank_line(line):
                blank_count += 1
                if blank_count == 1:
                    surf_card_start = True
                    # read the rest file
                    while not surf_card_end:
                        line = fin.readline()
                        if utils.is_blank_line(line):
                            blank_count += 1
                            if blank_count == 2:
                                surf_card_end = True
                        if utils.is_comment(line):
                            continue
                        if is_surf_title(line):
                            line_ele = line.split()
                            if '*' in line_ele[0]:
                                surf_id = int(line_ele[0][1:])
                            else:
                                surf_id = int(line_ele[0])
                            if surf_id > max_surf_id:
                                max_surf_id = surf_id
                        else:  # continue line
                            pass
    return max_surf_id


def proper_cell_geom(cell_geom):
    """
    Add parentheses () if ':' exist in the description.
    """
    if ':' in cell_geom:
        # check parentheses
        lstack = []
        push_chars, pop_chars = "(", ")"
        # check left part
        lstr = cell_geom.strip().split(':')[0]
        for c in lstr:
            if c in push_chars:
                lstack.append(c)
            elif c in pop_chars:
                lstack.pop()
        if len(lstack) > 0:
            return cell_geom
        else:
            return f"({cell_geom})"
    else:
        return cell_geom


def calc_divide_planes(aabb, distance=10.0, direction='X'):
    """
    Split the aabb if it is too large (length > distance) on either one dimension.

    Parameters:
    -----------
    aabb : list 
    distance : float
        The distance to split the cell.

    Returns:
    --------
    coords : list of floats
        The coords of the plane along the direction
    """
    coords = []
    start = 2*(ord(direction.upper()) - ord('X'))
    end = start + 1
    for i in range(math.floor(aabb[start]), math.ceil(aabb[end]), distance):
        if i > aabb[start]:
            coords.append(i)
    return coords
