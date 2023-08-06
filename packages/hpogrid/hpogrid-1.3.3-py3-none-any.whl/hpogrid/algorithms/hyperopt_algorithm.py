from typing import Dict, Tuple

from hpogrid.search_space import HyperOptSpace
from .base_algorithm import BaseAlgorithm

class HyperOptAlgorithm(BaseAlgorithm):
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)
        
    def _get_algorithm(self, **args):
        
        search_space = HyperOptSpace(self.search_space).search_space
        
        from ray.tune.suggest.hyperopt import HyperOptSearch
        algorithm = HyperOptSearch(search_space, metric=self.metric, mode=self.mode, **args)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import HyperOptGenerator
        generator = HyperOptGenerator(search_space=self.search_space,
                                metric=self.metric, mode=self.mode)
        generator.domain = algorithm.domain
        generator.trials = algorithm._hpopt_trials
        generator.rstate = algorithm.rstate
        
        generator.feed(restore_points[0], restore_points[1])