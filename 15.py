while True:
        print("Options:")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to end the program")
        user_input=input("num1:num2")
        if user_input == "quit":
            break
        elif user_input=="add":
            input(float("num1"))
            input(float("num2"))
        elif user_input=="subtract":
            '
        elif user_input=="multiply":
            'num1'*'num2'
        elif user_input=="divide":
            'num1'/'num2'
        else:
            print("Unknown input")
