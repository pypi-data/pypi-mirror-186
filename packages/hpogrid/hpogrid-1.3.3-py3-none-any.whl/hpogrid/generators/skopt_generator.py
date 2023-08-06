import copy
from typing import List, Dict

from .base_generator import Generator
from hpogrid.search_space.skopt_space import SkOptSpace

#default_method = "GP"
#methods = ["GP", "RF", "ET", "GBRT"]

class SkOptGenerator(Generator):
    def get_searcher(self, search_space:Dict, metric:str, mode:str, **args):
        search_space = SkOptSpace(search_space).get_search_space()
        from skopt import Optimizer
        searcher = Optimizer(search_space)
        self.labels = [hp.name for hp in search_space]
        return searcher

    def _ask(self, searcher, n_points:int = None):
        points = []
        points_raw = searcher.ask(n_points)
        for point_raw in points_raw:
            point = dict(zip(self.labels, point_raw))
            points.append(copy.deepcopy(point))
        return points

    def _tell(self, searcher, point:Dict, value):
        value = self._to_metric_values(value)
        x = [point[label] for label in self.labels]
        searcher.tell(x, self.signature * value)
