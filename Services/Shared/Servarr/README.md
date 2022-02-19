## ImportFeaturettes

That one is meant to run as a post-processing script in Radarr/Sonarr so that it automatically imports any extras that are in the completed download folder. This is something especially common with movies where most a lot of releases include movie extras that are in a folder named "Featurettes".

I've set it so the script is ran when a download has completed and when manually importing movies/show episodes too, that way I don't have to manually move the "Featurettes" folder over.

To add the script to Radarr/Sonarr, head to `Settings`, `Connect` and add a `Custom Script`. Name it however you like (mine is named "Import Featurettes") and set the path of the script to `/shared/Servarr/ImportFeaturettes/script.sh`. The path to the script depends on how you mounted the folder to the container, but if you're using the docker-compose file as it is on this repository, the latter path is the correct one. As for the trigger, only choose `Be notified when movies are successfully imported`.

This script can also be set up as a post-processing script in Sonarr in the exact same way.

Whenever featurettes are imported using that script, some details are logged in a file for Radarr and Sonarr respectively in the same folder as the script.
