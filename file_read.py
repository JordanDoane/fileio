#file_read.py

import sys
import os.path
from os import path

file_name = "‪‪C:\Users\jorda\Desktop\\file"

def is_file(file_name):
	if path.isfile(file_name) == False:
		print(f"File does not exist matching this path: { file_name }")
		exit()
		
def read_file(file_name, dct):
	with open(file_name, 'r') as file:
		for line in file:
			string = line
			if '#' not in string and string.isspace() == False:
				lst = string.split()
				#print(lst)
				
				kwd = lst[0]
				setting = lst[1]
				if kwd in dct:
					dct.update({kwd : setting})
					print(dct)

def dct_update():
	pass
					
					
				
			

def main():
	
	#dict
	dct = {"device_name" : None,"device_port" : None,
	 "device_purpose" : None}
	
	#Check if file exists
	is_file(file_name)
	
	#reading file
	read_file(file_name, dct)
	
	#seperate lines into variables
	
				
	


if __name__ == "__main__": main()
