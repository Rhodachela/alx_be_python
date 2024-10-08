
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
           return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return("Error: Cannot divide by 0!")
            elif num1 == 0:
                return("Error: Cannot use o for this operation!")
            else:
                return num1 / num2
        case _:
            return("Invalid operation")

