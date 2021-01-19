## Parsing vnstat output

This is meant to run as a cronjob to get the total traffic out and in of the machine and display it on a panel on Grafana.

Replace `<user>` in the [bash file](./script.sh) and the line below to your needs, as well as the paths if needed. Also don't forget to make the bash file executable (`chmod +x`).

Then setup a cron job (I run mine every 5 minutes) by adding a line to your crontab like so:
```
*/5 * * * * /home/<user>/Services/Shared/Grafana/InternetUsage/vnstatParsing/script.sh
```

The JSON for my panel on Grafana dashboard is (I have 2; one for download traffic and another one for upload traffic):
```json
{
  "datasource": "Database",
  "fieldConfig": {
    "defaults": {
      "custom": {},
      "unit": "bytes",
      "decimals": 2,
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "#299c46",
            "value": null
          },
          {
            "color": "rgba(237, 129, 40, 0.89)",
            "value": 25
          },
          {
            "color": "#d44a3a",
            "value": 50
          }
        ]
      },
      "mappings": [
        {
          "$$hashKey": "object:223",
          "id": 0,
          "op": "=",
          "text": "N/A",
          "type": 1,
          "value": "null"
        }
      ],
      "nullValueMode": "connected"
    },
    "overrides": []
  },
  "gridPos": {
    "h": 4,
    "w": 3,
    "x": 18,
    "y": 73
  },
  "hideTimeOverride": true,
  "id": 243,
  "interval": "5m",
  "links": [],
  "maxDataPoints": 100,
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": [
        "lastNotNull"
      ],
      "fields": ""
    },
    "orientation": "horizontal",
    "textMode": "auto",
    "colorMode": "value",
    "graphMode": "area",
    "justifyMode": "auto"
  },
  "pluginVersion": "7.3.7",
  "targets": [
    {
      "alias": "Download Today",
      "groupBy": [
        {
          "params": [
            "month"
          ],
          "type": "tag"
        }
      ],
      "measurement": "internet_usage",
      "orderByTime": "ASC",
      "policy": "default",
      "refId": "B",
      "resultFormat": "time_series",
      "select": [
        [
          {
            "type": "field",
            "params": [
              "download"
            ]
          }
        ]
      ],
      "tags": [],
      "limit": "",
      "query": "SELECT \"download\" FROM \"internet_usage\" WHERE (\"day\" = 'select tag value') AND $timeFilter GROUP BY \"day\"",
      "rawQuery": false
    }
  ],
  "type": "stat",
  "timeFrom": "now/d",
  "transformations": [
    {
      "id": "organize",
      "options": {}
    }
  ],
  "timeShift": null,
  "cacheTimeout": null,
  "title": ""
}
```