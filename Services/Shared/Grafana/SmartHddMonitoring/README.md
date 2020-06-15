I want to have a panel on my Grafana dashboard that shows the probability of drive failures. Something like the drive failure rate that snapraid shows would be perfect, however, I do not use snapraid.

Initial thoughts were to use:
1. SMART 5 - Reallocated_Sector_Count
2. SMART 187 - Reported_Uncorrectable_Errors
3. SMART 188 - Command_Timeout
4. SMART 197 - Current_Pending_Sector_Count
5. SMART 198 - Offline_Uncorrectable

to judge the probability of drive failure.

For now though, this only gets the SMART status of the drives.
The files `raw.txt` and `upload.txt` do need to exist beforehand.

NOTE: this script needs to be ran as sudo