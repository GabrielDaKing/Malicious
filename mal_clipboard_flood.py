import pyperclip
from random import choice
from string import ascii_letters,digits,whitespace
from time import sleep

def flood():

	#while True:

		text = ''.join(choice(ascii_letters+digits+whitespace) for i in range(2))
		pyperclip.copy(text)
		sleep(3600)

if __name__=="__main__":
	flood()