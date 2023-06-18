-----------------------------------------------------------------------------------------------------------
#This is a Python code that creates a simple calculator application that asks a user to enter 
#two numbers and the operation (e.g. +, -, x, etc.) that they’d like to perform on the numbers.
# Display the answer to the equation. Every equation entered by the user should be written to a text file. 
#Uses defensive programming ,this program  can  handles unexpected events and user inputs.
#------------------------------------------------------------------------------------------------------------

def calculator():
    while True:
        try:
            # Ask user for choice of entering two numbers or reading from file
            choice = input("Enter '1' to enter two numbers and an operator or '2' to read equations from a file: ")
            if choice == "1":
                # Ask user for two numbers and an operator
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                operator = input("Enter operator (+, -, *, /): ")
                # Perform calculation based on operator
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
                # Write equation to file
                with open("equations.txt", "a") as f:
                    f.write(f"{num1} {operator} {num2} = {num1+num2}\n")
            elif choice == "2":
                # Ask user for filename
                filename = input("Enter filename: ")
                try:
                    with open(filename) as f:
                        # Read equations from file and perform calculations
                        for line in f:
                            parts = line.split()
                            num1 = float(parts[0])
                            num2 = float(parts[2])
                            operator = parts[1]
                            if operator == "+":
                                result = num1 + num2
                            elif operator == "-":
                                result = num1 - num2
                            elif operator == "*":
                                result = num1 * num2
                            elif operator == "/":
                                result = num1 / num2
                            else:
                                result = "Invalid equation"
                            print(f"{line.strip()} = {result}")
                except FileNotFoundError:
                    # Handle file not found error
                    print(f"File not found: {filename}")
            else:
                # Handle invalid choice error
                print("Invalid choice")
        except ValueError:
            # Handle invalid input error
            print("Invalid input")
        except ZeroDivisionError:
            # Handle division by zero error
            print("Cannot divide by zero")

calculator()
