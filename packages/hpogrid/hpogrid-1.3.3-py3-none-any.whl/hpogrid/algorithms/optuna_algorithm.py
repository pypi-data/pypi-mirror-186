from typing import Dict, Tuple

from hpogrid.search_space import OptunaSpace
from .base_algorithm import BaseAlgorithm

class OptunaAlgorithm(BaseAlgorithm):
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)
        
    def _get_algorithm(self, **args):
        
        search_space = OptunaSpace(self.search_space).search_space
        
        from ray.tune.suggest.optuna import OptunaSearch
        algorithm = OptunaSearch(space=search_space, metric=self.metric, mode=self.mode, **args)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import OptunaGenerator
        generator = OptunaGenerator(search_space=self.search_space,
                                    metric=self.metric, mode=self.mode)
        generator.searcher = algorithm._ot_study
        
        generator.feed(restore_points[0], restore_points[1])