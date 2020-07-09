To enable Discord notifications for Netdata (not preserved across recreates):

1. `sudo docker exec -it netdata /bin/bash`
2. `cd /etc/netdata`
3. `./edit-config health_alarm_notify.conf`
4. Add Discord Webhook URL
5. `export NETDATA_ALARM_NOTIFY_DEBUG=1`
6. `/usr/libexec/netdata/plugins.d/alarm-notify.sh test`
7. `export NETDATA_ALARM_NOTIFY_DEBUG=0 (if good)`