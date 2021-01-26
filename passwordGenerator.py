import random

characters = f"1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIKLMNPQRSTUVWXYZ,./;'[]`<>?<>?~!@#$%^&*()_+"
password_length = int(input("Enter length of password: "))
generated_password = random.sample(characters, password_length)
generated_password_formatted = "".join(generated_password)
print(generated_password_formatted)

