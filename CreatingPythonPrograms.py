"""
Student Name: Saravenus Khon
Date: 03/29/2025
Assignment: Creating Python Programs
"""

while True:
    # this is where I started
    print("\n Please select Option 1 or 2:")
    print("Option 1: Add and Subtract a pair of numbers")
    print("Option 2: Multiply and Divide a pair of numbers")

    choice = input("Please Select 1 or 2: ").strip()

    # Validate input to accept only "1" or "2"
    if choice not in ["1", "2"]:
        print("Invalid choice, please enter 1 or 2.")
        continue  # Restart the loop if the user input is not 1 or 2

    # Prompt the user for two numbers
    num1 = float(input("Enter your first number: "))
    num2 = float(input("Enter your second number: "))

    # Perform Addition and Subtraction here
    if choice == "1":
        sum = num1 + num2
        difference = num1 - num2
        print("\n Option 1 (Part 1) : Addition and Subtraction for the noobs.. J/K!")
        print(f"{num1} + {num2} = {sum}")
        print(f"{num1} - {num2} = {difference}")

    # Perform Multiplication and Division here
    else:
        product = num1 * num2
        quotient = num1 / num2 if num2 != 0 else "Undefined (division by zero not allowed.. Nope! )"

        print("\n Option 2 (Part 2 ): Multiplication and Division! the fun stuff")
        print(f"{num1} × {num2} = {product}")
        print(f"{num1} ÷ {num2} = {quotient}")

    # Ask if the user wants to keep playing
    retry = input("\n Want to try another set of numbers? [Yes or No]: ").strip().lower()
    if retry != "yes":
        print("Thanks for playing!")
        break  # Exit the loop
