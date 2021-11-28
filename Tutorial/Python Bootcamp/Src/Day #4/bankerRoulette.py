import random

names = input("Write the name of the players separated by a command and a space, like: Luca, Angela, Pietro...").split(", ")

unluckyOne = random.randint(0, len(names) - 1)
whoPay = names[unluckyOne]

print(f"{whoPay} will pay the dinner")
