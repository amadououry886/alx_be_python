num1 =float(input("Enter the first number: "))
num2 =float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:


  case "+":
    result = num1 + num2
    print(f"The result is {result}.")

  case "-":
    result = num1 - num2
    print(f"The operation is {result}")

  case "*":
    result = num1 * num2
    print(f"The result is {num1 * num2}.")
    
  case "/":
      if num2 != 0:
        result = num1 /num2
        print(f"The operation is {result}")
   
      else:
        print("Cannot divide by Zero.")
  case _:
       print("This operation is not valid")

 

