#!/usr/bin/sh

export PYTHONPATH=/home/helio/github/RIDE/utest/:$PYTHONPATH
export PYTHONPATH=/home/helio/github/RIDE/src/:$PYTHONPATH

export PYTHONROOT=/usr/bin

cd /home/helio/github/RIDE/
pytest -k test_ --ignore-glob=/usr/lib64/python3.10/site-packages/* --ignore-glob=/home2/helio/.local/* -v  --cov --cov-report=xml --cov-report=html ./utest 

