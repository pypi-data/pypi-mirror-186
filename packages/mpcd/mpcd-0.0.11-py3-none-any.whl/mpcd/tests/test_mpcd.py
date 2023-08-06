"""
this is just a basic sanity check, not a really legit test suite.
"""

import pytest
import numpy as np
import os
import shutil
import tempfile

header1 = """\
# .PCD v0.7 - Point Cloud Data file format
VERSION 0.7
FIELDS x y z i
SIZE 4 4 4 4
TYPE F F F F
COUNT 1 1 1 1
WIDTH 500028
HEIGHT 1
VIEWPOINT 0 0 0 1 0 0 0
POINTS 500028
DATA binary_compressed
"""

header2 = """\
VERSION .7
FIELDS x y z normal_x normal_y normal_z curvature boundary k vp_x vp_y vp_z principal_curvature_x principal_curvature_y principal_curvature_z pc1 pc2
SIZE 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4 4
TYPE F F F F F F F F F F F F F F F F F
COUNT 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
WIDTH 19812
HEIGHT 1
VIEWPOINT 0.0 0.0 0.0 1.0 0.0 0.0 0.0
POINTS 19812
DATA ascii
"""

@pytest.fixture
def pcd_fname():
    import mpcd
    return os.path.join(mpcd.__path__[0], 'test_data',
                        'partial_cup_model.pcd')

@pytest.fixture
def ascii_pcd_fname():
    import mpcd
    return os.path.join(mpcd.__path__[0], 'test_data',
                        'ascii.pcd')

@pytest.fixture
def bin_pcd_fname():
    import mpcd
    return os.path.join(mpcd.__path__[0], 'test_data',
                        'bin.pcd')

def cloud_centroid(pc):
    xyz = np.empty((pc.points, 3), dtype=np.float)
    xyz[:,0] = pc.pc_data['x']
    xyz[:,1] = pc.pc_data['y']
    xyz[:,2] = pc.pc_data['z']
    return xyz.mean(0)

def test_parse_header():
    from mpcd.mpcd import _parse_header
    lines = header1.split('\n')
    md = _parse_header(lines)
    assert (md['version'] == '0.7')
    assert (md['fields'] == ['x', 'y', 'z', 'i'])
    assert (md['size'] == [4, 4, 4, 4])
    assert (md['type'] == ['F', 'F', 'F', 'F'])
    assert (md['count'] == [1, 1, 1, 1])
    assert (md['width'] == 500028)
    assert (md['height'] == 1)
    assert (md['viewpoint'] == [0, 0, 0, 1, 0, 0, 0])
    assert (md['points'] == 500028)
    assert (md['data'] == 'binary_compressed')


def test_from_path(pcd_fname):
    from mpcd import PointCloud
    pc = PointCloud.from_path(pcd_fname)

    fields = 'x y z normal_x normal_y normal_z curvature boundary k vp_x vp_y vp_z principal_curvature_x principal_curvature_y principal_curvature_z pc1 pc2'.split()
    for fld1, fld2 in zip(pc.fields, fields):
        assert(fld1 == fld2)
    assert (pc.width == 19812)
    assert (len(pc.pc_data) == 19812)




