# RLApps

RLlib-based general reinforcement learning algorithms collections (derived from [John B. Lanier's implementation](https://github.com/indylab/nxdo)). I bumped it up to Ray v1.12 and fixed some errors. More general RL algorithms will be introduced.

**NOTE**: As a nice gRPC and RLlib derivation, I recommend our groupmates to use it as a good practice. In addition, please feel free to enrich this repo by submitting your PRs.

## Installation

(Tested on Ubuntu 20.04)

### Set up Conda environment and python modules
After installing [Anaconda](https://docs.anaconda.com/anaconda/install/), enter the repo directory and create the new environment:
```shell script
conda create -n rlapps python==3.8 -y
conda activate rlapps
bash ./install.sh
```

### Advanced Installation Notes (Optional)

If you need to compile/recompile OpenSpiel without pip installing it, perform the following steps with your conda env *active*. (The conda env needs to be active so that OpenSpiel can find and compile against the python development headers in the env. Python version related issues may occur otherwise):
```shell script
mkdir build
cd build
CC=clang CXX=clang++ cmake -DPython_TARGET_VERSION=3.6 -DCMAKE_CXX_COMPILER=${CXX} -DPython3_FIND_VIRTUALENV=FIRST -DPython3_FIND_STRATEGY=LOCATION ../open_spiel
make -j$(nproc)
cd ../../..
```

To import OpenSpiel without using pip, add OpenSpiel directories to your PYTHONPATH in your ~/.bashrc ([more details here](https://github.com/deepmind/open_spiel/blob/master/docs/install.md)):
```shell script
# Add the following lines to your ~/.bashrc:
# For the python modules in open_spiel.
export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel_submodule>
# For the Python bindings of Pyspiel
export PYTHONPATH=$PYTHONPATH:/<path_to_open_spiel_submodule>/build/python
```

### Next Steps

See [Running Experiments](/docs/experiments.md)
