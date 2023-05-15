#!/bin/bash

if [ "$1" == "change" ]; then
    python3 configs.py
fi

#python3 configs.py

. ./config.sh 

python3 phone-price.py

nohup python3 db_show.py &