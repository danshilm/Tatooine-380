Install instructions for Varken are [here](https://wiki.cajun.pro/books/varken/page/docker) if you don't want to use my compose file.

Pay special attention to section 4 of the docs under the heading `docker-compose` which states that:
> The Grafana container requires specific folder permissions ([since 5.1](https://grafana.com/docs/installation/docker/#migration-from-a-previous-version-of-the-docker-container-to-5-1-or-later)). Change the user/group ownership of your grafana data directory to 472. Example: `chown 472:472 /opt/dockerconfigs/grafana` 