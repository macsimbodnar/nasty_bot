import time
from nasty_bot import NastyBot

if __name__ == "__main__":
	
	nasty_bot = NastyBot(message_id=1490039026379, group='19:c4e5e2a9247a4032a33abff9298a600e@thread.skype')
	
	nasty_bot.send_message('Hello to everyone! \nSono Nasty Bot e sono qui per allietare le vostre lunge giornate a Metid e, perchè no, anche insultarvi.')
	time.sleep(30)

	while True:
		frase = nasty_bot.generate_nasty()
		nasty_bot.send_message(frase);
		time.sleep(5)
		frase = nasty_bot.generate_nasty()
		nasty_bot.send_message(frase);
		time.sleep(5)
		frase = nasty_bot.generate_nasty()
		nasty_bot.change_title(frase);
		time.sleep(1800)
