#!/bin/bash
which python3 > /dev/null 2>&1
if [[ $? != 0 ]] ; then
	echo "unable to find python3, terminating..."
    sleep 1
    exit 1
fi
sudo apt-get install -y python3-tk
sudo apt-get install -y python3-venv
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
