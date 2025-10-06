while True:
    print("Welcome to the calculator! Follow the instructions below.")

    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    operator = input("Choose an operator (+, -, *, /): ")

    try:
        num1_float = float(num1)
        num2_float = float(num2)
    except ValueError:
        print("Only numbers are allowed. Please try again...")
        continue

    if operator is None or operator.strip() == "":
        print("Error: You must enter an operator.")
        continue

    elif operator == "+":
        result = num1_float + num2_float
        print(f"The result is {num1_float} + {num2_float} = {result}")

    elif operator == "-":
        result = num1_float - num2_float
        print(f"The result is {num1_float} - {num2_float} = {result}")

    elif operator == "/":
        if num2_float == 0:
            print("Error: Cannot divide by zero.")
            continue
        result = num1_float / num2_float
        print(f"The result is {num1_float} / {num2_float} = {result}")

    elif operator == "*":
        result = num1_float * num2_float
        print(f"The result is {num1_float} * {num2_float} = {result}")

    else:
        print("Invalid operator. Please try again.")

    exit_choice = input("Do you want to exit? Type (y)es to quit: ").lower().strip()
    if exit_choice.startswith("y"):
        print("Exiting... See you later!")
        break
