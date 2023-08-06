import math
import json

class BaseSpace():

    test_space = {
        'activation' : {
            'method': 'categorical',
            'dimension': {
                'categories': ['relu', 'sigmoid'],
                'grid_search' : 0
            }
        },
        'learning_rate' : {
            'method': 'loguniform',
            'dimension': {
                'low': 1e-6,
                'high': 1e-1,
                'base': 10
            }
        },
        'batchsize': {
            'method': 'categorical',
            'dimension': {
                'categories': [64,128,256,512,1024,2048],
                'grid_search' : 0
            }
        },
        'max_depth': {
            'method': 'uniformint',
            'dimension': {
                'low': 1,
                'high': 30
            }
        },
        'subsample': {
            'method': 'uniform',
            'dimension': {
                'low': 0.1,
                'high': 1.0
            }
        }
    }

    test_space_base_e = {
        'activation' : {
            'method': 'categorical',
            'dimension': {
                'categories': ['relu', 'sigmoid'],
                'grid_search' : 0
            }
        },
        'learning_rate' : {
            'method': 'loguniform',
            'dimension': {
                'low': math.e**-11,
                'high': math.e**-6,
                'base': math.e
            }
        },
        'batchsize': {
            'method': 'categorical',
            'dimension': {
                'categories': [64,128,256,512,1024,2048],
                'grid_search' : 0
            }
        },
        'max_depth': {
            'method': 'uniformint',
            'dimension': {
                'low': 1,
                'high': 30
            }
        },
        'subsample': {
            'method': 'uniform',
            'dimension': {
                'low': 0.1,
                'high': 1.0
            }
        }
    }    

    def __init__(self, search_space = None):
        self.reset_space()
        if search_space is not None:
            self.create(search_space)


    def get_search_space(self):
        return self.search_space
    
    def reset_space(self):
        self.library = 'base'
        self.search_space = {}

    def _method_error(self, method):
        raise ValueError(f'the method {method} is not supported in {self.library}')

    def import_json(file):
        self.search_space = json.load(open(file))        
        
    def create(self,search_space = None):
        if search_space is None:
            search_space = self.search_space
        elif isinstance(search_space, str):
            search_space = json.loads(search_space)

        methods_map = {
            'categorical': self.categorical,
            'uniform': self.uniform,
            'uniformint': self.uniformint,
            'quniform': self.quniform,
            'loguniform': self.loguniform,
            'qloguniform': self.qloguniform,
            'normal': self.normal,
            'qnormal': self.qnormal,
            'lognormal': self.lognormal,
            'qlognormal': self.qlognormal,
            'fixed': self.fixed,
        }

        for hp in search_space:
            method = search_space[hp]['method']
            if method not in methods_map:
                self._method_error(method)
            space_value = methods_map[method](label = hp, **search_space[hp]['dimension'])
            if space_value is None:
                self._method_error(method)
            self.append(space_value)
        return self.search_space


    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search = False):
        '''
        returns one of the categories, which should be a list
        '''
        space_value = (label, {'method': 'categorical', 
                               'dimension': {
                                   'categories': categories,
                                   'grid_search': grid_search}})
        return space_value

    def uniformint(self, label, low, high):
        '''
        returns a random integer in the range [low, high).
        '''
        space_value = (label, {'method': 'uniformint', 
            'dimension': { 'low': low, 'high': high}})
        return space_value

    def uniform(self, label, low, high):
        '''
        returns a value uniformly distributed between low and high.
        '''
        space_value = (label, {'method': 'uniform', 
            'dimension': { 'low': low, 'high': high}})
        return space_value

    def quniform(self, label, low, high, q):
        '''
        returns a value like round(uniform(low, high) / q) * q
        '''
        space_value = (label, {'method': 'quniform', 
            'dimension': { 'low': low, 'high': high, 'q': q}})
        return space_value

    def loguniform(self, label, low, high, base):
        '''
        loguniform returns a value drawn according to power(uniform(low, high), base = base) 
        so that the logarithm of the return value is uniformly distributed
        '''
        space_value = (label, {'method': 'loguniform', 
            'dimension': { 'low': low, 'high': high, 'base': base}})
        return space_value

    def qloguniform(self, label, low, high, q, base):
        '''
        Returns a value like round(exp(uniform(low, high)) / q) * q
        '''
        space_value = (label, {'method': 'qloguniform', 
            'dimension': { 'low': low, 'high': high, 'q': q, 'base': base}})
        return space_value

    def normal(self, label, mu, sigma):
        '''
        returns a real value that's normally-distributed with mean mu and standard deviation sigma
        '''
        space_value = (label, {'method': 'normal', 
            'dimension': { 'mu': mu, 'sigma': sigma}})
        return space_value


    def lognormal(self, label, mu, sigma, base):
        '''
        returns a value drawn according to power(normal(mu, sigma), base) so that the logarithm of the 
        return value is normally distributed
        '''
        space_value = (label, {'method': 'lognormal', 
            'dimension': { 'mu': mu, 'sigma': sigma, 'base': base}})
        return space_value

    def qnormal(self, label, mu, sigma, q):
        '''
        returns a value like round(normal(mu, sigma) / q) * q
        '''
        space_value = (label, {'method': 'qnormal', 
            'dimension': { 'mu': mu, 'sigma': sigma, 'q': q}})
        return space_value

    def qlognormal(self, label, mu, sigma, q, base):
        '''
        returns a value like round(power(normal(mu, sigma), base) / q) * q
        '''
        space_value = (label, {'method': 'qlognormal', 
            'dimension': { 'mu': mu, 'sigma': sigma, 'q': q, 'base': base}})
        return space_value

    def fixed(self, value):
        '''
        returns a fixed value
        '''
        space_value = (label, {'method': 'fixed', 'dimension': value})
        return space_value
    
    @classmethod
    def transform(cls, search_points):
        if not isinstance(search_points, list):
            search_points = [search_points]
        import pandas as pd
        search_space = pd.DataFrame(search_points).to_dict('list')
        base_space = cls()
        for hp in search_space:
            base_space.append(base_space.categorical(hp, search_space[hp]))
        return base_space.search_space