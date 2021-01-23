# taking user temp value
out = True
while out:
    try:
        temperature = float(input("Enter temperature value: "))
        out = False
    except ValueError:
        print("Enter numeric unit, try again!")

# taking user input unit
# the while loop is to prevent the user from entering a different option from the ones provided

valid_in = True
while valid_in:
    temp_unit = input("Enter input unit, C for Celsius, K for Kelvin  or F for Fahrenheit: ")
    if temp_unit.lower() == "c":
        valid_in = False
    elif temp_unit.lower() == "f":
        valid_in = False
    elif temp_unit.lower() == "k":
        valid_in = False

    else:
        print("Incorrect input, enter a valid option!")
        valid_in = True

# creating th logics and formula
if temp_unit.lower() == "c":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, K for Kelvin or F for Fahrenheit: ")
    if conversion_unit.lower() == "k":
        converted_temp = temperature + 273
        print(f"Temperature is {converted_temp} degrees in kelvin from Celsius!")

    elif conversion_unit.lower() == "f":
        converted_temp = 1.8 * temperature + 32
        print(f"Temperature is {converted_temp} degrees in fahrenheit from Celsius!")

elif temp_unit.lower() == "k":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, C for Celsius or F for Fahrenheit: ")
    if conversion_unit.lower() == "c":
        converted_temp = temperature - 273
        print(f"Temperature is {converted_temp} degrees in Celsius from Kelvin!")

    elif conversion_unit.lower() == "f":
        converted_temp = 1.8 * (temperature - 273) + 32
        print(f"Temperature is {converted_temp} degrees in Fahrenheit from Kelvin!")

elif temp_unit.lower() == "f":
    # prompt user for unit to convert to
    conversion_unit = input("Enter output unit, K for Kelvin or C for Celsius: ")
    if conversion_unit.lower() == "c":
        converted_temp = 0.6 * (temperature - 32)
        print(f"Temperature is {converted_temp} degrees in Celsius from Fahrenheit!")

    elif conversion_unit.lower() == "k":
        converted_temp = 0.6 * (temperature - 32) + 273
        print(f"Temperature is {converted_temp} degrees in Kelvin from Fahrenheit!")
