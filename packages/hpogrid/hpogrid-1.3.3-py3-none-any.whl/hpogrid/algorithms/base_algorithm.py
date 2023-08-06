from abc import ABC, abstractmethod
from typing import Dict, Optional, Tuple

class BaseAlgorithm():
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        self.metric = metric
        self.mode = mode
        self.search_space = search_space
        self.optimizer = None
        self.algorithm = None
    
    @abstractmethod
    def _get_algorithm(self, max_concurrent:int=None, **args):
        pass
    
    @abstractmethod
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        pass
    
    def create(self, max_concurrent:int=None, restore_points:Optional[Tuple]=None, **args):
        algorithm = self._get_algorithm(**args)
        # restore search points
        if restore_points:
            self._restore_search_points(algorithm, restore_points)
        # limit max concurrency
        if algorithm and max_concurrent:
            from ray.tune.suggest import ConcurrencyLimiter
            algorithm = ConcurrencyLimiter(algorithm, max_concurrent=max_concurrent)
        self.algorithm = algorithm
        
        return algorithm