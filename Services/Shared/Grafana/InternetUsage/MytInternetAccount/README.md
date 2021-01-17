## Myt Internet Account Usage Scraper

This is meant to run as a cronjob (I run it hourly personally) to grab the remaining volume of data you can still use in one month IF you use [MyT Home](https://home.myt.mu/) as your ISP.

Modify the `internetAccountUsername`, `internetAccountPassword` and `influx` variables to your needs and make sure to install the required packages with `npm install` first inside the MytInternetAccount folder. 

To run the script, use something like this:
```bash
node /home/user/Services/Shared/Grafana/InternetUsage/MytInternetAccount/app.js >> /home/user/Services/Shared/Grafana/InternetUsage/MytInternetAccount/last_run.log 2>&1
```

The JSON for my panel on my Grafana dashboard is:
```json
{
  "datasource": "Database",
  "fieldConfig": {
    "defaults": {
      "custom": {},
      "unit": "deckbytes",
      "thresholds": {
        "mode": "absolute",
        "steps": [
          {
            "color": "green",
            "value": null
          }
        ]
      },
      "mappings": []
    },
    "overrides": []
  },
  "gridPos": {
    "h": 2,
    "w": 5,
    "x": 13,
    "y": 79
  },
  "id": 242,
  "interval": "1h",
  "options": {
    "reduceOptions": {
      "values": false,
      "calcs": [
        "lastNotNull"
      ],
      "fields": ""
    },
    "orientation": "auto",
    "textMode": "auto",
    "colorMode": "background",
    "graphMode": "area",
    "justifyMode": "auto"
  },
  "pluginVersion": "7.3.7",
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
  "type": "stat",
  "timeFrom": null,
  "timeShift": null,
  "title": ""
}
```