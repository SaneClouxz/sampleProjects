# This is a sample ATM project
# Greeting
print("Hello User, create your 4 digits pin")

# user create pin
password = int(input("Create 4 digit pin: "))

# Confirmation message
print(" ")
print("PIN created successfully!!")
print(" ")

# request pin to access main_menu
pin = int(input("Please enter your pin: "))
print(" ")

# Correct pin move user to main menu
if pin == password:
    print("----------------------------------")
    print("Welcome User, press key to engage")
    print("----------------------------------")
    print(">1 Withdraw Cash ")
    print(">2 Balance ")
    print(">3 Transfer money ")
    print(">4 View Transactions")
