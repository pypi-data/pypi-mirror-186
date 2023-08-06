<img src="https://gitlab.cern.ch/clcheng/ReadmeImagery/-/raw/master/images/hpogrid/hpogrid_logo.png">


[![Python](https://img.shields.io/pypi/pyversions/hpogrid.svg?style=plastic)](https://badge.fury.io/py/hpogrid)
[![PyPI](https://badge.fury.io/py/hpogrid.svg)](https://badge.fury.io/py/hpogrid)

# Hyperparameter Optimization on the Grid
This package provides a framework for performing hyperparameter optimization (HPO) using the ATLAS grid resources. 

# Table of Contents
1.  [Basic Workflow](#basic-workflow)
2.  [Getting the code](#getting-the-code)
3.  [Setup and Installation](#setup-and-installation)
    * [Using the default conda environment](#using-the-default-conda-environment)
    * [Using singularity](#using-singularity)
    * [Inside a custom virtual environment](#inside-a-custom-virtual-environment)
4.  [Quick Start](#quick-start)
5.  [Managing Configuration Files](#managing-configuration-files)
    * [HPO Configuration](#hpo-configuration)
    * [Grid Configuration](#grid-configuration)
    * [Model Configuration](#model-configuration)
    * [Search Space onfiguration](#search-space-configuration)
6.  [Creating a Custom Project with the Configuration Files](#creating-a-custom-project-with-the-configuration-files)
    * [Create a project configuration file directly](#create-a-project-configuration-file-directly)
7.  [Adapting Training Scripts for Hyperparameter Optimization](#adapting-training-scripts-for-hyperparameter-optimization)
    * [Training model as an objective function](#method-1-training-model-as-an-objective-function)
    * [Training model as a trainable class](#method-2-training-model-as-a-trainable-class)
8.  [Running Hyperparameter Optimization Jobs](#Running-Hyperparameter-Optimization-Jobs)
9.  [Integration with iDDS Workflow](#integration-with-idds-workflow)
10. [Monitoring Job Status](#monitoring-job-status)
11. [Visualizing Hyperparamter Optimization Results](#visualizing-hyperparameter-optimization-results)
12. [Command Line Options](#command-line-options)
13. [Advanced Examples](#advanced-examples)
    * [Example Payload: PID with Recurrent Neural Networks in TRT Detector](#example-payload-pid-with-recurrent-neural-networks-in-trt-detector)
    * [Example Payload: FastCaloGAN](#example-payload-fastcalogan)
    * [Example Payload: BBYY Analysis](#example-payload-bbyy-analysis)
    * [Custom Example: CIFAR10_CNN](#custom-example-cifar10_cnn)
14. [Important Notes](#important-notes)
    * [Working Directory of Container](#working-directory-of-contaianer)
    * [Location of Input Dataset](#location-of-input-datatset)

# Basic Workflow

<img src="https://gitlab.cern.ch/clcheng/ReadmeImagery/-/raw/master/images/hpogrid/WorkflowDiagram.png" width="800">

The execution of the above hyperparameter optimization workflow can be done entirely using the _hpogrid tool_ provided by this repository. The sample usage and instruction for using the _hpogrid tool_ is given in the next few sections.

The workflow can be divided into the following steps:

**Step 1**: Prepare the configuration files for a hyperparameter optimization task which will submitted to the ATLAS grid site. A total of four configuration files are required. They are:
1. **HPO Configuration**: Configurations that define how the hyperparameter optimization is performed. Such as:
    * A search algorithm for deciding the next hyperparameter search points
    * A scheduler method for early stopping of poor performing points, relocation of resources to more promising points and so on
    * The number of hyperparameter points to be evaluated
2. **Search Space Configuration**: Configurations that define the hyperparameter search space. This includes the sampling method for a particular hyperparameter (such as uniform or normal sampling or logirthmic based uniform sampling) and its range of allowed values.
3. **Model Configuration**: Configurations that contains information of the training model that is called by the hyperparameter optimization alogrithm. This should include 
    * The name of the training script which contains the class/function defining the training model
    * The name of the class/function that defines the training model
    * The parameters that should be passed to the training model. For details please refer to the section (Adaptation of Training Script)
4. **Grid Configuration**: Configurations that define settings for grid job submission. Such as
    * The container inside which the training scripts are run
    * The names of input and output datasets
    * The name of the grid site where the hyperparameter optimization jobs are run

The above configuration files are then merged into a single configuration file called the **project configuration** which will be used for submitting grid jobs or running jobs locally. 
Alternatively, one can directly prepare the project configuration file with a specified format. For details please refer to [this section](#project-configuration).

**Step 2**: Upload the input dataset via rucio which will be retrieved by the grid site when the hyperparameter optimization task is executed.

**Step 3**: Adapt the training script(s) to conform with the format required by the hyperparameter optimization library (Ray Tune).

**Step 4**: Submit the hyperparamter optimization task and monitor its progress.

**Step 5**: Retrieve the hyperparamter optimization results after completion. The results can be output into various formats supported by the _hpogrid tool_ for visualization. 

# Getting the code
To get the code, use the following command:
```
git clone ssh://git@gitlab.cern.ch:7999/aml/hyperparameter-optimization/alkaid-qt/hpogrid/hpogrid.git
```

# Setup and Installation (within lxplus)

### Using the default conda environment

You can setup the conda environment with the necessary packages using the command (from the base path of the project):
```
source setupenv.sh
```
This will setup the default conda environment _ml-base_ which contain all necessary machine-learning packages and the latest version of ROOT.

### Using singularity

Alternatively, you may use an equivalent singularity image by typing:
```
singularity shell /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest
```

### Inside a custom virtual environment

Activate your custom environment then use the command (from the base path of the project):
```
source setupenv.sh no-conda
```
Then install the hpogrid package:
```
pip install hpogrid

```

# Quick start

* For details of how to **adapt a training script to the HPO library**, please refer to [this section](#adapting-the-training-script-for-hyperparameter-optimization)
* For details of how to **create, update, display a configuration file**, please refer to [this section](#managing-configuration-files)
* Make sure to source setupenv.sh before running the examples below

### Example 1: Optimizing a simple objective function

Given a simple [objective function](#method-1-training-model-as-an-objective-function) with the evaluation metric defined by `loss = (height - 14)**2 - abs(width - 3)` with hyperparameters `-100 < height < 100` and `0 < width < 20`. The goal is to minimize the metric `loss`.
The training script with the implementation of the above objective function can be found in `example/scripts/simple_objective.py`. 

To try out this example, simply type:
```
source examples/setup/simple_objective.sh
```

To test this example locally:
```
hpogrid run simple_objective
```

To submit a job for this example to the grid:
```
hpogrid submit simple_objective
```

### Example 2: Optimizing a simple trainable class

Given a simple [trainble class](#method-2-training-model-as-a-trainable-class) with the evaluation metric defined by the Easom function `loss = -cos(alpha)*cos(beta)*exp(-((alpha-pi)**2+(beta-pi)**2))` with hyperpraamters `-10 < alpha < 10` and `beta ∈ [-1,0,1,2,3,4]`. The goal is to minimize the metric `loss`.
The training script with the above trainable class can be found in `example/scripts/simple_trainable.py`.

To try out this example, simply type:
```
source examples/setup/simple_trainable.sh
```

To test this example locally:
```
hpogrid run simple_trainable
```

To submit a job for this example to the grid:
```
hpogrid submit simple_trainable
```



### Example 3: Optimizing a convolutional neural network for the MNIST dataset
The training script with the implementation of a convolutional neural network for the MNIST dataset (for classifying digits) can be found in `exmple/scripts/mnist.py`.

To try out this example, simply type:
```
source examples/setup/MNIST_CNN.sh
```

To test this example locally:
```
hpogrid run MNIST_CNN
```

To submit a job for this example to the grid:
```
hpogrid submit MNIST_CNN
```

# Managing Configuration Files

In general, the command for managing configuraton files takes the form:
```
hpogrid <config_type> <action> <config_name> [<options>]
```

The `<config_type>` argument specifies the type of configuration to be handled. The avaliable types are
- `hpo_config` : Configuration for hyperparamter optimization
- `grid_config` : Configuration for grid job submission
- `model_config` : Configuration for the machine learning model (which the hyperparameters are to be optimized)
- `search_space` : Configuration for the hyperparameter search space

The `<action>` argument specifies the action to be performed. The available actions are
- `create` : Create a new configuration
- `recreate` : Recreate an existing configuration (the old configuration will be overwritten)
- `update` : Update an existing configuration (the old configuration except those to be updated will be kept)
- `remove` : Remove an existing configuration
- `list` : List the name of existing configurations (the `<config_name>` argument is omitted)
- `show` : Display the content of an existing configuration

The `<config_name>` argument specifies name given to a configuration file. 

The `[<options>]` arguments specify the configuration settings for the corresponding configuration type. The available options are explained below.

* The configuration files are stored in the directory `config/`

## HPO Configuration

These are configurations that define how the hyperparameter optimization is performed. 

The command for managing hpo configuration is:

```
hpogrid hpo_config <action> <config_name> [<options>]
```

For creation, modification of the configuration file, the following options are available
 
| **Option** | **Description** | **Default** | **Choices** |
| ---------- | ---------- | ----------- | ----------- |
| `algortihm` | Algorithm for hyperparameter optimization | 'random' | 'hyperopt', 'skopt', 'bohb', 'ax', 'tune', 'random', 'bayesian' |
| `metric` | Evaluation metric to be optimized | 'accuracy' | - |
| `mode` | Optimization mode (either 'min' or 'max')| 'max' | 'max', 'min'
| `scheduler` | Trial scheduling method for hyperparameter optimization | 'asynchyperband' | 'asynchyperband', 'bohbhyperband', 'pbt' |
| `num_trials` | Number of trials (search points) | 100 | - |
| `max_concurrent` | Maximum number of trials to be run concurrently | 3 | - |
| `log_dir` | Logging directory | "./log" | - |
| `verbose` | Check to enable verbosity | False | - |
| `stop` | Stopping criteria | '{"training_iteration": 1}' | - |
| `scheduler_param` | Extra parameters for the trial scheduler | {} | - |
| `algorithm_param` | Extra parameters for hyperparameter optimization algorithm | {} | - |

* For details about the hyperparamter optimization algorithm, please refer to [here](#hyperparameter-optimization-algorithms)
* For how scheduler works in hyperparameter optimization, please refer to [here](#hyperparameter-optimization-schedulers)
* Here the key `training_iteration` for the option `stop` refers to how many times the training function is called before a trial is finished.

#### Example of creating an hpo configuration:

```
hpogrid hpo_config create my_example_config --algorithm random --metric loss --mode min --num_trials 100
```

#### Example of modifying an existing hpo configuration (old settings will be kept):

```
hpogrid hpo_config update my_example_config --algorithm bayesian
```

#### Example of recreating an existing hpo configuration (old settings will not be kept):

```
hpogrid hpo_config recreate --algorithm bayesian --metric loss --mode min --num_trials 100
```

#### To list all hpo configurations:

```
hpogrid hpo_config list
```

#### To show the content of an existing hpo configuration:

```
hpogrid hpo_config show my_example_config
```

## Grid Configuration

These are configurations that define settings for grid job submission. 

The command for managing grid configuration is:

```
hpogrid grid_config <action> <config_name> [<options>]
```

For creation, modification of the configuration file, the following options are available

| **Option** | **Description** | **Default** | 
| ---------- | ---------- | ----------- | 
| `site` | Grid site where the jobs are submitted (multiple inputs are allowed) | `ANALY_MANC_GPU_TEST,ANALY_MWT2_GPU,ANALY_BNL_GPU_ARC`  | 
| `container` | Docker or singularity container which the jobs are run | `/cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest` | 
| `retry` | Check to enable retrying faild jobs | - | 
| `inDS` | Name of input dataset | - | 
| `outDS` | Name of output dataset | `user.${{RUCIO_ACCOUNT}}.hpogrid.{HPO_PROJECT_NAME}.out.$(date +%Y%m%d%H%M%S)` |

#### Example of creating a grid configuration:

```
hpogrid grid_config create my_example_config --site ANALY_MANC_GPU_TEST --inDS user.${RUCIO_ACCOUNT}.mydataset01
```

#### Example of modifying an existing grid configuration (old settings will be kept):

```
hpogrid grid_config update my_example_config --container docker://gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest
```

#### Example of recreating an existing grid configuration (old settings will not be kept):

```
hpogrid grid_config recreate my_example_config --site ANALY_BNL_GPU_ARC --inDS user.${RUCIO_ACCOUNT}.mydataset02
```

#### To list all grid configurations:

```
hpogrid grid_config list
```

#### To show the content of an existing grid configuration:

```
hpogrid grid_config show my_example_config
```

## Model Configuration

Configurations that contains information of the training model that is called by the hyperparameter optimization alogrithm.

The command for managing model configuration is:

```
hpogrid model_config <action> <config_name> [<options>]
```

For creation, modification of the configuration file, the following options are available

| **Option** | **Description** |
| ---------- | ---------- | 
| `script` | Name of the training script where the function or class that defines the training model will be called to perform the training|
| `model` | Name of the function or class that defines the training model |
| `param` | Extra parameters to be passed to the training model |

#### Example of creating a model configuration:

```
hpogrid model_config create my_example_config --script train.py --model advanced_rnn --param '{"input_path": "mypath/signl_point/", "epochs": 100}'
```

#### Example of modifying an existing model configuration (old settings will be kept):

```
hpogrid model_config update --model revised_rnn
```

#### Example of recreating an existing model configuration (old settings will not be kept):

```
hpogrid model_config recreate my_example_config --script train.py --model revised_rnn --param '{"input_path": "mypath/bkg_point/", "epochs": 200}'
```

#### To list all model configurations:

```
hpogrid model_config list
```

#### To show the content of an existing model configuration:

```
hpogrid model_config show my_example_config
```


## Search Space Configuration

These are configurations that defines hyperparameter search space. 

The command for managing search space configuration is:

```
hpogrid search_space <action> <config_name> [<options>]
```

For creation, modification of the configuration file, the command takes the form:

```
hpogrid search_space <action> <config_name> -s <search_space_definition>
```

The format for defining a search space in command line is through a json decodable string:

```
'{"NAME_OF_HYPERPARAMETER":{"method":"SAMPLING_METHOD","dimension":{"DIMENSION":"VALUE"}},
"NAME_OF_HYPERPARAMETER":{"method":"SAMPLING_METHOD","dimension":{"DIMENSION":"VALUE"}}, ...}'
```

Supported sampling methods for a hyperparameter:

| **Method** | **Description** | **Dimension**  |
| ---------- | --------------- | -------------- | 
| `categorical` | Returns one of the values in `categories`, which should be a list. If `grid_search`is set to 1, each value must be sampled once.| `categories`, `grid_search`| 
| `uniform`  | Returns a value uniformly between `low` and `high` | `low`, `high` |
| `uniformint` | Returns an integer value uniformly between `low` and `high` |  `low`, `high` | 
| `quniform` | Returns a value like round(uniform(`low`, `high`) / `q`) * `q` | `low`, `high`, `q` | 
| `loguniform` | Returns a value drawn according to exp(uniform(`low`, `high`)) so that the logarithm of the return value is uniformly distributed. | `low`, `high`, `base` |
| `qloguniform` | Returns a value like round(exp(uniform(`low`, `high`)) / `q`) * `q`|  `low`, `high`, `base`, `q` |
| `normal` | Returns a real value that's normally-distributed with mean `mu` and standard deviation `sigma`.| `mu`, `sigma` |
| `qnormal` | Returns a value like round(normal(`mu`, `sigma`) / `q`) * `q`| `mu`, `sigma`, `q`| 
| `lognormal` | Returns a value drawn according to exp(normal(`mu`, `sigma`)) so that the logarithm of the return value is normally distributed.| `mu`, `sigma`, `base`|
| `qlognormal` |  Returns a value like round(exp(normal(`mu`, `sigma`)) / `q`) * `q`| `mu`, `sigma`, `base`, `q`|

#### Example of creating a search space configuration:

```
hpogrid search_space create my_search_space -s '{ "lr":{"method":"loguniform","dimension":{"low":1e-5,"high":1e-2, "base":10}},\
"batchsize":{"method":"categorical","dimension":{"categories":[32,64,128,256,512,1024]}},\
"num_layers":{"method":"uniformint","dimension":{"low":3,"high":10}},\
"momentum":{"method":"uniform","dimension":{"low":0.5,"high":1.0}} }'
```

#### Example of modifying a search space configuration (old settings will be kept):

```
 hpogrid search_space update my_search_space -s '{"new_hp":{"method":"lognormal","dimension":{"mu":1,"sigma":1}}}'
```

#### Example of recreating a search space configuration (old settings will not be kept):

```
hpogrid search_space recreate my_search_space -s '{ "lr":{"method":"categorical", "dimension":{"categories": [1e-4,1e-3,1e-2,1e-1}},\
"batchsize":{"method":"categorical","dimension":{"categories":[32,64,128,256,512,1024]}}}'
```

#### To list all search space configurations:

```
hpogrid search_space list
```

#### To show the content of an existing search space configuration:

```
hpogrid search_space show my_example_config
```

# Creating a Custom Project with the Configuration Files

The `model`, `grid`, `hpo` and `search space` configuration files contains all information needed for setting up a hyperparameter optimization task. 

For convenience, all the configuration files will be combined to form a master configuration file, called the **project configuration** with an associated project name. This project configuration file is responsible
for running hyperparameter optimization tasks locally, via the grid or via iDDS. 

* To create a custom project with the `model`, `grid`, `hpo` and `search space` configuration files:
 ```
 hpogrid project create <project_name> [--options]
 ```
 
| **Option** | **Description** |
| ---------- | --------------- |
| `scripts_path` | The path to where the training scripts (or the directory containing the training scripts) are located |
| `hpo_config` | The hpo configuration to use for this project |
| `grid_config` | The grid configuration to use for this project |
| `model_config` | The model configuration to use for this project |
| `search_space` | The search space configuration to use for this project |

* Similarly, one can modify the project configuration by specifying different `model`, `grid`, `hpo` and `search space` configurations or a different scripts path:
 ```
 hpogrid project update <project_name> [--options]
 ```
 
* Or to recreate the project:
 ```
 hpogrid project recreate <project_name> [--options]
 ```

* To list out all the projects:

```
hpogrid project list <expression>
```

where `<expression>` is some regular expression for filtering the project names.

* To show the content of an existing project

```
hpogrid project show <project_name>
```

### Create a project configuration file directly

Alternatively, one can simply create the project configuration file directly in either `json` or `yaml` format. See the following examples:

* Example 1: Project configuration file for the `simple_objective` peoject (in yaml format)

```
project_name: simple_objective
scripts_path: /afs/cern.ch/work/c/chlcheng/Repository/hpogrid/examples/scripts/simple_objective.py
model_config:
  script: simple_objective.py
  model: simple_objective
search_space:
  height:
    method: uniform
    dimension:
      low: -100
      high: 100
  width:
    method: uniform
    dimension:
      low: 0
      high: 20
hpo_config:
  algorithm: hyperopt
  metric: loss
  mode: min
  scheduler: asynchyperband
  num_trials: 200
  max_concurrent: 3

grid_config:
  site: ANALY_MANC_GPU_TEST,ANALY_MWT2_GPU,ANALY_BNL_GPU_ARC
  container: /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest
  inDS: null
```  
  
* Example 2: Project configuration file for the `MNIST_CNN` peoject (in yaml format)  
```
project_name: MNIST_CNN
scripts_path: /afs/cern.ch/work/c/chlcheng/Repository/hpogrid/examples/scripts/MNIST_CNN
model_config:
  script: mnist_cnn.py
  model: MNIST_CNN
search_space:
  hidden:
    method: categorical
    dimension:
      categories:
      - 32
      - 64
      - 128
      grid_search: 0
  beta_1:
    method: uniform
    dimension:
      low: 0.5
      high: 1
  batchsize:
    method: categorical
    dimension:
      categories:
      - 32
      - 64
      - 128
      - 256
      - 512
      grid_search: 0
  lr:
    method: loguniform
    dimension:
      low: 1.0e-05
      high: 0.1
hpo_config:
  algorithm: nevergrad
  metric: loss
  mode: min
  num_trials: 200
  max_concurrent: 3
  algorithm_param:
    method: DoubleFastGADiscreteOnePlusOne
grid_config:
  site: ANALY_MANC_GPU_TEST,ANALY_MWT2_GPU,ANALY_BNL_GPU_ARC
  container: /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest
  inDS: null
```         

* Example 3: Project configuration file for the `BBYY_analysis` peoject (in yaml format)   
```
project_name: BBYY_SM
scripts_path: /afs/cern.ch/work/c/chlcheng/Repository/hpogrid/examples/scripts/BBYY/
model_config:
  script: train_bdt.py
  model: yybb_bdt
  param:
    channel: SM
    num_round: 10000
search_space:
  min_child_weight:
    method: uniformint
    dimension:
      low: 0
      high: 100
  colsample_bytree:
    method: uniform
    dimension:
      low: 0.3
      high: 1
  scale_pos_weight:
    method: uniform
    dimension:
      low: 0
      high: 9
  max_delta_step:
    method: uniform
    dimension:
      low: 0
      high: 20
  subsample:
    method: uniform
    dimension:
      low: 0.5
      high: 1
  eta:
    method: uniform
    dimension:
      low: 0.01
      high: 0.05
  alpha:
    method: uniform
    dimension:
      low: 0
      high: 1
  lambda:
    method: uniform
    dimension:
      low: 0
      high: 10
  max_depth:
    method: uniformint
    dimension:
      low: 3
      high: 20
  gamma:
    method: uniform
    dimension:
      low: 0
      high: 10
  max_bin:
    method: uniformint
    dimension:
      low: 10
      high: 500
hpo_config:
  algorithm: nevergrad
  metric: auc
  mode: max
  scheduler: asynchyperband
  num_trials: 1000
  max_concurrent: 3
  algorithm_param:
    method: DoubleFastGADiscreteOnePlusOne
grid_config:
  site: ANALY_MANC_GPU_TEST,ANALY_MWT2_GPU,ANALY_BNL_GPU_ARC
  container: /cvmfs/unpacked.cern.ch/gitlab-registry.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid:latest
  inDS: user.chlcheng:user.chlcheng.hpo.bbyy.dataset.01
```

# Adapting Training Scripts for Hyperparameter Optimization

The hpogrid workflow uses the **Ray Tune** library for carrying out hyperparameter optimization. There are two ways to adapt your training script to fit the format accepted by the library.

### **Method 1**: Training model as an objective function

Suppose you have a training script named `train.py` which contains an objective function called `my_objective`. Then for each _trial_ of the hyperparameter optimization, the Ray Tune library will generate a set of hyperparameters which will then be fed into this objective function. The objective function should then return a value for the evaluation metric which will allow the optimization algorithm to determine the next hyperparameter point. 

Example training script:
```python
def my_objective(config, reporter):
    height = config["height"]
    width = config["width"]
    loss = (height - 14)**2 - abs(width - 3)
    reporter(loss=loss)
```
- The objective function should contain the `config` argument. It is a dictionary where the values of all hyperparameters and other model parameters (i.e. any parameters you want to put in) are stored. Simply use `config['parameter_name']` to reference the value.
- The objective function should contain the `repoorter` argument. It is a function that reports the value of the evaluation metric (loss in this case) at the end of the training.

You can also put whatever you want inside the training script:
```python
kMyConstant = 1

def calculate_loss(height, width):
    loss = (height - 14)**2 - abs(width - 3)
    loss *= kMyConstant
    return loss

def my_objective(config, reporter):
    height = config["height"]
    width = config["width"]
    loss = calculate_loss(height, width)
    reporter(loss=loss)
```

For the above two examples, you should create your model configuration like this:
```
hpogrid model_config create test_model --script train.py --model my_objective
```


### **Method 2**: Training model as a trainable class

Suppose you have a training script named `train.py` which contains a class called `my_trainable`. Then for each _trial_ of the hyperparameter optimization, the Ray Tune library will do the following:
1. Generate a set of hyperparameters which will then be fed into the class object.
2. Initialize the class object by calling the `initialize` function inside the class.
3. For each `training_iteration` (as defined in the hpo configuration), the `step` function will be called which should return a dictionary containing information about the training result (e.g. value of the evaluation metric) for that training iteration.
4. (this step depends on the scheduler used as defined in the hpo configuration) If after some training iterations the value of the evaluation does not look promising, the model will be saved via the `save_checkpoint` function and the training will be temporarily or permanently stopped and a new set of hyperparameters will run. If the algorithm thinks the old set of hyperparameters may worth continue training, then the `load_checkpoint` function will be called to continue the previously stopped training.
5. The trial is said to be finished if either
    * The stopping criteria is reached, e.g. training_iteration reached a certain value, or
    * The training is stopped by the scheduler (due to low performance of the set of hyperparameters)

Example training script:
```python
import numpy as np
from hpogrid.iterface.tune import CustomModel

class MyTrainableClass(CustomModel):

    def initialize(self, config):
        self.timestep = 0

    def step(self):
        self.timestep += 1
        alpha = self.config.get("alpha", 1) # or alpha = config['alpha']
        beta = self.config.get("beta", 1) # or beta = config["beta"]
        loss = self.calculate_loss(alpha, beta)
        return {"loss": loss, 'timestep': self.timestep}}

    def save_checkpoint(self, checkpoint_dir):
        path = os.path.join(checkpoint_dir, "checkpoint")
        with open(path, "w") as f:
            f.write(json.dumps({"timestep": self.timestep}))
        return path

    def load_checkpoint(self, checkpoint_path):
        with open(checkpoint_path) as f:
            self.timestep = json.loads(f.read())["timestep"]
            
    def calculate_loss(self, alpha, beta):
        loss = np.tanh(float(self.timestep) / alpha)
        loss *= beta
        return loss
```

- The trainable class must inherit from the `CustomModel` class for the Ray Tune library to recognize the class structure. It is a class derived from the `ray.tune.Trainable` parent class.
- The functions `save_checkpoint` and `load_checkpoint` are optional if you only train for one training iteration (i.e. `initialize` is called only once)

If you do not need to make use of the scheduler to speed up your training by terminating low performant trainings, or your training cannot be split into successive training iterations. You can leave out the `save_checkpoint` and `load_checkpoint` functions. For example:

```python
import numpy as np
from hpogrid.iterface.tune import CustomModel

class MyTrainableClass(CustomModel):

    def initialize(self):
        alpha = self.config.get("alpha", 1) # or alpha = config['alpha']
        beta = self.config.get("beta", 1) # or beta = config["beta"]
        loss = self.calculate_loss(alpha, beta)
        return {"loss": loss}
            
    def calculate_loss(self, alpha, beta):
        loss = np.tanh(1/alpha)
        loss *= beta
        return loss
```

# Running Hyperparameter Optimization Jobs

- To run locally:

```
hpogrid run <project_name> [--options]
```


| **Option** | **Description** |  **Default** |
| ---------- | ---------- | ------------ |
| `search_points` | A json file containing a list of hyperparameter search points to evaluate | - |

- To submit a grid job:

```
hpogrid submit <project_name> [--options]
```

| **Option** | **Description** |  **Default** |
| ---------- | ---------- | ------------ |
| `n_jobs` | The number of grid jobs to be submitted (useful for random search, i.e. to run a single search point per job) | 1 |
| `site` | The site to where the jobs are submitted (this will override the site setting in the grid configuration | - |
| `search_points` | A json file containing a list of hyperparameter search points to evaluate | - |
| `mode` | Choose between 'grid' or 'idds' for running a normal grid job or through the idds workflow| 'grid' |

Alternatively if you are creating your own configuration file, you may simply do
```
hpogrid submit <path_to_project_configuration_file> [--options]
```

# Integration with iDDS workflow

As mentioned in the above section, one can submit the job that runs the iDDS workflow by doing:
```
hpogrid submit <project_name> [--options] --mode idds
#or
hpogrid submit <path_to_project_configuration_file> [--options] --mode idds
```

# Monitoring Job Status

To get the status of recent grid jobs:

```
hpogrid tasks show [--options]
```

| **Option** | **Description** |  **Default** |
| ---------- | ---------- | ------------ |
| `username` | Filter tasks by username | '''name of user holding the grid certificate''' |
| `limit` | The maximum number of tasks to query | 1000 |
| `days` | Filter tasks within the recent `N` days | 30 |
| `taskname` | Filter tasks by taskname (accept wildcards) | - |
| `jeditaskid` | Only show the task with the specified jeditaskid | - |
| `metadata` | Print out the metadata of a task | False |
| `sync` | Force no caching on the PanDA server | False |
| `range` | Filter tasks by jeditaskid range | - |
| `output` | Output result with the filename if specified | - |
| `outcol` | Data columns to be saved in output | 'jeditaskid', 'status', 'taskname', 'computingsite', 'metastruct' | 



# Visualizing Hyperparamter Optimization Results
To get the hpo result for a specific project:
```
hpogrid report <project_name> [--options]
```
| **Option** | **Description** |  **Default** | **Choices** | 
| ---------- | --------------- | ------------ | ----------- |
| `limit` | the maximum number of tasks to query | 1000 | - |
| `days` | filter tasks within the recent `N` days | 30 | - |
| `taskname` | filter tasks by taskname (accept wildcards) | - | - |
| `range` | filter tasks by jeditaskid range | - | - |
| `extra` | extra data columns to be displayed and saved | - | 'site', 'task_time_s', 'time_s', 'taskid' |
| `outname` | output file name (excluding extension) | hpo_result | - |
| `to_json` | output result to a json file | False | - |
| `to_html` | output result to an html file | False | - |
| `to_csv` | output result to a csv file | False | - |
| `to_pcp` | output result as a parallel coordinate plot | False | - |
| `to_mlflow` | output result to a mlflow compatible file | False | - |

# Command Line Options
* To kill a job by jeditaskid
```
hpogrid tasks kill <jeditaskid>
```

* To retry a job by jeditaskid
```
hpogrid tasks retry <jeditaskid>
```

* To see a list of available GPU sites
```
hpogrid sites
```


# Advanced Examples

### Example Payload: PID with Recurrent Neural Networks in TRT Detector

To try out this example, simply type:
```
source examples/setup/RNN_TRT.sh
```

To test locally:
```
hpogrid run RNN_TRT
```

**Note**: The training scripts are not provided for confidentiality. 
### Example Payload: FastCaloGAN

To try out this example, simply type:
```
source examples/setup/FastCaloGAN.sh
```

To test locally:
```
hpogrid run FastCaloGAN_photon_200_205
```

**Note**: The training scripts are not provided for confidentiality. 
### Example Payload: BBYY Analysis
To try out this example, simply type:
```
source examples/setup/BBYY_analysis.sh
```

To test locally:
```
hpogrid run BBYY_SM
hpogrid run BBYY_BSM
```

**Note**: The training scripts are not provided for confidentiality. 
### Custom Example: CIFAR10_CNN

This is an example of using convolutional neural network on the CIFAR10 dataset. 

To try out this example, simply type:
```
source examples/setup/CIFAR10_CNN.sh
```

To test locally:
```
hpogrid run CIFAR10_CNN
```

# Important Notes

### Working Directory of Container
* When running a grid job inside a container, you can check the working directory inside your script by calling
```
import hpogrid
working_directory = hpogrid.get_workdir()
```

In most cases, you can obtain the working directory by simpling calling `os.path.getcwd()`.

### Location of Input Dataset
* When running a grid job inside a container, you can check the data directory (where the inDS is located) inside your script by calling
```
import hpogrid
data_directory = hpogrid.get_datadir()
```

Similarly, the default data directory should be the same as `os.path.getcwd()`.


