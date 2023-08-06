# Copyright 2023 Cegal AS
# All rights reserved.
# Unauthorized copying of this file, via any medium is strictly prohibited.



import numpy as np
import datetime
import typing
import re


IPY2 = 'ipy2'
CPY3 = 'cpy3'


def python_env():
    return CPY3


def iterable_values(arr):
    return arr.flat


def clone_array(arr: np.ndarray) -> np.ndarray:
    return arr.copy()


def to_backing_arraytype(nparray):
    ''' Creates and returns a .NET Array that mirrors the provided numpy array

    @nparray: numpy array

    @Returns: .NET Array with element type matching nparray.dtype and identical dimensions with content that matches the provided numpy array
    '''
    return nparray

######################## Conversions from .NET ###########################

def from_backing_arraytype(src):
    ''' Creates and returns a numpy Array that mirrors the provided .NET array

    @src: .NET Array in in-process mode and a protobuf type in out-of-process mode

    @Returns: numpy Array with dtype matching src's element type, and identical dimensions with content that matches the provided .NET Array
    '''
    return src

def _to_shaped_ndarray(val, size_i, size_j, size_k, np_type, spanning_dims = 'ijk'):
    if type(size_i) == int:
        size_i = (size_i, size_i+1)
    if type(size_j) == int:
        size_j = (size_j, size_j+1)
    if type(size_k) == int:
        size_k = (size_k, size_k+1)
    if isinstance(val, list):
        val = np.array(val)

    if not hasattr(val, "__len__"):
        val_ndarray = np.empty(size_k, dtype = np_type)
        val_ndarray.fill(val)        
    else:
        val_ndarray = val
    
    if spanning_dims == 'ij':
        di, dj = size_i[1]-size_i[0], size_j[1] - size_j[0]
        val_ndarray.shape = (di, dj)
    elif spanning_dims == 'k':
        dk = size_k[1]-size_k[0]
        val_ndarray.shape = (dk)
    else:
        di, dj, dk = size_i[1]-size_i[0], size_j[1] - size_j[0], size_k[1]-size_k[0]
        val_ndarray.shape = (di, dj, dk)
            
    return val_ndarray.astype(np_type, copy = False, subok = True)

###################

def _ensure_1d_array(val, i, np_typ, net_typ, convert):
    if isinstance(val, np.ndarray):
        return val.astype(dtype=np_typ, copy=False)
    elif isinstance(val, list):
        if len(val) > i:
            raise ValueError("too many values")
        array = np.empty((i), np_typ)
        for index in range(0, i):
            array[index] = convert(val[index])
        return array

    raise ValueError("Cannot convert %s into 1d array" % val)

def ensure_1d_float_array(val, i):
    """Converts a flat list into a Array[float] if necessary"""
    return _to_shaped_ndarray(val, 1, 1, (0, i), np.float32, spanning_dims = 'k')

def ensure_1d_int_array(val, i):
    """Converts a flat list into a Array[int] if necessary"""
    return _to_shaped_ndarray(val, 1, 1, (0, i), np.int32, spanning_dims = 'k')

def ensure_2d_float_array(val, i, j):
    """Converts a flat or nested list into a Array[float]
    if necessary"""
    return _to_shaped_ndarray(val, (0, i), (0, j), 1, np.float32, spanning_dims = 'ij')

def ensure_2d_int_array(val, i, j):
    """Converts a flat or nested list into a Array[float]
    if necessary"""
    return _to_shaped_ndarray(val, (0, i), (0, j), 1, np.int32, spanning_dims = 'ij')

def ensure_3d_float_array(val, i, j, k):
    return _to_shaped_ndarray(val, (0, i), (0, j), (0, k), np.float32)

def ensure_3d_int_array(val, i, j, k):
    return _to_shaped_ndarray(val, (0, i), (0, j), (0, k), np.int32)

def str_has_content(s: typing.Optional[str]) -> bool:
    """Returns False if the string is None, empty, or just whitespace"""
    if s is None:
        return False
    return bool(s.strip())

def str_or_none(s: typing.Optional[str]) -> typing.Optional[str]:
    if not str_has_content(s):
        return None
    return s

def about_equal(a, b):
    return abs(a-b) < 0.0000001

def floatarray(lst):
    return ensure_1d_float_array(lst, len(lst))

def intarray(lst):
    return ensure_1d_int_array(lst, len(lst))

def to_python_datetime(dt: typing.Union[typing.Any, datetime.datetime]) -> datetime.datetime:
    if isinstance(dt, datetime.datetime):
        return dt
    else:
        raise ValueError("Argument was expected to be a datetime.datetime object, got {}".format(dt))

def from_python_datetime(dt):
    return dt

def native_accessor(accessor):
    if not isinstance(accessor, tuple):
        raise TypeError("accessor is not tuple")
    return accessor


# Unit header is on the form "{name} [{unit}]"
unit_header_regex = r"(?P<objectname>.+)(?P<unit>\[.+\]|\[\])$"
def to_unit_header(name, unit):
    header = name + ' [' + unit + ']'
    if not is_valid_unit_header(header):
        raise ValueError("\"" + header + "\" is not a valid unit header")
    return header

def name_from_unit_header(header):
    if is_valid_unit_header(header):
        return re.search(unit_header_regex, header).group(1).rstrip()

def unit_from_unit_header(header):
    unit_with_brackets = re.search(unit_header_regex, header).group(2)
    return str(unit_with_brackets)[1:-1]

def is_valid_unit_header(header):
    return re.fullmatch(unit_header_regex, header) is not None