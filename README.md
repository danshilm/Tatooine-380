# Tatooine-380
A collection of scripts and dockers for my home media server
The *rrs work with Nzb360.

The compose file contains:
- tecnativa/docker-socket-proxy
- traefik (v2.2)
- authelia/authelia
- dperson/openvpn-client
- linuxserver/qbittorrent
- linuxserver/radarr
- linuxserver/sonarr
- linuxserver/lidarr
- linuxserver/bazarr
- linuxserver/lazylibrarian
- linuxserver/sabnzbd
- linuxserver/jackett
- linuxserver/nzbhydra
- linuxserver/plex
- linuxserver/tautulli
- linuxserver/jellyfin
- linuxserver/emby
- linuxserver/airsonic
- linuxserver/ombi
- mariadb (v10.1)
- phpmyadmin/phpmyadmin
- afian/filerun
- linuxserver/lychee
- netdata/netdata
- linuxserver/heimdall
- tzahi12345/youtubedl-material

The compose file in Monitoring contains:
- grafana/grafana
- prom/prometheus
- influxdb
- boerderij/varken
- atribe/speedtest-for-influxdb-and-grafana
- amir20/dozzle

TODO:
- [ ] Minify compose file and traefik labels
- [ ] Adapt [guillaumebriday/traefik-custom-error-pages](https://github.com/guillaumebriday/traefik-custom-error-pages) for Traefik:v2.2 (refer to [this example](https://github.com/jamescurtin/traefik-proxy) on how to be clean)
- [ ] Move sensitive stuff to docker secrets instead of .env