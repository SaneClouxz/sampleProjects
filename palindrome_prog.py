user_input = input("Enter words: ")
words = user_input.split(" ")
for word in words:
    if word == word[::-1]:
        print(f"{word} is a palindrome!")
    else:
        print(f'{word} is not a palindrome!')