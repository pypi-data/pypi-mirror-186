import numpy as np
from typing import Union, Type

try:
    from scipy.spatial import cKDTree as kdt
except ImportError:
    from scipy.spatial import KDTree as kdt

import math
import re


def calc_z(
    list_vals: Union[list, np.ndarray],
    val: float = None,
) -> Union[float, list]:
    # remove selected value before calculating z
    if val is not None:
        if isinstance(val, list):
            list_vals.remove(val)  # remove val from list
        elif isinstance(val, np.ndarray):
            list_vals = list_vals[list_vals != val]
        else:
            pass
    sum_mapval = np.sum(list_vals)
    mean_mapval = sum_mapval / len(list_vals)
    # median_mapval = np.median(list_vals)
    std_mapval = np.std(list_vals)
    if val is None:
        if std_mapval == 0.0:
            z = [0.0] * len(list_vals)
        else:
            z = np.round((np.array(list_vals) - mean_mapval) / std_mapval, 2)
    else:
        if std_mapval == 0.0:
            z = 0.0
        else:
            z = (val - mean_mapval) / std_mapval
    return z


def calc_z_median(
    list_vals: Union[list, np.ndarray],
    val: float = None,
) -> Union[float, list]:
    # remove selected value before calculating z
    if val is not None:
        if isinstance(val, list):
            list_vals.remove(val)  # remove val from list
        elif isinstance(val, np.ndarray):
            list_vals = list_vals[list_vals != val]
        else:
            pass

    # sum_smoc = np.sum(list_vals)
    median_smoc = np.median(list_vals)
    mad_smoc = np.median(np.absolute(np.array(list_vals) - median_smoc))
    if val is None:
        if mad_smoc == 0.0:
            z = [0.0] * len(list_vals)
        else:
            z = np.around((np.array(list_vals) - median_smoc) / mad_smoc, 2)
    else:
        if mad_smoc == 0.0:
            z = 0.0
        else:
            z = round(((val - median_smoc) / mad_smoc), 2)
    return z


def get_indices_sphere(
    gridtree: Type[kdt],
    coord: Union[list, np.ndarray],
    dist: float = 5.0,
) -> list:
    list_points = gridtree.query_ball_point([coord[0], coord[1], coord[2]], dist)
    return list_points


# utility functions to compare dict/list/str/num including a tolerance
# for any numeric comparisons within
def compare_dict_almost_equal(self, dict1: dict, dict2: dict, num_rel_tol: float):
    diff_dict = {}
    for k in dict2:
        assert k in dict1
        if dict1[k] != dict2[k]:
            diff_dict[k] = dict2[k]
    for k in diff_dict:
        if isinstance(dict1[k], dict):
            self.compare_dict_similarity(dict1[k], dict2[k], num_rel_tol)
        elif type(dict1[k]) in [list, tuple]:
            self.compare_list_similarity(dict1[k], dict2[k], num_rel_tol)
        else:
            self.compare_values(dict1[k], dict2[k], num_rel_tol)


def compare_list_almost_equal(self, list1, list2, num_rel_tol):
    for n in range(len(list1)):
        if isinstance(list1[n], dict):
            self.compare_dict_similarity(list1[n], list2[n], num_rel_tol)
        if type(list1[n]) in [list, tuple]:
            self.compare_list_similarity(list1[n], list2[n], num_rel_tol)
        else:
            self.compare_values(list1[n], list2[n], num_rel_tol)


def compare_values_almost_equal(self, value1, value2, num_rel_tol):
    if isinstance(value1, str):
        l1 = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", value1)
        l2 = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", value2)
        assert len(l1) == len(l2)
        if len(l1) == 1:
            assert math.isclose(float(l1[0]), float(l2[0]), rel_tol=num_rel_tol)
        else:
            assert l1 == l2
    else:
        try:
            assert math.isclose(float(l1), float(l2), rel_tol=num_rel_tol)
        except ValueError:
            assert l1 == l2


def get_moc(array1: np.ndarray, array2: np.ndarray) -> float:
    num = np.sum(array1 * array2)
    den = np.sqrt(np.sum(np.square(array1)) * np.sum(np.square(array2)))
    if den == 0.0:
        if num == 0.0:
            return 1.0
        return -1.0
    return num / den


def get_ccc(array1: np.ndarray, array2: np.ndarray) -> float:
    num = np.sum((array1 - np.mean(array1)) * (array2 - np.mean(array2)))
    den = np.sqrt(
        np.sum(np.square(array1 - np.mean(array1)))
        * np.sum(np.square(array2 - np.mean(array2)))
    )
    if den == 0.0:
        if num == 0.0:
            return 1.0
        return -1.0
    return num / den
