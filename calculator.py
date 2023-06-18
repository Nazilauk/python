#-------------------------------------------------------------------------------------------------------------
#Here is an example of a simple calculator application that asks a user to enter two numbers and the operation 
#(e.g. +, -, x, etc.) that they’d like to perform on the numbers. Display the answer 
#Also this Example of DEFENSIVE PROGRAMMING;
#--------------------------------------------------------------------------------------------------------------
def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operator = input("Enter operator (+, -, *, /): ")
            if operator == "+":
                print(num1 + num2)
            elif operator == "-":
                print(num1 - num2)
            elif operator == "*":
                print(num1 * num2)
            elif operator == "/":
                print(num1 / num2)
            else:
                print("Invalid operator")
            with open("equations.txt", "a") as f:
                f.write(f"{num1} {operator} {num2} = {num1+num2}\n")
        except ValueError:
            print("Invalid input")
        except ZeroDivisionError:
            print("Cannot divide by zero")

calculator()


