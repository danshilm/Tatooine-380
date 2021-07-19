# Tatooine-380

A collection of scripts and dockers for my home media server.

NOTE: The \*rrs and Tautulli work with [Nzb360](https://nzb360.com/) and [Lunasea](https://www.lunasea.app/).

The compose file in [Stack](Services/Stack) contains:

- [tecnativa/docker-socket-proxy](https://github.com/Tecnativa/docker-socket-proxy)
- [traefik](https://github.com/traefik/traefik) v2.4.8
- [traefik-custom-error-pages](https://github.com/guillaumebriday/traefik-custom-error-pages)
- [authelia/authelia](https://github.com/authelia/authelia) v4.29.4
- [dperson/openvpn-client](https://github.com/dperson/openvpn-client)
- [linuxserver/qbittorrent](https://docs.linuxserver.io/images/docker-qbittorrent)
- [linuxserver/radarr](https://docs.linuxserver.io/images/docker-radarr)
- [linuxserver/sonarr](https://docs.linuxserver.io/images/docker-sonarr)
- [linuxserver/lidarr](https://docs.linuxserver.io/images/docker-lidarr)
- [randomninjaatk/amd](https://github.com/RandomNinjaAtk/docker-amd)
- [linuxserver/bazarr](https://docs.linuxserver.io/images/docker-bazarr)
- [hotio/readarr](https://github.com/Readarr/Readarr)
- [linuxserver/sabnzbd](https://docs.linuxserver.io/images/docker-sabnzbd)
- [linuxserver/jackett](https://docs.linuxserver.io/images/docker-jackett)
- [flaresolverr/flaresolverr](https://github.com/FlareSolverr/FlareSolverr)
- [linuxserver/nzbhydra](https://docs.linuxserver.io/images/docker-nzbhydra2)
- [hotio/prowlarr](https://github.com/Prowlarr/Prowlarr/)
- [linuxserver/plex](https://docs.linuxserver.io/images/docker-plex)
- [linuxserver/tautulli](https://docs.linuxserver.io/images/docker-tautulli)
- [linuxserver/jellyfin](https://docs.linuxserver.io/images/docker-jellyfin)
- [linuxserver/emby](https://docs.linuxserver.io/images/docker-emby)
- [linuxserver/embystat](https://docs.linuxserver.io/images/docker-embystat)
- [deluan/navidrome](https://github.com/deluan/navidrome)
- [sctx/overseerr](https://github.com/sct/overseerr)
- [phpmyadmin/phpmyadmin](https://hub.docker.com/r/phpmyadmin/phpmyadmin)
- [afian/filerun](https://hub.docker.com/r/afian/filerun) + [mariadb](https://hub.docker.com/_/mariadb?tab=tags&page=1&ordering=-name&name=10.1) v10.1
- [linuxserver/nextcloud](https://docs.linuxserver.io/images/docker-nextcloud) + [mariadb](https://hub.docker.com/_/mariadb?tab=tags&page=1&ordering=-name&name=10.5.8) v10.5.8
- [tzahi12345/youtubedl-material](https://github.com/Tzahi12345/YoutubeDL-Material)
- [lycheeorg/lychee](https://github.com/LycheeOrg/Lychee)
- [b4bz/homer](https://github.com/bastienwirtz/homer) v21.03.2
- [linuxserver/heimdall](https://docs.linuxserver.io/images/docker-heimdall)

The compose file in [Monitoring](Services/Monitoring) contains:

- [netdata/netdata](https://github.com/netdata/netdata)
- [grafana/grafana](https://github.com/grafana/grafana)
- [prom/prometheus](https://github.com/prometheus/prometheus)
- [influxdb](https://github.com/influxdata/influxdb) v1.8
- [boerderij/varken](https://github.com/Boerderij/Varken)
- [atribe/speedtest-for-influxdb-and-grafana](https://github.com/atribe/Speedtest-for-InfluxDB-and-Grafana)
- [amir20/dozzle](https://github.com/amir20/dozzle)
- [analogj/scrutiny](https://github.com/AnalogJ/scrutiny)

TODO:

- [ ] Minify compose file and traefik labels
- [ ] Move sensitive stuff to docker secrets instead of .env
