#mal_flood.py
import os.path
from string import ascii_letters,digits
from random import choice

def flood():
	save_loc = 'C:/Users/gncis/Documents/Adobe'

	name = ''.join(choice(ascii_letters+digits) for i in range(10))
	text = ''.join(choice(ascii_letters+digits) for i in range(10))

	file_name = os.path.join(save_loc, name+".txt")

	with open(file_name+".txt", "w+") as file:
		file.write(text)

if __name__=="__main__":
	flood()