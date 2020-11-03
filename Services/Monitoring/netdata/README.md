Netdata is as plug and play as monitoring thousands of metrics can be. There are a few additional charts that I added to my Netdata install:

1. _dockerd_ to monitor containers
2. _smartd_ to monitor hdd temp and other SMART stats
3. _traefik_ health monitoring

For dockerd, smartd and traefik, refer to their manual [here](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/dockerd/), [here](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/smartd_log) and [here](https://learn.netdata.cloud/docs/agent/collectors/python.d.plugin/traefik/) respectively. (NOTE: does NOT work for Traefik v2)

If you want discord notifications for netdata, follow the instructions [here](enableDiscordNotifications.md).

A note about exporting metrics to OpenTSDB: I've noticed some weird high CPU usage when exporting the metrics to InfluxDB using OpenTSDB using the `exporting.conf` config file, so I'm still using the `[backend]` option in my `netdata.conf` file. Here's what that option looks like:

```
[backend]
	enabled = yes
	type = opentsdb
	destination = localhost:4242
	update every = 5
	send charts matching = system.uptime system.cpu system.load system.ram system.swap system.net cpu.cpu0 cpu.cpu1 cpu.cpu2 cpu.cpu3 sensors.coretemp_isa_0000_temperature traefik_local.average_respose_time disk_space._media_seagateironwolf disk_space._ smartd_log.temperature* disk.sda disk.sdb disk.sdc cgroup_*.cpu_limit cgroup_*.mem_usage cgroup_*.net_eth* cgroup_*.throttle_io docker_engine_local.engine_daemon_container_states_containers
```