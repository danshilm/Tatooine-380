#!/bin/bash

# shopt -s nocaseglob
now=$(date +'%F %T')
touch /shared/ImportMovieFeaturettes/lastrun.log
logfile="/shared/ImportMovieFeaturettes/lastrun.log"

if [[ $radarr_eventtype == "Test" ]] ; then
	echo "$now: Test successful!" >> $logfile
fi

## these folder names are based on what I've seen when grabbing movies from Torrents/Usenet, so add to the list if there's any mossing
if [[ $radarr_eventtype == "Grab" ]] || [[ $radarr_eventtype == "Download" ]]; then
	for featurettesFolderName in "Extras" "Behind the Scenes" "behindthescenes" "Deleted scenes" "deletedscenes" "Featurettes" "Interviews" "Scenes" "Shorts"
	do
		if [[ -d "$radarr_moviefile_sourcefolder/$featurettesFolderNames" ]]; then
			echo "$now: Found Featurette folder ($featurettesFolderName) in completed folder download location: \"$radarr_moviefile_sourcefolder\"" >> $logfile
			echo "$now: Copying Featurette folder to movie path: \"$radarr_movie_path\"" >> $logfile
			# change to move instead of copy?
			cp -r "$radarr_moviefile_sourcefolder/$featurettesFolderName" "$radarr_movie_path/$featurettesFolderName"
		fi
	done
fi
