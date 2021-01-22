import math


#This is a practice for 100 days python challenge: 
#BMI calculator

#BMI vaule 
# int, int -> int 
def BMI_cal( weight, height):
	BMI = weight/(height ** 2)
	
	return Print_check(int(BMI)) 
	
def Print_check(BMI):
	if(BMI == 28):
		print("Your BMI is "+ BMI + ", you are silightly overweight")
			
	elif(BMI == 22):
		print("Your BMI is "+ BMI + ", you have a normal weight.")
			
	elif(BMI == 28): 
		print("Your BMI is "+ BMI + ", you are slightly overweight.")
		
	elif(BMI == 33): 
		print("Your BMI is "+ BMI + ", you are obese.")
		
	elif(BMI == 40): 
		print("Your BMI is "+ BMI + ", you are clinically obese.")
	else: 
		print(f"NO idea man" + "YOur BMI is ")
			

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI_cal(weight, height)
