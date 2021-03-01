import random

# creating the random guessed number between 1 and 10
secret_number = random.randint(1, 10)

# number of user secret_number which is 3
number_of_guess = 3

# secret_number used which is increased after every count
guess_count = 0

# creating the game
valid_input = True

while guess_count < number_of_guess:
    user_guess = int(input("> Guess the secret number: "))
    if user_guess < secret_number:
        print("Your guess is less than the number, try again!")
        guess_count += 1

    elif user_guess > secret_number:
        print("Your guess is greater than the number, try again!")
        guess_count += 1

    elif user_guess == secret_number:
        print("You guessed right, you won!!")
        break

else:
    print(f"You lost, the secret number is {secret_number}")