import math

from .base_space import BaseSpace

class HyperOptSpace(BaseSpace):
    def __init__(self, search_space=None):
        self.library = 'hyperopt'
        super().__init__(search_space)

    def reset_space(self):
        self.search_space = {}
        
    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search=False):
        if grid_search != False:
            raise ValueError(f'{self.library} does not allow grid search')
        from hyperopt import hp
        return (label, hp.choice(label, categories))

    def uniformint(self, label, low, high):
        from hyperopt import hp
        return (label, hp.uniformint(label, low, high))

    def uniform(self, label, low, high):
        from hyperopt import hp
        return (label, hp.uniform(label, low, high))

    def quniform(self, label, low, high, q):
        return (label, hp.uniform(label, low, high, q))

    def loguniform(self, label, low, high, base = math.e):
        if base != math.e:
            raise ValueError(f'{self.library} search space only allows base e for loguniform sampling')
        from hyperopt import hp
        return (label, hp.loguniform(label, math.log(low), math.log(high)))

    def qloguniform(self, label, low, high, q, base=math.e):
        if base != math.e:
            raise ValueError(f'{self.library} search space only allows base e for qloguniform sampling')
        from hyperopt import hp
        return (label, hp.qloguniform(label, math.log(low), math.log(high)), q)

    def normal(self, label, mu, sigma):
        from hyperopt import hp
        return (label, hp.normal(label, mu, sigma))

    def qnormal(self, label, mu, sigma, q):
        from hyperopt import hp
        return (label, hp.normal(label, mu, sigma, q))

    def lognormal(self, label, mu, sigma, base):
        if base != math.e:
            raise ValueError(f'{self.library} search_space only allows base e for lognormal sampling')
        from hyperopt import hp
        return (label, hp.lognormal(label, mu, sigma))

    def qlognormal(self, label, mu, sigma, q, base=math.e):
        if base != math.e:
            raise ValueError(f'{self.library} search_space only allows base e for qlognormal sampling')
        from hyperopt import hp
        return (label, hp.qlognormal(label, mu, sigma, q))

    def fixed(self, value):
        return (label, value)
