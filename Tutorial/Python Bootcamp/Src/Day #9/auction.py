import os

auction = []

while True:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))

    entry = { 
        "name" : name, 
        "bid"  : bid
        }

    auction.append(entry)

    if input("Are there other users? 'Yes' or 'No' --> " ).lower() == "yes" :
        os.system("clear")
    else:
        break

max_bid = 0
winner = ""

for user in auction:
    if user["bid"] > max_bid:
        max_bid = user["bid"]
        winner = user["name"]

print(f"The winner is {winner} with a bid of ${max_bid}")
