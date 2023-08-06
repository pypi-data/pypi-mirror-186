from copy import deepcopy
from enum import Enum
from typing import Union, Optional

class GeneralEnum(Enum):
    @classmethod
    def parse(cls, expr:str):
        if isinstance(expr, cls):
            return expr
        _expr = expr.strip().upper()
        if _expr in cls.__members__:
            return cls[_expr]
        else:
            options = list(cls.__members__)
            raise RuntimeError(f"invalid option: {expr} (allowed options: {', '.join(options)})")
    @classmethod
    def get_members(cls):
        return [i.lower() for i in cls.__members__]
    

class RunMode(GeneralEnum):
    LOCAL = 0
    GRID  = 1
    IDDS  = 2

            
class ConfigType(GeneralEnum):
    BASE         = 0
    PROJECT      = 1
    HPO          = 2
    SEARCH_SPACE = 3
    MODEL        = 4
    GRID         = 5

class ConfigAction(GeneralEnum):
    NONE     = 0
    LIST     = 1
    SHOW     = 2
    REMOVE   = 3
    CREATE   = 4
    RECREATE = 5
    UPDATE   = 6
    
    @staticmethod
    def to_str(value, tense:str="past"):
        if value == ConfigAction.CREATE:
            if tense == "past":
                return "created"
            elif tense == "cont":
                return "creating"
        elif value == ConfigAction.RECREATE:
            if tense == "past":
                return "recreated"
            elif tense == "cont":
                return "recreating"
        elif value == ConfigAction.UPDATE:
            if tense == "past":
                return "udpated"
            elif tense == "cont":
                return "updating"
        return value

class GeneratorMethod(GeneralEnum):
    GRID      = 0
    SKOPT     = 1
    NEVERGRAD = 2
    HYPEROPT  = 3
    AX        = 4
    BOHB      = 5
    OPTUNA    = 6
    
class SchedulerType(GeneralEnum):
    ASYNCHYPERBAND = 0
    BOHBHYPERBAND  = 1
    PBT            = 2
    
class SearchSpaceType(GeneralEnum):
    AX        = 0
    BOHB      = 1
    HYPEROPT  = 2
    NEVERGRAD = 3
    PBT       = 4
    SKOPT     = 5
    TUNE      = 6
    OPTUNA    = 7
    
class AlgorithmType(GeneralEnum):
    AX        = 0
    BOHB      = 1
    HYPEROPT  = 2
    NEVERGRAD = 3
    SKOPT     = 4
    TUNE      = 5
    RANDOM    = 6
    GRID      = 7
    BAYESIAN  = 8
    OPTUNA    = 9

kProjectConfigNameJson = 'config.json'
kProjectConfigNameYaml = 'config.yaml'

kiDDSConfigName = 'idds_config.json'
kiDDSSearchSpaceName = 'search_space.json'
kiDDSHPinput = 'input.json'
kiDDSHPoutput = 'output.json'
kiDDSMetrics = "metrics.tgz"

#####################################################
##############    Paths Related      ################
#####################################################

# user config paths relative to userdata/
kConfigPaths = {
    ConfigType.PROJECT      : 'projects',
    ConfigType.HPO          : 'hpo',
    ConfigType.SEARCH_SPACE : 'search_space',
    ConfigType.MODEL        : 'model',
    ConfigType.GRID         : 'grid'
}

kDockerBasePath = '/workDir'
kiDDSBasePath = kDockerBasePath
kGridSiteWorkDir = '/srv/workDir/'
kDefaultProxyPath = '/etc/pki/tls/cert.pem'

#####################################################
############    Grid Site Related      ##############
#####################################################

kGPUSiteNGPU = {
    'ANALY_MANC_GPU_TEST': 10, #single queue, no submission parameters, 1 GPU per job
    'ANALY_QMUL_GPU_TEST': 6, # GPUNumber=x for now is hardcoded in the dev APF JDL,number of GPUs per job limited by cgroups, K80=2*K40, so total of 6 gpu slots avalable.
    'ANALY_MWT2_GPU': 8, #single queue, no submission parameters, 1 GPU per job
    'ANALY_BNL_GPU_ARC': 12, #also shared with Jupyter users who have priority
    'ANALY_INFN-T1_GPU': 2 #single queue, no submission parameters, 1 GPU per job
}

kDefultGridSiteType  = ['analysis', 'unified']
kDefaultGridSiteInfo = ['state', 'status', 'maxinputsize', 'maxmemory', 'maxtime', 'corecount', 'corepower']

#########################################################
#############    Configuration Defaults    ##############
#########################################################

kDefaultContainer = '/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest'
kDefaultContainer2 = '/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/clcheng/hyperparameter-optimization-on-the-grid:latest'
kDefaultiDDSContainer = 'gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest'
kDefaultContainer4 = 'docker://gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:base'

kSearchAlgorithms = AlgorithmType.get_members()
kDefaultSearchAlgorithm = 'random'

kAlgoMap = {
    'random': 'tune',
    'bayesian': 'hyperopt'
}

kSchedulers = SchedulerType.get_members()
kDefaultScheduler = 'asynchyperband'

kGenerators = GeneratorMethod.get_members()
kDefaultGenerator = 'nevergrad'
kDefaultMetric = 'loss'
kMetricMode = ['min', 'max']
kDefaultMetricMode = 'min'
kDefaultTrials = 100
kDefaultMaxConcurrent = 3
kDefaultStopping = {'training_iteration': 1}
kDefaultResource = {"cpu": 0, "gpu": 0}
kDefaultLogDir = None
kDefaultVerbosity = 0
kDefaultGridExtraParam  = {}
kDefaultSchedulerParam  = None
kDefaultAlgorithmParam  = None
kDefaultModelParam      = {}

kDefaultOutDS = 'user.${{RUCIO_ACCOUNT}}.hpogrid.{HPO_PROJECT_NAME}.out.$(date +%Y%m%d%H%M%S)'

kDefaultExtraColumns = []


kSearchSpaceFormat = {
    'categorical': {
        'categories' : { 'type': list, 'required': True},
        'grid_search' : { 'type': int, 'required': False, 'default': 0}
    },
    'uniform': {
        'low': { 'type': (float, int), 'required': True},
        'high': { 'type': (float, int), 'required': True}
    },
    'uniformint': {
        'low': { 'type': int, 'required': True},
        'high': { 'type': int, 'required': True}
    },
    'quniform': {
        'low': { 'type': (float, int), 'required': True},
        'high': { 'type': (float, int), 'required': True},
        'q': { 'type': (float, int), 'required': True}
    },
    'loguniform': {
        'low': { 'type': (float, int), 'required': True},
        'high': { 'type': (float, int), 'required': True},
        'base': { 'type': (float, int), 'required': False}
    },
    'qloguniform': {
        'low': { 'type': (float, int), 'required': True},
        'high': { 'type': (float, int), 'required': True},
        'q': { 'type': (float, int), 'required': True},
        'base': { 'type': (float, int), 'required': False}
    },
    'normal': {
        'mu': { 'type': (float, int), 'required': True},
        'sigma': { 'type': (float, int), 'required': True}
    },
    'qnormal': {
        'mu': { 'type': (float, int), 'required': True},
        'sigma': { 'type': (float, int), 'required': True},
        'q': { 'type': (float, int), 'required': True}
    },
    'lognormal': {
        'mu': { 'type': (float, int), 'required': True},
        'sigma': { 'type': (float, int), 'required': True},
        'base': { 'type': (float, int), 'required': False}
    },
    'qlognormal': {
        'mu': { 'type': (float, int), 'required': True},
        'sigma': { 'type': (float, int), 'required': True},
        'base': { 'type': (float, int), 'required': False},
        'q': { 'type': (float, int), 'required': True}
    },
    'fixed': {
        'value': { 'type': None, 'required': True}
    }
}

kConfigFormat = {
    ConfigType.PROJECT:{
        'project_name': {
            'required': True,
            'type': str
        },
        'scripts_path': {
            'abbr': 'p',
            'description': 'Path to the location of training scripts ' +\
                           ' (or the directory containing the training scripts)',
            'required': True,
            'type': str
        },
        'model_config': {
            'abbr': 'm',
            'description': 'Name of the model configuration to use',
            'required': True,
            'type': dict
        },
        'search_space': {
            'abbr': 's',
            'description': 'Name of the search space configuration to use',
            'required': True,
            'type':dict
        },
        'hpo_config': {
            'abbr': 'o',
            'description': 'Name of the hpo configuration to use',
            'required': True,
            'type':dict
        },
        'grid_config': {
            'abbr': 'g',
            'description': 'Name of the grid configuration to use',
            'required': True,
            'type':dict
        }        
    },
    ConfigType.HPO:{
        'algorithm': {
            'abbr': 'a',
            'description': 'Algorithm for hyperparameter optimization',
            'required': False,
            'type': str,
            'choice': kSearchAlgorithms,
            'default': kDefaultSearchAlgorithm
        },
        'scheduler': {
            'abbr': 's',
            'description': 'Trial scheduling method for hyperparameter optimization',
            'required': False,
            'type': str,
            'choice': kSchedulers,
            'default': kDefaultScheduler
        },        
        'metric' : {
            'abbr': 'm',
            'description': 'Evaluation metric to be optimized',
            'required': False,
            'type': str,
            'default': kDefaultMetric
        },
        'extra_metrics': {
            'abbr': 'e',
            'description': 'Additional metrics to be saved during the training (separated by commas)',
            'required': False,
            'type': (list, type(None)),
            'default': None
        },
        'mode' : {
            'abbr': 'o',
            'description': 'Mode of optimization (either "min" or "max")',
            'required': False,
            'type': str,
            'choice': kMetricMode,
            'default': kDefaultMetricMode
        },
        'resource': {
            'abbr': 'r',
            'description': 'A json decodable string defining the resource allocated to each trial, use all cpu and gpu by default',
            'required': False,
            'type': (dict, type(None)),
            'default': deepcopy(kDefaultResource)
        },
        'num_trials': {
            'abbr': 'n',
            'description': 'Number of trials (search points) to run',
            'required': True,
            'type': int,
        },
        'log_dir': {
            'abbr': 'l',
            'description': 'Directory for saving Ray Tune logs, default is /tmp/',
            'required': False,
            'type': (str, type(None)),
            'default': kDefaultLogDir
        },
        'verbose': {
            'abbr': 'v',
            'description': 'Verbosity level of Ray Tune',
            'required': False,
            'type': int,
            'default': kDefaultVerbosity
        },
        'max_concurrent': {
            'abbr': 'c',
            'description': 'Maximum number of trials to be run concurrently',
            'required': False,
            'type': int,
            'default': kDefaultMaxConcurrent
        },
        'stop': {
            'abbr': None,
            'description': 'A json decodable string defining the stopping criteria for the training',
            'required': False,
            'type': dict,
            'default': deepcopy(kDefaultStopping)
        },
        'scheduler_param': {
            'abbr': None,
            'description': 'A json decodable string defining the extra parameters given to the trial scheduler',
            'required': False,
            'type': (dict, type(None)),
            'default': None
        },
        'algorithm_param': {
            'abbr': None,
            'description': 'A json decodable string defining the extra parameters given to the hyperparameter optimization algorithm',
            'required': False,
            'type': (dict, type(None)),
            'default': None
        }
    },
    ConfigType.GRID: {
        'site': {
            'abbr': 's',
            'description': 'Name of the grid site(s) to where the jobs are submitted',
            'required': False,
            'type': (list, str, type(None)),
            'default': None
        },
        'container': {
            'abbr': 'c',
            'description': 'Name of the docker or singularity container in which the jobs are run',
            'required': False,
            'type': str,
            'default': kDefaultContainer
        },
        'inDS': {
            'abbr': 'i',
            'description': 'Name of (rucio) input dataset', 
            'required': False,
            'type': (str, type(None)),
            'default': None
        },
        'outDS': {
            'abbr': 'o',
            'description': 'Name of output dataset',
            'required': False,
            'type': str,
            'default': kDefaultOutDS
        },            
        'retry': {
            'abbr': 'r',
            'description': 'Check to enable retrying faild jobs',
            'required': False,
            'type': (bool, int),
            'default': 0
        },
        'extra': {
            'abbr': 'e',
            'description': 'Extra options passed to panda command',
            'required': False,
            'type': dict,
            'default': deepcopy(kDefaultGridExtraParam)
        }
    },
    ConfigType.MODEL:{
        'script': {
            'abbr': 's',
            'description': 'Name of the training script where the function or class that defines'+\
                           ' the training model will be called to perform the training',
            'required': True,
            'type': str
        },
        'model': {
            'abbr': 'm',
            'description': 'Name of the function or class that defines the training model',
            'required': True,
            'type': str
        },
        'param': {
            'abbr': 'p',
            'description': 'Extra parameters to be passed to the training model',
            'required': False,
            'type': dict,
            'default': deepcopy(kDefaultModelParam)
        }
    },
    ConfigType.SEARCH_SPACE:{
        'search_space': {
            'abbr': 's',
            'description': 'A json decodable string defining the search space',
            'required': True,
            'type': dict,
        }
    }
}

kHPOGridMetadataFormat = ['task_time_s', 'start_timestamp', 'project_name', 
                          'result', 'hyperparameters', 'metric', 'start_datetime', 
                          'best_config', 'best_metric_score', 'end_datetime', 'mode']

kGridSiteMetadataFileName = 'userJobMetadata.json' #jobReport.json

#########################################################
###############    PanDA Tasks Related    ###############
#########################################################

kPanDATaskOutputColumns = ['jeditaskid', 'status', 'taskname', 'computingsite', 'site', 'metastruct']