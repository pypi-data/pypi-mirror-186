import os
import click

from hpogrid.core.defaults import *

from hpogrid.clis.core import ListOption

@click.group(name='tasks')
def manage_tasks(**kwargs):
    """
    Monitor grid jobs
    """
    pass

@manage_tasks.command(name='show')
@click.option('-u', '--username', default=None, 
              help='filter tasks by username')
@click.option('-l', '--limit', type=int, default=1000,
              help='maximum number of tasks to query', show_default=True)
@click.option('-d', '--days', type=int, default=30,
              help='filter tasks within the last N days', show_default=True)
@click.option('-n', '--taskname', default=None,
              help='filter tasks by taskname (accept wildcards)')
@click.option('-r', '--range', 'taskid_range', default=None,
              help='filter tasks by jeditaskid range')
@click.option('-i', '--jeditaskid', default=None,
              help='only show the task with the specified jeditaskid (accept wildcards)')
@click.option('-m', '--metadata', is_flag=True,
              help='print out the metadata of a task')
@click.option('-s', '--status', cls=ListOption, default=[],
              help='filter tasks by task status, separated by commas, '
              'e.g. running,finished,done')
@click.option('--sync', is_flag=True,
              help='force no caching on the PanDA server')
@click.option('-o', '--outname', default=None,
              help='output result with the filename if specified')
@click.option('-c', '--outcol', cls=ListOption, default=kPanDATaskOutputColumns,
              help='data columns to be saved in output, seperated by commas')
def show_task(**kwargs):
    """
    Show an overview of task status
    """
    from hpogrid.interface.panda import PandaTaskManager
    PandaTaskManager(skip_pbook=True).show(**kwargs)
    
@manage_tasks.command(name='kill', short_help="Kill a PanDA task")
@click.argument('ID', type=int)
def kill_task(**kwargs):
    """
    Kill a task
    
    ID: JEDI task ID
    """
    from hpogrid.interface.panda import PandaTaskManager
    kwargs['task_id'] = kwargs.pop('id')
    PandaTaskManager().kill(**kwargs)

@manage_tasks.command(name='retry', short_help="Retry a PanDA task")
@click.argument('ID', type=int)
def retry_task(**kwargs):
    """
    Retry a task
    
    ID: JEDI task ID
    """    
    from hpogrid.interface.panda import PandaTaskManager
    kwargs['task_id'] = kwargs.pop('id')
    PandaTaskManager().retry(**kwargs)
    
@manage_tasks.command(name='kill_and_retry', short_help="Kill and retry a PanDA task")
@click.argument('ID', type=int)
def kill_and_retry_task(**kwargs):
    """
    Kill and retry a task
    
    ID: JEDI task ID
    """      
    from hpogrid.interface.panda import PandaTaskManager
    kwargs['task_id'] = kwargs.pop('id')
    PandaTaskManager().killAndRetry(**kwargs)

    
@click.command(name='run', short_help='Run an HPO task')
@click.argument('INPUT')
@click.option('-p', '--search_points', default=None,
              help='A json file containing the manual search points to run')
@click.option('-m', '--mode', default='local', type=click.Choice(['local', 'grid', 'idds'], case_sensitive=False),
              help='Platform for running hyperparameter optimization', show_default=True)
def run_tasks(**kwargs):
    """
    Run an HPO task
    
    INPUT: Name of project / Path to a project configuration file    
    """
    kwargs['source'] = kwargs.pop('input')    
    from hpogrid.components import HPOTask
    job = HPOTask.load(**kwargs)
    job.run() 
    
@click.command(name='submit', short_help='Submit an HPO task to the grid/idds',
               context_settings=dict(ignore_unknown_options=True, allow_extra_args=True,))
@click.argument('INPUT')
@click.option('-n', '--n_jobs', type=int, default=1,
              help='number of (repeated) jobs to submit', show_default=True)
@click.option('-s', '--site', default=None,
              help='site to submit the job to '
            '(this will override the grid config site setting)')
@click.option('-t', '--time', type=int, default=-1,
              help='same as maxCpuCount in prun which specifies the maximum cpu time'
                   ' for a job (prevent being killed by looping job detection)', show_default=True)
@click.option('-m', '--mode', type=click.Choice(['grid', 'idds'], case_sensitive=False), default='grid',
              help='mode for job submission', show_default=True)
@click.option('-p', '--search_points', default=None,
              help='json file containing a list of '
                   'search points to evaluate (for non-idds jobs only)')
@click.option('-d', '--debug', is_flag=True,
              help='activate debug mode')
@click.option('--scripts_path', default=None,
              help='path to the training script or directory containing the training scripts')
@click.pass_context
def submit_tasks(ctx, **kwargs):
    """
    Submit an HPO task to the grid/idds
    
    INPUT: Name of project / Path to a project configuration file
    """
    kwargs['config_input'] = kwargs.pop('input')
    from hpogrid import GridHandler
    GridHandler().submit(**kwargs, extra=ctx.args)
    
    
@click.command(name='report_grid')
@click.argument('project_name')
@click.option('-l', '--limit', type=int, default=1000,
              help='maximum number of tasks to query', show_default=True)
@click.option('-d', '--days', type=int, default=30,
              help='filter tasks within the last N days', show_default=True)
@click.option('-n', '--taskname', default=None,
              help='filter tasks by taskname (accept wildcards)')
@click.option('-r', '--range', 'taskid_range', default=None,
              help='filter tasks by jeditaskid range')
@click.option('-e', '--extra', 'extra_columns', default='',
              help='extra data columns (separated by commas) to be displayed and saved. '
                   'Available options: site, task_time_s, time_s, taskid, start_timestamp, '
                   'start_datetime, end_datetime', show_default=True)
@click.option('--summary', is_flag=True, 
              help='save a complete hpo result summary as a json file')
@click.option('--to_json', is_flag=True,
              help='output result to a json file')
@click.option('--to_html', is_flag=True,
              help='output result to an html file')
@click.option('--to_csv', is_flag=True,
              help='output result to a csv file')
@click.option('--to_pcp', is_flag=True,
              help='output result as a parallel coordinate plot')
@click.option('--to_mlflow', is_flag=True,
              help='output result as an mlflow tracker directory')
@click.option('-o', '--outname', default='hpo_result',
              help='output file name (excluding extension)', show_default=True)
@click.option('--min', 'metric_min', type=float, default=None,
              help='filter results by minimum value of metric')
@click.option('--max', 'metric_max', type=float, default=None,
              help='filter results by maximum value of metric')        
def report_grid(**kwargs):
    """
    Display a report of an HPO task that ran on grid
    """
    from hpogrid.interface.panda import PandaTaskReport
    kwargs['extra_columns'] = [i.strip() for i in kwargs['extra_columns'].split(',') if i.strip()]
    PandaTaskReport().display(**kwargs)
    
@click.command(name='report')
@click.option('-e', '--extra', 'extra_columns', default='',
              help='extra columns to included (separated by comma)')
@click.option('--min', 'metric_min', type=float, default=None,
              help='filter results by minimum value of metric')
@click.option('--max', 'metric_max', type=float, default=None,
              help='filter results by maximum value of metric')
@click.argument('filename')     
def report(**kwargs):
    """
    Display a report of an HPO task that ran locally
    """
    from hpogrid.components import HPOReport
    filename = kwargs.pop('filename')
    if not os.path.exists(filename):
        raise FileNotFoundError(f"input file {filename} does not exist")
    report  = HPOReport.from_json(filename)
    kwargs['extra_columns'] = [i.strip() for i in kwargs['extra_columns'].split(',') if i.strip()]
    report.show()