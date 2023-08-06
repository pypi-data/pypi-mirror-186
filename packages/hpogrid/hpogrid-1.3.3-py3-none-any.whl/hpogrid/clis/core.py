import json

import click

from hpogrid.core.defaults import *

class ListOption(click.Option):
    def type_cast_value(self, ctx, value):
        if isinstance(value, str):
            return [i.strip() for i in value.split(',') if i.strip()]
        return value
    
class DictOption(click.Option):
    def type_cast_value(self, ctx, value):
        if isinstance(value, str):
            return json.loads(value)
        return value    
    
@click.command(name='generate')
@click.option('-l', '--lib', default=kDefaultGenerator, type=click.Choice(kGenerators, case_sensitive=False),
              help='optimization library to use', show_default=True)
@click.option('-s', '--space', required=True, 
              help='json file containing search space definition')
@click.option('-n', '--n_point', type=int, required=True, 
              help='number of search points to generate')
@click.option('-m', '--max_point', type=int, default=None, 
              help='(iDDS only) maximum number of points to generate in entire iDDS workflow')
@click.option('--metric', default=kDefaultMetric, 
              help='evaluation metric', show_default=True)
@click.option('--mode', default=kDefaultMetricMode, type=click.Choice(kMetricMode, case_sensitive=False),
              help='evaluation mode', show_default=True)
@click.option('-i', '--infile', default=None,
              help='(iDDS only) iDDS input')
@click.option('-o', '--outfile', default=None,
              help='(iDDS only) iDDS output')
@click.option('--method', default=None,
              help='(nevergrad library only) optimizer type')
def generate(**kwargs):
    """
    Generate hyperparameter search points
    """
    from hpogrid.interface.idds.steering import SteeringIDDS
    SteeringIDDS().run_generator(**kwargs)
    
@click.command(name='idds_log', short_help='Tool for retrieving iDDS logs')
@click.argument('ID', type=int)
def idds_log(**kwargs):
    """
    Tool for retrieving iDDS logs
    
    ID: JEDI task ID for the iDDS job
    """
    from hpogrid.interface.main import download_log
    kwargs['workload_id'] = kwargs.pop('id')
    download_log(**kwargs)
    
@click.command(name='sites')
@click.option('-n', '--name', default=None, 
              help='filter grid site by name')
@click.option('--gpu_sites/--all_sites', 'gpu', default=True, 
              help='show gpu sites only or all sites', show_default=True)
@click.option('--active/--all_status', default=True, 
              help='show active sites only or sites with any status', show_default=True)
@click.option('-t', '--site_type', default=kDefultGridSiteType, cls=ListOption,
              help='filter sites by type', show_default=True)
@click.option('-i', '--info', default=kDefaultGridSiteInfo, cls=ListOption, 
              help='list of site info to show, separated by commas', show_default=True)
def display_sites(**kwargs):
    """
    Show available grid sites
    """
    from hpogrid.components import GridSiteInfo
    GridSiteInfo.show(**kwargs)