from typing import Dict, Tuple

from hpogrid.search_space import BOHBSpace
from .base_algorithm import BaseAlgorithm

class BOHBAlgorithm(BaseAlgorithm):
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)
        
    def _get_algorithm(self, **args):
        
        search_space = BOHBSpace(self.search_space).search_space
        
        from ray.tune.suggest.bohb import TuneBOHB
        algorithm = TuneBOHB(search_space, metric=self.metric, mode=self.mode, **args)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import BOHBGenerator
        generator = BOHBGenerator(search_space=self.search_space,
                                  metric=self.metric, mode=self.mode)
        generator.searcher = algorithm.bohber
        
        generator.feed(restore_points[0], restore_points[1])    