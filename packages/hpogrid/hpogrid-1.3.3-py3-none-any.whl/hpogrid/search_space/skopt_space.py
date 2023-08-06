from .base_space import BaseSpace

class SkOptSpace(BaseSpace):

    def __init__(self, search_space=None):
        self.library = 'skopt'
        super().__init__(search_space)    

    def reset_space(self):
        self.search_space = []

    def append(self, space_value):
        self.search_space.append(space_value)

    def categorical(self, label, categories, grid_search = False):
        if grid_search != False:
            raise ValueError(f'{self.library} does not allow grid search')
        from skopt.space import Categorical
        return Categorical(name=label, categories=categories)

    def uniformint(self, label, low, high):
        from skopt.space import Integer
        return Integer(name=label, low=low, high=high, prior="uniform")

    def uniform(self, label, low, high):
        from skopt.space import Real
        return Real(name=label, low=low, high=high, prior='uniform')

    def loguniform(self, label, low, high, base=10):
        from skopt.space import Real
        return Real(name=label, low=low, high=high, prior='log-uniform', base=base)

    def loguniformint(self, label, low, high, base=10):
        from skopt.space import Integer
        return Integer(name=label, low=low, high=high, prior="log-uniform", base=base)

    def fixed(self, label, value):
        return self.categorical(label=label, categories=[value])
    
    @staticmethod
    def transform(search_points, reference=None):
        if not isinstance(search_points, list):
            search_points = [search_points]
        sp_hyperparams = list(search_points[0])
        if not all(set(sp_hyperparams)==set(sp) for sp in search_points):
            raise ValueError('Inconsistent list of hyperparamters among'
                             ' search points')
        if reference and (set(reference) != set(sp_hyperparams)):
            raise ValueError('Inconsistent hyperparamters between search points'
                             ' and search space')
        # always respect the order of reference search space
        hyperparameters = list(reference) if reference else sp_hyperparams
        initial_points = []
        for sp in search_points:
            initial_points.append([sp[hp] for hp in hyperparameters])
        return initial_points