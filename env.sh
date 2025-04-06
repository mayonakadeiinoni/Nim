#!/bin/bash
set -eus
echo 7

#python=/usr/bin/python3.10
python=python3.10
envdir=./env

echo 7
$python -m venv $envdir
. $envdir/bin/activate

pip install --upgrade pip setuptools
pip install --upgrade pip
pip install wheel
#pip install -r ./requirements.txt
#pip3 install torch torchvision torchaudio
#pip install --upgrade -r ./requirements.txt
#pip install git+https://github.com/haoheliu/audioldm_eval
pip install ipykernel
pip install jupyter
pip install jupyter_contrib_nbextensions
pip install --upgrade notebook==6.4.12 #jupyter nbconvert --to python ipynbファイルが使えるようにする。
