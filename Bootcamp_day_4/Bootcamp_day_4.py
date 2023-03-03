#Day 4 pseudorandomness

#random int
import random

random_integer = random.randint(1,100)

print(random_integer)


#random float

random_float=random.random()*5

print(random_float)

#head or tails 

result = random.randint(0,1)

answer = input("what is your choice? Head or tail?\n")


if result == 0 and answer == "head":
    print("Head! Congratulation, you won!")
elif result == 0 and answer == "tail":
    print("Head! You lost. Try again!")
elif result == 1 and answer == "tail":
    print("Tail! Congratulation, you won!")
elif result == 1 and answer == "head":
    print("Tail! You lost. Try again!")

print("Game Over")



#python list

states_of_america = ["Florida","New York","Texas","California"]

print(states_of_america[2])
print(states_of_america[-2])
states_of_america[2] = "Teksas"
print(states_of_america)

states_of_america.append("Pawlowo")
print(states_of_america)
states_of_america.extend(["Pieskowo","Kotkowo"])
print(states_of_america)

states_of_america.insert(1,"Pacanowo")

print(states_of_america)

#Who pay the bill

name_string = input("Give me everybody`s names,separated by a comma. ")

names  = name_string.split(",")

#rand_index = random.randint(0,len(name_string)-1)

person_to_pay = random.choice(names)
print(f"{person_to_pay} will pay the bill!! ")



#nested list

row1 =[0,0,0]
row2 =[0,0,0]
row3 =[0,0,0]

map =[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to enter '1' in 3x3 matrix? ")

column_raw = int(position[0])
row_raw = int(position[1])
column_final = column_raw - 1
row_final = row_raw - 1
map[column_final][row_final]=1

print(f"{row1}\n{row2}\n{row3}")



#rock paper scisors



rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''



player_move = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

computer_move = random.randint(0,2)

if player_move == 0 and computer_move == 0:
    print(f"Player move:\n{rock}\nComputer move:\n{rock}\n It`s a draw ")
elif player_move == 1 and computer_move == 1:
    print(f"Player move:\n{paper}\nComputer move:\n{paper}\n It`s a draw ")
elif player_move == 2 and computer_move == 2:
    print(f"Player move:\n{scissors}\nComputer move:\n{scissors}\n It`s a draw! ")
elif player_move == 0 and computer_move == 1:
    print(f"Player move:\n{rock}\nComputer move:\n{paper}\n You lost! ")
elif player_move == 0 and computer_move == 2:
    print(f"Player move:\n{rock}\nComputer move:\n{scissors}\n You won! ")
elif player_move == 1 and computer_move == 0:
    print(f"Player move:\n{paper}\nComputer move:\n{rock}\n You won! ")
elif player_move == 1 and computer_move == 2:
    print(f"Player move:\n{paper}\nComputer move:\n{scissors}\n You lost! ")
elif player_move == 2 and computer_move == 0:
    print(f"Player move:\n{scissors}\nComputer move:\n{rock}\n You lost! ")
elif player_move == 2 and computer_move == 1:
    print(f"Player move:\n{scissors}\nComputer move:\n{paper}\n You won! ")

#another way is to place moves in the list and use coresponding index to simplify the code i.e' moves = [rock, paper, scissors]


