print("""

PYTHON CALCULATOR
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

""")

print("""

operations available: +  -  *  /  &

""")

def calculator(a, b, op):
    """ Compute operation on passed values"""
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return round( a / b, 3 )
    elif op == "%":
        return a % b
    else:
        print("Invalida Operation, repeat please\n")
        return "NA"
    

while True:
    first_value  = int( input("First number: ") )
    operation    =      input("Choose operator: ")
    second_value = int( input("Second number: "))
    result = calculator(first_value, second_value, operation)
    if result != "NA":
        print(f"{first_value} {operation} {second_value} = {result}\n")