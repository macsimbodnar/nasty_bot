import time
from nasty_bot import NastyBot

if __name__ == "__main__":
	
	nasty_bot = NastyBot()

	while True:
		
		nasty_bot.change_title();
		frase = nasty_bot.generate_nasty()
		nasty_bot.send_message(frase);
		time.sleep(10)
		frase = nasty_bot.generate_nasty()
		nasty_bot.send_message(frase);
		time.sleep(10)
		frase = nasty_bot.generate_nasty()
		nasty_bot.send_message(frase);
		time.sleep(1780)
