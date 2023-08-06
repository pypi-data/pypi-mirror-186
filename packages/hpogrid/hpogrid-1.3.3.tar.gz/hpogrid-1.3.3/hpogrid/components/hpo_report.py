import os
import sys
import copy
import json

import pandas as pd
from tabulate import tabulate

from hpogrid.core.defaults import *
from .validation import validate_job_metadata

kSupportedExtraColumns = ['site', 'task_time_s', 'time_s', 'taskid', 'start_timestamp',
                         'start_datetime','end_datetime']

class HPOReport():
    def __init__(self, data=None, verbose=True):
        self.verbose = verbose
        self.reset()
        if data:
            self.append(data)

    def reset(self):
        self.attrib = {}
        self.data = []

    def set_primary(self, data):
        self.attrib['project_name'] = data['project_name']
        self.attrib['hyperparameters'] = data['hyperparameters']
        self.attrib['metric'] = data['metric']
        self.attrib['mode'] = data['mode']
        if self.verbose:
            print('INFO: Setting up HPO report with the following attributes')
            print('Project Name     : {project_name} \n'
                  'Hyperparameters  : {hyperparameters}\n'
                  'Metric           : {metric}\n'
                  'Mode             : {mode}'.format(**self.attrib))

    def check_consistency(self, data):
        if not validate_job_metadata(data):
            if self.verbose:
                print('ERROR: Invalid format for HPO result summary. '
                    'Result summary will be skipped')
            return False

        if not self.data:
            self.set_primary(data)

        if (data['project_name'] != self.attrib['project_name']):
            if self.verbose:
                print('INFO: Expecting HPO project name "{}" but "{}" is received. '
                    'Result summary will be skipped.')
            return False
        ####################################################################################### 
        if (set(self.attrib['hyperparameters']) != set(data['hyperparameters'])):
            if self.verbose:
                print('INFO: Inconsistent hyperparameter space. '
                        'Result summary will be skipped.')
            return False
        #######################################################################################
        if (self.attrib['metric'] != data['metric']) or (self.attrib['mode'] != data['mode']):
            if self.verbose:
                print('INFO: Inconsistent metric definition. '
                    'Result summary will be skipped.')
            return False
        return True

    def append(self, data, extras=None):
        if isinstance(data, str):
            data = json.load(open(data))
        if not isinstance(data, list):
            data = [data]
        for d in data:
            if not self.check_consistency(d):
                return None
            keys_to_save = ['start_datetime', 'start_timestamp',
                            'end_datetime', 'task_time_s', 'best_config', 'result']
            result = {key: d[key] for key in keys_to_save}
            if extras:
                for key in extras:
                    result[key] = extras[key]
            self.data.append(result)

    def _check_data(self):
        if not self.data:
            print('ERROR: No HPO results to report.')
            return False
        return True

    @classmethod
    def from_json(cls, fname, verbose=True):
        with open(fname, 'r') as json_file:
            data = json.load(json_file)
        return cls(data, verbose)
    
    @classmethod
    def from_summary(cls, fname, verbose=True):
        with open(fname, 'r') as json_file:
            data = json.load(json_file)
        instance = cls()
        instance.data = data.pop('jobs', None)
        instance.attrib = data
        return instance

    def merge_data(self, extra_columns=None, skip_time=True,
                   metric_min=None, metric_max=None, sort_by_metric=True):
        merged_data = []
        for data in self.data:
            for index in data['result']:
                result = copy.deepcopy(data['result'][index])
                merged_data.append(result)
        if extra_columns:
            extras = []
            for data in self.data: 
                for index in data['result']:
                    extras.append({col: data[col] for col in extra_columns})
            for data, extra in zip(merged_data, extras):
                data.update(extra)
        if skip_time:
            for data in merged_data:
                data.pop('time_s')
                data.pop("timestamp", None)
        df = pd.DataFrame(merged_data)
        
        if self.attrib['mode'] == 'min':
            sort_ascending = True
        elif self.attrib['mode'] == 'max':
            sort_ascending = False
        
        if sort_by_metric:
            df = df.sort_values(by=self.attrib['metric'] , ascending=sort_ascending).reset_index(drop=True)
        if metric_min is not None:
            df = df[df[self.attrib['metric']] > metric_min]
        if metric_max is not None:
            df = df[df[self.attrib['metric']] < metric_max]
        merged_data = df.to_dict('records')
        return merged_data

    def to_summary(self, fname, indent=2):
        if not self._check_data():
            return None
        report = self.attrib
        report['jobs'] = self.data
        with open(fname, 'w') as file:
            json.dump(report, file, indent=indent)

    def to_json(self, fname, extra_columns=None, skip_time=True, 
                metric_min=None, metric_max=None, indent=2):
        if not self._check_data():
            return None
        data = self.merge_data(extra_columns, skip_time, 
                               metric_min=metric_min,
                               metric_max=metric_max)
        with open(fname, 'w') as output:
            json.dump(data, output, indent=indent)

    def to_dataframe(self, extra_columns=None, skip_time=True, metric_min=None, 
                     metric_max=None, sort_by_metric=True):
        if not self._check_data():
            return None        
        data = self.merge_data(extra_columns, skip_time, 
                               metric_min=metric_min,
                               metric_max=metric_max,
                               sort_by_metric=sort_by_metric)
        df = pd.DataFrame(data)
        return df

    def to_mlflow(self, extra_columns=None, skip_time=True,
                 metric_min=None, metric_max=None):
        if not self._check_data():
            return None
        from mlflow.tracking import MlflowClient
        client = MlflowClient()
        experiment_id = client.create_experiment(self.attrib['project_name'])
        hyperparameters = self.attrib['hyperparameters']
        metric = self.attrib['metric']
        
        if not extra_columns:
            extra_columns = ['start_timestamp']
        elif 'start_timestamp' not in extra_columns:
            extra_columns.append('start_timestamp')
        merged_data = self.merge_data(extra_columns, skip_time=False, 
                                       metric_min=metric_min,
                                       metric_max=metric_max)
        for data in merged_data:
            start_time = int(data['start_timestamp']*1000)
            end_time = int((data['start_timestamp']+data['time_s'])*1000)
            run = client.create_run(experiment_id, start_time=start_time)
            run_id = run.info.run_id
            for hp in hyperparameters:
                client.log_param(run_id, hp, data[hp])
            client.log_metric(run_id, metric, data[metric])
            client.set_terminated(run_id, end_time=end_time)
            
    def to_html(self, fname=None, extra_columns=None, skip_time=True,
               metric_min=None, metric_max=None):
        if not self._check_data():
            return None
        df = self.to_dataframe(extra_columns, skip_time,
                               metric_min=metric_min,
                               metric_max=metric_max)                               
        html_text = df.to_html()
        if fname:
            with open(fname, 'w') as outfile:
                outfile.write(html_text)
        return html_text

    def to_parallel_coordinate_plot(self, fname=None, extra_columns=None, skip_time=True,
                                   metric_min=None, metric_max=None):
        if not self._check_data():
            return None
        import hiplot as hip
        merged_data = self.merge_data(extra_columns, skip_time, 
                                       metric_min=metric_min,
                                       metric_max=metric_max)

        html_text = hip.Experiment.from_iterable(merged_data).to_html()
        if fname:
            with open(fname, 'w') as outfile:
                outfile.write(html_text)
        return html_text

    def to_csv(self, fname, extra_columns=None, skip_time=True,
               metric_min=None, metric_max=None):
        if not self._check_data():
            return None
        df = self.to_dataframe(extra_columns, skip_time, 
                               metric_min=metric_min,
                               metric_max=metric_max)
        csv = df.to_csv(fname, encoding='utf-8')
        return csv

    def show(self, extra_columns=None, skip_time=True, metric_min=None, metric_max=None):
        if not self._check_data():
            return None
        df = self.to_dataframe(extra_columns, skip_time, metric_min=metric_min,
                               metric_max=metric_max)
        print(tabulate(df, showindex=True, headers=df.columns, tablefmt="psql",stralign='center'))