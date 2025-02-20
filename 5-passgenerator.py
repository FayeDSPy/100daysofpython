import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# Easy
# print("Welcome to the PyPassword Generator!")
# nr_letters = int(input("How many letters would you like in your password?\n"))
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))
#
# password = ""
#
# for x in range(0, nr_letters):
#     password += random.choice(letters)
#
# for x in range(0, nr_numbers):
#     password += random.choice(numbers)
#
# for x in range(0, nr_symbols):
#     password += random.choice(symbols)
#
# print(password)

# Hard
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

password_list = []

# Adding random letters
for x in range(nr_letters):
    password_list.append(random.choice(letters))

# Adding random numbers
for x in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Adding random symbols
for x in range(nr_symbols):
    password_list.append(random.choice(symbols))

# Print the password list before shuffling
print("Before shuffling:", password_list)

# Shuffle the password list to randomize the order
random.shuffle(password_list)

# Print the password list after shuffling
print("After shuffling:", password_list)

password = ""
for x in password_list:
    password += x

# Print the final password
print(f"Your password is: {password}")