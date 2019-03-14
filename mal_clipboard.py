import pyperclip
import random

def ad():
	
	websites = ['Get good deals at www.amazon.com',
	'Get Connected at www.facebook.com',
	'Spread some love at www.shaadi.com',
	'Extremely intelligent? www.twitter.com']

	website= random.choice(websites)
	
	pyperclip.copy(website)

if __name__=="__main__":
	ad()