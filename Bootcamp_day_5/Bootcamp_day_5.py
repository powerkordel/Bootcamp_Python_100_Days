
#Day 5 for loop (bit of while)
import random


student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] =int(student_heights[n])
print(student_heights)
total = 0
sum_of_items = 0
for h in student_heights:
  total += h
  sum_of_items +=1


avarage = total/sum_of_items

print(f"{avarage} is the avarage height of students")



student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] =int(student_scores[n])
print(student_scores)
#max() function can do it faster but:

highest_score = 0
for s in student_scores:
    if s > highest_score:
        highest_score = s
print(f"The highest score is {highest_score}")



# range

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Buzz")
    elif number % 5 == 0 :
        print("Fizz")
    else:
        print(number)


# password generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password=""
n = 0
i = 0
e = 0
while n != nr_letters:
    password += random.choice(letters)
    n +=1

while i != nr_symbols:
    password += random.choice(symbols)
    i +=1

while e != nr_numbers:
    password += str(random.choice(numbers))
    e +=1

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

n = 0
i = 0
e = 0
passwordo = []

while n != nr_letters:
    passwordo.insert(random.randint(0,nr_letters-1),random.choice(letters))
    n +=1

while i != nr_symbols:
    passwordo.insert(random.randint(0,nr_symbols-1),random.choice(symbols))
    i +=1

while e != nr_numbers:
    passwordo.insert(random.randint(0,nr_numbers-1),random.choice(numbers))
    e +=1

print(passwordo)
random.shuffle(passwordo)
print(passwordo)
random.shuffle(passwordo)
print(passwordo)
random.shuffle(passwordo)
print(passwordo)
random.shuffle(passwordo)
print(passwordo)
passwordo_final = ""

for c in passwordo:
    passwordo_final += c


print(passwordo_final)

# you can do above with for loop : for number in range (1,nr_letters + 1) , and also you can use random.shuffle()