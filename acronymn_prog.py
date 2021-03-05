user_input = input("Enter texts here: ")
user_input_split = user_input.split(" ")
split = []

for word in user_input_split:
    split.append(word[0].upper())

acronym = ''.join(split)
print(acronym)