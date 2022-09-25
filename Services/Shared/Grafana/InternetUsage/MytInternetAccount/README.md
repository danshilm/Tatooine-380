## Myt Internet Account Usage Scraper

This is meant to run as a cronjob everyday to grab the remaining volume of data you can still upload/download in one month IF you use [MyT Home](https://home.myt.mu/) as your ISP.

Modify the `mytLoginDetails` and `influxdbDetails` variables to your needs and make sure to install the required packages with `yarn install` first inside the MytInternetAccount folder.

To run the script, use something like this:

```bash
cd /home/$USER/Services/Shared/Grafana/InternetUsage/MytInternetAccount && yarn dev
```

### Troubleshooting

If your cron isn't running, it might be because crons run in a pretty restricted environment; the PATH environment variable is usually only `/bin:/usr/bin`, so if whatever you're trying to run isn't being ran (for e.g. a `yarn` or `pnpm` command), check that.

I'd recommend setting the PATH variable in a bash script that's set to run in the crontab.

### Grafana Panel

The JSON for my panel on my Grafana dashboard is below. Keep in mind to update it to your own needs (it's probably just easier to refer to some of the key properties of the panel when making your own).

And here's what it looks like:

![bandwidth left panel](https://i.imgur.com/tozFOwb.png)

<details>
  <summary>Click to view panel json</summary>
  
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
    "datasource": {
      "uid": "000000006",
      "type": "influxdb"
    },
    "pluginVersion": "v1.0",
    "timeFrom": "now/M",
    "hideTimeOverride": true,
    "fieldConfig": {
      "defaults": {
        "mappings": [],
        "thresholds": {
          "mode": "absolute",
          "steps": [
            {
              "color": "green",
              "value": null
            }
          ]
        },
        "unit": "bytes"
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
      "textMode": "auto",
      "colorMode": "background",
      "graphMode": "area",
      "justifyMode": "auto",
      "text": {}
    },
    "targets": [
      {
        "alias": "Bandwidth Left",
        "datasource": {
          "type": "influxdb",
          "uid": "000000006"
        },
        "groupBy": [],
        "measurement": "internet_usage_myt",
        "orderByTime": "ASC",
        "policy": "default",
        "queryType": "randomWalk",
        "refId": "A",
        "resultFormat": "time_series",
        "select": [
          [
            {
              "type": "field",
              "params": [
                "data_left"
              ]
            }
          ]
        ],
        "tags": []
      }
    ],
    "interval": "1h"
  }
```

</details>
