import keyboard
import time
from random import choice
from string import ascii_letters, digits

def main():

	#while True:

	#time.sleep(3600)

	text = '+'.join(choice(ascii_letters+digits) for i in range(10))

	keyboard.press_and_release(text)

if __name__ == '__main__':
	main()