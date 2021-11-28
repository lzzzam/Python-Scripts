import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

symbols = [rock, paper, scissors]

user_symbol = int(input("Chosse between Rock, Paper or Scissors (0, 1 or 2) ==> "))
computer_symbol = random.randint(0,2)

if user_symbol > 2:
    print("Value out of valid range, retry!")
    exit

print("User selected:\n")
print(symbols[user_symbol] + "\n")

print("Computer Selected:\n")
print(symbols[computer_symbol] + "\n")

if user_symbol == 0: #rock 
    if computer_symbol == 0:    #rock vs rock
        print("Nobody Win 😶")
    elif computer_symbol == 1:  #rock vs paper
        print("You Lose 😓 ")
    else:                       #rock vs scissors
        print("You Win 😁")
elif user_symbol == 1: #paper
    if computer_symbol == 0:    #paper vs rock
        print("You Win 😁")
    elif computer_symbol == 1:  #paper vs paper
        print("Nobody Win 😶")
    else:                       #paper vs scissors
        print("You Lose 😓 ")
elif user_symbol == 2: #scissors
    if computer_symbol == 0:    #scissors vs rock
        print("You Lose 😓 ")
    elif computer_symbol == 1:  #scissors vs paper
        print("You Win 😁")
    else:                       #scissors vs scissors
        print("Nobody Win 😶")