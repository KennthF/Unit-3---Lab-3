import calculator

first_input = float(input("Enter in first number: "))
second_input = float(input("Enter in second number: "))
operation = input("Would you like to add/subtract/multiply/divide: ").lower()

if operation == "add":
    sum = calculator.add(first_input, second_input)
    print(f"Sum: {sum}")

elif operation == "subtract":
    difference = calculator.minus(first_input, second_input)
    print(f"Difference: {difference}")

elif operation == "multiply":
    product = calculator.multiply(first_input, second_input)
    print(f"Product: {product}")

elif operation == "divide":
    quotient = calculator.divide(first_input, second_input)
    print(f"Quotient: {quotient}")

else:
    print("\nInvalid Operator")