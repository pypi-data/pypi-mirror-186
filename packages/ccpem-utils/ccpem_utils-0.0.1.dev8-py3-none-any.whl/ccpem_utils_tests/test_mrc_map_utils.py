#
#     Copyright (C) 2021 CCP-EM
#
#     This code is distributed under the terms and conditions of the
#     CCP-EM Program Suite Licence Agreement as a CCP-EM Application.
#     A copy of the CCP-EM licence can be obtained by writing to the
#     CCP-EM Secretary, RAL Laboratory, Harwell, OX11 0FA, UK.
#

import unittest
import os
import shutil
import tempfile
import math
from ccpem_utils_tests import test_data
import subprocess
from ccpem_pyutils.scripts import get_map_parameters


class MapParseTests(unittest.TestCase):
    def setUp(self):
        """
        Setup test data and output directories.
        """
        self.test_data = os.path.dirname(test_data.__file__)
        self.test_dir = tempfile.mkdtemp(prefix="map_parse")
        # Change to test directory
        self._orig_dir = os.getcwd()
        os.chdir(self.test_dir)

    def tearDown(self):
        os.chdir(self._orig_dir)
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_run_subprocess_get_map_parameters(self):
        map_input = os.path.join(self.test_data, "emd_3488.mrc")
        subprocess.call(
            [
                "python3 "
                + os.path.realpath(get_map_parameters.__file__)
                + " -m "
                + map_input
                + " -odir "
                + self.test_dir,
            ],
            shell=True,
        )
        assert os.path.isfile(
            os.path.join(self.test_dir, "emd_3488_map_parameters.json")
        )
        assert math.isclose(
            os.stat(
                os.path.join(self.test_dir, "emd_3488_map_parameters.json")
            ).st_size,
            275,
            rel_tol=0.05,
        )
