from hpogrid.core.defaults import ConfigType
from hpogrid.configuration import ConfigurationBase

class HPOConfiguration(ConfigurationBase):
    _CONFIG_TYPE_ = ConfigType.HPO
    _CONFIG_DISPLAY_NAME_ = 'HPO'
    _LIST_COLUMNS_ = ['HPO Configuration']