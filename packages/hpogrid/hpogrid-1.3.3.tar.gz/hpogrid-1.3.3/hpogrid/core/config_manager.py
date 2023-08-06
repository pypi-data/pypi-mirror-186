import os
import sys
import glob
import json
import fnmatch
from typing import Dict, List, Union, Optional

from .defaults import (kConfigPaths, kProjectConfigNameJson, RunMode, ConfigType)
from .environment_settings import get_workdir, get_run_mode

def get_base_path():
    import hpogrid
    return hpogrid.userdata_path        

def get_config_dir(config_type:Union[str, ConfigType]):
    """Returns the directory that stores configuration files of a particular configuration type
    
    Args:
        config_type: str
            Type of configuration
    """
    config_type = ConfigType.parse(config_type)
    config_dir = os.path.join(get_base_path(), kConfigPaths[config_type])
    return config_dir
    
def get_project_path(proj_name:str):
    if get_run_mode() in [RunMode.GRID, RunMode.IDDS]:
        proj_path = get_workdir()
    elif get_run_mode() == RunMode.LOCAL:
        proj_dir = get_config_dir(ConfigType.PROJECT)
        proj_path = os.path.join(proj_dir, proj_name)
    return proj_path

def get_project_script_dir(proj_name:str):
    project_path = get_project_path(proj_name)
    project_script_path = os.path.join(project_path, "scripts")
    return project_script_path

def get_project_config_dir(proj_name:str):
    project_path = get_project_path(proj_name)
    project_config_path = os.path.join(project_path, "config")
    return project_config_path

def get_project_config_path(proj_name:str):
    project_config_dir = get_project_config_dir(proj_name)
    config_path = os.path.join(project_config_dir, kProjectConfigNameJson)
    return config_path
                        
def get_project_config(proj_name:str):
    config_path = get_project_config_path(proj_name)
    if not os.path.exists(config_path):
        raise FileNotFoundError(f'Missing project configuration file: {config_path}')
    config = load_configuration(config_path)
    return config

def get_config_list(config_type:Union[str, ConfigType], expr=None) -> List[str]:
    config_type = ConfigType.parse(config_type)
    if config_type == ConfigType.PROJECT:
        # takes into account when running jobs externally
        if get_run_mode() in [RunMode.GRID, RunMode.IDDS]:
            config_path = get_project_config_path(None)
            config = load_configuration(config_path)
            config_list = [config['project_name']]
        elif get_run_mode() == RunMode.LOCAL:
            config_dir = get_config_dir(config_type)
            config_list = [d for d in os.listdir(config_dir) if 
                           os.path.isdir(os.path.join(config_dir, d))]
    else:
        config_dir = get_config_dir(config_type)
        config_list = glob.glob(os.path.join(config_dir, "*"))
        config_list = [os.path.basename(p) for p in config_list]
        config_list = [os.path.splitext(p)[0] for p in config_list]
    # filter config name by wildcard
    expr = expr if expr is not None else '*'
    config_list = fnmatch.filter(config_list, expr)

    return config_list

def get_project_list(expr=None):
    return get_config_list(ConfigType.PROJECT, expr=expr)

def is_project(obj:str):
    if not isinstance(obj, str):
        return False
    return obj in get_project_list()

def load_configuration(config_input:[Dict, str]) -> Dict:
    """Returns project configuration given input
    
    Args:
        config_input: dict, str
            If dict, it is the configuration itself
            If str, it is either the name of the project,
            of path to a configuration file.
    """
    if isinstance(config_input, dict):
        return config_input
    elif isinstance(config_input, str):
        ext = os.path.splitext(config_input)[1]
        # check if config_input is a project name
        if not ext:
            if is_project(config_input):
                return get_project_config(config_input)
            else:
                raise ValueError(f'project "{config_input}" does not exist')
        # check if configuration file exists
        if not (os.path.exists(config_input)):
            raise FileNotFoundError(f"configuration file {config_input} does not exist.")
        # load configuration file
        with open(config_input, 'r') as file:
            if ext in ['.txt', '.yaml']:
                config = yaml.safe_load(file)
            elif ext == '.json':
                config = json.load(file)
            else:
                raise ValueErrror(f'the configuration file has an unsupported '
                                  f'file extension: {txt} (allowed: txt, yaml, json)')
        return config
    else:
        raise ValueError(f'unknown configuration format: {config_input}')