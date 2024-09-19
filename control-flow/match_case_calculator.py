num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 !=0:
            result = num1 / num2
        else:
            result = "Undefined (Cannot divide by zero)"

if isinstance (result, (int, float)):
    print(f"The result is {result}")

else:
    print(f"Error: {result}")


