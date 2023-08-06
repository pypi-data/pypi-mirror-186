class BOHBHyperBandScheduler():
    
    def __init__(self):
        self.scheduler = None
        
    def create(self, metric, mode, **args):
        from ray.tune.schedulers import HyperBandForBOHB
        self.scheduler = HyperBandForBOHB(metric=metric, mode=mode, **args)
        return self.scheduler
