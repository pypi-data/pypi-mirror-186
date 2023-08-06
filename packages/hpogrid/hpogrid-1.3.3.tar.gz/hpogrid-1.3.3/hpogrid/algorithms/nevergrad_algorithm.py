from typing import Dict, Tuple

from hpogrid.search_space import NeverGradSpace
from .base_algorithm import BaseAlgorithm

class NeverGradAlgorithm(BaseAlgorithm):
    
    kDefaultBudget = 100
    kDefaultMethod = "RandomSearch"
    
    def __init__(self, metric:str, mode:str, search_space:Dict):
        super().__init__(metric=metric, mode=mode, search_space=search_space)

    def _get_algorithm(self, **args):
        
        search_space = NeverGradSpace(self.search_space).get_search_space()
        
        method = args.pop('method', self.kDefaultMethod)
        import nevergrad as ng
        optimizer = ng.optimizers.registry[method](
                parametrization=search_space, budget=self.kDefaultBudget)
        
        from ray.tune.suggest.nevergrad import NevergradSearch
        algorithm = NevergradSearch(optimizer, None, metric=self.metric, mode=self.mode, **args)
        
        return algorithm
    
    def _restore_search_points(self, algorithm, restore_points:Tuple):
        from hpogrid.generators import NeverGradGenerator
        generator = NeverGradGenerator(search_space=self.search_space,
                                       metric=self.metric, mode=self.mode)
        generator.searcher = algorithm._nevergrad_opt
        
        generator.feed(restore_points[0], restore_points[1])    