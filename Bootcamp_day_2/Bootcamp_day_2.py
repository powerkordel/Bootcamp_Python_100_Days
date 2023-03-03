
#Day 2 Data Types


print("hello"[0])

print(123 + 345)

x = 123_456_789

print(x)

num_char = str(len(input("What is your name? ")))
print("Your name has " + num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float(100.5))

#Task

two_digit_number = input("Type a two digit number: ")

a = int(two_digit_number[0])
b = int(two_digit_number[1])

print(a + b)



#operators PEMADS ();**;*;/;+;-

#bmi calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")


bmi = int(weight)/float(height)**2

print(int(bmi))


# round after coma showss how many numbers after dot 
print (round(8/3,4))

#f-String
score =6

print(f"your score is: {score}")


#life in weeks

age = input("What is your age? ")

final_age = 90

left_age = final_age - int(age)

left_age_months = left_age * 12
left_age_weeks = left_age * 52
left_age_days = left_age * 365

print(f"You have {left_age_days} days, {left_age_weeks} weeks,  and {left_age_months} months left.")


# tip calculator

print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
procentage_tip = int(input("What procentage tip would you like to give? 10, 12, or 15? "))
number_people = int(input("How many people to split the bill? "))
final_bill = (total_bill * (procentage_tip/100))+total_bill

each_to_pay = final_bill/number_people
final_pay = "{:.2f}".format(each_to_pay)
print(f"Each person should pay: ${final_pay}")