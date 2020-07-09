To enable Discord notifications for Netdata (persist across container recreation):

1. Add Discord Webhook URL to `health_alarm_notify.conf` in the config folder [here](config/health_alarm_notify.conf#551).
2. Add the `DEFAULT_RECIPIENT_DISCORD` which is the channel you want the notifications to go to [here](config/health_alarm_notify.conf#557) (REQUIRED on a fresh install).
3. `sudo docker-compose up -d --force-recreate netdata`
3. `sudo docker exec -it /bin/sh netdata`
4. `export NETDATA_ALARM_NOTIFY_DEBUG=1`
5. `/usr/libexec/netdata/plugins.d/alarm-notify.sh test`
6. `export NETDATA_ALARM_NOTIFY_DEBUG=0` (if it works)