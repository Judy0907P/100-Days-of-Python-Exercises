print("Welcome to the rollercoaster")
height=int(input("what is your height in cm/"))

if height > 120:
    print("You can ride the roller coaster")
    age=int(input("what is your age?"))
    bill=0
    if age<=12:
        bill=5
        print("child tickets are $5")
    elif age<=18:
        bill=8
        print("youth tickets are $8")
    elif age>45 and age<55:
        print("Midlife crisis! free ride!")
    else:
        bill=10
        print("adult tickets are $10")
else:
    print("sorry, you cannot ride")


wants_photo= input("do you want to have a photo take? Type y for Yes and n for No")
if wants_photo == "y":
    #add $3 to their bill
    bill=bill+3

print(f"your final bill is {bill}")



number_to_check=int(input("what is your input?"))
if number_to_check % 2==0:
    print("good")
else:
    print("bad")


print("welcome to pizzahut")
size=input("what size do you choose? S/M/L: ")
pep=input("do you want to add pep? Y or N: ")
extra_cheese=input("do you want extra cheese? Y or N: ")

# to do: work out how much they need to pay based on their sieze choice

bill=0
if size=="S":
    bill="15"
elif size=="M":
    bill=="20"
elif size=="L":
    bill="25"
else: 
    print("You typed the wrong inputs")

# to do: work out how much to add to their bill based on their pepperoni
if pep=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
 


# to do : work out their final amount on whether if they want extra cheese
if extra_cheese=="Y":
    bill+=1

print(f"Your final bill is: ${bill}")


print('''
      

#multply lines of string

     ''' )

print("welcome to treasure island")
print("your mission is to fint the treasure")
choice1=input('you\'re at a crossroad. where do you want to go? Type "left" or "right"\n').lower()
if choice1=="left":
    #continue in game
    choice2=input('you \'ve come to a lake. ' 
                'there is an island in the middle of the lake. ' 
                ' Type "wait" to wait for a boat. '
                'Type "swim" to swim across.\n').lower()
    if choice2=="swim":
        #continue in gamr
        choice3=input('you arrive at the island unharmed. '
                      'there is a house with 3 doors. '
                      'One red, one yellow and one blue.'
                      'which color do you choose?\n ').lower()
        if choice3== "red":
            print('game over')
        elif choice3=="yello":
            print('you win')
        elif choice3=="blue":
            print('game over')
        else:
            print('game over')

    else:
        print("game over")
        
else:
    print("game over")
