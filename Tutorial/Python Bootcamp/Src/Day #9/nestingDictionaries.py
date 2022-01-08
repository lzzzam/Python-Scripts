
workmate = []

def add_workmate(name, age, skills, mood):
    workmate.append( { 
        "name"   : name,
        "age"    : age,
        "skills" : skills,
        "mood"   : mood
        } )


add_workmate("Wolfgang", 38, ["C", "C++", "ARM", "Project management"], "Smart")
add_workmate("Manuel", 39, ["Jenkins", "CI", "Visual Studio Code"], "calm")
add_workmate("Michael", 34, ["C++", "Javascript", "Unit Testing"], "Rompi palle")
add_workmate("Rok", 36, ["FW", "Python"], "Honest")
add_workmate("Markus", 42, ["C", "ARM", "compiler", "everything"], "strict")



for person in workmate:
    name = person["name"]
    age  = person["age"]
    skills = person["skills"]
    mood = person["mood"]
    print(f"{name} is {age} years old, can use {skills}, and is a {mood} person")