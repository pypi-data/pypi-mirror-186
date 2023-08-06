import copy
from typing import Optional, List, Dict

from .base_generator import Generator
from hpogrid.search_space import OptunaSpace

class OptunaGenerator(Generator):
    
    def get_searcher(self, search_space:Dict, metric:str, mode:str, seed:Optional[int]=None, **args):
        import optuna as ot

        search_space = OptunaSpace(search_space).get_search_space()
        
        if mode == 'max':
            direction = "maximize"
        elif mode == 'min':
            direction = "minimize"
        else:
            raise ValueError('mode of evaluation metric can only be "min" or "max"')

        pruner  = ot.pruners.NopPruner()
        storage = ot.storages.InMemoryStorage()
        sampler = ot.samplers.TPESampler(seed=seed)

        study = ot.study.create_study(storage=storage, sampler=sampler,
                                      pruner=pruner, study_name=None,
                                      load_if_exists=True, direction=direction)
        
        self._space = search_space
        
        return study

    def _tell(self, searcher, point:Dict, value):
        import optuna as ot
        trial = ot.trial.create_trial(state=ot.trial.TrialState.COMPLETE,
                                      value=value, params=point,
                                      distributions=self._space,
                                      intermediate_values=None)
        searcher.add_trial(trial)

    def _ask(self, searcher, n_points:int =None):
        points = []
        for _ in range(n_points):
            trial = searcher.ask(fixed_distributions=self._space)
            point = trial.params
            points.append(copy.deepcopy(point))
        return points