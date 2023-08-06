import os
import sys
import glob
import json
import fnmatch
from copy import deepcopy
from json import JSONDecodeError
from typing import Optional, Union, Dict, List

from hpogrid.core.defaults import ConfigAction, ConfigType, kConfigFormat
from hpogrid.core.config_manager import get_config_dir, get_config_list, load_configuration
from hpogrid.utils import stylus

from hpogrid.components import AbstractObject

class ConfigurationBase(AbstractObject):
    
    _CONFIG_TYPE_ = ConfigType.BASE
    _CONFIG_DISPLAY_NAME_ = '<CONFIG>'
    _LIST_COLUMNS_ = ['General Configuration']
    _SHOW_COLUMNS_ = ['Attribute', 'Value']    
    _CONFIG_FORMAT_ = {}
    _OUTPUT_EXPR_ = "{name}"
    _DEFAULT_OPT_ARG_ = '0'*99
    
    def __init__(self, name:Optional[str]=None, verbosity:str="INFO"):
        super().__init__(verbosity=verbosity)
        self._config = {}
        self._name = name
        
    def __getitem__(self, key:str):
        return self.config[key]
        
    @classmethod
    def load(cls, filename:str):
        config = cls.load_config(filename)
        instance = cls()
        instance._config = config
        return instance
        
    @property
    def config(self):
        return self._config
    
    @property
    def name(self):
        '''Name of configuration
        '''
        return self._name
        
    @classmethod
    def get_config_dir(cls):
        return get_config_dir(cls._CONFIG_TYPE_)
    
    @classmethod
    def get_config_path(cls, config_name:str=None, extension:str='json'):
        """Returns the full path of a configuration file
        
        Args:
            config_name: str
                Name of the configuration file
            extension: str, default='json'
                File extension for configuration file
        """
        
        config_dir = cls.get_config_dir()
        filename   = cls._OUTPUT_EXPR_.format(name=config_name)
        filename   = os.path.splitext(filename)[0] + f".{extension}"
        config_path = os.path.join(config_dir, filename)
        return config_path    
    
    @classmethod
    def get_config_list(cls, expr:str=None):
        """Returns a list of configuration files for a specific type of configuration
        
        Args:
            expr: str
                Regular expression for filtering name of configuration files
        """
        return get_config_list(cls._CONFIG_TYPE_, expr)
    
    @classmethod
    def load_config(cls, name:str):
        """Returns a specified configuration file
        
        Args:
            name: str
                Name of configuration file
        """
        if not os.path.exists(name):
            config_path = cls.get_config_path(name)
            if not os.path.exists(config_path):
                raise FileNotFoundError(f'configuration file {config_path} does not exist.')
        else:
            config_path = name
        config = load_configuration(config_path)
        return cls.validate(config)
    
    @classmethod
    def locate(cls, name:str):
        """Display the content of a configuration file
        
        Args:
            name: str
                Name of configuration file        
        """
        config_path = cls.get_config_path(name)
        if not os.path.exists(config_path):
            raise FileNotFoundError(f'no configuration file found with name \"{name}\"')
        print(config_path)
    
    @classmethod
    def list(cls, expr:str=None):
        """List out configuration files for a specific type of configuration as a table
        
        Args:
            expr: str
                Regular expression for filtering name of configuration files        
            exclude: list[str]
                Configuration files to exclude from listing
        """
        config_list = cls.get_config_list(expr)
        table = stylus.create_table(config_list, cls._LIST_COLUMNS_)
        print(table)
        
    @classmethod
    def show(cls, name:str):
        """Display the content of a configuration file
        
        Args:
            name: str
                Name of configuration file        
        """
        config = cls.load_config(name)
        table = stylus.create_formatted_dict(config, cls._SHOW_COLUMNS_, indexed=False)
        print(table)
        
    @classmethod
    def remove(cls, expr:str):
        """Removes a configuration file
        
        Args:
            expr: str
                Name of the configuration file to remove (accept wildcard)
        """
        config_list = cls.get_config_list(expr)
        if not config_list:
            cls.stdout.error(f'ERROR: No configuration file found that matches the epxression "{expr}"')
            return None
        for name in config_list:
            config_path = cls.get_config_path(name)
            if os.path.exists(config_path):
                os.remove(config_path)
                cls.stdout.info(f'INFO: Removed file {config_path}')
            else:
                cls.stdout.error(f'ERROR: Cannot remove file {config_path}. File does not exist.')
            
    def _validate_arguments(self, **args):
        if 'name' not in args:
            raise ValueError('missing argument: config_name')
        return args
    
    @classmethod
    def _validate(cls, config):
        cls.stdout.info(f'INFO: Validating {cls._CONFIG_DISPLAY_NAME_} configuration...')
        result = cls.validate(config)
        cls.stdout.info(f'INFO: Successfully validated {cls._CONFIG_DISPLAY_NAME_} configuration')
        return result
    
    @classmethod
    def validate(cls, config:Dict):
        validated_config = deepcopy(config)
        config_format = kConfigFormat[cls._CONFIG_TYPE_]
        for key in config_format:
            if key in config:
                # check if the value type of the config is correct
                value_type = config_format[key]['type']
                # if attribute type is dict, parse string input as dict
                if ((value_type == dict) or (isinstance(value_type, tuple) and (dict in value_type))) and \
                   isinstance(config[key], str):
                    try:
                        validated_config[key] = json.loads(config[key])
                    except JSONDecodeError:
                        raise RuntimeError(f'ERROR: Cannot decode the value of "{key}" as dictionary. '
                                           'Please check your input.')
                # if attribute type is list, parse string input as list by delimitation            
                elif ((value_type == list) or (isinstance(value_type, tuple) and (list in value_type))) and \
                    isinstance(config[key], str):
                    validated_config[key] = config[key].split(",")
                elif not isinstance(config[key], value_type):
                    if isinstance(value_type, tuple):
                        print_type = stylus.type2str(value_type[0])
                    else:
                        print_type = stylus.type2str(value_type)
                    raise ValueError(f'The value of "{key}" must be of type {print_type}')
                # check if the value of the config is allowed
                if ('choice' in config_format[key]) and (config[key] not in config_format[key]['choice']):
                    raise ValueError('The value of "{}" must be one of the followings: {}'.format(
                                     key, str(config_format[key]['choice']).strip('[]')))
            else:
                if config_format[key]['required']:
                    raise ValueError('The required item "{}" is missing from the configuration'.format(key))
                # fill in default config if not specified
                if 'default' in config_format[key]:
                    cls.stdout.info('INFO: Added the item "{}" with default value {} to the configuration'.format(
                                     key, str(config_format[key]['default'])))
                    validated_config[key] = config_format[key]['default']
        for key in config:
            if key not in config_format:
                raise ValueError(f'unknown item "{key}" found in the configuration') 
        return validated_config        
    
    def create(self, **args):
        args = self._validate_arguments(**args)
        return self._configure(action='create', **args)
        
    def recreate(self, **args):
        args = self._validate_arguments(**args)
        return self._configure(action='recreate', **args)
        
    def update(self, **args):
        args = self._validate_arguments(**args)
        config_name = args['name']
        config_path = self.get_config_path(config_name)
        if not os.path.exists(config_path):
            raise FileNotFoundError(f'cannot update file {config_path}. File does not exist.')        
        old_config = self.load_config(config_name)
        new_config = {k:v for k,v in args.items() if v is not None}
        updated_config = {**old_config, **new_config}
        return self._configure(action='update', **updated_config)
    
    def _configure(self, action:Union[ConfigAction, str], **args):
        config_name = args.pop('name')      
        config = self._validate(args)
        self._name = config_name
        self._config = config
        return config
    
    def save(self, name=None, config=None, action:Union[ConfigAction, str]='create'):
        if (name is None) and (config is None):
            name = self._name
            config = self._config
        if name is None: 
            raise ValueError('configuration name undefined')
        config_dir = self.get_config_dir()
        if not os.path.exists(config_dir):
            os.makedirs(config_dir)
        config_path = self.get_config_path(name)
        action = ConfigAction.parse(action)
        if (os.path.exists(config_path)) and (action==ConfigAction.CREATE):
            self.stdout.error(f'ERROR: {self._CONFIG_DISPLAY_NAME_.title()} configuration "{config_path}" '
                              'already exists. If you want to overwrite, use "recreate" or "update" instead.')
        else:
            with open(config_path, 'w') as config_file:
                json.dump(config, config_file, indent=2)
            action_str = ConfigAction.to_str(action, tense="past").title()
            self.stdout.info(f'INFO: {action_str} {self._CONFIG_DISPLAY_NAME_} configuration {config_path}')
            self.show(name)