from titles import *

title("Exceptions")

try:
    age = int(input("Age: "))
    income = 20000
    risk = income/age
    print(risk)
except ZeroDivisionError:   #name of error appears in the terminal when unhandled error occurs
    print("Age cannot be 0")
except ValueError:
    print("Invalid value")



