import os
import sys
import json
import shutil
import numbers
import inspect
import tarfile
from typing import List, Dict
from contextlib import contextmanager
from subprocess import Popen, PIPE
import shlex

import numpy as np

def old_div(a, b):
    """
    DEPRECATED: import ``old_div`` from ``past.utils`` instead.

    Equivalent to ``a / b`` on Python 2 without ``from __future__ import
    division``.

    TODO: generalize this to other objects (like arrays etc.)
    """
    if isinstance(a, numbers.Integral) and isinstance(b, numbers.Integral):
        return a // b
    else:
        return a / b

def run_command(cmd):
    args = shlex.split(cmd, posix=False)
    with Popen(args, stdout=PIPE, bufsize=1, universal_newlines=True) as p:
        while True:
            line = p.stdout.readline()
            if not line:
                break
            print(line)    
        exit_code = p.poll()
    return exit_code


class NpEncoder(json.JSONEncoder):
    import numpy as np
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, np.bool_):
            return bool(obj)            
        else:
            return super(NpEncoder, self).default(obj)

def copytree(src, dst, symlinks=False, ignore=None):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dst, item)
        if os.path.isdir(s):
            shutil.copytree(s, d, symlinks, ignore)
        else:
            shutil.copy2(s, d)
            
def pretty_path(path:str):
    return os.path.abspath(os.path.realpath(os.path.expandvars(os.path.expanduser(path))))

def pretty_dirname(path:str):
    path = pretty_path(path)
    if os.path.isdir(path):
        return path
    else:
        return os.path.dirname(path)
    
def is_nan_or_inf(value):
    return np.isnan(value) or np.isinf(value)    
        
@contextmanager
def cd(newdir):
    prevdir = os.getcwd()
    os.chdir(os.path.expanduser(newdir))
    try:
        yield
    finally:
        os.chdir(prevdir)

def get_physical_devices(device_type='GPU'):
    import tensorflow as tf
    physical_devices = tf.config.list_physical_devices(device_type)
    return physical_devices

def get_n_gpu():
    #return len(get_physical_devices(device_type='GPU'))
    import torch
    return torch.cuda.device_count()

def get_n_cpu():
    return os.cpu_count()


def extract_tarball(input_path:str, output_path:str) ->List[str]:
    import hpogrid
    tarfiles = [ f for f in os.listdir(input_path) if f.endswith('tar.gz')]
    extracted_files = []
    for f in tarfiles:
        tar = tarfile.open(f, "r:gz")
        hpogrid.stdout.info('INFO: Untaring the file {}'.format(f))
        tar.extractall(path=output_path)
        extracted_files += tar.getnames()
        tar.close()
    return extracted_files

def remove_files(files:List[str]):
    for f in files:
        if os.path.isfile(f):
            os.remove(f)
        elif os.path.isdir(f):
            shutil.rmtree(f)        
            
def is_function_or_method(obj):
    """Check if an object is a function or method.
    Args:
        obj: The Python object in question.
    Returns:
        True if the object is an function or method.
    """
    return inspect.isfunction(obj) or inspect.ismethod(obj) or is_cython(obj)


def is_class_method(f):
    """Returns whether the given method is a class_method."""
    return hasattr(f, "__self__") and f.__self__ is not None  


"""
import socket
hostname = socket.gethostname()
"""
