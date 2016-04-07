#!/bin/bash

venv_version="virtualenv-15.0.1"
if [ ! -f ~/$venv_version".tar.gz" -a ! -d $venv_version ]
then
    wget -P ~ "https://pypi.python.org/packages/source/v/virtualenv/"$venv_version".tar.gz#md5=28d76a0d9cbd5dc42046dd14e76a6ecc"
    tar xvf ~/$venv_version".tar.gz"
else
    echo "Found virtualenv package"
fi

if [ ! -d ~/virtualenvs ]
then
    mkdir ~/virtualenvs
else
    echo "Found virtualenv folder"
fi
if [ ! -d ~/virtualenvs/pythonkurs ]
then
    python ~/$venv_version/virtualenv.py virtualenvs/pythonkurs
else
    echo "Found virtual environment"
fi

if [ ! -d $HOME/Python-SoSe2016 ]
then
        mkdir $HOME/Python-SoSe2016
fi

if ! grep -q "source /usr/bin/virtualenvwrapper.sh" ~/.bashrc
then
        echo "source /usr/bin/virtualenvwrapper.sh" >> ~/.bashrc
fi

if ! grep -q "export WORKON_HOME=\$HOME/virtualenvs" ~/.bashrc
then
        echo "export WORKON_HOME=\$HOME/virtualenvs" >> ~/.bashrc
fi

if ! grep -q "export PROJECT_HOME=\$HOME/Python-SoSe2016" ~/.bashrc
then
        echo "export PROJECT_HOME=\$HOME/Python-SoSe2016" >> ~/.bashrc
fi
