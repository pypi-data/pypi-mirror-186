"""
    Module for formatting tables, texts and figures used in hpogrid
"""
import yaml
import copy

import pandas as pd
from tabulate import tabulate

kDefaultTableStyle = 'psql'
kDefaultStrAlign = 'left'

class ColorCode():
    RED = '\033[0;91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = '\033[5m'
    
def str_presenter(dumper, data):
    """configures yaml for dumping multiline strings
    Ref: https://stackoverflow.com/questions/8640959/how-can-i-control-what-scalar-form-pyyaml-uses-for-my-data"""
    if len(data.splitlines()) > 1:  # check for multiline string
        return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
    return dumper.represent_scalar('tag:yaml.org,2002:str', data)

yaml.add_representer(str, str_presenter)
yaml.representer.SafeRepresenter.add_representer(str, str_presenter)    
    
def insert_newlines(string, every=64):
    return '\n'.join(string[i:i+every] for i in range(0, len(string), every))

def type2str(typevar):
    if isinstance(typevar, tuple):
        return ', '.join([t.__name__ for t in typevar])
    else:
        return typevar.__name__    

def join_options(options):
    return ' '.join(["--{} {}".format(key,value) for (key,value) in options.items()])

def create_table(data, columns=None, indexed=True, transpose=False,
    tableformat=kDefaultTableStyle, stralign=kDefaultStrAlign):
    df = pd.DataFrame(data, columns=columns)
    if transpose:
        df = df.transpose()
    table = tabulate(df, showindex=indexed, headers=df.columns, 
        tablefmt=tableformat,
        stralign=stralign)
    return table

def format_dict_str_len(source):
    if isinstance(source, dict):
        for key, value in source.items():
            source[key] = format_dict_str_len(value)
        return source
    elif isinstance(source, str) and (len(source) > 80):
        return insert_newlines(source, 80)
    else:
        return source

def create_formatted_dict(data, columns=None, indexed=True, transpose=False,
    tableformat=kDefaultTableStyle, stralign=kDefaultStrAlign):
    _data = copy.deepcopy(data)
    _data = format_dict_str_len(_data)  
    if isinstance(_data, dict):
        for key in _data:
            if isinstance(_data[key], dict):
                _data[key] = yaml.dump(_data[key], allow_unicode=True,
                                       default_flow_style=False, sort_keys=False)
    df = pd.DataFrame(_data.items(), columns=columns)
    if transpose:
        df = df.transpose()
    
    table = tabulate(df, showindex=indexed, headers=df.columns, 
        tablefmt=tableformat,
        stralign=stralign)
    return table