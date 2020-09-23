#file_read.py

import sys
import os.path
from os import path

file_name = "test.txt"

def is_file(file_name):
	if path.isfile(file_name) == False:
		print(f"File does not exist matching this path: { file_name }")
		exit()

def read_file(file_name, dct):
	with open(file_name, 'r') as file:
		for line in file:
			if '#' not in line and line.isspace() == False:
				lst = line.split()
				device_attribute = lst[0]
				setting = lst[1]
				if device_attribute in dct:
					dct.update({device_attribute : setting})
					

def settings_update():
	pass
					
def read_lines(file_name):
    with open(file_name, 'r') as file:
	    file_contents = file.readlines()
	    return file_contents 					
				
			

def main():
	
	#dict
	settings = {"device_name" : None,"device_port" : None,
	 "device_purpose" : None}
	
	#Check if file exists
	is_file(file_name)
	
	#reading file
	read_file(file_name, settings)
	
	#seperate lines into variables
	print(settings)		
	


if __name__ == "__main__": main()
