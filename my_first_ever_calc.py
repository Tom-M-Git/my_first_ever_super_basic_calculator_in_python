while True:
    print("Hi")
    print("'quit' for quitting, 'add' for addition, 'subtract' for subtraction…and so on.")
    
    userInput = input(": ")
    
    if userInput == "quit":
        break
    elif userInput == "add":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("The answer is" + result)
    elif userInput == "subtract":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("The answer is" + result)
    elif userInput == "multiply":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("The answer is" + result)
    elif userInput == "divide":
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("The answer is" + result)
