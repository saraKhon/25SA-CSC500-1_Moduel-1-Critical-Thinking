
"""
student Name: Saravenus Khon
date: 03/26/2025
Assignment:Creating Python Programs
"""
while True:
    # prompting the user for two numbers
    num1 = int(input("Enter your first number here: "))
    num2 = int(input("Enter the second number here: "))


    # Perform the addition steps here
    # Perform the subtraction steps here
    sum = num1 + num2
    difference = num1 - num2

    # Displays the addition and subtraction results
    print("Part 1: ")
    print(num1, "+", num2, "= ", sum)
    print(num1, "-", num2, "=", difference)

    # asks the user if they want to continue
    option = input("want to try another set of numbers?  [Yes or No ] ").strip().lower()
    if option != "yes":
        print("Thanks for playing")
        break  # breaks out of the loop

#test



