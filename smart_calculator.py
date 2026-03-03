while True:
    num1 = float(input("Enter first number: "))
    operator = input("Choose +, -, *, or /: ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", num1 + num2)
    elif operator == "-":
        print("Result:", num1 - num2)
    elif operator == "*":
        print("Result:", num1 * num2)
    elif operator == "/":
        print("Result:", num1 / num2)
    else:
        print("Invalid operator.")

    restart = input("Run again? (y/n): ")

    if restart.lower() != "y":
        print("Goodbye 👋")
        break
