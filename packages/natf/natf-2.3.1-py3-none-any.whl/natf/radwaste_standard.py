#!/usr/bin/env python3
# -*- coding:utf-8 -*-
''' class Radwaste.'''
import sys
import os
import numpy as np
import pandas as pd
import re
from natf import utils

if sys.version_info[0] > 2:
    basestring = str

thisdir = os.path.dirname(os.path.abspath(__file__))

# define radwaste classes to int dit
rwc2int = {'Clearance': 1, 'VLLW': 2, 'LLW': 3,
           'LLWC': 3, 'LLWB': 3, 'LLWA': 3,
           'ILW': 4, 'HLW': 5}


class RadwasteStandard(object):
    """Class Radwaste, used to store radioactive waste classification information"""

    def __init__(self, standard):
        self._standard = standard
        self._files = self.get_standard_default_files()
        self._classes = []  # names of the different classes
        # chn2018
        self._chn2018_df = None  # CHN2018 use
        # russian
        self._df = None  # RUSSIAN use
        # usnrc
        self._dfl = None  # USNRC long live table use
        self._dfs = None  # USNRC short live table use
        self._dfede = None  # USNRC
        self.read_standard()

    @property
    def standard(self):
        return self._standard

    @standard.setter
    def standard(self, value):
        if not isinstance(value, str):
            raise ValueError('standard must be a string!')
        if value not in ('CHN2018', 'USNRC', 'USNRC_FETTER', 'UK', 'RUSSIAN'):
            raise ValueError("standard {0} not supported!".format(value))
        self._standard = value

    @property
    def files(self):
        return self._files

    @files.setter
    def files(self, value):
        if not isinstance(value, list):
            raise ValueError("files must be a list!")
        for f in value:
            if not os.path.isfile(f):
                raise ValueError("File {0} not found".format(f))
        self._flies = value

    @property
    def classes(self):
        return self._classes

    @classes.setter
    def classes(self, value):
        if not isinstance(value, list):
            raise ValueError("classes must be a list!")
        for item in value:
            if not isinstance(item, str):
                raise ValueError("class name should be string")
        self._classes = value

    @property
    def df(self):
        return self._df

    @df.setter
    def df(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("df must be a dataframe.")
        self._df = value

    @property
    def chn2018_df(self):
        return self._chn2018_df

    @chn2018_df.setter
    def chn2018_df(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("chn2018_df must be a dataframe.")
        self._chn2018_df = value

    @property
    def dfl(self):
        return self._dfl

    @dfl.setter
    def dfl(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("dfl must be a dataframe.")
        self._dfl = value

    @property
    def dfs(self):
        return self._dfs

    @dfs.setter
    def dfs(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("dfs must be a dataframe.")
        self._dfs = value

    @property
    def dfede(self):
        return self._dfede

    @dfede.setter
    def dfede(self, value):
        if not isinstance(value, pd.DataFrame):
            raise ValueError("dfede must be a dataframe.")
        self._dfede = value

    def get_standard_default_files(self):
        """Get filename for specific standard."""
        files = []
        standard_dir = os.path.join(
            thisdir, "radwaste_standards", self.standard)
        if self.standard == 'CHN2018':
            files.append(os.path.join(standard_dir, self.standard + ".csv"))
        elif self.standard == 'USNRC':
            # long live table
            files.append(os.path.join(
                standard_dir, self._standard + "_LL.csv"))
            # short live table
            files.append(os.path.join(
                standard_dir, self._standard + "_SL.csv"))
            # EDE table
            files.append(os.path.join(standard_dir,
                                      self._standard + "_EDE_MASS.csv"))
        elif self.standard == 'USNRC_FETTER':
            files.append(os.path.join(standard_dir, self._standard + ".csv"))
            # EDE table
            files.append(os.path.join(os.path.join(thisdir, "radwaste_standards", "USNRC"),
                                      "USNRC_EDE_MASS.csv"))
        elif self.standard == 'RUSSIAN':
            files.append(os.path.join(standard_dir, self._standard + ".csv"))
        return files

    def read_standard(self):
        """Read the csv into dataframe."""
        if self.standard == 'CHN2018':
            df = pd.read_csv(self.files[0])
            self._chn2018_df = df
            self._classes = self._chn2018_df.columns[1:]
        elif self.standard == 'USNRC':
            dfl = pd.read_csv(self.files[0])
            dfs = pd.read_csv(self.files[1])
            dfede = pd.read_csv(self.files[2])
            self._dfl = dfl
            self._dfs = dfs
            self._dfede = dfede
            self._classes = ['LLWA', 'LLWB', 'LLWC']
        elif self.standard == 'USNRC_FETTER':
            df = pd.read_csv(self.files[0])
            dfede = pd.read_csv(self.files[1])
            self._df = df
            self._dfede = dfede
            self._classes = ['LLWA', 'LLWB', 'LLWC']
        elif self.standard == 'UK':
            self._classes = ['Clearance', 'LLW', 'ILW', 'HLW']
        elif self.standard == 'RUSSIAN':
            self._classes = ['LLW', 'ILW']
            self._df = pd.read_csv(self.files[0])

    def get_nuc_limits_chn2018(self, nuc):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.

        Returns:
        --------
        Limit of the nuclide in specific material, unit [Bq/kg].
        """
        col_num = len(self.chn2018_df.columns)
        limits = np.array(
            self.chn2018_df.loc[self.chn2018_df['Nuclide'] == nuc]).flatten()
        limits = limits[1:]
        # nuc not found in the list, set to default inf
        if len(limits) == 0:
            limits = np.array([float('inf')]*(col_num-1))
        return limits

    def get_nuc_limit_usnrc_clearance(self, nuc, material_type='Steel'):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.
        material_type: string
            The material type. Nuclide in different types of materials has
            different EDE values. Therefore, the material type should be
            provided. The default material type is set to Steel.

        Returns:
        --------
        Clearance limit of the nuclide in specific nuclide, unit [Bq/kg].
        """

        edes = np.array(self.dfede.loc[self.dfede['Nuclide'] == nuc]).flatten()
        if len(edes) == 0:  # nuc not in the list
            return float('inf')  # set to inf as default
        ede = edes[1]  # [uSv/hr per Bq/g]
        limit = 10 * 1e3 / ede  # [Bq/kg]
        return limit

    def get_nuc_limits_usnrc(self, nuc, half_life, density):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.
        half_life: float
            Half life of the nuclide, unit: [s].
        density: float
            Density of the material where the nuclide exists, unit: [g/cm3].
            Required in 'USNRC' and 'USNRC_FETTER' standard because of the
            unit conversion.

        Returns:
        --------
        Limit of the nuclide in specific material, unit [Bq/kg].
        """

        # check if the half life provided
        if half_life is None:
            raise ValueError("Half of the nuclide must be provided in "
                             "USNRC standard")

        if nuc in ('Pu241', 'Cm242') or (not utils.is_short_live(half_life)):
            # long lvie nuclide or Pu242/Cm242
            col_num = len(self.dfl.columns)
            # use data from USNRC_LL
            limits = np.array(
                self.dfl.loc[self.dfl['Nuclide'] == nuc]).flatten()
            limits = limits[1:]
        else:
            #  short-live
            col_num = len(self.dfs.columns)
            # use data from USNRC_SL
            if half_life < 3600.0*24*365.25*5:
                limits = np.array([700.0, 700.0, 700.0])
            else:
                limits = np.array(
                    self.dfs.loc[self.dfs['Nuclide'] == nuc]).flatten()
                limits = limits[1:]

        # convert the unit from Ci/m3 or Ci/g to Bq/kg
        if nuc in ('Pu241', 'Cm242'):
            # convert from Ci/g to Bq/kg
            limits = np.multiply(limits, utils.ci2bq(1.0)*1e3)
        else:
            # convert from Ci/m3 to Bq/kg
            limits = np.multiply(limits, utils.ci2bq(1.0)/density/1e3)

        # nuc not found in the list, set to default inf
        if len(limits) == 0:
            limits = np.array([float('inf')]*(col_num-1))
        return limits

    def get_nuc_limits_usnrc_fetter(self, nuc, half_life, density):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.
        half_life: float
            Half life of the nuclide, unit: [s].
        density: float
            Density of the material where the nuclide exists, unit: [g/cm3].
            Required in 'USNRC' and 'USNRC_FETTER' standard because of the
            unit conversion.

        Returns:
        --------
        Limit of the nuclide in specific material, unit [Bq/kg].
        """

        # check density
        if density is None:
            raise ValueError("Density must be provide in 'USNRC_FETTER'")
        if half_life < 3600.0*24*365.25*5:
            limits = np.array([700.0, 700.0, 700.0])
            # convert from Ci/m3 to Bq/kg
            limits = np.multiply(limits, utils.ci2bq(1.0)/density/1e3)
        else:
            limits_s = np.array(
                self.df.loc[self.df['Nuclide'] == nuc]).flatten()
            if len(limits_s) > 1:
                limit_c = convert_nrc_fetter_limit(
                    limits_s[-1], density=density)
                limits = [limit_c*0.01, limit_c*0.1, limit_c]
            else:
                # nuc not in table
                limits = [float('inf'), float('inf'), float('inf')]
        return limits

    def get_nuc_limits_russian(self, nuc, half_life=None):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.
        half_life: float
            Half life of the nuclide, unit: [s].

        Returns:
        --------
        Limit of the nuclide in specific material, unit [Bq/kg].
        """

        if half_life is not None:
            if utils.is_short_live(half_life, threshold=5):
                limits = [float('inf')]
                return limits
        else:
            # read table first
            limits = np.array(self.df.loc[self.df['Nuclide'] == nuc]).flatten()
            limits = limits[1:]
            if len(limits) == 0:
                # nuc not in table
                if is_u(nuc) or is_alpha_5(nuc):
                    limits = [3.7e6]
                else:
                    limits = [float('inf')]
            else:
                return limits
        return limits

    def get_nuc_limits(self, nuc, half_life=None, density=None):
        """Get the limits for different class of a specific nuclide.

        Parameters:
        -----------
        nuc: string
            Nuclide name. Eg. H3, Cs137.
        half_life: float, optional
            Half life of the nuclide, unit: s. Required in USNRC standard.
        density: float, optional
            Density of the material where the nuclide exists, unit: g/cm3.
            Required in 'USNRC' and 'USNRC_FETTER' standard because of the
            unit conversion.

        Returns:
        --------
        Limit of the nuclide in specific material, unit Bq/kg.
        """

        # CHN2018 standard
        if self.standard == 'CHN2018':
            return self.get_nuc_limits_chn2018(nuc)
        # USNRC standard
        elif self.standard == 'USNRC':
            return self.get_nuc_limits_usnrc(nuc, half_life, density)
        # USNRC_FETTER standard
        elif self.standard == 'USNRC_FETTER':
            return self.get_nuc_limits_usnrc_fetter(nuc, half_life, density)
        # RUSSIAN standard
        elif self.standard == 'RUSSIAN':
            return self.get_nuc_limits_russian(nuc, half_life)

    def determine_class_chn2018(self, indices, decay_heat):
        """Determine the radwaste class CHN2018, according to the indices and
        the decay heat.

        Parameters:
        -----------
        indices: numpy array (1D)
            Indices of difference class of a specific cooling time.
            Eg. clear index, VLLW index, ...
        decay_heat: float
            Decay heat of a cooling time. Unit: kW/m3.
        """

        # if the decay heat is above 2kW/m3, it's HLW
        # if decay_heat > 2:
        #    return 'HLW'
        # if the decay heat is no more than 2kW/m3, check the indices
        # check indices length
        if len(indices) != len(self.chn2018_df.columns) - 1:
            raise ValueError("indices length wrong")
        for i in range(len(indices)):
            if indices[i] <= 1.0:
                return self.chn2018_df.columns[1+i]
        # not any index no more than 1, higher class
        return 'ILW'

    def determine_class_usnrc(self, rwi_ll, rwi_sl, ci):
        """Determine the radwaste class USNRC, according to the rw.

        Parameters:
        -----------
        rwi_ll: numpy array (1D)
            Indices of difference class of a specific cooling time for long
            lived nuclides and Pu241 and Cm242.
            Eg. LLWA, LLWB, LLWC, ILW
        rwi_sl: numpy array (1D)
            Indices of difference class of a specific cooling time for short
            lived nuclides.
        ci: int
            Clearance index under USNRC standard.
        """

        # Clearance if ci <= 1
        if ci <= 1.0:
            return 'Clearance'

        classes = ['LLWA', 'LLWB', 'LLWC', 'ILW']
        # check indices length
        if len(rwi_ll) != len(self.dfl.columns) - 1 or \
                (len(rwi_sl) != len(self.dfl.columns) - 1):
            raise ValueError("radwaste indices length wrong")

        class_ll, class_sl, class_al = 3, 3, 3
        # class according to rwi_ll
        for i in range(len(rwi_ll)):
            if rwi_ll[i] <= 1.0:
                class_ll = i
                break
        # class according to rwi_sl
        for i in range(len(rwi_sl)):
            if rwi_sl[i] <= 1.0:
                class_sl = i
                break

        # combine two class
        if class_ll == 0:
            class_al = class_sl
        elif class_ll > 0 and class_ll <= 2:
            if class_sl <= 2:
                class_al = 2

        return classes[class_al]

    def determine_class_usnrc_fetter(self, rwi, ci):
        """Determine the radwaste class USNRC, according to the rw.

        Parameters:
        -----------
        rwi: numpy array (1D)
            Indices of difference class of a specific cooling time.
        ci: int
            Clearance index under USNRC standard.
        """

        # Clearance if ci <= 1
        if ci <= 1.0:
            return 'Clearance'

        classes = ['LLWA', 'LLWB', 'LLWC']
        # class according to rwi_ll
        for i in range(len(rwi)):
            if rwi[i] <= 1.0:
                return classes[i]

        # all rwi bigger than 1
        return 'ILW'

    def determine_class_uk(self, alpha_acts, acts, decay_heat, total_ci):
        """Determine the radwaste class UK, according to the alpha activity,
        total specific activity and the decay heat.

        Parameters:
        -----------
        alpha_acts: float
            Specific activity of alpha decay nuclides.
        acts: float
            Specific activity of all the nuclides.
        decay_heat: float
            Decay heat of a cooling time. Unit: kW/m3.
        """

        # input check
        if alpha_acts < 0 or acts < 0 or decay_heat < 0:
            raise ValueError("Negative data!")
        # if the decay heat is above 2kW/m3, it's HLW
        # if decay_heat > 2:
        #    return 'HLW'
        if total_ci <= 1.0:
            return 'Clearance'
        # if the decay heat is no more than 2kW/m3, check the alpha_acts and acts
        if alpha_acts <= 4.0e6 and (acts-alpha_acts) <= 1.2e7:
            return 'LLW'
        else:
            return 'ILW'

    def determine_class_russian(self, indices):
        """Determine the radwaste class RUSSIAN, according to the indices.

        Parameters:
        -----------
        indices: numpy array (1D)
            Indices of difference class of a specific cooling time.
            Eg. clear index, LLW index, ...
        """

        # check indices length
        if len(indices) != len(self.df.columns) - 1:
            raise ValueError("indices length wrong")
        for i in range(len(indices)):
            if indices[i] <= 1.0:
                return self.df.columns[1+i]
        # not any index no more than 1, higher class
        return 'ILW'


def convert_nrc_fetter_limit(limit_cs, density):
    """
    Convert the NRC_FETTER limit from string to a float.
    """
    if limit_cs == 'TMSA':
        limit_c = float('inf')
        return limit_c

    tokens = limit_cs.strip().split()
    if len(tokens) == 1:
        value = float(limit_cs)  # unit Ci/m3
        limit_c = utils.ci2bq(value) / density / 1e3  # unit: Bq/kg
        return limit_c

    if len(tokens) == 2:
        value = float(tokens[0])
        unit = tokens[1]  # unit is  (nCi/g)
        limit_c = 1e-9 * utils.ci2bq(value) * 1e3  # unit: Bq/kg
        return limit_c

    # unknown limit_cs
    raise ValueError("limit_cs {0} format wrong".format(limit_cs))


def rwc_to_int(rwc, standard='CHN2018'):
    """Convert rwc to int."""
    if standard == 'CHN2018':
        rwc2inp = {'Clearance': 1, 'VLLW': 2, 'LLW': 3, 'ILW': 4, 'HLW': 5}
    elif standard in ['USNRC', 'USNRC_FETTER']:
        rwc2inp = {'Clearance': 1, 'LLWA': 3,
                   'LLWB': 3, 'LLWC': 3, 'ILW': 4, 'HLW': 5}
    elif standard == 'RUSSIAN':
        rwc2inp = {'LLW': 3, 'ILW': 4, 'HLW': 5}
    elif standard == 'UK':
        rwc2inp = {'Clearance': 1, 'LLW': 3, 'ILW': 4, 'HLW': 5}
    else:
        raise ValueError(f"standard: {standard} not supported")
    return rwc2inp[rwc]


def ctr_to_int(ctr):
    """Convert cooling time requirement to int."""
    # convert ctr to float
    if '<' in ctr:
        ctr = float(ctr[1:]) * 0.99
    elif '>' in ctr:
        ctr = float(ctr[1:]) * 1.01
    else:
        ctr = float(ctr)

    # check ctr
    if ctr <= 1:  # green
        return 1
    elif 1 < ctr and ctr <= 10:  # blue
        return 2
    elif 10 < ctr and ctr <= 100:  # yellow
        return 3
    elif 100 < ctr and ctr <= 1000:  # pink
        return 4
    elif 1000 < ctr:  # red
        return 5
    else:
        raise ValueError(f"Wrong ctr: {ctr}")


def is_u(nuc):
    """Check whether a nuclide is U"""
    u_pattern = re.compile("^U[0-9]*", re.IGNORECASE)
    if re.match(u_pattern, nuc):
        return True
    else:
        return False


def is_alpha_5(nuc):
    """Check whether a nuclide is alpha emitting and half-life > 5 year"""
    alpha_5_nucs = ('Np237', 'Pu238', 'Pu239', 'Pu240', 'Pu241', 'Pu242', 'Pu244',
                    'Am241', 'Am242m', 'Am243', 'Cm243', 'Cm244', 'Cm245', 'Cm246',
                    'Cm247', 'Cm248', 'Cf249', 'Cf250', 'Cf251')
    if nuc in alpha_5_nucs:
        return True
    else:
        return False
