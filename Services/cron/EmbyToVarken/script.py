# go through all sessions
# find those with "NowPlayingItem"
# fill in the same data as varken does

import requests
import json
import re
from datetime import datetime, timezone, date, timedelta
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
from influxdb.exceptions import InfluxDBServerError
from hashlib import md5

EMBY_URL = "http://localhost:8096/emby/Sessions?api_key=apikey"
# INFLUX_URL = "http://localhost:8086/write?db=varken"
response = requests.get(url = EMBY_URL)
sessions = response.json()
client = InfluxDBClient(host='localhost', port=8086, database='varken')
payload = []

def hashit(string):
	encoded = string.encode()
	hashed = md5(encoded).hexdigest()
	return hashed

for session in sessions:
	session_dict = {}
	if ("NowPlayingItem" in session):

		if ("SeriesName" in session['NowPlayingItem']):
			# will change in the future for SeriesName - S00E00 EpisodeName
			# it's just more easily identifiable that way
			media_title = session['NowPlayingItem']['SeriesName'] + " - " + session['NowPlayingItem']['Name']
			session_dict['title'] = media_title
			session_dict['media_type'] = "Episode"
		else:
			session_dict['title'] = session['NowPlayingItem']['Name']
			session_dict['media_type'] = "Movie"

		if (session['PlayState']['PlayMethod'] == "DirectStream"):
			session_dict['video_decision'] = "Direct Stream"
		elif (session['PlayState']['PlayMethod'] == "DirectPlay"):
			session_dict['video_decision'] = "Direct Play"
		else:
			session_dict['video_decision'] = "Transcode"
		
		if (session['PlayState']['PlayMethod'] == "DirectStream" or session['PlayState']['PlayMethod'] == "DirectPlay"):
			session_dict['quality_profile'] = "Original"
			
			if (session['NowPlayingItem']['Width'] <= 640):
				session_dict['quality'] = "SD"
			elif (session['NowPlayingItem']['Width'] <= 854):
				session_dict['quality'] = "480p"
			elif (session['NowPlayingItem']['Width'] <= 1280):
				session_dict['quality'] = "720p"
			elif (session['NowPlayingItem']['Width'] <= 1920):
				session_dict['quality'] = "1080p"
			elif (session['NowPlayingItem']['Width'] <= 2560):
				session_dict['quality'] = "1440p"
			elif (session['NowPlayingItem']['Width'] <= 3840):
				session_dict['quality'] = "4K"

			session_dict['transcode_hw_decoding'] = 0
			session_dict['transcode_hw_encoding'] = 0

		else:

			if (session['TranscodingInfo']['Width'] <= 640):
				session_dict['quality'] = "SD"
				session_dict['quality_profile'] = "SD"
			elif (session['TranscodingInfo']['Width'] <= 854):
				session_dict['quality'] = "480p"
				session_dict['quality_profile'] = "480p"
			elif (session['TranscodingInfo']['Width'] <= 1280):
				session_dict['quality'] = "720p"
				session_dict['quality_profile'] = "720p"
			elif (session['TranscodingInfo']['Width'] <= 1920):
				session_dict['quality'] = "1080p"
				session_dict['quality_profile'] = "1080p"
			elif (session['TranscodingInfo']['Width'] <= 2560):
				session_dict['quality'] = "1440p"
				session_dict['quality_profile'] = "1440p"
			elif (session['TranscodingInfo']['Width'] <= 3840):
				session_dict['quality'] = "4K"
				session_dict['quality_profile'] = "4K"

			if (session['TranscodingInfo']['VideoDecoderIsHardware'] == True):
				session_dict['transcode_hw_decoding'] = 1
			else:
				session_dict['transcode_hw_decoding'] = 0

			if (session['TranscodingInfo']['VideoEncoderIsHardware'] == True):
				session_dict['transcode_hw_encoding'] = 1
			else:
				session_dict['transcode_hw_encoding'] = 0

		if (session['PlayState']['IsPaused'] == True):
			session_dict['player_state'] = 1
		else:
			session_dict['player_state'] = 0

		session_dict['progress_percent'] = round((session['PlayState']['PositionTicks'] / session['NowPlayingItem']['RunTimeTicks']) * 100)

		if (session_dict['video_decision'] == "Direct Play" or session_dict['video_decision'] == "Direct Stream"):
			session_dict['audio_codec'] = session['NowPlayingItem']['MediaStreams'][session['PlayState']['AudioStreamIndex']]['Codec']
		else:
			session_dict['audio_codec'] = session['TranscodingInfo']['AudioCodec']

		hash_id = hashit(f"{session['Id']}{session['UserName']}{session['DeviceId']}")
		now = now = datetime.now(timezone.utc).astimezone().isoformat()
		payload.append(
			{
				"measurement": "Tautulli",
				"tags": {
					"type": "Session",
					"session_id": session['Id'],
					"friendly_name": session['UserName'],
					"username": session['UserName'],
					"title": session_dict['title'],
					"product": session['Client'],
					"platform": session['DeviceName'],
					"product_version": session['ApplicationVersion'],
					"quality": session_dict['quality'],
					"video_decision": session_dict['video_decision'],
					"transcode_decision": session_dict['video_decision'],
					"transcode_hw_decoding": session_dict['transcode_hw_decoding'],
					"transcode_hw_encoding": session_dict['transcode_hw_encoding'],
					"media_type": session_dict['media_type'],
					"audio_codec": session_dict['audio_codec'].upper(),
					"audio_profile": session_dict['audio_codec'].upper(),
					"stream_audio_codec": session_dict['audio_codec'].upper(),
					"quality_profile": session_dict['quality_profile'],
					"progress_percent": session_dict['progress_percent'],
					# "region_code": geodata.subdivisions.most_specific.iso_code,
					"location": "wip",
					"full_location": "wip",
					# "latitude": 0,
					# "longitude": 0,
					"player_state": session_dict['player_state'],
					"device_type": session['Client'],
					"relayed": 0,
					"secure": 1,
					"server": 1
				},
				"time": now,
				"fields": {
					"hash": hash_id
				}
			}
		)

if (payload != []):
	try:
		# print("sending to InfluxDB")
		r = client.write_points(payload)
		# print(r)
	except (InfluxDBServerError, ConnectionError) as e:
		print('Error writing data to influxdb. Dropping this set of data. '
            'Check your database! Error: %s', e)

# print(sessions)
print(payload)
client.close()
