class PBTScheduler():
    
    def __init__(self):
        self.scheduler = None
        
    def create(self, metric, mode, space, **args):
        from hpogrid.search_space import PBTSpace
        search_space = PBTSpace(space).search_space
        from ray.tune.schedulers import PopulationBasedTraining
        self.scheduler = PopulationBasedTraining(
            metric=metric, 
            mode=mode, 
            hyperparam_mutations = search_space,
            **args)
        return self.scheduler