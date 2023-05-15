#!/bin/bash

python3 configs.py

. ./config.sh 

python3 phone-price.py

python3 db_show.py