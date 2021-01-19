#!/bin/bash

NOW=$(date +'%F %T')
cd /home/<user>/Services/Shared/Grafana/InternetUsage/vnstatParsing
echo "Getting vnstat output and storing to vnstatOutput.json"
vnstat -i wlp1s0 --json d 1 > vnstatOutput.json
echo "Running script"
python3 -u parseVnstatOutput.py day
echo "Done"