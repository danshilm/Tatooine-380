## InfluxDB Metrics

I was a fan of the average response time metric that Traefik offered on their dashboard prior to v2, so I went ahead and enabled the collection of metrics for Traefik in an InfluxDB database (that database was created beforehand) so I can have a similar but more detailed bunch of metrics about my traefik instance on the Grafana dashbaord that I use.

To enable the collection of traefik metrics, simply modify the `[metrics]` option in the [traefik.toml](./traefik.toml) configuration file to your own needs.

## Logrotate

To setup logrotate for the traefik logs daily, create a `traefik.conf` file in `/etc/logrotate.d/` and add these contents to the file:

```
<${USERDIR}>/Services/Stack/traefik2/logs/*.log {
	daily
	rotate 14
	compress
	delaycompress
	dateext
	missingok
}
```

Refer to the [`.env` file](../.env) for the `<${USERDIR}>` and replace it here. 

For more information about the directives used above, refer to the [man pages](https://linux.die.net/man/8/logrotate) of logrotate.