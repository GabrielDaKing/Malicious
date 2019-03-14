import pyautogui
import keyboard
import time

def main():

	pyautogui.moveTo(1900, 25)
	pyautogui.click()
	keyboard.write("chrome")
	keyboard.press_and_release('enter')
	time.sleep(5)
	keyboard.press_and_release('ctrl+n')
	keyboard.write("stuff")


if __name__ == '__main__':
	main()