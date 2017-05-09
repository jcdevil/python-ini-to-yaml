#!/bin/bash

echo "installing pyyaml"
pip install pyyaml --upgrade
echo "running test"
python ini_to_yml.py --in tests/example.ini --out tests/example.yml

