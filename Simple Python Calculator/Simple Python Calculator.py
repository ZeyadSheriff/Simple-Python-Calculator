import math
print("------------------------------------------------------------------------------------------")
print("Hello to our simple calculator. We are updating it constantly.")

while True:
    A = input("Type (Yes) to run the program or (No) to exit: ").lower()

    if A == "no":
        print("Thanks for trying our calculator")
        break
    elif A != "yes":
        print("Invalid choice, Please type (Yes) or (No).")
        continue

    try:
        B = float(input("Please, enter the first number: "))
        C = input("Enter the operator (+) (-) (*) (/) (**) (sqrt): ")
        if C != "sqrt":
            D = float(input("Please, enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        continue

    result = None

    if C == "+":
        result = B + D
    elif C == "-":
        result = B - D
    elif C == "*":
        result = B * D
    elif C == "/":
        if D == 0:
            print("Division by zero isn't allowed")
            continue
        result = B / D
    elif C == "**":
        result = B ** D
    elif C == "sqrt":
        if B < 0:
            print("Cannot calculate square root of negative number.")
            continue
        result = math.sqrt(B)    
    else:
        print("Unknown operator, Please try again.")
        continue

    print("-----------------------------------------------")
    if C == "sqrt":
        print(f"The result of √{B} = {result}")
    else:
        print(f"The result of {B} {C} {D} = {result}")
    print("-----------------------------------------------")

    again = input("Do you want to do another calculation? (Yes/No): ").lower()
    if again != "yes":
        print("Thanks for using our calculator")
        break