#!/bin/bash

cd /home/user/Services/Stack
echo "Stopping radarr.."
docker-compose stop radarr
cp /home/user/Services/Radarr/nzbdrone.db /home/user/Services/Shared/Radarr/TmmToRadarr/
cd /home/user/Services/Shared/Radarr/TmmToRadarr/
echo "Removing last empty line from movielist.csv..."
sed -i '$d' Exported/movielist.csv
echo "Updating records in radarr db - check last_run.log for info"
runuser -l user -c 'python3 /home/user/Services/Shared/Radarr/TmmToRadarr/updateRadarrDBEntries.py >> /home/user/Services/Shared/Radarr/TmmToRadarr/last_run.log'
echo "Copying back to radarr config directory and making backup of current db.."
rm /home/danshil/Services/Radarr/nzbdrone.db*
cp nzbdrone.db /home/user/Services/Radarr/
mv --backup=numbered nzbdrone.db Backups/
cd /home/danshil/Services/Stack
echo "Starting radarr..."
docker-compose up -d --force-recreate radarr