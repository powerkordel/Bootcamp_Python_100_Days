

#Day 3 If Else elif statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have to grow taller before you can ride.")

# even/odd program
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print(f"Number {number} is even.")
else:
    print(f"Number {number} is odd.")



#nested if/else/elif

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have  to grow taller before you can ride.")



#interactive BMI

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = int(weight)/float(height)**2
formated_bmi = "{:.2f}".format(bmi)
if bmi < 18.5:
    print(f"your BMI is {formated_bmi}. You are underweight")
elif bmi > 18.5 and bmi < 25:
    print(f"your BMI is {formated_bmi}. You have a normal weight")
elif bmi > 25 and bmi < 30:
    print(f"your BMI is {formated_bmi}. You are overweight")
elif bmi > 30 and bmi < 35:
    print(f"your BMI is {formated_bmi}. You are obese")
elif bmi > 35:
    print(f"your BMI is {formated_bmi}. You are clinically obese")


# Leap year

year = int(input("Which year do you want to check? "))

if year %4 ==0:
    if year % 100==0:
        if year % 400 == 0:
            print("This is the leap year.")
        else:
            print("not a leap year")
    else:
        print("This is the leap year.")
else:
    print("not a leap year")



# multiple statement

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child ticket $5")
    elif age <= 18:
        bill = 8
        print("Youth ticket $8")
    else:
        bill = 12
        print("Adult ticket $12")
    wants_photo = input("Do you want a photo taken? Y/N. ")
    if wants_photo == "Y":
        bill +=3
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have  to grow taller before you can ride.")



#pizza order program
print("Welcome to Python Pizza Deliveries!")
size = input("What size of pizza do you want? S,M or L? ")
add_pepperoni = input("Do you want peperpni> Y/N? ")
extra_cheese = input("Do you want extra cheese? Y/N?")

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill+=2
        if extra_cheese == "Y":
            bill +=1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
         bill+=3
         if extra_cheese == "Y":
            bill +=1
elif size =="L":
    bill = 25
    if add_pepperoni == "Y":
         bill+=3
         if extra_cheese == "Y":
            bill +=1

print(f"Your final bill is ${bill} ")


#Love calculator.




print("Welcome to Love Calculator")
name1 = input("What is your name?\n")
name2 = input("What is her name?\n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")

true = t + r + u + e

l =lower_case_string.count("l")
o= lower_case_string.count("o")
v=lower_case_string.count("v")
e=lower_case_string.count("e")

love = l + o + v + e

love_score =int(str(true) + str(love))

if (love_score < 10) or (love_score>90):
    print(f"Your love score is {love_score}, you go togehter like coke and menthos")
elif (love_score>=40) and (love_score <=50):
    print(f"Your love score is {love_score}, you go alright together")
else:
    print(f"Your love score is {love_score}")


# game

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")
