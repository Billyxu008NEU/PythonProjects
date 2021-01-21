# 100 Days of Code -> 54.Day 5 Project: Create a Password Generator 



#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

def PasswordGen_Easy():
	Password = ""
	for i in range(1, nr_letters + 1):
		Pass_letters = random.choice(letters)
		Password += Pass_letters 
		
	for i in range(1, nr_symbols + 1): 
		Pass_symbols = random.choice(symbols)
		Password += Pass_symbols
		
	for i in range(1, nr_numbers + 1): 
		Pass_numbers = random.choice(numbers)
		Password += Pass_numbers
		
	print(Password)
	
	
	
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
	
	
def PasswordGen_Hard(): 
	
	Final = []
	
	for i in range(1, nr_letters + 1):
		Pass_letters = random.choice(letters)
		Final.append(Pass_letters)
		
	for i in range(1, nr_symbols + 1): 
		Pass_symbols = random.choice(symbols)
		Final.append(Pass_symbols)
		
	for i in range(1, nr_numbers + 1): 
		Pass_numbers = random.choice(numbers)
		Final.append(Pass_numbers)
	
	

	print(Final)
	
	random.shuffle(Final)
	
	print(Final)
	

	password = ""
	for x in Final: 
		password += x
		
	print(f"Your Password not in order is now generated: {password}")
	
	
	
#PasswordGen_Easy()	
PasswordGen_Hard()
	


