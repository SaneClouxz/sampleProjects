prompt = True

while prompt:
    user_input = input("Enter a number: ")
    if int(user_input) % 2 == 0:
        print(f'{user_input} is an even number')
        another_number_prompt = input('Do you want to try another number? Enter Y for Yes and N for No: ')

        if another_number_prompt.lower() == 'y':
            prompt = True
        elif another_number_prompt.lower() == 'n':
            prompt = False

    elif int(user_input) % 2 == 1:
        print(f'{user_input} is an odd number')
        another_number_prompt = input('Do you want to try another number? Enter Y for Yes and N for No: ')

        if another_number_prompt.lower() == 'y':
            prompt = True
        elif another_number_prompt.lower() == 'n':
            print("Alright, have a great day")
            prompt = False

