from a_variables_and_types import LEGAL_AGE

# CONDITIONAL STATEMENTS

# Simple if-else
age = int(input("Enter your age: "))
if age >= LEGAL_AGE:
    print("You are an adult")
else:
    print("You are a minor")

print("-----------")

# If-elif-else
x = 0
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

print("-----------")

# Match-case (Python 3.10+)
name = "Juliana"
match name:
    case "Ana":
        print("Not Juliana")
    case "Juliana":
        surname = input("Enter your surname: ")
        print(name, surname)
