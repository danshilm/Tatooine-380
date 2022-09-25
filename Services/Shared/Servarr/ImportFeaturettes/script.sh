#!/usr/bin/env bash

now=$(date +'%F %T')
radarr_logfile="$(pwd)/radarr_lastrun.log"
[ ! -f "$radarr_logfile" ] && touch "$radarr_logfile"

sonarr_logfile="$(pwd)/sonarr_lastrun.log"
[ ! -f "$sonarr_logfile" ] && touch "$sonarr_logfile"

if [[ $radarr_eventtype == "Test" ]]; then
	echo "$now: Test successful!" >> "$radarr_logfile"
fi

if [[ $radarr_eventtype == "Download" ]]; then
	for featurettesFolderName in "Extras" "Behind the Scenes" "behindthescenes" "Deleted scenes" "deletedscenes" "Featurettes" "Interviews" "Scenes" "Shorts"; do
		if [[ -d "$radarr_moviefile_sourcefolder/$featurettesFolderName" ]]; then
			echo "$now: Found Featurette folder \"$featurettesFolderName\" in completed folder download location \"$radarr_moviefile_sourcefolder\"" >> "$radarr_logfile"
			echo "$now: Copying Featurette folder to movie path \"$radarr_movie_path\"" >> "$radarr_logfile"
			cp -r "$radarr_moviefile_sourcefolder/$featurettesFolderName" "$radarr_movie_path/$featurettesFolderName"
			echo "$now: Done importing featurettes"
		fi
	done
fi

if [[ $sonarr_eventtype == "Test" ]]; then
	echo "$now: Test successful!" >> "$sonarr_logfile"
fi

if [[ $sonarr_eventtype == "Download" ]]; then
	for featurettesFolderName in "Extras" "Behind the Scenes" "behindthescenes" "Deleted scenes" "deletedscenes" "Featurettes" "Interviews" "Scenes" "Shorts"; do
		if [[ -d "$sonarr_episodefile_sourcefolder/$featurettesFolderName" ]]; then
			echo "$now: Found Featurette folder \"$featurettesFolderName\" in completed folder download location \"$sonarr_episodefile_sourcefolder\"" >> "$sonarr_logfile"
			echo "$now: Copying Featurette folder to show path \"$sonarr_series_path\"" >> "$sonarr_logfile"
			cp -r "$sonarr_episodefile_sourcefolder/$featurettesFolderName" "$sonarr_series_path/$featurettesFolderName"
			echo "$now: Done importing featurettes"
		fi
	done
fi
