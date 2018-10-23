#!/bin/bash

echo `date "+%F %H:%M:%S"` " -----START-----"
cd /root/eink-weather
python3 weather_scrap.py
python test2.py
echo `date "+%F %H:%M:%S"` " -----STOP-----"


