## Myt Internet Account Usage Scraper

This is meant to run as a cronjob everyday to grab the remaining volume of data you can still upload/download in one month IF you use [MyT Home](https://home.myt.mu/) as your ISP.

Modify the `mytLoginDetails` and `influxdbDetails` variables to your needs and make sure to install the required packages with `yarn install` first inside the MytInternetAccount folder. 

To run the script, use something like this:

```bash
cd /home/user/Services/Shared/Grafana/InternetUsage/MytInternetAccount && yarn --silent start >> last_run.log 2>&1
```

The JSON for my panel on my Grafana dashboard is below. Keep in mind to update it to your own needs (it's probably just easier to refer to some of the key properties of the panel when making your own).
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
      "groupBy": [
        {
          "params": [
            "monthyear"
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
            "type": "field",
            "params": [
              "data_used"
            ]
          },
          {
            "type": "math",
            "params": [
              "*-1+2000000000000"
            ]
          }
        ]
      ],
      "tags": [],
      "datasource": {
        "uid": "000000006",
        "type": "influxdb"
      },
      "query": "SELECT \"data_used\" FROM \"internet_usage_myt\" WHERE $timeFilter GROUP BY \"monthyear\"",
      "rawQuery": false
    }
  ],
  "interval": null
}
```

</details>
