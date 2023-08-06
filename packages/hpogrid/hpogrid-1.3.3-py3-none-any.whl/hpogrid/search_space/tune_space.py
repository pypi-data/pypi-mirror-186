import math

import numpy as np

from .base_space import BaseSpace

from hpogrid.utils.helper import old_div

class TuneSpace(BaseSpace):

    def __init__(self, search_space = None):
        self.library = 'tune'
        super().__init__(search_space)    
        

    def reset_space(self):
        self.search_space = {}

    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search = False):
        method = None
        from ray import tune
        if grid_search:
            method = tune.grid_search(categories)
        else:
            method = tune.choice(categories)
        return (label, method)

    def uniform(self, label, low, high):
        from ray import tune
        return (label, tune.uniform(low, high))
    
    def uniformint(self, label, low, high):
        from ray import tune
        return (label, tune.randint(low, high))

    def loguniform(self, label, low, high, base=10):
        from ray import tune
        return (label, tune.loguniform(low, high, base))

    def qloguniform(self, label, low, high, base=10):
        logmin = np.log(low) / np.log(base)
        logmax = np.log(high) / np.log(base)
        from ray import tune
        return (label, tune.sample_fram(lambda _: 
            np.round(old_div(base**(np.random.uniform(logmin, logmax)),q))*q))

    def quniform(self, label, low, high, q):
        from ray import tune
        return (label, tune.sample_from(lambda _: 
            np.round(old_div(np.random.uniform(low, high),q))*q))

    def quniformint(self, label, low, high, q):
        from ray import tune
        return (label, tune.sample_from(lambda _: 
            np.round(old_div(np.random.uniform(low, high),q))*q))

    def normal(self, mu, sigma):
        from ray import tune
        return (label, tune.sample_from(lambda _: sigma*np.random.randn()+mu))

    def qnormal(self, mu, sigma, q):
        from ray import tune
        return (label, tune.sample_from(lambda _: 
            np.round(old_div(sigma*np.random.randn()+mu,q))*q))

    def lognormal(self, mu, sigma, base = math.e):
        from ray import tune
        return (label, tune.sample_from(lambda _: 
            np.power(sigma*np.random.randn()+mu, base))) 

    def qlognormal(self, mu, sigma, q, base=math.e):
        from ray import tune
        return (label, tune.sample_from(lambda _: 
            np.round(old_div(np.power(sigma*np.random.randn()+mu, base),q))*q ))         

    def fixed(self, value):
        return (label, value)
                