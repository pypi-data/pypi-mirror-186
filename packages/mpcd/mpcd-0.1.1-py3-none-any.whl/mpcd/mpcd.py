from pickletools import uint8
import numpy as np
import re
import warnings
import struct
import lzf
import argparse
from pathlib import Path
import time
from functools import wraps
import os
from multiprocessing import Process
import copy
from .visualizer import PointCloudVisualizer

numpy_pcd_type_mappings = [
    (np.dtype("float32"), ("F", 4)),
    (np.dtype("float64"), ("F", 8)),
    (np.dtype("uint8"), ("U", 1)),
    (np.dtype("uint16"), ("U", 2)),
    (np.dtype("uint32"), ("U", 4)),
    (np.dtype("uint64"), ("U", 8)),
    (np.dtype("int8"), ("I", 1)),
    (np.dtype("int16"), ("I", 2)),
    (np.dtype("int32"), ("I", 4)),
    (np.dtype("int64"), ("I", 8)),
]
numpy_type_to_pcd_type = dict(numpy_pcd_type_mappings)
pcd_type_to_numpy_type = dict((q, p) for (p, q) in numpy_pcd_type_mappings)


def _parse_binary_compressed_pc_data(f, dtype, metadata):
    fmt = "II"
    compressed_size, uncompressed_size = struct.unpack(
        fmt, f.read(struct.calcsize(fmt))
    )
    compressed_data = f.read(compressed_size)

    buf = lzf.decompress(compressed_data, uncompressed_size)
    if len(buf) != uncompressed_size:
        raise Exception("Error decompressing data")
    # the data is stored field-by-field
    pc_data = np.zeros(metadata["points"], dtype=dtype)
    ix = 0
    for dti in range(len(dtype)):
        dt = dtype[dti]
        bytes = dt.itemsize * metadata["points"]
        column = np.frombuffer(buf[ix : (ix + bytes)], dt)
        pc_data[dtype.names[dti]] = column
        ix += bytes
    return pc_data


def _parse_binary_pc_data(f, dtype, metadata):
    rowstep = metadata["points"] * dtype.itemsize
    # for some reason pcl adds empty space at the end of files
    buf = f.read(rowstep)
    return np.frombuffer(buf, dtype=dtype)


def _parse_ascii_pc_data(f, dtype, metadata):
    return np.loadtxt(f, dtype=dtype, delimiter=" ")


def _parse_header(lines):
    metadata = {}
    for ln in lines:
        if ln.startswith("#") or len(ln) < 2:
            continue
        match = re.match("(\w+)\s+([\w\s\.]+)", ln)
        if not match:
            warnings.warn("warning: can't understand line: %s" % ln)
            continue
        key, value = match.group(1).lower(), match.group(2)
        if key == "version":
            metadata[key] = value
        elif key in ("fields", "type"):
            metadata[key] = value.split()
        elif key in ("size", "count"):
            metadata[key] = list(map(int, value.split()))
        elif key in ("width", "height", "points"):
            metadata[key] = int(value)
        elif key == "viewpoint":
            metadata[key] = list(map(float, value.split()))
        elif key == "data":
            metadata[key] = value.strip().lower()

    # add some reasonable defaults
    if "count" not in metadata:
        metadata["count"] = [1] * len(metadata["fields"])
    if "viewpoint" not in metadata:
        metadata["viewpoint"] = [0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]
    if "version" not in metadata:
        metadata["version"] = ".7"
    return metadata


def _build_dtype(metadata):
    fieldnames = []
    typenames = []
    for f, c, t, s in zip(
        metadata["fields"], metadata["count"], metadata["type"], metadata["size"]
    ):
        np_type = pcd_type_to_numpy_type[(t, s)]
        if c == 1:
            fieldnames.append(f)
            typenames.append(np_type)
        else:
            fieldnames.extend(["%s_%04d" % (f, i) for i in range(c)])
            typenames.extend([np_type] * c)
    dtype = np.dtype(list(zip(fieldnames, typenames)))
    return dtype


def _point_cloud_from_fileobj(f):
    """parse pointcloud coming from file object f"""
    header = []
    while True:
        ln = f.readline().strip()
        if not isinstance(ln, str):
            ln = ln.decode("utf-8")
        header.append(ln)
        if ln.startswith("DATA"):
            metadata = _parse_header(header)
            dtype = _build_dtype(metadata)
            break
    if metadata["data"] == "ascii":
        pc_data = _parse_ascii_pc_data(f, dtype, metadata)
    elif metadata["data"] == "binary":
        pc_data = _parse_binary_pc_data(f, dtype, metadata)
    elif metadata["data"] == "binary_compressed":
        pc_data = _parse_binary_compressed_pc_data(f, dtype, metadata)
    else:
        print(
            'DATA field is neither "ascii" or "binary" or\
                "binary_compressed"'
        )
    return (metadata, pc_data)


def _write_header(metadata, rename_padding=False):
    """Given metadata as dictionary, return a string header."""
    template = """\
VERSION {version}
FIELDS {fields}
SIZE {size}
TYPE {type}
COUNT {count}
WIDTH {width}
HEIGHT {height}
VIEWPOINT {viewpoint}
POINTS {points}
DATA {data}
"""
    str_metadata = metadata.copy()

    if not rename_padding:
        str_metadata["fields"] = " ".join(metadata["fields"])
    else:
        new_fields = []
        for f in metadata["fields"]:
            if f == "_":
                new_fields.append("padding")
            else:
                new_fields.append(f)
        str_metadata["fields"] = " ".join(new_fields)
    str_metadata["size"] = " ".join(map(str, metadata["size"]))
    str_metadata["type"] = " ".join(metadata["type"])
    str_metadata["count"] = " ".join(map(str, metadata["count"]))
    str_metadata["width"] = str(metadata["width"])
    str_metadata["height"] = str(metadata["height"])
    str_metadata["viewpoint"] = " ".join(map(str, metadata["viewpoint"]))
    str_metadata["points"] = str(metadata["points"])
    tmpl = template.format(**str_metadata)
    return tmpl


def _build_ascii_fmtstr(pc):
    """Make a format string for printing to ascii.

    Note %.8f is minimum for rgb.
    """
    fmtstr = []
    for t, cnt in zip(pc.type, pc.count):
        if t == "F":
            fmtstr.extend(["%.10f"] * cnt)
        elif t == "I":
            fmtstr.extend(["%d"] * cnt)
        elif t == "U":
            fmtstr.extend(["%u"] * cnt)
        else:
            raise ValueError("don't know about type %s" % t)
    return fmtstr

    def save_point_cloud(self, pc, fname, mode="binary_compressed"):
        assert mode in ["ascii", "binary", "binary_compressed"]
        with open(fname, "w") as f:
            self.point_cloud_to_fileobj(pc, f, mode)


def _point_cloud_to_fileobj(pc, fileobj, data_compression=None):
    """write pointcloud as .pcd to fileobj.
    if data_compression is not None it overrides pc.data.
    """
    metadata = pc.get_metadata()
    if data_compression is not None:
        data_compression = data_compression.lower()
        assert data_compression in ("ascii", "binary", "binary_compressed")
        metadata["data"] = data_compression

    header = _write_header(metadata).encode("utf-8")
    fileobj.write(header)
    if metadata["data"].lower() == "ascii":
        fmtstr = _build_ascii_fmtstr(pc)
        np.savetxt(fileobj, pc.pc_data, fmt=fmtstr)
    elif metadata["data"].lower() == "binary":
        fileobj.write(pc.pc_data.tobytes())
    elif metadata["data"].lower() == "binary_compressed":
        uncompressed_lst = []
        for fieldname in pc.pc_data.dtype.names:
            column = np.ascontiguousarray(pc.pc_data[fieldname]).tobytes()
            uncompressed_lst.append(column)
        uncompressed = b"".join(uncompressed_lst)
        uncompressed_size = len(uncompressed)
        # print("uncompressed_size = %r"%(uncompressed_size))
        buf = lzf.compress(uncompressed)
        if buf is None:
            buf = uncompressed
            compressed_size = uncompressed_size
        else:
            compressed_size = len(buf)
        fmt = "II"
        fileobj.write(struct.pack(fmt, compressed_size, uncompressed_size))
        fileobj.write(buf)
    else:
        raise ValueError("unknown DATA type")
    # we can't close because if it's stringio buf then we can't get value after


def _metadata_is_consistent(metadata):
    """Sanity check for metadata. Just some basic checks."""
    checks = []
    required = (
        "version",
        "fields",
        "size",
        "width",
        "height",
        "points",
        "viewpoint",
        "data",
    )
    for f in required:
        if f not in metadata:
            print("%s required" % f)
    checks.append((lambda m: all([k in m for k in required]), "missing field"))
    checks.append(
        (
            lambda m: len(m["type"]) == len(m["count"]) == len(m["fields"]),
            "length of type, count and fields must be equal",
        )
    )
    checks.append((lambda m: m["height"] > 0, "height must be greater than 0"))
    checks.append((lambda m: m["width"] > 0, "width must be greater than 0"))
    checks.append((lambda m: m["points"] > 0, "points must be greater than 0"))
    checks.append(
        (
            lambda m: m["data"].lower() in ("ascii", "binary", "binary_compressed"),
            "unknown data type:" "should be ascii/binary/binary_compressed",
        )
    )
    ok = True
    for check, msg in checks:
        if not check(metadata):
            print("error:", msg)
            ok = False
    return ok


def _pc_from_path(fname):
    """load pcd and return a PointCloud instance"""
    with open(fname, "rb") as f:
        meta, pc = _point_cloud_from_fileobj(f)
        return PointCloud(meta, pc)


def _pc_concat(pc_list):
    """concatenate multiple point clouds"""
    metas = [i.get_metadata() for i in pc_list]
    fields_unique = np.unique(np.array([i["fields"] for i in metas]), axis=0)
    size_unique = np.unique(np.array([i["size"] for i in metas]), axis=0)
    type_unique = np.unique(np.array([i["type"] for i in metas]), axis=0)
    points_list = [i["points"] for i in metas]
    width_list = [i["width"] for i in metas]
    height_list = [i["height"] for i in metas]
    data_list = [i["data"] for i in metas]
    # all concat pc has same fields, size and type
    try:
        assert (
            fields_unique.shape[0] == 1
            and size_unique.shape[0] == 1
            and type_unique.shape[0] == 1
            and len(set(data_list)) == 1
            # and len(set(width_list)) == 1
            # and len(set(height_list)) == 1
        )
    except:
        from IPython import embed

        embed(colors="neutral")
    meta = pc_list[0].get_metadata()
    meta["points"] = np.sum(points_list)
    meta["width"] = meta["points"]
    meta["height"] = 1
    pc = np.concatenate([pc.pc_data for pc in pc_list])
    return PointCloud(meta, pc)


class PointCloud:
    """Wrapper for point cloud data.

    The variable members of this class parallel the ones used by
    the PCD metadata (and similar to PCL and ROS PointCloud2 messages),

    ``pc_data`` holds the actual data as a structured numpy array.

    The other relevant metadata variables are:

    - ``version``: Version, usually .7
    - ``fields``: Field names, e.g. ``['x', 'y' 'z']``.
    - ``size.`: Field sizes in bytes, e.g. ``[4, 4, 4]``.
    - ``count``: Counts per field e.g. ``[1, 1, 1]``. NB: Multi-count field
      support is sketchy.
    - ``width``: Number of points, for unstructured point clouds (assumed by
      most operations).
    - ``height``: 1 for unstructured point clouds (again, what we assume most
      of the time.
    - ``viewpoint``: A pose for the viewpoint of the cloud, as
      x y z qw qx qy qz, e.g. ``[0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0]``.
    - ``points``: Number of points.
    - ``type``: Data type of each field, e.g. ``[F, F, F]``.
    - ``data``: Data storage format. One of ``ascii``, ``binary`` or ``binary_compressed``.

    See `PCL docs <http://pointclouds.org/documentation/tutorials/pcd_file_format.php>`__
    for more information.
    """

    vis = PointCloudVisualizer()

    def __init__(self, metadata, pc_data):
        self.metadata_keys = metadata.keys()
        self.__dict__.update(metadata)
        self.pc_data = pc_data
        self.check_sanity()

    def get_metadata(self):
        """returns copy of metadata"""
        metadata = {}
        for k in self.metadata_keys:
            metadata[k] = copy.copy(getattr(self, k))
        return metadata

    def check_sanity(self):
        md = self.get_metadata()
        assert _metadata_is_consistent(md)
        assert len(self.pc_data) == self.points
        assert self.width * self.height == self.points
        assert len(self.fields) == len(self.count)
        assert len(self.fields) == len(self.type)

    def save_ascii(self, fname):
        self.save_pcd(fname, "ascii")

    def draw_bev(
        self,
        color="gray",
        r=0,
        show=True,
        save=False,
        save_path=None,
        draw_distance_marker=True,
        draw_orin_marker=True,
        auto_rot=True,
    ):
        draw = self.vis.draw_pcloud(
            self.to_ndarray(["x", "y"]),
            color,
            r,
            draw_distance_marker,
            draw_orin_marker,
            show,
            auto_rot,
            save,
            save_path,
        )
        return draw

    @staticmethod
    def draw_bev_overlay(
        pc_tuple,
        draw_distance_marker=True,
        draw_orin=True,
        show=True,
        auto_rot=True,
        save=False,
        save_path=None):
        return PointCloud.vis.draw_pc_overlay(
            pc_tuple,
            draw_distance_marker,
            draw_orin,
            show,
            auto_rot,
            save,
            save_path,
        )


    def to_ndarray(self, fields=None):
        if not fields:
            fields = self.fields
        assert set(fields).issubset(
            set(self.fields)
        ), f"Invalid fields, only support {str(self.fields)}"
        field_list = [self.pc_data[f].reshape(-1, 1) for f in fields]
        points = np.concatenate((field_list), axis=1)
        points = points[~np.isnan(points)[:, 0]]
        points.astype(np.float32)
        return points

    def to_lidar_ndarray(self):
        try:
            points = self.to_ndarray(fields=["x", "y", "z", "intensity"])
        except:
            points = self.to_ndarray(fields=["x", "y", "z"])
            print(points.shape)
            points = np.concatenate(
                [points, np.ones((points.shape[0], 1), dtype=np.float32)], axis=1
            )
        return points

    def to_radar_ndarray(self):
        try:
            points = self.to_ndarray(fields=["x", "y", "z", "rcs", "radial_vel"])
        except:
            points = self.to_ndarray(fields=["x", "y", "z"])
        return points

    def save_pcd(self, fname, compression=None, **kwargs):
        if "data_compression" in kwargs:
            warnings.warn("data_compression keyword is deprecated for" " compression")
            compression = kwargs["data_compression"]
        with open(fname, "wb") as f:
            _point_cloud_to_fileobj(self, f, compression)

    def coor_trans(self, extr_mat):
        if extr_mat.__class__.__name__ != "ndarray":
            extr_mat = np.array(extr_mat)

        # assignment destination is read-only, so need copy
        pc_data = self.pc_data.copy()
        assert "x" in self.fields and "y" in self.fields and "z" in self.fields

        x = pc_data["x"]
        y = pc_data["y"]
        z = pc_data["z"]
        xyz_1 = np.vstack((x, y, z, np.ones((1, x.shape[0]))))
        xyz_1_trans = np.dot(extr_mat, xyz_1)
        pc_trans = np.ascontiguousarray((xyz_1_trans[:3]).T)

        pc_data["x"] = pc_trans[:, 0]
        pc_data["y"] = pc_trans[:, 1]
        pc_data["z"] = pc_trans[:, 2]
        self.pc_data = pc_data
        return self

    def copy(self):
        new_pc_data = np.copy(self.pc_data)
        new_metadata = self.get_metadata()
        return PointCloud(new_metadata, new_pc_data)

    def downsample(self, sample_ratio):
        pc_data = self.pc_data.copy()
        self.pc_data = pc_data[::sample_ratio]
        self._adjust_field()
        return self

    def _parse_condition(self, condition_str):
        operator_list = ["<=", ">=", "==", "!=", "<", ">"]
        condition_str = condition_str.replace(" ", "")
        for operator in operator_list:
            if operator in condition_str:
                logic = operator
                break
        else:
            raise ValueError("Invalid logic operator")

        field = condition_str.split(operator)[0]
        value = condition_str.split(operator)[1]
        if field+logic+value!=condition_str:
            raise ValueError('condition incorrect')
        assert field and logic and value, 'condition incorrect'
        return field, logic, value

    def filter_by_condition(self, conditions):
        # keep the points that satisfy the condition
        if not isinstance(conditions, list):
            conditions = [conditions]
        for condition in conditions:
            field, logic, value = self._parse_condition(condition)
            condition=f"self.pc_data['{field}'] {logic} {value}"
            pc_data = self.pc_data[eval(condition)]
            self.pc_data = pc_data
        self._adjust_field()
        return self


    def _adjust_field(self):
        self.points = self.pc_data.shape[0]
        self.width = self.points
        self.height = 1

    @staticmethod
    def from_path(fname):
        return _pc_from_path(fname)

    @staticmethod
    def pc_concat(pc_list):
        return _pc_concat(pc_list)
