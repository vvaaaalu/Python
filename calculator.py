while True:
   print("Options:")
   print("Enter 'add' to add two numbers")
   print("Enter 'subtract' to subtract two numbers")
   print("Enter 'multiply' to multiply two numbers")
   print("Enter 'divide' to divide two numbers")
   print("Enter 'quit' to end the program")
   user_input = input(": ")

   if user_input == "quit":
      break
   elif user_input == "add":
       a= float(input("enter first number"))
       b= int(input("enter first number"))
       z= str(a+b)
       print("The answer is"+z)
   elif user_input == "subtract":
       a = int(input("enter first number"))
       b = int(input("enter first number"))
       z = print(a - b)

   elif user_input == "multiply":
       a = int(input("enter first number"))
       b = int(input("enter first number"))
       z = print(a * b)
   elif user_input == "divide":
       a = int(input("enter first number"))
       b = int(input("enter first number"))
       z = print(a / b)
   else:
      print("Unknown input")
