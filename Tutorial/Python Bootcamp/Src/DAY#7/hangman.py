import os
from hangmanDraw import *

word  = "mutandinipatatini"
guess = []
error = 0
game_over = False   #True if user lose 

def initGuess():
    global guess
    for i in range(0,len(word)):
        guess.append("_")
        

def updateGuess(letter):
    letter_is_present = False
    #search for letter in word
    for i in range(0, len(word)):
        if letter == word[i]:
            guess[i] = letter
            letter_is_present = True
    return letter_is_present

def drawWord():
    print("\n")
    draw_guess = ""
    for i in range(0, len(word)):
        draw_guess += f"{guess[i]} "
    print(draw_guess)

def drawHangman(error):
    print("\n")
    print(hangman[error])

def clearConsole():
    os.system("clear")

def drawScreen(error):
    clearConsole()
    drawWord()
    drawHangman(error)


#start
initGuess()

while True:

    drawScreen(error)

    #read user input and check if present in word
    letter = input("\nGuess a letter: ")
    letter_is_present = updateGuess(letter)

    if letter_is_present == True:
        if "_" in guess:
            continue
        else:
            break             #end game with Win
    else:
        error += 1
        if error == max_error_count:
            game_over = True  #end game with Lose
            break
   
#update screen before finishing game
drawScreen(error)

if game_over == True:
    print("\n YOU LOSE\n\n")
else:
    print("\n YOU WIN\n\n")