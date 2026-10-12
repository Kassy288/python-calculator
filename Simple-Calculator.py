print("Basic Calculator Program")

#create2 input programs to store numbers for calculating 

first=int(input("Enter First Number: "))

second=int(input("Enter Second Number: "))

#Create an input program to select operation type 
print("""
Operation type
Addition = +
Subtraction = -
Division = /
Multiplication = *

""")
#create an input field for selecting operation

operationtype = input("Select 1 of the following:*, +, -, /: ")

# Create a conditon to satisfy the basic calculation operation type

if operationtype == "+":
    addition = first+second
    print(addition)
elif operationtype == "-":
    subtraction = first-second
    print(subtraction)
elif operationtype == "/":
    Division = first/second
    print(Division)    
elif operationtype == "*":
    Multiplication = first*second
    print(Multiplication)
else :
    print("Invalid operation")
    