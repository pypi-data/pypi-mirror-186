import itertools
from typing import List, Dict

from .base_generator import Generator

class GridGenerator(Generator):
    def get_searcher(self, search_space:Dict, metric:str, mode:str, **args):
        labels = list(search_space)
        # check that all samplings methods are categorical
        for label in labels:
            if search_space[label]['method'] != 'categorical':
                raise ValueError('Search space must be defined by categorical values for grid search')
        category_combinations = [search_space[label]['dimension']['categories'] for label in labels]
        
        search_points = list(set(itertools.product(*category_combinations)))
        self.labels = labels
        return search_points

    def _tell(self, searcher, point:Dict, value):
        # search point values
        value = tuple([point[label] for label in self.labels])
        if value in searcher:
            searcher.remove(value)

    def _ask(self, searcher, n_points:int =None):
        points = []
        if n_points > len(searcher):
            n_points = len(searcher)
        for i in range(n_points):
            points.append({ k:v for k,v in zip(self.labels, searcher[i])})
        return points