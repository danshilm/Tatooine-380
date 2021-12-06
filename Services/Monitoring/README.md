This has a compose file comprising of (almost) everything that I use to monitor my system. Netdata is in the compose file in the EntryPoint folder. 

__Grafana__ is used to display the dashboard.

__InfluxDB__ is where all the metrics are stored in.

__Netdata__ is just [sexy as hell](https://user-images.githubusercontent.com/1153921/80827388-b9fee100-8b98-11ea-8f60-0d7824667cd3.gif).

__Speedtest__ is used to get periodical speedtests and show it on the Grafana dashboard.

__Varken__ is used to get stats about Plex and all the *rrs.

__Dozzle__ is an easy way to view logs for all your Docker containers.

__Scrutiny__ is used to keep an eye on my hard disks/SSDs using SMART tests and sends out notifications when things don't look too good.

__MonitoRSS__ is to get notified of updates. That can be updates to software you use, a subreddit, a GitHub repository; basically anything that has an RSS feed. If it doesn't have an RSS feed, you can also use a tool to generate an RSS feed for it.
