bill = float(input("What is the total bill to pay? "))
percentage = float(input("What percentage do you want to give? ")) / 100.0
people = int(input("How many people?"))

payForEachPerson = round ( (bill * (1.0 + percentage)) / people, 2 ) 

print(f"Each person must pay {payForEachPerson}")
