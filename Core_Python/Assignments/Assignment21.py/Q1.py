def calculator():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        
        op= input("Enter operator (+, -, *, /): ")

    
        if op not in ['+', '-', '*', '/']:
            raise ValueError("Invalid Operator")

        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by Zero is not allowed")
            result = num1 / num2

        print(f"Result: {num1} {op} {num2} = {result}")

    except ValueError as ve:
        print("Error:", ve)

    except ZeroDivisionError as zde:
        print("Error:", zde)

calculator()
