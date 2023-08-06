class AsyncHyperBandScheduler():
    
    def __init__(self):
        self.scheduler = None
        
    def create(self, metric, mode, **args):
        from ray.tune.schedulers import AsyncHyperBandScheduler
        self.scheduler = AsyncHyperBandScheduler(metric=metric, mode=mode, **args)
        return self.scheduler
