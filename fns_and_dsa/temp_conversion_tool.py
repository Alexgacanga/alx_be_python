FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)
def convert_to_celsius(fahrenheit):
    return fahrenheit * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR
try:
    input_value = float(input("Enter the temperature to convert: "))
    units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()
    if units == "f":
        print(f"{input_value}\u00B0F is {convert_to_celsius(input_value)}\u00B0C")
    elif units == "c":
        print(f"{input_value}\u00B0C is {convert_to_fahrenheit(input_value)}\u00B0F")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")