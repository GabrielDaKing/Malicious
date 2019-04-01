import keyboard
import pyautogui
from time import sleep

def download_python():

	keyboard.press_and_release("windows")
	sleep(3)
	keyboard.write("cmd")
	sleep(1)
	keyboard.press_and_release("enter")
	sleep(5)
	keyboard.write("pip install keyboard")
	sleep(1)
	keyboard.press_and_release("enter")
	sleep(5)
	keyboard.write("pip install pyperclip")
	sleep(1)
	keyboard.press_and_release("enter")

if __name__ == '__main__':
	download_python()

