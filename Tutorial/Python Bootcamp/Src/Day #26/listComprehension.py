#exercise 1
numbers = list(range(1,100))
sq_numbers = [n**2 for n in numbers]
print(sq_numbers)

#exercise 2
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

#exercise 3
import os

DIR_PATH = os.path.dirname(__file__)
FILE1_PATH = os.path.join(DIR_PATH, "file1.txt")
FILE2_PATH = os.path.join(DIR_PATH, "file2.txt")

with open(FILE1_PATH, "r") as f:
    list1 = [int(line.strip("\n")) for line in f.readlines()]

    
with open(FILE2_PATH, "r") as f:
    list2 = [int(line.strip("\n")) for line in f.readlines()]

new_list = [n for n in list1 if n in list2]

print(list1)
print(list2)
print(new_list)


#exercise 4
import random
students        = ["Luca", "Rosa", "Paolo", "Rok", "Manuel"]
studentsScores  = {s : random.randint(1,100) for s in students}
studentsPassed  = {student : score for (student,score) in studentsScores.items() if score > 50}

print(studentsPassed)

#exercise 5
sentence = "L'altro giorno sono stato al mare con Rosanna e mi sono divertito"
words    = sentence.split()

words_length = { word:len(word) for word in words}
print(words_length.items())


#exercise 6

def toFarenaith(t):
    return t * 9/5 + 32

weather_c = {
    "Lunedi"  : 25,
    "Martedi" : 23,
    "Mercoledi" : 24,
    "Giovedi" : 21,
    "Venerdi" : 19,
    "Sabato"  : 22,
    "Domenica" : 24
}

weather_f = {day:toFarenaith(temp) for (day, temp) in weather_c.items()}

print(weather_f)


#exercise 7
import pandas as pd
from os.path import dirname, join

DIR_NAME = dirname(__file__)
NANO_FILE = join(DIR_NAME, "nano_alphabet.csv")

data = pd.read_csv(NANO_FILE)

nano_dict = {row.letter : row.word for (index, row) in data.iterrows()}

name = "Luca"

name_spelling = [nano_dict[letter.upper()] for letter in name]

print(name_spelling)