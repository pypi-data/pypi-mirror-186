from hpogrid.core.defaults import ConfigType
from hpogrid.configuration import ConfigurationBase

class ModelConfiguration(ConfigurationBase):
    _CONFIG_TYPE_ = ConfigType.MODEL
    _CONFIG_DISPLAY_NAME_ = 'model'
    _LIST_COLUMNS_ = ['Model Configuration']