To enable Discord notifications for Netdata (not preserved across recreates):

1. `sudo docker exec -it netdata /bin/bash`
2. `cd /etc/netdata`
3. `./edit-config health_alarm_notify.conf`
4. Disable E-mail notifications
5. Add Discord Webhook URL
6. `export NETDATA_ALARM_NOTIFY_DEBUG=1`
7. `/usr/libexec/netdata/plugins.d/alarm-notify.sh test`
8. `export NETDATA_ALARM_NOTIFY_DEBUG=0 (if good)`