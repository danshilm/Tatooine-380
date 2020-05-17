This script is to fill the gap that varken doesn't deal with out-of-the-box for Emby. This is still however, the very first iteration of this script and only fills the `Current Streams` panel of the Varken Grafana dashboard. I do have plans to make it work for the stats about the `Current Streams, Current Transcodes, WAN Bandwidth and LAN bandwidth` though since it doesn't match up with that is shown in the `Current Streams` panel.

Basically, what the script does it replicate the functionality of the script that Varken runs, but for Emby. This has several drawbacks though:

1. The script queries Emby directly, which isn't what I'd prefer and is by far not the best way of doing it. The better option would be to query the [Tautulli equivalent of Emby](https://github.com/mregni/EmbyStat). However, that is still in the beta stages and doesn't yet track the current Emby sessions.
2. It does not incorporate all the features that Varken has, like IP location and whatnot (yet?).
3. I have to run it as a systemd service with a timer that runs it every 30s. This sometimes results in gaps of a few seconds in the current streams panel where the streams don't appear. This is probably due to the running time of the script and the time interval of the panel in Grafana. I adjusted mine to run every 28s since the script takes around 1s to run on my system.

To run this as a systemd service, create 2 files at `/etc/systemd/system/` one with the `.service` extension and another similarly named file with the `.timer` extension. Mine are called _embytovarken_.

The `.service` file for my system looks like this:
```
[Unit]
Description=Fills current streams tab in Grafana dashboard

[Service]
ExecStart=/usr/bin/python3 /home/user/Services/cron/EmbyToVarken/script.py
```

and the `.timer` file looks like this:
```
[Unit]
Description=Fill current streams tab in Grafana dashboard every 28s

[Timer]
OnUnitActiveSec=28s
OnBootSec=10s

[Install]
WantedBy=timers.target
```

Then reload the daemon with `systemctl daemon-reload` and then start the timer (NOT the service) with `systemctl start embytovarken.timer`. If all is good, enable it with `systemctl enable embytovarken.timer`.

Documentation about systemd services can be found [here](https://www.freedesktop.org/software/systemd/man/systemd.service.html) and [there](https://www.linux.com/topic/desktop/setting-timer-systemd-linux/).