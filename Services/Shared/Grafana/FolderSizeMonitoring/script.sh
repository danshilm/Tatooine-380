#!/usr/bin/env bash

# cd to appropriate folder
cd /home/user/Services/Shared/Grafana/FolderSizeMonitoring

# get folder sizes
sudo du -s /media/TheVault/PlexMediaServer/* > file_sizes.txt
sudo du -s /home/user/Services/ >> file_sizes.txt

# replace /media/TheVault/PlexMediaServer/ with nothing as well as /home/user/
sed -i 's/\/media\/TheVault\/PlexMediaServer\///g' file_sizes.txt
sed -i 's/\home\/user\///g' file_sizes.txt

# folders to monitor are: Anime, Collections, Movies, Readables, TvShows, Services
Anime=$(grep "Anime" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
Collections=$(grep "Collections" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
Movies=$(grep -e "Movies$" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
Movies4K=$(grep "Movies-4K" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
Readables=$(grep "Readables" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
TvShows=$(grep -w "TvShows" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')
Services=$(grep "Services" file_sizes.txt | grep -oP '\d*\s+' | tr -d '[:space:]')

echo "folder_sizes,folder=Anime size=$Anime" > upload.txt
echo "folder_sizes,folder=Collections size=$Collections" >> upload.txt
echo "folder_sizes,folder=Movies size=$Movies" >> upload.txt
echo "folder_sizes,folder=Movies-4K size=$Movies4K" >> upload.txt
echo "folder_sizes,folder=Readables size=$Readables" >> upload.txt
echo "folder_sizes,folder=TvShows size=$TvShows" >> upload.txt
echo "folder_sizes,folder=Services size=$Services" >> upload.txt

# send to influxdb
curl -i -XPOST 'http://localhost:8086/write?db=manual' --data-binary @upload.txt
