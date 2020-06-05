#!/bin/bash

cd /home/user/Services/Stack
echo "Stopping radarr.."
docker-compose down radarr
cp /home/user/Services/Radarr/nzbdrone.db /home/user/Services/Shared/Radarr/TmmToRadarr/
cd /home/user/Services/Shared/Radarr/TmmToRadarr/
echo "Updating records in radarr db - check last_run.log for info"
runuser -l user -c 'python3 /home/user/Services/Shared/Radarr/TmmToRadarr/updateRadarrDBEntries.py >> /home/user/Services/Shared/Radarr/TmmToRadarr/last_run.log'
echo "Copying back to radarr config directory and making backup of current db.."
cp --backup=numbered nzbdrone.db /home/user/Services/Radarr/
rm nzbdrone.db
cd /home/user/Services/Stack
echo "Starting radarr..."
docker-compose up -d radarr