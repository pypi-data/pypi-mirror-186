import os
import sys
import json
from typing import Optional, List, Dict

from ray.tune import Callback

class TuneCallback(Callback):
    
    def custom_setup(self, hyperparameters:Optional[List]=None, metrics:Optional[List]=None, cache_dir:Optional[str]=None, **info):
        
        self._hpogrid_hyperparameters = hyperparameters
        self._hpogrid_metrics = metrics
        self._hpogrid_cache_dir = cache_dir
        
    def get_trial_info(self, trial: "Trial"):
        try:
            name = trial.trainable_name
            pid  = trial._get_default_result_or_future()['pid']
        except:
            name = "?????"
            pid  = "?????"
        return {"name": name, "pid": pid}
    
    def get_msg_prefix(self, trial: "Trial", pid:Optional[int]=None):
        trial_info = self.get_trial_info(trial)
        if pid is not None:
            trial_info['pid'] = pid
        msg_prefix = f"({trial_info['name']} pid={trial_info['pid']})"
        return msg_prefix
    
    def format_message(self, text:str, prefix:str, fill_space:bool=False):
        prefix_str = prefix if not fill_space else " "*len(prefix)
        text = f"\033[36m{prefix_str}\033[0m {text}"
        return text
        
    def on_trial_start(self, iteration: int, trials: List["Trial"],
                       trial: "Trial", **info):
        if self._hpogrid_hyperparameters:
            prefix = self.get_msg_prefix(trial)
            sys.stdout.write(self.format_message("Hyperparameters: \n", prefix))
            for name in self._hpogrid_hyperparameters:
                if name in trial.config:
                    value = trial.config[name]
                    sys.stdout.write(self.format_message(f"\t{name} = {value}\n", prefix))

    def on_trial_result(self, iteration, trials, trial, result, **info):

        if self._hpogrid_metrics:
            prefix = self.get_msg_prefix(trial, pid=result.get("pid", None))
            sys.stdout.write(self.format_message("Results: \n", prefix))
            for name in self._hpogrid_metrics:
                if name in result:
                    value = result[name]
                    sys.stdout.write(self.format_message(f"\t{name} = {value}\n", prefix))

        if self._hpogrid_cache_dir:
            cache_filename = f"timestamp_{result['timestamp']}_trial_{result['trial_id']}.json"
            cache_path = os.path.join(self._hpogrid_cache_dir, cache_filename)
            with open(cache_path, "w") as cache_file:
                json.dump(result, cache_file, indent=2)