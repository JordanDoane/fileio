
with open("text.txt", 'w+') as file:
	file.write("Hello world")
	
with open("text.txt", 'r') as file:
	data = file.readline()
	print(data)
	if data == "Hello world":
		print("works")
	
	

    
