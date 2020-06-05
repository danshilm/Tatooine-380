Netdata is as plug and play as monitoring thousands of metrics can be. There are a few additional charts that I added to my Netdata install. 

1. _dockerd_ to monitor containers
2. _smartd_ to monitor hdd temp and other SMART stats
3. _traefik_ health monitoring

For dockerd, refer to their [manual](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/dockerd/).

For smartd, refer to their [manual](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/smartd_log).

For traefik, refer to their [manual](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/traefik/). (NOTE: does NOT work for Traefik v2)