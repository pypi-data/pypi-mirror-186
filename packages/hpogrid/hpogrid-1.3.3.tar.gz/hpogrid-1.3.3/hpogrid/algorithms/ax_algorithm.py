from typing import Dict, Tuple

from hpogrid.search_space import AxSpace
from .base_algorithm import BaseAlgorithm

class AxAlgorithm(BaseAlgorithm):
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)

    def _get_algorithm(self, **args):
        
        search_space = AxSpace(self.search_space).get_search_space()
        
        kwargs = {**args}
        if 'enforce_sequential_optimization' not in kwargs:
            kwargs['enforce_sequential_optimization'] = False
        if 'verbose_logging' not in kwargs:
            kwargs['verbose_logging'] = False

        from ray.tune.suggest.ax import AxSearch
        algorithm = AxSearch(search_space, metric=self.metric, mode=self.mode, **kwargs)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import AxGenerator
        generator = AxGenerator(search_space=self.search_space,
                                metric=self.metric, mode=self.mode)
        generator.searcher = algorithm._ax
        
        generator.feed(restore_points[0], restore_points[1])