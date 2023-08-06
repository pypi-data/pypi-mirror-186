from abc import ABC, abstractmethod
import copy
import json
from typing import List, Dict, Union
from functools import partial

from hpogrid.utils import stylus
from hpogrid.utils.helper import is_nan_or_inf

class Generator(ABC):
    def __init__(self, search_space:Dict, metric:str, mode:str, **args):
        self.evaluated_points = []
        self.metric = metric
        self.mode = mode
        self.search_space = search_space
        if mode == "max":
            self.signature = -1.
        elif mode == "min":
            self.signature = 1.
        self.searcher = self.get_searcher(search_space, metric, mode, **args)

    def set_searcher(self, searcher):
        self.searcher = searcher

    @abstractmethod
    def get_searcher(self, search_space:Dict, metric:str, mode:str, **args):
        pass

    @abstractmethod
    def _ask(self, searcher, n_points:int =1):
        pass

    @abstractmethod
    def _tell(self, searcher, point:Dict, result):
        pass
    
    def ask(self, n_points:int =1):
        return self._ask(self.searcher, n_points)
 
    def tell(self, point:Dict, result):
        if (result is None) or is_nan_or_inf(result):
            return None
        self._tell(self.searcher, point, result)

    def feed(self, points:List, results:List, redo=False):
        '''Feed a list of points to the generator
        '''
        assert len(points)==len(results), 'points and results must have the same length'
        if redo:
            self.clear_history()
        for point, result in zip(points, results):
            self.tell(point, result)

    def clear_history(self):
        self.searcher = self.get_searcher(self.search_space, self.metric, self.mode)

    def _to_metric_values(self, results:Union[List, Dict, float, int]):

        def extract_from_dict(data):
            if self.metric in data:
                return data[self.metric]
            else:
                raise KeyError('result should contain value for'
                ' the metric: {}'.format(self.metric))
        if isinstance(results, List):
            if all(isinstance(r, Dict) for r in results):
                return [extract_from_dict(r) for r in results]
            elif all(isinstance(r, (int, float, type(None))) for r in results):
                return results
            else:
                raise ValueError('invalid result format.')
        elif isinstance(results, Dict):
            return extract_from_dict(results)
        elif isinstance(results, (int, float)):
            return results
            
    def show(self, points:List, results:Union[List, None]=None):
        if results:
            assert len(points)==len(results), 'points and results must have the same length'
            metric_values = self._to_metric_values(results)
            data = [ {**p, self.metric:r } for p,r in zip(points, results) if r is not None]
        else:
            data = points
        table = stylus.create_table(data)
        print(table)        
        
    def show_pending(self, points:List, results:Union[List, None]=None):
        if results:
            assert len(points)==len(results), 'points and results must have the same length'
            metric_values = self._to_metric_values(results)
            data = [ p for p,r in zip(points, results) if r is None]
        else:
            data = points
        table = stylus.create_table(data)
        print(table)           