len(1234)#yype error, number has no length
len("12234")
123,345,674#large number
123_234_546#large number
print(type(123))#type checking
print(int("113")+int("233"))
print(int("abc"))+int("233")#ValueError
print("Name of your pet is "+ len(input("what is your pet's name?")))#value error
print("Name of your pet is "+ str(len(input("what is your pet's name?"))))
print("my age is "+str(12))
#f-string
score=0
height=1.8
is_winning=True
print(f"Your score is = {score}, your height is {height} and you are winning is {is_winning} ")
print(123-3)
print(5/3)
print(5//3)
print(2**3)
bmi=84/1.65**2
print(bmi)
print(int(bmi))
print(round(bmi))
print(round(bm1,2))
print(6 + 4 / 2 - (1 * 2))#the result is presented as float so 6.0
print("welcome to the tip calculator")
bill = float(input("what was the total bill? $"))
tip = int(input("what percentahe tip would you like you like to give? 10 12 15 "))
people = int(input("how many people to split the bill"))
bill_with_tip=round(bill*(1+tip/100)/people,2)
print(f"Each person should pay: ${bill_with_tip}")


