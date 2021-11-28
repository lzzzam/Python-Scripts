import random

bet = int(input("You bet on Head or Tail? [Head=0 or Tail=1] ==> "))

coinFace = random.randint(0,100) % 2

if bet == coinFace:
    print("You Win")
else:
    print("You Lose")
