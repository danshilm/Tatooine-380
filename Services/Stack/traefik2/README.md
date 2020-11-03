## InfluxDB Metrics

I was a fan of the average response time metric that Traefik offered on their dashboard prior to v2, so I went ahead and enabled the collection of metrics for Traefik in an InfluxDB database (that database was created beforehand) so I can have a similar but more detailed bunch of metrics about my traefik instance on the Grafana dashbaord that I use.

To enable the collection of traefik metrics, simply modify the `[metrics]` option in the [traefik.toml](./traefik.toml) configuration file to your own needs.