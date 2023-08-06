from hpogrid.search_space.base_space import BaseSpace

class OptunaSpace(BaseSpace):

    def __init__(self, search_space=None):
        self.library = 'optuna'
        super().__init__(search_space)    

    def reset_space(self):
        self.search_space = {}

    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search=False):
        if grid_search != False:
            raise ValueError(f'{self.library} does not allow grid search')
        from optuna.distributions import CategoricalDistribution
        return (label, CategoricalDistribution(categories))

    def uniformint(self, label, low, high):
        from optuna.distributions import IntUniformDistribution
        return (label, IntUniformDistribution(low, high))

    def uniform(self, label, low, high):
        from optuna.distributions import UniformDistribution
        return (label, UniformDistribution(low, high))

    def loguniform(self, label, low, high, base=10):
        from optuna.distributions import LogUniformDistribution
        return (label, LogUniformDistribution(low, high))

    def loguniformint(self, label, low, high, base=10):
        from optuna.distributions import IntLogUniformDistribution
        return (label, IntLogUniformDistribution(low, high))

    def fixed(self, label, value):
        return self.categorical(label=label, categories=[value])
