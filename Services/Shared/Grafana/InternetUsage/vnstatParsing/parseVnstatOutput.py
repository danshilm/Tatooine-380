import sys
import json
from datetime import date, datetime, timezone
from influxdb import InfluxDBClient
from influxdb.exceptions import InfluxDBServerError
from requests.exceptions import ConnectionError

# change the connection details to connect to your influxdb container/install
client = InfluxDBClient(host='localhost', port=8086, database='Database')
payload = []

def main(period):
	if period == 'day':
		with open('vnstatOutputTest.json', 'r') as read_file:
			data = json.load(read_file)

			for one_period in data['interfaces'][0]['traffic'][period]:
				now = datetime.now(timezone.utc).astimezone().isoformat()
				print(
					f"Download: {round(one_period['rx']/1024)} MB, Upload: {round(one_period['tx']/1024)} MB.")
				payload.append(
					{
						'measurement': 'internet_usage',
						'tags': {
							'year': one_period['date']['year'],
							'month': f"{one_period['date']['month']:02}",
							'day': f"{one_period['date']['day']:02}",
						},
						'time': now,
						'fields': {
							'download': one_period['rx'],
							'upload': one_period['tx']
						}
					}
				)
	else:
		print('Invalid period of time argument')
	
	if (payload != []):
		try:
			r = client.write_points(payload)
			print(f"Response: {r}")
		except (InfluxDBServerError, ConnectionError) as e:
			print('Error writing data to influxdb. Dropping this set of data. '
				'Check your database! Error: %s', e)

	client.close()

if __name__ == '__main__':
	main(sys.argv[1])
