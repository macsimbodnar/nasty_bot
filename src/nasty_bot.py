import requests
import json
import random

soggetti = ['Max', 'Davide', 'Giorgio', 'Jacopo', 'Andrea', 'Gabry', 'Bianca', 'Francesco', 'Chiara', 'Seppia']

verbi = ['caga', 'ama tantissumo urinare', 'scopa', 'ama ravanare', 'perlustra','rumina', 'si diverte a fumare', 'utilizza', 'si diverte a picchiare', 'scoreggia', 'continua a puntualizzare', 'corteggia', 'saccheggia', 'stalkerizza', 'annusa solitamente', 'ama sparare', 'suda abbondantemente', 'si diverte a bere']

predicato = ['di soppiatto', 'con le mani', 'lo stantuffo', 'sua sorella', 'la sorella di Davide', 'l\'unicorno di Bianca', 'sul computer', 'il glutine', 'l\'omino delle macchinette', 'le chiappe di Maurizio Costanzo', 'il Piccolo Lucio', 'l\'ano di Gianni Morandi', 'il pappagallo', 'con Chuck Norris', 'la tavoletta del cesso', 'il perizoma di Mara Maionchi', 'nella borraccia di Giorgio', 'in mutande', 'senza calze', 'ogni volta che beve il tea delle 16.00', 'ogni volta che fa la mossa della piccionata', 'durante gli eventi di Spazio Petardo', 'ai concerti di Laura Pausini', 'una canzone neomelodica napoletana di Luca Sarracino', 'il pappagallo di Ada', 'mentre usa lo Studio di Pok', 'Padre Maronno', 'ascoltando pezzi di Gigi D Agostino', 'una lasagna/lavagna']

titolo =['Piovono Panini senza Glutine', 'Sudo rm -rf/', 'NastyBot conquista Metid', 'L\'orario di merda', 'Chuck Norris non vi ama', 'Il pappagallo senza gambe', 'Gli amici del piccolo lucio', 'Luca Sarracino fans club', 'le principesse della Disney', 'ascoltando pezzi di Gigi D Agostino', 'una Lasagna con la Lavagna']

class NastyBot:
	"""A Nasty class for Nasty class bot"""

	def __init__(self, content_type = 'application/json',
						accept = 'application/json, text/javascript',
						accept_encoding = 'gzip, deflate, sdch, br',
						accept_language = 'it-IT,it;q=0.8,en-US;q=0.6,en;q=0.4',
						behavior_override = 'redirectAs404',
						cache_control = 'no-cache, no-store, must-revalidate',
						client_info = 'os=Linux; osVer=U; proc=Linux x86_64; lcid=en-us; deviceType=1; country=IT; clientName=skype.com; clientVer=908/1.85.0.29//skype.com',
						connection = 'keep-alive',
						context_id = 'tcid=149009530369523223',
						expires = '0',
						host = 'client-s.gateway.messenger.live.com',
						origin = 'https://web.skype.com',
						pragma = 'no-cache',
						referer = 'https://web.skype.com/it/',
						registration_token = 'registrationToken=U2lnbmF0dXJlOjI6Mjg6QVFRQUFBQytPQ0ozbkpObjk4eUp4TzdRV1hpaDtWZXJzaW9uOjY6MToxO0lzc3VlVGltZTo0OjE5OjUyNDc5NDI5Mjg0MDIwOTk0MDI7RXAuSWRUeXBlOjc6MToxO0VwLklkOjI6MjM6dGhlbWF6ZXJmYWtlckBnbWFpbC5jb207RXAuRXBpZDo1OjM2OmE4YjUzODRiLTc1YmUtNDlkNC1hMWM0LTZlYzI4NmVlYmQzOTtFcC5Mb2dpblRpbWU6NzoxOjA7RXAuQXV0aFRpbWU6NDoxOTo1MjQ3OTQyOTI4NDAwNTM2ODgzO0VwLkF1dGhUeXBlOjc6MjoxNTtFcC5FeHBUaW1lOjQ6MTk6NTI0Nzk0Mzc5MjM3NzM4NzkwNDtVc3IuTmV0TWFzazoxMToxOjM7VXNyLlhmckNudDo2OjE6MDtVc3IuUmRyY3RGbGc6MjowOjtVc3IuRXhwSWQ6OToxOjA7VXNyLkV4cElkTGFzdExvZzo0OjE6MDtVc2VyLkF0aEN0eHQ6Mjo0MjA6Q2xOcmVYQmxWRzlyWlc0WGRHaGxiV0Y2WlhKbVlXdGxja0JuYldGcGJDNWpiMjBCQTFWcFl4UXhMekV2TURBd01TQXhNam93TURvd01DQkJUUXhPYjNSVGNHVmphV1pwWldTbDRVYzU5WGhCNFFBQUFBQUFBRUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFTYkdsMlpUcDBhR1Z0WVhwbGNtWmhhMlZ5QUFBQUFBQUFBQUFBQjA1dlUyTnZjbVVBQUFBQUJBQUFBQUFBQUFBQUFBQUFwZUZIT2ZWNFFlRUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBRVNiR2wyWlRwMGFHVnRZWHBsY21aaGEyVnlBQUFBQUFBQUFBQUFDQUFBQUFOVmFXTUlTV1JsYm5ScGRIa09TV1JsYm5ScGRIbFZjR1JoZEdVSVEyOXVkR0ZqZEhNT1EyOXVkR0ZqZEhOVmNHUmhkR1VJUTI5dGJXVnlZMlVOUTI5dGJYVnVhV05oZEdsdmJoVkRiMjF0ZFc1cFkyRjBhVzl1VW1WaFpFOXViSGs9Ow==',
						user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
						group = '19:a39038e324a342b89aa173e51f00eccf@thread.skype',
						message_id = 1490106318744):

		self.content_type = content_type
		self.accept = accept
		self.accept_encoding = accept_encoding
		self.accept_language = accept_language
		self.behavior_override = behavior_override
		self.cache_control = cache_control
		self.client_info = client_info
		self.connection = connection
		self.context_id = context_id
		self.expires = expires
		self.host = host
		self.origin = origin
		self.pragma = pragma
		self.referer = referer
		self.registration_token = registration_token
		self.user_agent = user_agent
		self.group = group
		self.message_id = message_id
		
		print('I signori Max e Davide Consiglieri e Alleati dei Magici Malfattori sono fieri di presentarvi Il Nasty Bot')




	def change_title(self, topic=random.choice(titolo), group = ''):

		print('Lumus')
		if group == '':
			group = self.group
		
		url = 'https://client-s.gateway.messenger.live.com/v1/threads/'+ group + '/properties?name=topic';
		payload = '{"topic":"' + topic + '"}'
		content_length = len(payload)

		headers = {'content-type': self.content_type, 'Accept': self.accept, 'Accept-Encoding': self.accept_encoding, 
								'Accept-Language':  self.accept_language, 'BehaviorOverride': self.behavior_override, 
								'Cache-Control': self.cache_control, 'ClientInfo': self.client_info, 'Connection': self.connection, 
								'Content-Length': content_length, 'ContextId': self.context_id, 'Expires': self.expires, 
								'Host': self.host, 'Origin': self.origin, 'Pragma': self.pragma, 'Referer': self.referer, 
								'RegistrationToken': self.registration_token, 'User-Agent': self.user_agent}

		
		r = requests.put(url, data=payload, headers=headers)
		print("Nox")
		print(r)

		return None



	def send_message(self, message='', message_id='', group=''):	
		print('Giuro solennemente di non avere buone intenzion')
		if message_id == '':
			message_id = self.message_id

		if group == '':
			group = self.group

		url = 'https://client-s.gateway.messenger.live.com/v1/users/ME/conversations/' + group + '/messages'
		payload = '{"content":"' + message + '","messagetype":"RichText","contenttype":"text","Has-Mentions":"false","imdisplayname":"Nasty Bot","clientmessageid":"' + str(message_id) + '"}'
		content_length = len(payload)

		headers = {'content-type': self.content_type, 'Accept': self.accept, 'Accept-Encoding': self.accept_encoding, 
								'Accept-Language':  self.accept_language, 'BehaviorOverride': self.behavior_override, 
								'Cache-Control': self.cache_control, 'ClientInfo': self.client_info, 'Connection': self.connection, 
								'Content-Length': content_length, 'ContextId': self.context_id, 'Expires': self.expires, 
								'Host': self.host, 'Origin': self.origin, 'Pragma': self.pragma, 'Referer': self.referer, 
								'RegistrationToken': self.registration_token, 'User-Agent': self.user_agent}


		r = requests.post(url, data=payload, headers=headers)
		
		self.message_id = message_id + 100
		print("Fatto il misfatto")
		print(r)
		return r

	def generate_nasty(self):
		nasty = random.choice(soggetti) + " " + random.choice(verbi) + " " + random.choice(predicato)
		return nasty
