#!/bin/bash

home=$(readlink -e ~)
source $home/.bashrc
pip install numpy
pip install Pillow 
pip install IPython
pip install jupyter

