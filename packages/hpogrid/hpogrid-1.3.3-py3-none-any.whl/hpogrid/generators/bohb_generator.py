import copy
from typing import List, Dict

from .base_generator import Generator
from hpogrid.search_space.bohb_space import BOHBSpace

class BOHBGenerator(Generator):
    
    kDefaultBudget = 100

    def get_searcher(self, search_space:Dict, metric:str, mode:str, **args):
        
        search_space = BOHBSpace(search_space).get_search_space()
        
        from hpbandster.optimizers.config_generators.bohb import BOHB
        searcher = BOHB(search_space)
        
        return searcher

    def _ask(self, searcher, n_points:int = None):
        points = []
        for _ in range(n_points):
            point, info = searcher.get_config(None)
            points.append(copy.deepcopy(point))
        return points

    def _tell(self, searcher, point:Dict, value:float):
        value = self._to_metric_values(value)
        result = BOHBResultWrapper(point, self.signature * value)
        searcher.new_result(result)

class BOHBResultWrapper():
    
    def __init__(self, config:Dict, loss:float, budget:int=BOHBGenerator.kDefaultBudget):
        self.result = {"loss": loss}
        self.kwargs = {"budget": budget, "config": config.copy()}
        self.exception = None