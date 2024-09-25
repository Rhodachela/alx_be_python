FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    celsius = (fahrenheit -32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()
        
        if unit == "f":
             celsius = convert_to_celsius(temperature)
             print(f"The temperature {temperature}℉ is {celsius:.2f}℃")
        elif unit == "c":
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"The temperature {temperature}℃ is {fahrenheit:.2f}℉")
        else:
            print("Invalid input. Enter C for celsius and F for fahrenheit.")

if __name__ == "__main__":
    main()