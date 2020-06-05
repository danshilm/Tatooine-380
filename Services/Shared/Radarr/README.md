## TmmToRadarr

I use [TinyMediaManager](https://www.tinymediamanager.org/) to manage and rename my movies and tv shows instead of only Radarr and Sonarr since those aren't as useful as TMM. However, since there is no way to get the rename pattern in Radarr to match the one I have in TMM, I have to rename my movies in TMM, then manually go edit each movie in Radarr to match the correct folder.

You first have to manually export the movies whose records you want updated in Radarr from TMM using the template I have in the `Template` folder.
Export the movies to the `Exported` folder (make sure it's empty before doing it btw).

This is where this comes script comes in. It works like this:

1. Stop Radarr so we don't end up with corrupted database (still unsure if need to remove the journal and wal files for sqlite)
2. Copy sqlite DB to `TmmToRadarr` folder (a backup is made in step 4)
3. Get the movies from the exported csv list and use their `tmdbId` to match them to the ones in Radarr
4. Copy sqlite DB back to Radarr config directory and make numbered backup
5. Restart Radarr again

NOTE: Run the script as `sudo` so it can start and stop the docker containers. The script is run as a standard user though, since I don't want to 'polute' my superuser account with unnecessary stuff.

I'll script the part where one has to manually export from TMM since I already do it once a week usually and there aren't any mismatches since Radarr already makes a `.nfo` file which has the `tmdbId` of the movies.