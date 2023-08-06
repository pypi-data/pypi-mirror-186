from hpogrid.core.defaults import ConfigType
from hpogrid.configuration import ConfigurationBase

class GridConfiguration(ConfigurationBase):
    _CONFIG_TYPE_ = ConfigType.GRID
    _CONFIG_DISPLAY_NAME_ = 'grid'
    _LIST_COLUMNS_ = ['Grid Configuration']