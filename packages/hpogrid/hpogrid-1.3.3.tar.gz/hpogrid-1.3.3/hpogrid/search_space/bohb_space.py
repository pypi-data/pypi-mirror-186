import math

from .base_space import BaseSpace

class BOHBSpace(BaseSpace):

    def __init__(self, search_space=None):
        self.library = 'bohb'
        super().__init__(search_space)    
        
    def reset_space(self):
        import ConfigSpace as CS
        self.search_space = CS.ConfigurationSpace(seed=1)    

    def append(self, space_value):
        self.search_space.add_hyperparameter(space_value)

    def categorical(self, label, categories, grid_search = False):
        if grid_search != False:
            raise ValueError(f'{self.library} does not allow grid search')
        import ConfigSpace.hyperparameters as CSH
        return CSH.CategoricalHyperparameter(name=label, choices=categories)

    def uniformint(self, label, low, high):
        import ConfigSpace.hyperparameters as CSH
        return CSH.UniformIntegerHyperparameter(name=label, lower=low, upper=high)

    def uniform(self, label, low, high):
        import ConfigSpace.hyperparameters as CSH
        return CSH.UniformFloatHyperparameter(name=label, lower=low, upper=high)

    def quniform(self, label, low, high, q):
        import ConfigSpace.hyperparameters as CSH
        return CSH.UniformFloatHyperparameter(name=label, lower=low, upper=high, q=q)

    def qloguniform(self, label, low, high, q, base=math.e):
        if base != math.e:
            raise ValueError(f'{self.library} only allows base e for qloguniform')
        import ConfigSpace.hyperparameters as CSH
        return CSH.UniformFloatHyperparameter(name=label, lower=low, upper=high, q=q, log=True)

    def loguniform(self, label, low, high, base=math.e):
        if base != math.e:
            raise ValueError(f'{self.library} only allows base e for loguniform')
        import ConfigSpace.hyperparameters as CSH
        return CSH.UniformFloatHyperparameter(name=label, lower=low, upper=high, log=True)

    def normal(self, label, mu, sigma):
        import ConfigSpace.hyperparameters as CSH
        return CSH.NormalFloatHyperparameter(name=label, mu=mu, sigma=sigma)

    def qnormal(self, label, mu, sigma, q):
        import ConfigSpace.hyperparameters as CSH
        return CSH.NormalFloatHyperparameter(name=label, mu=mu, sigma=sigma, q=q)

    def qlognormal(self, label, mu, sigma, q, base=math.e):
        import ConfigSpace.hyperparameters as CSH
        if base != math.e:
            raise ValueError(f'{self.library} only allows base e for qlognormal')
        return CSH.NormalFloatHyperparameter(name=label, mu=mu, sigma=sigma, q=q, log=True)

    def fixed(self, label, value):
        import ConfigSpace.hyperparameters as CSH
        return CSH.CategoricalHyperparameter(name=label, choices=[value])
