import os

from ray.tune import Trainable

from hpogrid.core import environment_settings as es
from hpogrid.utils.helper import cd

class CustomModel(Trainable):
    
    def initialize(self, config):
        raise NotImplementedError('the "initialize" method must be overriden for initializing the train model.')
        
    def setup(self, config):
        workdir = es.get_workdir()
        with cd(workdir) as _:
            self.initialize(config)