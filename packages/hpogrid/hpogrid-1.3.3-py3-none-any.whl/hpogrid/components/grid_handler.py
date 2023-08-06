import os
import sys
import glob
import json
import tempfile
from typing import Optional, Dict, List

from hpogrid import semistaticmethod
from hpogrid.core.defaults import *
from hpogrid.core import config_manager
from hpogrid.utils import helper, stylus

from .abstract_object import AbstractObject

class GridHandler(AbstractObject):
    
    def __init__(self, verbosity:str="INFO"):
        super().__init__(verbosity=verbosity)
    
    @semistaticmethod
    def submit(self, config_input:str, n_jobs:int=1, site:str=None, time:int=-1, search_points:List=None,
               mode:str='grid', debug:bool=False, scripts_path:str=None, extra:Optional[Dict]=None):
        if extra is None:
            extra = []
        config = self.preprocess_config(config_input, scripts_path)
        if mode == 'grid':
            self.submit_grid(config, n_jobs=n_jobs, site=site, time=time,
                             search_points=search_points, debug=debug, extra=extra)
        elif mode == 'idds':
            self.submit_idds(config, n_jobs=n_jobs, site=site, debug=debug, extra=extra)
        else:
            raise ValueError('Unknown job submission mode: {}'.format(mode))
            
    @semistaticmethod
    def preprocess_config(self, config_input:str, scripts_path:str=None):
        config = config_manager.load_configuration(config_input)
        from hpogrid.configuration import ProjectConfiguration
        config = ProjectConfiguration._validate(config)
        project_name = config['project_name']
        if not config_manager.is_project(project_name):
            self.stdout.info(f'INFO: Creating project directory for "{project_name}"')
            ProjectConfiguration.create_project(config, scripts_path=scripts_path, action='create')
        elif not config_manager.is_project(config_input):
            self.stdout.info(f'INFO: Replacing project directory for "{project_name}"')
            ProjectConfiguration.create_project(config, scripts_path=scripts_path, action='recreate')
        return config
        
    @semistaticmethod
    def submit_idds(self, config:Dict, n_jobs:int=1, site:str=None, debug:bool=False,
                    extra:Optional[Dict]=None):
        if extra is None:
            extra = []
        project_path = config_manager.get_project_path(config['project_name'])
        self.stdout.info(f'INFO: Submitting {n_jobs} idds grid job(s)')
        with tempfile.TemporaryDirectory() as tmpdirname:
            from hpogrid.interface.idds.main import transpose_config
            idds_config, search_space = transpose_config(config)
            idds_config_path = os.path.join(tmpdirname, 'idds_config.json')
            search_space_path = os.path.join(tmpdirname, 'search_space.json')
            # create temporary files for idds configuration and search space
            with open(idds_config_path, 'w') as idds_config_file:
                json.dump(idds_config, idds_config_file)
            with open(search_space_path, 'w') as search_space_file:
                json.dump(search_space, search_space_file)  
            command = self.format_idds_command(config, tmpdirname, site=site, extra=extra)
            with helper.cd(project_path):
                if debug:
                    self.stdout.info('INFO: iDDS configuration is')
                    table = stylus.create_formatted_dict(idds_config, ['Attribute', 'Value'], indexed=False)
                    self.stdout.info(table)
                    # submit jobs
                    self.stdout.info('INFO: The idds command is ')
                    self.stdout.info(f'{command}')
                for _ in range(n_jobs):
                    os.system(command)
    @semistaticmethod
    def submit_grid(self, config:Dict, n_jobs:int=1, site:str=None, time:int=-1, debug:bool=False,
                    search_points:List=None, scripts_path:str=None, extra:Optional[Dict]=None):
        if extra is None:
            extra = []
        project_path = config_manager.get_project_path(config['project_name'])
        print(f'INFO: Submitting {n_jobs} grid job(s)')
        command = self.format_grid_command(config, site=site, time=time,
                                           search_points=search_points,  extra=extra)
        with helper.cd(project_path):
            # submit jobs
            for _ in range(n_jobs):
                if debug:
                    self.stdout.info('INFO: The prun command is ')
                    self.stdout.info(f'{command}')
                os.system(command)
                
    @staticmethod
    def format_idds_command(config:Dict, tmpdirname:str, site:str=None, extra:Optional[Dict]=None):
        if extra is None:
            extra = []
        idds_config_path = os.path.join(tmpdirname, 'idds_config.json')
        search_space_path = os.path.join(tmpdirname, 'search_space.json')
        options = {'loadJson': idds_config_path,
                   'searchSpaceFile': search_space_path}
        proj_name = config['project_name']
        grid_config = config['grid_config']
        # override site settings if given
        if not site:
            site = grid_config['site']
                
        if site:
            if isinstance(site, str):
                if site != 'ANY':
                    options['site'] = site
            elif isinstance(site, list):
                options['site'] = ','.join(site)
            else:
                raise ValueError('Invalid site settings: {}'.format(site))
            # specify architecture for gpu/cpu site
            if 'GPU' in options['site']:
                options['architecture'] = 'nvidia-gpu'
        # options excluded from idds configuration file due to
        # possible bash variable expansion
        in_ds = config['grid_config']['inDS']
        out_ds = config['grid_config']['outDS']
        
        if in_ds:
            options['trainingDS'] = in_ds
            
        if '{HPO_PROJECT_NAME}' in out_ds:
            out_ds = out_ds.format(HPO_PROJECT_NAME=proj_name)
        options['outDS'] = out_ds
                
        command = 'phpo {} {}'.format(stylus.join_options(options), ' '.join(extra))    
        return command
    
    @staticmethod
    def format_grid_command(config:Dict, site:str=None, time:int=-1,
                            search_points:List=None, extra:Optional[Dict]=None):
        if extra is None:
            extra = []
        options = {'forceStaged': '',
                   'useSandbox': '',
                   'noBuild': '',
                   'alrb': ''}
        
        grid_config = config['grid_config']
        proj_name = config['project_name']
        
        options['containerImage'] = grid_config['container']
        
        search_points = '' if not search_points else '--search_points {}'.format(search_points)

        options['exec'] = '"pip install --upgrade hpogrid && '+\
                          'hpogrid run {} --mode grid {}"'.format(proj_name, search_points)

        if not grid_config['retry']:
            options['disableAutoRetry'] = ''

        if grid_config['inDS']:
            options['inDS'] = grid_config['inDS']

        if '{HPO_PROJECT_NAME}' in grid_config['outDS']:
            grid_config['outDS'] = grid_config['outDS'].format(HPO_PROJECT_NAME=proj_name)
                
        options['outDS'] = grid_config['outDS']
                
        if time != -1:
            options['maxCpuCount'] = str(time)
        
        # override site settings if given
        if not site:
            site = grid_config['site']
                
        if site:
            if isinstance(site, str):
                if site != 'ANY':
                    options['site'] = site
            elif isinstance(site, list):
                options['site'] = ','.join(site)
            else:
                raise ValueError('Invalid site settings: {}'.format(site))
            # specify architecture for gpu/cpu site
            if 'GPU' in options['site']:
                options['architecture'] = 'nvidia-gpu'
        
        command = 'prun {} {}'.format(stylus.join_options(options), ' '.join(extra))
        return command        
                