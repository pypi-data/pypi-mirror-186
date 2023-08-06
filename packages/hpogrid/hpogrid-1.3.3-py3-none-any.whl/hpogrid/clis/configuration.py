from copy import deepcopy

import click
from click import Option, Argument

from hpogrid.core.defaults import *
from .core import ListOption, DictOption

config_params = {
    ConfigType.HPO: [
        Argument(('NAME',)),
        Option(('-a', '--algorithm',), default=kDefaultSearchAlgorithm,
               type=click.Choice(kSearchAlgorithms, case_sensitive=False),
               help=kConfigFormat[ConfigType.HPO]['algorithm']['description'], show_default=True),
        Option(('-s', '--scheduler',), default=kDefaultScheduler,
               type=click.Choice(kSchedulers, case_sensitive=False),
               help=kConfigFormat[ConfigType.HPO]['scheduler']['description'], show_default=True),
        Option(('-m', '--metric',), default=kDefaultMetric,
               help=kConfigFormat[ConfigType.HPO]['metric']['description'], show_default=True),
        ListOption(('-e', '--extra_metrics',), default=kDefaultMetric,
               help=kConfigFormat[ConfigType.HPO]['extra_metrics']['description'], show_default=True),
        Option(('-o', '--mode',), default=kDefaultMetricMode,
               type=click.Choice(kMetricMode, case_sensitive=False),
               help=kConfigFormat[ConfigType.HPO]['mode']['description'], show_default=True),
        DictOption(('-r', '--resource',), default=None, 
               help=kConfigFormat[ConfigType.HPO]['resource']['description']),
        Option(('-n', '--num_trials',), type=int, required=True,
               help=kConfigFormat[ConfigType.HPO]['num_trials']['description']),
        Option(('-l', '--log_dir',), default=None,
               help=kConfigFormat[ConfigType.HPO]['log_dir']['description']),
        Option(('-v', '--verbose',), default=0, type=int,
               help=kConfigFormat[ConfigType.HPO]['verbose']['description'], show_default=True),
        Option(('-c', '--max_concurrent',), type=int, default=kDefaultMaxConcurrent,
               help=kConfigFormat[ConfigType.HPO]['max_concurrent']['description'], show_default=True),
        DictOption(('--stop',), default=kDefaultStopping,
               help=kConfigFormat[ConfigType.HPO]['stop']['description'], show_default=True),
        DictOption(('--scheduler_param',), default=None,
               help=kConfigFormat[ConfigType.HPO]['scheduler_param']['description']),
        DictOption(('--algorithm_param',), default=None,
               help=kConfigFormat[ConfigType.HPO]['algorithm_param']['description'])
    ],
    ConfigType.GRID:[
        Argument(('NAME',)),
        ListOption(('-s', '--site',), default=None,
               help=kConfigFormat[ConfigType.GRID]['site']['description']),
        Option(('-c', '--container',), default=kDefaultContainer,
               help=kConfigFormat[ConfigType.GRID]['container']['description'], show_default=True),
        Option(('-i', '--inDS', 'inDS',), default=None,
               help=kConfigFormat[ConfigType.GRID]['inDS']['description']),
        Option(('-o', '--outDS', 'outDS',), default=kDefaultOutDS,
               help=kConfigFormat[ConfigType.GRID]['outDS']['description'], show_default=True),
        Option(('-r', '--retry',), is_flag=True,
               help=kConfigFormat[ConfigType.GRID]['retry']['description']),
        DictOption(('-e', '--extra',), default={},
               help=kConfigFormat[ConfigType.GRID]['extra']['description'], show_default=True)
    ],
    ConfigType.MODEL:[
        Argument(('NAME',)),
        Option(('-s', '--script',), required=True,
               help=kConfigFormat[ConfigType.MODEL]['script']['description']),
        Option(('-m', '--model',), required=True,
               help=kConfigFormat[ConfigType.MODEL]['model']['description']),
        DictOption(('-p', '--param',), default={},
               help=kConfigFormat[ConfigType.MODEL]['param']['description'], show_default=True)
    ],
    ConfigType.SEARCH_SPACE:[
        Argument(('NAME',)),
        DictOption(('-s', '--search_space',), default={},
               help=kConfigFormat[ConfigType.SEARCH_SPACE]['search_space']['description'], show_default=True)
    ],
    ConfigType.PROJECT:[
        Argument(('NAME',)),
        Option(('-p', '--scripts_path',), required=True,
               help=kConfigFormat[ConfigType.PROJECT]['scripts_path']['description']),
        Option(('-m', '--model_config',), required=True,
               help=kConfigFormat[ConfigType.PROJECT]['model_config']['description']),
        Option(('-s', '--search_space',), required=True,
               help=kConfigFormat[ConfigType.PROJECT]['search_space']['description']),
        Option(('-o', '--hpo_config',), required=True,
               help=kConfigFormat[ConfigType.PROJECT]['hpo_config']['description']),
        Option(('-g', '--grid_config',), required=True,
               help=kConfigFormat[ConfigType.PROJECT]['grid_config']['description'])
    ]
}


@click.group(name='hpo_config')
@click.pass_context
def hpo_config(ctx):
    """
    Manage configuration for hyperparameter optimization
    """
    from hpogrid.configuration import HPOConfiguration
    ctx.obj = {"class": HPOConfiguration}
    

@click.group(name='grid_config')
@click.pass_context
def grid_config(ctx):
    """
    Manage configuration for grid job submission
    """
    from hpogrid.configuration import GridConfiguration
    ctx.obj = {"class": GridConfiguration}
        
    
@click.group(name='model_config')
@click.pass_context
def model_config(ctx):
    """
    Manage configuration for the machine learning model
    """
    from hpogrid.configuration import ModelConfiguration
    ctx.obj = {"class": ModelConfiguration}
    
@click.group(name='search_space')
@click.pass_context
def search_space_config(ctx):
    """
    Manage configuration for hyperparameter search space'
    """
    from hpogrid.configuration import SearchSpaceConfiguration
    ctx.obj = {"class": SearchSpaceConfiguration}
    
    
@click.group(name='project')
@click.pass_context
def project_config(ctx):
    """
    Manage an HPO project
    """
    from hpogrid.configuration import ProjectConfiguration
    ctx.obj = {"class": ProjectConfiguration}
    

@click.command(name='list')
@click.option("-e", "--expr", help="filter out configuration files that matches the expression")
@click.pass_context
def list_config(ctx, **kwargs):
    """
    List configuration files
    """
    cls = ctx.obj["class"]()
    cls.list(**kwargs)
    
@click.command(name='show', short_help="Display the contents of a configuration file")
@click.argument("NAME")
@click.pass_context
def show_config(ctx, **kwargs):
    """
    Display the contents of a configuration file
    
    NAME: Name of the configuration file
    """    
    cls = ctx.obj["class"]()
    cls.show(**kwargs)    
    
@click.command(name='remove', short_help="Remove configuration file(s)")
@click.argument("NAME")
@click.pass_context
def remove_config(ctx, **kwargs):
    """
    Remove configuration file(s)
    
    NAME: Name of the configuration file (accept wildcard)
    """ 
    
    cls = ctx.obj["class"]()
    cls.remove(**kwargs)
    
@click.command(name='where', short_help="Display the path of a configuration file")
@click.argument("NAME")
@click.pass_context
def locate_config(ctx, **kwargs):
    """
    Display the path of a configuration file
    
    NAME: Name of the configuration file
    """    
    cls = ctx.obj["class"]()
    cls.locate(**kwargs)
    
@click.pass_context 
def create_config(ctx, **kwargs):
    """
    Create a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.create(**kwargs)
    cls.save(action=ConfigAction.CREATE)
    
@click.pass_context
def update_config(ctx, **kwargs):
    """
    Update a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.update(**kwargs)
    cls.save(action=ConfigAction.UPDATE)
    
@click.pass_context
def recreate_config(ctx, **kwargs):
    """
    Recreate a configuration file
    
    NAME: Name of the configuration file
    """
    cls = ctx.obj["class"]()
    cls.recreate(**kwargs)
    cls.save(action=ConfigAction.RECREATE)
    
for gp in [hpo_config, grid_config, model_config, search_space_config, project_config]:
    gp.add_command(list_config)
    gp.add_command(show_config)
    gp.add_command(remove_config)
    gp.add_command(locate_config)
    
for gp, params in [(hpo_config, config_params[ConfigType.HPO]),
                   (grid_config, config_params[ConfigType.GRID]),
                   (model_config, config_params[ConfigType.MODEL]),
                   (search_space_config, config_params[ConfigType.SEARCH_SPACE]),
                   (project_config, config_params[ConfigType.PROJECT])]:
    cmd_create = click.Command('create', callback=create_config, params=params, 
                               short_help="Create a configuration file")
    cmd_update = click.Command('update', callback=update_config, params=deepcopy(params),
                               short_help="Update a configuration file")
    cmd_recreate = click.Command('recreate',  callback=recreate_config, params=params,
                                 short_help="Recreate a configuration file")
    for param in cmd_update.params:
        if isinstance(param, click.Option):
            param.required = False
            param.default = None
    gp.add_command(cmd_create)
    gp.add_command(cmd_update)
    gp.add_command(cmd_recreate)