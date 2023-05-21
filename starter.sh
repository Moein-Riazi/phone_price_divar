#!/bin/bash

if [ "$1" == "-v" ]; then
    read -p "Enter the price you want: " FIT_PRICE
    echo -e "\nexport FIT_PRICE=$FIT_PRICE" >> config.sh
fi

if [ "$1" == "-p" ]; then
    MASIR=$(pwd)
    crontab -l > mycron
    echo "*/30 * * * * bash $MASIR/starter.sh" >> mycron
    crontab mycron
    echo "successfull!, program will automatically run every 30 minutes"
fi

if [ "$1" == "-c" ]; then
    python3 configs.py
fi

#python3 configs.py

. ./config.sh 

python3 phone-price.py

#nohup python3 db_show.py > moein & 1>&2 /dev/null 
nohup  python3 db_show.py > /dev/null 2>&1&