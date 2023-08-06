from hpogrid.search_space.base_space import BaseSpace

class NeverGradSpace(BaseSpace):

    def __init__(self, search_space=None):
        self.library = 'nevergrad'
        super().__init__(search_space)    

    def reset_space(self):
        self.search_space = {}

    def get_search_space(self):
        import nevergrad as ng
        return ng.p.Instrumentation(**self.search_space)

    def append(self, space_value):
        self.search_space[space_value[0]] = space_value[1]

    def categorical(self, label, categories, grid_search = False):
        if grid_search != False:
            raise ValueError(f'{self.library} does not allow grid search')
        import nevergrad as ng
        return (label, ng.p.Choice(categories))

    def uniformint(self, label, low, high):
        import nevergrad as ng
        return (label, ng.p.Scalar(lower=low, upper=high).set_integer_casting())

    def uniform(self, label, low, high):
        import nevergrad as ng
        return (label, ng.p.Scalar(lower=low, upper=high))

    def loguniform(self, label, low, high, base=10):
        import nevergrad as ng
        return (label, ng.p.Log(lower=low, upper=high, exponent=base))

    def loguniformint(self, label, low, high, base=10):
        import nevergrad as ng
        return (label, ng.p.Log(lower=low, upper=high, exponent=base).set_integer_casting())

    def fixed(self, label, value):
        return self.categorical(label=label, categories=[value])
