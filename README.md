# Tatooine-380
A collection of scripts and dockers for my home media server

TODO:
- [X] Add Traefik configurations
- [X] Add Authelia configurations
- [ ] Minify compose file and traefik labels
- [ ] Make Sabnzbd and Authelia work with Nzb360
- [ ] Adapt [guillaumebriday/traefik-custom-error-pages](https://github.com/guillaumebriday/traefik-custom-error-pages) for Traefik:v2.2 (refer to [this example](https://github.com/jamescurtin/traefik-proxy) on how to be clean)
- [ ] Move sensitive stuff to docker secrets instead of .env
- [X] Add netdata
- [X] Standardize folders so that Sonarr/Radarr don't think they are moving files across different drives - refer to [avoid common pitfalls](https://sonarr.tv/#downloads-v3-docker)