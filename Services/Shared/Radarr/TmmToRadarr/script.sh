#!/bin/bash

now=$(date +'%F %T')
cd /home/user/Services/Stack
docker-compose stop radarr
cp -p /home/user/Services/Radarr/radarr.db /home/user/Services/Shared/Radarr/TmmToRadarr/
echo "Removing last empty line from movielist.csv..."
sed -i '$d' /home/user/Services/Shared/Radarr/TmmToRadarr/Exported/movielist.csv
echo "Updating records in radarr db - check last_run.log for info"
echo "=================== $now ===================" >> /home/user/Services/Shared/Radarr/TmmToRadarr/last_run.log
runuser -l user -c 'python3 /home/user/Services/Shared/Radarr/TmmToRadarr/tmmToRadarr.py updateRadarrEntries >> /home/user/Services/Shared/Radarr/TmmToRadarr/last_run.log'
echo "Copying back to radarr config directory.."
rm /home/user/Services/Radarr/radarr.db*
cp -p /home/user/Services/Shared/Radarr/TmmToRadarr/radarr.db /home/user/Services/Radarr/
docker-compose up -d --force-recreate radarr
sleep 3
echo "Triggering rescan for all movies..."
runuser -l user -c 'python3 /home/user/Services/Shared/Radarr/TmmToRadarr/tmmToRadarr.py rescanUpdatedRadarrMovies >> /home/user/Services/Shared/Radarr/TmmToRadarr/last_run.log'
echo "Cleanup..."
mv --backup=numbered /home/user/Services/Shared/Radarr/TmmToRadarr/radarr.db /home/user/Services/Shared/Radarr/TmmToRadarr/Backups/