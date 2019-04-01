import keyboard
import time
from random import choice
from string import ascii_letters, digits

def main():

	#while true:
	text = '+'.join(choice(ascii_letters+digits) for i in range(100))

	keyboard.press_and_release(text)

if __name__ == '__main__':
	main()