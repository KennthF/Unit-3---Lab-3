def add(num1,num2):
    result = first_number + second_number
    return result

def minus(num1,num2):
    result = first_number - second_number
    return result

def multiply(num1,num2):
    result = first_number * second_number
    return result

def divide(num1,num2):
    result = first_number / second_number
    return result

# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

output = 0
if operation == "add":
    output = add(first_input, second_input)
    print(f"Result: {output}")
    
elif operation == "subtract":
    output = minus(first_input, second_input)
    print(f"Result: {output}")

elif operation == "multiply":
    output = multiply(first_input, second_input)
    print(f"Result: {output}")

elif operation == "divide":
    output = divide(first_input, second_input)
    print(f"Result: {output}")

else:
    print("Sorry, I do not understand your request.")


