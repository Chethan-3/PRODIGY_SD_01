def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    unit = unit.lower()
    if unit == "celsius" or unit == "c":
        print(f"{value}°C is equal to {celsius_to_fahrenheit(value):.2f}°F and {celsius_to_kelvin(value):.2f}K")
    elif unit == "fahrenheit" or unit == "f":
        print(f"{value}°F is equal to {fahrenheit_to_celsius(value):.2f}°C and {fahrenheit_to_kelvin(value):.2f}K")
    elif unit == "kelvin" or unit == "k":
        print(f"{value}K is equal to {kelvin_to_celsius(value):.2f}°C and {kelvin_to_fahrenheit(value):.2f}°F")
    else:
        print("Invalid unit entered. Please enter Celsius, Fahrenheit, or Kelvin.")

# Get user input
temperature = float(input("Enter the temperature value: "))
unit = input("Enter the unit (Celsius, Fahrenheit, Kelvin): ")

convert_temperature(temperature, unit)
