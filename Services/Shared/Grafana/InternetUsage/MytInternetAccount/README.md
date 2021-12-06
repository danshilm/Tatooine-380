## Myt Internet Account Usage Scraper

This is meant to run as a cronjob (I run it hourly personally) to grab the remaining volume of data you can still use in one month IF you use [MyT Home](https://home.myt.mu/) as your ISP.

Modify the `internetAccountUsername`, `internetAccountPassword` and `influx` variables to your needs and make sure to install the required packages with `npm install` first inside the MytInternetAccount folder. 

To run the script, use something like this:
```bash
node /home/user/Services/Shared/Grafana/InternetUsage/MytInternetAccount/app.js >> /home/user/Services/Shared/Grafana/InternetUsage/MytInternetAccount/last_run.log 2>&1
```

The JSON for my panel on my Grafana dashboard is below. Keep in mind to update it to your own needs.
```json
{
  "id": 242,
  "gridPos": {
    "h": 3,
    "w": 5,
    "x": 15,
    "y": 80
  },
  "type": "stat",
  "datasource": "Manual",
  "pluginVersion": "8.0.4",
  "timeFrom": "now/M",
  "hideTimeOverride": true,
  "interval": "1h",
  "fieldConfig": {
    "defaults": {
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": null
          }
        ]
      },
      "mappings": [],
      "unit": "deckbytes"
    },
    "overrides": []
  },
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": [
        "lastNotNull"
      ],
      "fields": ""
    },
    "orientation": "auto",
    "text": {},
    "textMode": "auto",
    "colorMode": "background",
    "graphMode": "area",
    "justifyMode": "auto"
  },
  "targets": [
    {
      "alias": "Bandwidth Left",
      "groupBy": [
        {
          "params": [
            "month"
          ],
          "type": "tag"
        }
      ],
      "measurement": "internet_usage_myt",
      "orderByTime": "ASC",
      "policy": "default",
      "queryType": "randomWalk",
      "refId": "A",
      "resultFormat": "time_series",
      "select": [
        [
          {
            "params": [
              "data_left"
            ],
            "type": "field"
          }
        ]
      ],
      "tags": []
    }
  ],
  "maxDataPoints": null,
  "timeShift": null
}
```
