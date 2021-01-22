import sys

# taking user temp value
try:
    temp = float(input("Enter temperature value: "))
except ValueError:
    print("Enter numeric unit, exiting program, try again!")
    sys.exit()

# taking user input unit
temp_unit = input("Enter input unit, C for Celsius, K for Kelvin  or F for Fahreheit: ")

# creating th logics and formula
if temp_unit.lower() == "c":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, K for Kelvin or F for Fahrenheit: ")
    if conversion_unit.lower() == "k":
        converted_temp = temp + 273
        print(f"Temperature is {converted_temp} degrees in kelvin from Celsius!")

    elif conversion_unit.lower() == "f":
        converted_temp = 1.8 * temp + 32
        print(f"Temperature is {converted_temp} degrees in fahrenheit from Celsius!")

elif temp_unit.lower() == "k":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, C for Celsius or F for Fahrenheit: ")
    if conversion_unit.lower() == "c":
        converted_temp = temp - 273
        print(f"Temperature is {converted_temp} degrees in Celsius from Kelvin!")

    elif conversion_unit.lower() == "f":
        converted_temp = 1.8 * (temp - 273) + 32
        print(f"Temperature is {converted_temp} degrees in Fahrenheit from Kelvin!")

elif temp_unit.lower() == "f":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, K for Kelvin or C for Celsius: ")
    if conversion_unit.lower() == "c":
        converted_temp = 0.6 * (temp - 32)
        print(f"Temperature is {converted_temp} degrees in Celsius from Fahrenheit!")

    elif conversion_unit.lower() == "k":
        converted_temp = 0.6 * (temp - 32) + 273
        print(f"Temperature is {converted_temp} degrees in Kelvin from Fahrenheit!")
