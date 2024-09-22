def calculator():
    print("I'm simple calculator")

    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    print("choose an operation: ")
    '''choose an operation between 1/2/3/4 for simple calculation '''
    print("1 for addition: ")
    print("2 for subtraction: ")
    print("3 for multiplication: ")
    print("4 for division: ")

    operation = input("enter the number between (1/2/3/4) :") 

    if operation == '1':
        result = num1 + num2
        print(f"the result of {num1} + {num2} is: {result}")

    elif operation == '2':
        result = num1 - num2
        print(f"the result of {num1} - {num2} is: {result}")

    elif operation == '3':
        result = num1 * num2 
        print(f"the result of {num1} * {num2} is: {result}")

    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"the result of {num1} / {num2} is: {result}")
        else:
            print("error")
    else:
        print("invalid operation. choose b/n 1/2/3/4 ")

calculator()