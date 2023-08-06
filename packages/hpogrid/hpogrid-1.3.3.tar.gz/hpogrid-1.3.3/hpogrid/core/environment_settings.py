import os
import sys
from .defaults import kGridSiteWorkDir, RunMode

def get_run_mode():
    environ_val = os.environ.get('HPOGRID_RUN_MODE', 'LOCAL')
    return RunMode.parse(environ_val)

def get_datadir():
    return os.environ.get('HPOGRID_DATA_DIR', os.getcwd())

def get_workdir():
    return os.environ.get('HPOGRID_WORK_DIR', os.getcwd())

def get_grid_workdir():
    if os.path.exists(kGridSiteWorkDir):
        return kGridSiteWorkDir
    else:
        return os.getcwd()

def is_grid_job():
    return (get_run_mode() in [RunMode.GRID, RunMode.IDDS])

def is_idds_job():
    return (get_run_mode() == RunMode.IDDS)

def is_local_job():
    return (get_run_mode() == RunMode.LOCAL)
    
def setup(run_mode:str='local', silent:bool=False):
    from hpogrid import stdout
    if silent:
        print_msg = stdout.error
    else:
        print_msg = stdout.info
    print_msg('INFO: Setting up HPO task')
    
    run_mode = RunMode.parse(run_mode).name
    
    os.environ['HPOGRID_RUN_MODE'] = run_mode
    
    _run_mode = RunMode.parse(run_mode)
    if _run_mode == RunMode.LOCAL:
        os.environ['HPOGRID_DATA_DIR'] = os.getcwd()
        os.environ['HPOGRID_WORK_DIR'] = os.getcwd()
    elif _run_mode == RunMode.GRID:
        os.environ['HPOGRID_DATA_DIR'] = get_grid_workdir()
        os.environ['HPOGRID_WORK_DIR'] = get_grid_workdir()
    elif _run_mode == RunMode.IDDS:
        os.environ['HPOGRID_DATA_DIR'] = get_grid_workdir()
        os.environ['HPOGRID_WORK_DIR'] = get_grid_workdir()
    else:
        raise ValueError(f"unknown run mode: {run_mode.lower()}")
    print_msg(f'INFO: HPO task will run in {run_mode.lower()} environment')
    print_msg('INFO: Work directory is set to "{}"'.format(get_workdir()))
    print_msg('INFO: Data directory is set to "{}"'.format(get_datadir()))
    
def reset():
    os.environ.pop('HPOGRID_RUN_MODE', None)
    os.environ.pop('HPOGRID_DATA_DIR', None)
    os.environ.pop('HPOGRID_WORK_DIR', None)
    
def set_scripts_path(scripts_path:str, undo:bool=False):
    from hpogrid import stdout
    if (scripts_path in sys.path) and undo:
        stdout.info('INFO: Removed {} from $PYTHONPATH'.format(scripts_path))
        sys.path.remove(scripts_path)
        os.environ["PYTHONPATH"].replace(scripts_path+":","")
        
    if (scripts_path not in sys.path) and (not undo):
        stdout.info('INFO: Adding {} to $PYTHONPATH'.format(scripts_path))
        sys.path.append(scripts_path)
        os.environ["PYTHONPATH"] = scripts_path + ":" + os.environ.get("PYTHONPATH", "")

def get_scripts_path(proj_name:str):
    project_path = get_project_path(proj_name)
    scripts_path = os.path.join(project_path, 'scripts')
    return scripts_path
        
def set_scripts_path_from_project(proj_name:str, undo:bool=False):
    project_path = get_project_path(proj_name)
    scripts_path = os.path.join(project_path, 'scripts')
    set_scripts_path(scripts_path, undo=undo)       