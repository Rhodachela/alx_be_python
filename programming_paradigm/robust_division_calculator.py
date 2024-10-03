def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")   
        result =  num / denom
        return f"The result is {result:.2f}"

    except ZeroDivisionError as e:
        return str(e)
    except ValueError:
        print("Error: Invalid input. Enter a numerical integer")  
    
    

