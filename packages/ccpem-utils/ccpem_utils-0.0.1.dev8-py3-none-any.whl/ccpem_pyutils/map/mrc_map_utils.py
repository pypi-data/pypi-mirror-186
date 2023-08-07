#
#     Copyright (C) 2019 CCP-EM
#
#     This code is distributed under the terms and conditions of the
#     CCP-EM Program Suite Licence Agreement as a CCP-EM Application.
#     A copy of the CCP-EM licence can be obtained by writing to the
#     CCP-EM Secretary, RAL Laboratory, Harwell, OX11 0FA, UK.

from ccpem_pyutils.other.cluster import generate_kdtree
import numpy as np


def mrcmap_kdtree(map_instance):
    """
    Returns the KDTree of coordinates from a mrc map grid.

    Arguments:
        *map_instance*
            MrcFile or MapObjHandle Map instance.
    """
    if map_instance.__class__.__name__ == "MrcFile":
        origin = map_instance.header.origin.item()
        apix = map_instance.voxel_size.item()
        nz, ny, nx = map_instance.data.shape
    else:
        origin = map_instance.origin
        apix = map_instance.apix
        nz, ny, nx = map_instance.data.shape

    # convert to real coordinates
    zg, yg, xg = np.mgrid[0:nz, 0:ny, 0:nx]
    # to get indices in real coordinates
    zg = zg * apix[2] + origin[2] + apix[2] / 2.0
    yg = yg * apix[1] + origin[1] + apix[1] / 2.0
    xg = xg * apix[0] + origin[0] + apix[0] / 2.0
    indi = list(zip(xg.ravel(), yg.ravel(), zg.ravel()))
    gridtree = generate_kdtree(indi, leaf_size=42)
    return gridtree, indi
