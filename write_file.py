# write_file.py

import os.path
from os import path

file_name = "test.txt"

		
def main():
	
		
	if path.isfile("test.txt") == False: 
		
		print("Opening a new file.")
		
		with open(file_name, 'w+') as file:
			file.writelines(""" 
#This is a default file. Make changes where needed
			
	device_name = None
	device_ip = None
	device_purpose = None
			
			""")
			

	
	
	
		
	
	
	

if __name__ == "__main__": main()
