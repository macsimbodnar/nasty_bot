import requests
import json
import time
import random

soggetti = ['Max', 'Davide', 'Giorgio', 'Jacopo', 'Andrea', 'Gabry', 'Bianca', 'Francesco', 'Chiara', 'Seppia']

verbi = ['va', 'caga', 'urina', 'gingilla', 'scopa', 'ravana', 'perlustra','rumina', 'fuma', 'utilizza', 'picchia', 'scoreggia', 'puntualizza', 'corteggia', 'saccheggia', 'stalkerizza', 'annusa' ]

predicato = ['di soppiatto', 'con le mani', 'lo stantuffo', 'sua sorella', 'la sorella di Davide', 'l\'unicorno di Bianca', 'il computer', 'il glutine', 'l\'omino delle macchinette', 'le chiappe di Maurizio Costanzo', 'il Piccolo Lucio', 'l\'ano di Gianni Morandi', 'il pappagallo', 'Luke Skywalker', 'con Chuck Norris', 'la tavoletta del cesso', 'il perizoma di Mara Maionchi', 'nella borraccia di Giorgio']

content_type = 'application/json'
accept = 'application/json, text/javascript'
accept_encoding = 'gzip, deflate, sdch, br'
accept_language = 'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4'
behaviorOverride = 'redirectAs404'
cache_control = 'no-cache, no-store, must-revalidate'
client_info = 'os=Linux; osVer=U; proc=Linux x86_64; lcid=en-us; deviceType=1; country=IT; clientName=skype.com; clientVer=908/1.85.0.29//skype.com'
connection = 'keep-alive'
context_id = 'tcid=149003339670576180'
expires = '0' 
host = 'client-s.gateway.messenger.live.com'
origin = 'https://web.skype.com' 
pragma = 'no-cache'
referer = 'https://web.skype.com/it/'
registration_token = 'registrationToken=U2lnbmF0dXJlOjI6Mjg6QVFRQUFBQ2VjcGRrMDErTy9SckQzdjFSa1lPVDtWZXJzaW9uOjY6MToxO0lzc3VlVGltZTo0OjE5OjUyNDc5NDIzMTg4MzE5MTQxMzE7RXAuSWRUeXBlOjc6MToxO0VwLklkOjI6MjM6dGhlbWF6ZXJmYWtlckBnbWFpbC5jb207RXAuRXBpZDo1OjM2OjcwNWMzYWM4LTJiN2UtNDZhNC05YjQxLWIxYjc5Y2ZjYWU4YTtFcC5Mb2dpblRpbWU6NzoxOjA7RXAuQXV0aFRpbWU6NDoxOTo1MjQ3OTQyMzE4ODMwNTA3ODU4O0VwLkF1dGhUeXBlOjc6MjoxNTtFcC5FeHBUaW1lOjQ6MTk6NTI0Nzk0MzE3NjkxNzM4NzkwNDtVc3IuTmV0TWFzazoxMToxOjM7VXNyLlhmckNudDo2OjE6MDtVc3IuUmRyY3RGbGc6MjowOjtVc3IuRXhwSWQ6OToxOjA7VXNyLkV4cElkTGFzdExvZzo0OjE6MDtVc2VyLkF0aEN0eHQ6Mjo0MjA6Q2xOcmVYQmxWRzlyWlc0WGRHaGxiV0Y2WlhKbVlXdGxja0JuYldGcGJDNWpiMjBCQTFWcFl4UXhMekV2TURBd01TQXhNam93TURvd01DQkJUUXhPYjNSVGNHVmphV1pwWldTbDRVYzU5WGhCNFFBQUFBQUFBRUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFTYkdsMlpUcDBhR1Z0WVhwbGNtWmhhMlZ5QUFBQUFBQUFBQUFBQjA1dlUyTnZjbVVBQUFBQUJBQUFBQUFBQUFBQUFBQUFwZUZIT2ZWNFFlRUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBRVNiR2wyWlRwMGFHVnRZWHBsY21aaGEyVnlBQUFBQUFBQUFBQUFDQUFBQUFOVmFXTUlTV1JsYm5ScGRIa09TV1JsYm5ScGRIbFZjR1JoZEdVSVEyOXVkR0ZqZEhNT1EyOXVkR0ZqZEhOVmNHUmhkR1VJUTI5dGJXVnlZMlVOUTI5dGJYVnVhV05oZEdsdmJoVkRiMjF0ZFc1cFkyRjBhVzl1VW1WaFpFOXViSGs9Ow=='
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'


def change_title(topic, group = ''):

	if group == '':
		group = '19:688e93554a9f4374b088cc798e6647e8@thread.skype'
	
	url = 'https://client-s.gateway.messenger.live.com/v1/threads/'+ group + '/properties?name=topic';
	payload = '{"topic":"' + topic + '"}'
	content_length = 12 + len(topic)

	headers = {'content-type': content_type, 'Accept': accept, 'Accept-Encoding': accept_encoding, 'Accept-Language':  accept_language, 'BehaviorOverride': behaviorOverride, 'Cache-Control': cache_control, 'ClientInfo': client_info, 'Connection': connection, 'Content-Length': content_length, 'ContextId': context_id, 'Expires': expires, 'Host': host, 'Origin': origin, 'Pragma': pragma, 'Referer': referer, 'RegistrationToken': registration_token, 'User-Agent': user_agent}

	r = requests.put(url, data=payload, headers=headers)
	print("Fatto il misfatto")
	return r


def send_message(message, message_id):	


	url = 'https://client-s.gateway.messenger.live.com/v1/users/ME/conversations/19:c4e5e2a9247a4032a33abff9298a600e@thread.skype/messages'
	payload = '{"content":"' + message + '","messagetype":"RichText","contenttype":"text","Has-Mentions":"false","imdisplayname":"Nasty Bot","clientmessageid":"' + str(message_id) + '"}'
	
	content_length = len(payload)

	headers = {'content-type': content_type, 'Accept': accept, 'Accept-Encoding': accept_encoding, 'Accept-Language':  accept_language, 'BehaviorOverride': behaviorOverride, 'Cache-Control': cache_control, 'ClientInfo': client_info, 'Connection': connection, 'Content-Length': content_length, 'ContextId': context_id, 'Expires': expires, 'Host': host, 'Origin': origin, 'Pragma': pragma, 'Referer': referer, 'RegistrationToken': registration_token, 'User-Agent': user_agent}

	r = requests.post(url, data=payload, headers=headers)

	
	print("Fatto il misfatto 2")
	return r



def generate_nasty():

	nasty = ''
	nasty = random.choice(soggetti) +" "+ random.choice(verbi) +" "+ random.choice(predicato)

	return nasty


if __name__ == "__main__":
	
	message_id = 1490033396921
	send_message('Hello! \nSono Nasty Bot e sono qui per servire e insultare!', message_id)
	while True:
		message_id = message_id + 1
		send_message(generate_nasty(), message_id);
		time.sleep(5)
		

