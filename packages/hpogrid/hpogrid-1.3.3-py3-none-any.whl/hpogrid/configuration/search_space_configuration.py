import json
from copy import deepcopy
from json import JSONDecodeError

from hpogrid.utils.stylus import type2str
from hpogrid.core.defaults import kSearchSpaceFormat
from hpogrid.configuration import ConfigurationBase

class SearchSpaceConfiguration(ConfigurationBase):
    _CONFIG_TYPE_ = 'search_space'
    _CONFIG_DISPLAY_NAME_ = 'search space'
    _LIST_COLUMNS_ = ['Search Space Configuration']

    @classmethod
    def validate(cls, config):
        if 'search_space' in config:
            search_space = deepcopy(config['search_space'])
        else:
            search_space = config
        # if attribute type is dict, parse string input as dict
        if isinstance(search_space, str):
            try:
                search_space = json.loads(search_space)
            except JSONDecodeError:
                raise RuntimeError('ERROR: Cannot decode the value of "search_space" as dictionary.'
                    'Please check your input.')        
        config_format = kSearchSpaceFormat
        sampling_methods = list(config_format)
        kHPKeys = set(['method', 'dimension'])
        for hp in search_space:
            if (not isinstance(search_space[hp], dict)) or (set(search_space[hp].keys()) != kHPKeys):
                raise ValueError('Each hyperparameter must be defined by a dictionary containing the keys "method" and "dimension"')
            if not isinstance(search_space[hp]['dimension'], dict):
                raise ValueError('Dimension of a hyperparameter must be a dictionary containing the parameters of its sampling method')
            method = search_space[hp]['method']
            # check if hyperparameter sampling method is supported
            if method not in sampling_methods:
                raise ValueError('Sampling method "{}" is not supported. '
                                 'Supported methods are: {}'.format(method,','.join(sampling_methods)))
            for arg in config_format[method]:
                if arg in search_space[hp]['dimension']:
                    # check if the argument type of the sampling method is correct
                    value_type = config_format[method][arg]['type']
                    if not isinstance(search_space[hp]['dimension'][arg], value_type):
                        raise ValueError('The value of argument "{}" for the sampling method '
                                         '"{}" (for hyperparameter "{}") must be of type {}'.format(
                                         arg, method, hp, type2str(value_type)))
                else:
                    # check if a required argument for the sampling method is missing
                    if (config_format[method][arg]['required']):
                        raise ValueError('Missing argument "{}" for the sampling method "{}" '
                                         'for the hyperparameter "{}"'.format(arg, method, hp))
                    # set the argument to its default value if not specified
                    if ('default' in config_format[method][arg]):
                        cls.stdout.info('Info: The argument "{}" for the sampling method "{}" for'
                                        ' the hyperparameter "{}" will be set to its default value {}'.format(
                                        arg, method, hp, config_format[method][arg]['default']))
                        search_space[hp]['dimension'][arg] = config_format[method][arg]['default']

        return search_space