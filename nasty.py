import requests
import json

content_type = 'application/json'
accept = 'application/json, text/javascript'
accept_encoding = 'gzip, deflate, sdch, br'
accept_language = 'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4'
behaviorOverride = 'redirectAs404'
cache_control = 'no-cache, no-store, must-revalidate'
client_info = 'os=Linux; osVer=U; proc=Linux x86_64; lcid=en-us; deviceType=1; country=IT; clientName=skype.com; clientVer=908/1.85.0.27//skype.com'
connection = 'keep-alive'
context_id = 'tcid=149002675925422311'
expires = '0' 
host = 'client-s.gateway.messenger.live.com'
origin = 'https://web.skype.com' 
pragma = 'no-cache'
referer = 'https://web.skype.com/it/'
registration_token = 'registrationToken=U2lnbmF0dXJlOjI6Mjg6QVFRQUFBQ3ZoS0JiNTllOElwTVpGRndOWXBsWDtWZXJzaW9uOjY6MToxO0lzc3VlVGltZTo0OjE5OjUyNDc5NDIxNzIxMTc0NzAzMzI7RXAuSWRUeXBlOjc6MToxO0VwLklkOjI6Mzg6Y2lkLSgtNjA1NjIyODUyMjYwMjI4Njc0OSlAb3V0bG9vay5jb207RXAuRXBpZDo1OjM2OjE0MDRlZWQ3LTE3M2MtNGI5OC05ZTI1LTlhMDBlMWFiMDk5YjtFcC5Mb2dpblRpbWU6NzoxOjA7RXAuQXV0aFRpbWU6NDoxOTo1MjQ3OTQyMTcyMTE1NTk1MzAxO0VwLkF1dGhUeXBlOjc6MjoxNTtFcC5FeHBUaW1lOjQ6MTk6NTI0Nzk0MzAzNTI1NzM4NzkwNDtVc3IuTmV0TWFzazoxMToxOjM7VXNyLlhmckNudDo2OjE6MDtVc3IuUmRyY3RGbGc6MjowOjtVc3IuRXhwSWQ6OToxOjA7VXNyLkV4cElkTGFzdExvZzo0OjE6MDtVc2VyLkF0aEN0eHQ6Mjo0MjQ6Q2xOcmVYQmxWRzlyWlc0bVkybGtMU2d0TmpBMU5qSXlPRFV5TWpZd01qSTROamMwT1NsQWIzVjBiRzl2YXk1amIyMEJBMVZwWXhReEx6RXZNREF3TVNBeE1qb3dNRG93TUNCQlRReE9iM1JUY0dWamFXWnBaV1Jqc2JQM1B2VHpxd0FBQUFBQUFFQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQU1iV0ZqYzJsdFltOWtibUZ5QUFBQUFBQUFBQUFBQjA1dlUyTnZjbVVBQUFBQUJBQUFBQUFBQUFBQUFBQUFZN0d6OXo3MDg2c0FBQUFBQUFBQUFBQUFBQUFBQUFBQUFBRU1iV0ZqYzJsdFltOWtibUZ5QUFBQUFBQUFBQUFBQ0FBQUFBTlZhV01JU1dSbGJuUnBkSGtPU1dSbGJuUnBkSGxWY0dSaGRHVUlRMjl1ZEdGamRITU9RMjl1ZEdGamRITlZjR1JoZEdVSVEyOXRiV1Z5WTJVTlEyOXRiWFZ1YVdOaGRHbHZiaFZEYjIxdGRXNXBZMkYwYVc5dVVtVmhaRTl1YkhrPTs='
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'

def change_title(topic, gruppo = ''):

	if gruppo == '':
		gruppo = '19:688e93554a9f4374b088cc798e6647e8@thread.skype'
	
	url = 'https://client-s.gateway.messenger.live.com/v1/threads/'+ gruppo + '/properties?name=topic';
	payload = '{"topic":"' + topic + '"}'
	content_length = 12 + len(topic)

	headers = {'content-type': content_type, 'Accept': accept, 'Accept-Encoding': accept_encoding, 'Accept-Language':  accept_language, 'BehaviorOverride': behaviorOverride, 'Cache-Control': cache_control, 'ClientInfo': client_info, 'Connection': connection, 'Content-Length': content_length, 'ContextId': context_id, 'Expires': expires, 'Host': host, 'Origin': origin, 'Pragma': pragma, 'Referer': referer, 'RegistrationToken': registration_token, 'User-Agent': user_agent}

	r = requests.put(url, data=payload, headers=headers)
	print("Fatto il misfatto")
	return r

if __name__ == "__main__":
	change_title('Evviva la figa')