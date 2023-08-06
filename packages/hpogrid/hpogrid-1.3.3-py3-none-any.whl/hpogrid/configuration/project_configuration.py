import os
import json
import yaml
import shutil
from copy import deepcopy
from datetime import datetime
from typing import Dict, List, Union, Optional

from hpogrid import semistaticmethod
from hpogrid.core.defaults import kProjectConfigNameJson, ConfigType, ConfigAction
from hpogrid.core.config_manager import (get_project_script_dir, get_project_config_dir,
                                         get_project_config_path, get_project_path)
from hpogrid.utils.helper import copytree
from hpogrid.configuration import (ConfigurationBase, ModelConfiguration, 
                                   HPOConfiguration, GridConfiguration,
                                   SearchSpaceConfiguration)

class ProjectConfiguration(ConfigurationBase):
    _CONFIG_TYPE_ = ConfigType.PROJECT
    _CONFIG_DISPLAY_NAME_ = 'project'
    _LIST_COLUMNS_ = ['Project Title']
    _OUTPUT_EXPR_ = get_project_config_path("{name}")
    _CONFIG_FORMAT_ = \
        {
            'scripts_path': {
                'abbr': 'p',
                'description': 'Path to the location of training scripts'+\
                               ' (or the directory containing the training scripts)',
                'required': True,
                'type': str
            },
            'model_config': {
                'abbr': 'm',
                'description': 'Name of the model configuration to use',
                'required': True,
                'type': str
            },
            'search_space': {
                'abbr': 's',
                'description': 'Name of the search space configuration to use',
                'required': True,
                'type':str
            },
            'hpo_config': {
                'abbr': 'o',
                'description': 'Name of the hpo configuration to use',
                'required': True,
                'type':str
            },
            'grid_config': {
                'abbr': 'g',
                'description': 'Name of the grid configuration to use',
                'required': True,
                'type':str
            }
        }
    
    _CONFIG_CLS_ = {
        "model_config" : ModelConfiguration,
        "hpo_config"   : HPOConfiguration,
        "grid_config"  : GridConfiguration,
        "search_space" : SearchSpaceConfiguration
    }
    
    def __init__(self, name:Optional[str]=None, verbosity:str="INFO"):
        super().__init__(name=name, verbosity=verbosity)
        self._scripts_path = None
    
    def _validate_arguments(self, **args):
        args = super()._validate_arguments(**args)
        scripts_path = args.pop('scripts_path', None)
        if (scripts_path is None):
            self.stdout.info('INFO: Path to training scripts is not specified. Skipping...')
        elif (scripts_path is not None) and (not os.path.exists(scripts_path)):
            raise FileNotFoundError(f'Path to training scripts {scripts_path} does not exist.')
            
        self._scripts_path = scripts_path

        # check if input configuration files exist
        for config_type, config_cls in self._CONFIG_CLS_.items():
            if (config_type in args) and (args[config_type] is not None):
                config_name = args[config_type]
                args[config_type] = config_cls.load_config(config_name)
            else:
                self.stdout.info('INFO: Path to {} configuration is not specified. '
                                 'Skipping...'.format(config_cls._CONFIG_DISPLAY_NAME_))
        return args
    
    @classmethod
    def validate(cls, config:Dict):
        validated_config = deepcopy(config)
        for config_type, config_cls in cls._CONFIG_CLS_.items():
            validated_config[config_type] = config_cls.validate(config[config_type])
        return validated_config
    
    @classmethod
    def _validate(cls, config:Dict):
        cls.stdout.info('INFO: Validating project configuration...')
        result = cls.validate(config)
        cls.stdout.info('INFO: Validation complete.')
        return result
    
    @semistaticmethod
    def _save_scripts(self, source:str, dest:str):
        if os.path.exists(source):
            # copy training scripts to the project directory
            self.stdout.info(f'INFO: Copying training scripts from {source} to {dest}')
            # copy contents of directory to project/scrsipts/
            if os.path.isdir(source):
                copytree(source, dest)
            else:
                shutil.copy2(source, dest)
        else:
            raise FileNotFoundError(f'Path to training scripts {source} does not exist.')
    
    def move_to_backup(self, project_path:str):
        if not os.path.exists(project_path):
            raise FileNotFoundError(f"project path \"{project_path}\" does not exist")
        backup_dir = get_project_path("backup")
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        name = os.path.basename(project_path)
        backup_project_path = os.path.join(backup_dir, f'{name}_{timestamp}')
        shutil.move(project_path, backup_project_path)
        return backup_project_path
    
    def save(self, name=None, config=None, scripts_path=None, 
             action:Union[ConfigAction, str]='create'):
        if (name is None) and (config is None):
            name = self._name
            config = self._config
        if name is None: 
            raise ValueError('configuration name undefined')
        config = {'project_name':name, **config}
        
        project_dir = get_project_path(name)
        
        action = ConfigAction.parse(action)
        action_str = ConfigAction.to_str(action, tense="cont").title()
        print(f'INFO: {action_str} project "{name}"')
        if (os.path.exists(project_dir)):
            if  action == ConfigAction.CREATE:
                self.stdout.error(f'ERROR: Project "{name}" already exists. If you want to overwrite,'
                                   ' use "recreate" or "update" action instead of "create".')
                return None
            elif action == ConfigAction.RECREATE:
                backup_project_path = self.move_to_backup(project_dir)
                self.stdout.info('INFO: Recreating project. Original project moved to backup '
                                 f'directory {backup_project_path}.')
        
        # create directories if not already exist
        scripts_dir = get_project_script_dir(name)
        config_dir  = get_project_config_dir(name)
        if not os.path.exists(project_dir):
            os.makedirs(project_dir)
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        if not os.path.exists(scripts_dir):
            os.makedirs(scripts_dir)
        
        if scripts_path is None:
            scripts_path = self._scripts_path
        
        # copy training scripts
        if (scripts_path is not None):
            self._save_scripts(scripts_path, scripts_dir)
        
        config_path_json = self.get_config_path(name, extension='json')
        config_path_yaml = self.get_config_path(name, extension='yaml')

        action_str = ConfigAction.to_str(action, tense="past").title()
        with open(config_path_json, 'w') as config_file_json:
            json.dump(config, config_file_json, indent=2)
            self.stdout.info(f'INFO: {action_str} {self._CONFIG_TYPE_} configuration {config_path_json}')
        with open(config_path_yaml, 'w') as config_file_yaml:
            yaml.dump(config, config_file_yaml, default_flow_style=False, sort_keys=False)
            self.stdout.info(f'INFO: {action_str} {self._CONFIG_TYPE_} configuration {config_path_yaml}')
        self.show(name)
       
    @staticmethod
    def create_project(config:Dict, scripts_path:str=None, action:str='create'):
        project_name = config['project_name']
        project_config = ProjectConfiguration()
        project_config.save(project_name, config, scripts_path=scripts_path, action=action)