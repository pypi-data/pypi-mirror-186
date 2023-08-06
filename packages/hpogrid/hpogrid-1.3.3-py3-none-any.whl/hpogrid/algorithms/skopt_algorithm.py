from typing import Dict, Tuple

from hpogrid.search_space import SkOptSpace
from .base_algorithm import BaseAlgorithm

class SkOptAlgorithm(BaseAlgorithm):
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)
        
    def _get_algorithm(self, **args):
        
        search_space = SkOptSpace(self.search_space).search_space
        
        from skopt import Optimizer
        optimizer = Optimizer(search_space)
        labels = [hp.name for hp in search_space]
        
        from ray.tune.suggest.skopt import SkOptSearch
        algorithm = SkOptSearch(optimizer, labels, metric=self.metric, mode=self.mode, **args)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import SkOptGenerator
        generator = SkOptGenerator(search_space=self.search_space,
                                   metric=self.metric, mode=self.mode)
        generator.searcher = algorithm._skopt_opt
        
        generator.feed(restore_points[0], restore_points[1])