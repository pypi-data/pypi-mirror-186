from hpogrid._version import __version__
from hpogrid.core.decorators import *

import os
import pathlib

module_path = pathlib.Path(__file__).parent.absolute()
resource_path = os.path.join(module_path, "resources")
userdata_path = os.path.join(module_path, "userdata")

from hpogrid.utils.io import  VerbosePrint
stdout = VerbosePrint("INFO")

from hpogrid.core.environment_settings import get_datadir, get_workdir