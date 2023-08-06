import sys
import json

class MLFlowLogger():

    def __init__(self, exp_name='experiment'):
        from mlflow.tracking import MlflowClient
        self.client = MlflowClient()
        self.experiment_id = self.client.create_experiment(exp_name)
        self.run_ids = []

    def new_run(self):
        run = self.client.create_run(self.experiment_id)
        self.run_ids.append(run.info.run_id)

    def log_hyperparameters(self, hp_dict, run_id=None):
        run_id = run_id or self.run_ids[-1]
        for key, value in hp_dict.items():
            self.client.log_param(run_id, key, value)

    def log_metrics(self, metric_dict, run_id=None):
        run_id = run_id or self.run_ids[-1]
        for key, value in metric_dict.items():
            if not isinstance(value, float):
                continue
            self.client.log_metric(
                run_id, key, value)

    def terminate_run(self, run_id=None):
        run_id = run_id or self.run_ids[-1]
        self.client.set_terminated(run_id)

    def run_server(self):
        from mlflow.cli import cli
        sys.argv = ['mlflow','server']
        sys.exit(cli())

    @classmethod
    def from_json(cls, file):
        with open(file,'r') as log_file:
            log = json.load(log_file)
        from hpogrid.components.validation import validate_job_metadata
        if not validate_job_metadata(log):
            raise RuntimeError('Invalid format for hpo result summary.')
        mlflow_logger = cls(log['title'])
        hyperparameters = log['hyperparameters']
        metric = log['metric']
        for i in log['result']:
            hp_dict = {hp:log['result'][i][hp] for hp in hyperparameters}
            metric_dict ={metric:log['result'][i][metric]}
            mlflow_logger.new_run()
            mlflow_logger.log_hyperparameters(hp_dict)
            mlflow_logger.log_metrics(metric_dict)
            mlflow_logger.terminate_run()
        return mlflow_logger
