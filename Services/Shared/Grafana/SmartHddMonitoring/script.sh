#!/usr/bin/env bash

# cd to appropriate folder
cd /home/user/Services/Shared/Grafana/SmartHddMonitoring

# store results for every smartctl /dev/sd[a-c]
raw_sda="$(smartctl -H /dev/sda | grep 'test result' | cut -d ' ' -f 6)"
raw_sdb="$(smartctl -H /dev/sdb | grep 'test result' | cut -d ' ' -f 6)"
raw_sdc="$(smartctl -H /dev/sdc | grep 'test result' | cut -d ' ' -f 6)"

# store raw smartctl for debug info
date >> raw.txt
smartctl -H /dev/sda >> raw.txt
smartctl -H /dev/sdb >> raw.txt
smartctl -H /dev/sdc >> raw.txt

# if passed = 0, else = 1
if [ $raw_sda = PASSED ]; then
  sda=0
elif [ $raw_sda = FAILED]; then
  sda=1
else
  sda=0
fi
if [ $raw_sdb = PASSED ]; then
  sdb=0
elif [ $raw_sdb = FAILED]; then
  sdb=1
else
  sdb=0
fi
if [ $raw_sdc = PASSED ]; then
  sdc=0
elif [ $raw_sdc = FAILED]; then
  sdc=1
else
  sdc=0
fi

# store parsed results in file upload.txt
echo "smart_status,device=/dev/sda status=$sda" > upload.txt
echo "smart_status,device=/dev/sdb status=$sdb" >> upload.txt
echo "smart_status,device=/dev/sdc status=$sdc" >> upload.txt

# send to influxdb database manual
curl -i -XPOST 'http://localhost:8086/write?db=manual' --data-binary @upload.txt
