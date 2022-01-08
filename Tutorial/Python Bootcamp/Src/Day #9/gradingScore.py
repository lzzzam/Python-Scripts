students_score = {
    "Luca" : 89,
    "Paolo": 18,
    "Giuly": 65,
    "Toto" : 83,
    "Rosa" :100
}

students_grade = {}

for s in students_score:
    score = students_score[s] 
    grade = ""
    if score < 20:
        grade = "Pessimo"
    elif score < 40:
        grade = "Discreto"
    elif score < 60:
        grade = "Dignitoso"
    elif score < 80:
        grade = "Buono"
    elif score <= 100:
        grade = "Ottimo"
    
    students_grade[s] = grade

    
print(students_grade)
