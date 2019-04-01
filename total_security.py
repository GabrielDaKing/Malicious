from webbrowser import *
from time import *
from random import *

def webpage():

	#while True:

	a = randint(1, 5)
	websites = ['www.amazon.co.in','www.google.com','www.facebook.com','www.twitter.com','www.flipkart.com']

	open_new(websites[a])

if __name__=="__main__":
	webpage()