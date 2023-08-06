import os
import sys
import json
from typing import List, Dict
import numpy as np

from hpogrid.core.defaults import kDefaultGenerator, kDefaultMetric, kDefaultMetricMode, GeneratorMethod
from hpogrid.utils.helper import NpEncoder
from hpogrid.components import AbstractObject

class SteeringIDDS(AbstractObject):
    
    def __init__(self, verbosity:str="INFO"):
        super().__init__(verbosity=verbosity)

    def get_generator(self, space:Dict, metric:str=kDefaultMetric, mode:str=kDefaultMetricMode,
                      lib:str=kDefaultGenerator, **args):
        _lib = GeneratorMethod.parse(lib)
        if _lib == GeneratorMethod.NEVERGRAD:
            from hpogrid.generators import NeverGradGenerator
            return NeverGradGenerator(space, metric, mode, **args)
        elif _lib == GeneratorMethod.SKOPT:
            from hpogrid.generators import SkOptGenerator
            return SkOptGenerator(space, metric, mode, **args)
        elif _lib == GeneratorMethod.HYPEROPT:
            from hpogrid.generators import HyperOptGenerator
            return HyperOptGenerator(space, metric, mode, **args)
        elif _lib == GeneratorMethod.AX:
            from hpogrid.generators import AxGenerator
            return AxGenerator(space, metric, mode, **args)
        elif _lib == GeneratorMethod.BOHB:
            from hpogrid.generators import BOHBGenerator
            return BOHBGenerator(space, metric, mode, **args) 
        elif _lib == GeneratorMethod.GRID:
            from hpogrid.generators import GridGenerator
            return GridGenerator(space, metric, mode, **args)
        elif _lib == GeneratorMethod.OPTUNA:
            from hpogrid.generators import OptunaGenerator
            return OptunaGenerator(space, metric, mode, **args)         
        else:
            raise ValueError(f'Generator from library {lib} is not supported')

    def validate_idds_input(self, idds_input):
        '''
        old format
        {"points": [[{hyperparameter_point_1}, <loss_or_None>], ..., [{hyperparameter_point_N}, <loss_or_None>]], "opt_space": <opt space>}
        new format
        {"points": [[[<model_id_1>, {hyperparameter_point_1}], <loss_or_None>], ..., [[<model_id_N>, {hyperparameter_point_N}], <loss_or_None>]], "opt_space": ["model_id": <model_id>, "search_space": <search_space>]}
        '''
        keys = ['points', 'opt_space']
        # check main keys
        for key in keys:
            if key not in idds_input:
                raise KeyError('Key {} not found in idds input.'
                    ' Please check idds input format'.format(key))
        if not isinstance(idds_input['points'], List):
            raise ValueError('idds should have the data structure: Dict[List[...]]')

        for point in idds_input['points']:
            if not isinstance(point, List):
                raise ValueError('idds should have the data structure: Dict[List[List[...]]]')
            
            if (not isinstance(point[0], Dict)) and (not (isinstance(point[0], List) and isinstance(point[0][0], int) and isinstance(point[0][1], Dict))):
                raise ValueError('idds should have the data structure: Dict[List[List[Dict, Value]]] or Dict[List[List[List[int, Dict], Value]]]')
        # old format
        if isinstance(idds_input['opt_space'], Dict):
            return 1
        # new format
        elif isinstance(idds_input['opt_space'], List):
            for search_space in idds_input['opt_space']:
                if not isinstance(search_space, Dict):
                    raise ValueError('idds search space should be a dictionary not {}'.format(type(search_space)))
            return 2
        else:
            raise ValueError('invalid format for idds opt_space')

    def parse_idds_input(self, file):
        if not file:
            return None

        with open(file,'r') as input_file:
            idds_data = json.load(input_file)
            
        idds_format = self.validate_idds_input(idds_data)
        
        # old format
        if idds_format == 1:
            points = []
            results = []
            pending = 0
            input_data = idds_data['points']
            for data in input_data:
                point, result = data[0], data[1]
                points.append(point)
                results.append(result)
            search_space = idds_data.get('opt_space', None)
            return (points, results, search_space)
        
        elif idds_format == 2:
            model_results = {}
            for opt_space in idds_data.get('opt_space', []):
                model_id = opt_space.get('model_id', None)
                search_space = opt_space.get('search_space', None)
                if model_id is None:
                    raise ValueError('cannot extract model id from idds opt space')
                model_results[model_id] = {}
                model_results[model_id]['search_space'] = search_space
                model_results[model_id]['points'] = []
                model_results[model_id]['results'] = []
            for data in idds_data.get('points', []):
                model_id = data[0][0]
                if model_id not in model_results:
                    raise ValueError(f'missing search space definition for model id: {model_id}')
                point, result = data[0][1], data[1]
                model_results[model_id]['points'].append(point)
                model_results[model_id]['results'].append(result)
            return model_results
        else:
            raise RuntimeError('Failed to parse idds input')
    
    def generate_points(self, search_space, n_point, metric=kDefaultMetric, mode=kDefaultMetricMode,
                        lib=kDefaultGenerator, max_point=None, points=None,
                        results=None, **args):
        
        if not search_space:
            raise RuntimeError('search space is not specified in either idds input or '
            'through command line argument')
        
        # create generator
        generator = self.get_generator(search_space, metric, mode, lib, **args)

        n_evaluated = 0
        n_pending = 0

        # feed evaluated points
        if points and results:
            generator.feed(points=points, results=results)
            self.stdout.info(f'INFO: Fed the following results to the {lib} optimizer')
            generator.show(points=points, results=results)
            n_pending = results.count(None)
            self.stdout.info(f'INFO: There are {n_pending} point(s) pending.')
            generator.show_pending(points=points, results=results)
            n_evaluated = len(points) 

        # determine number of points to generate
        max_point = 9999 or max_point
        n_remaining = max_point - n_evaluated 
        if n_remaining < 0:
            raise ValueError('there are already more evaluated points than the'
            ' maximum points to generate for idds workflow')
        if n_point - n_pending <= 0:
            self.stdout.info('INFO: There are more points pending than the number of points to generate. '
                             'No new points will be generated.')
            return []
        
        n_generate = min(n_point-n_pending, n_remaining)

        # generate points
        new_points = generator.ask(n_generate)
        if GeneratorMethod.parse(lib) == GeneratorMethod.NEVERGRAD:
            extra_text = f" ({generator.searcher.name})"
        else:
            extra_text = ""
        self.stdout.info(f'INFO: Generated {n_generate} new points using the library {lib}{extra_text}')
        generator.show(new_points)

        return new_points

    def run_generator(self, space, n_point, metric=kDefaultMetric,
                      mode=kDefaultMetricMode, lib=kDefaultGenerator, max_point=None,
                      infile=None, outfile=None, **args):
        
        parsed_data = self.parse_idds_input(infile)
        
        # case no input points
        if parsed_data is None:
            if not space:
                raise ValueError('search space can not be empty')
            with open(space, 'r') as space_input:
                search_space = json.load(space_input)
            new_points = self.generate_points(search_space=search_space, n_point=n_point,
                                             metric=metric, mode=mode,
                                             lib=lib, max_point=max_point, **args)
        # old format
        elif isinstance(parsed_data, tuple):
            points, results, search_space = parsed_data[0], parsed_data[1], parsed_data[2]
            new_points = self.generate_points(search_space=search_space, n_point=n_point,
                                             metric=metric, mode=mode,
                                             lib=lib, max_point=max_point, 
                                             points=points, results=results, **args)
        elif isinstance(parsed_data, dict):
            new_points = []
            for model_id in parsed_data:
                self.stdout.info(f'Starting point generation for model ID: {model_id}')
                data = parsed_data[model_id]
                points, results, search_space = data["points"], data["results"], data["search_space"]
                model_specific_new_points = self.generate_points(search_space=search_space, n_point=n_point,
                                                                metric=metric, mode=mode,
                                                                lib=lib, max_point=max_point, 
                                                                points=points, results=results, **args)
                for point in model_specific_new_points:
                    new_points.append(tuple([model_id, point]))

        # save output
        if outfile:
            with open(outfile, 'w') as out:
                json.dump(new_points, out, indent=2, cls=NpEncoder)