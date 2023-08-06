import os
import re
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
VERSIONFILE="hpogrid/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setuptools.setup(
    name="hpogrid",
    version=verstr,
    author="Alkaid Cheng",
    author_email="chi.lung.cheng@cern.ch",
    description="A workflow for hyperparamter optimization using the ATLAS grid resources",
    #long_description=long_description,
    #long_description_content_type="text/markdown",
    url="https://gitlab.cern.ch/aml/hyperparameter-optimization/alkaid-qt/hpogrid",
    packages=setuptools.find_packages(),
    package_data={'hpogrid':['userdata/*/.keep', 'resources/*']},
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'pandas',
          'tqdm',
          'click',
          'tabulate',
          'numpy',
          'psutil'
      ],
    scripts=['bin/hpogrid'],
    python_requires='>=3.6',
)
