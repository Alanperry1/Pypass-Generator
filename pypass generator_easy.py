import random

# Lists of characters to choose from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Welcome message
welcome_message = "Welcome to the PyPassword Generator!"
print(welcome_message.upper())

# Generate password
password = ""

# User input for the number of letters
print("How many letters would you like in your password?")
num_letters = int(input())
for _ in range(num_letters):
    password += random.choice(letters)

# User input for the number of symbols
print("How many symbols would you like?")
num_symbols = int(input())
for _ in range(num_symbols):
    password += random.choice(symbols)

# User input for the number of numbers
print("How many numbers would you like?")
num_numbers = int(input())
for _ in range(num_numbers):
    password += random.choice(numbers)
import random

def shuffle_string(hash):
    # Convert string to a list of characters
    char_list = list(password)
    # Shuffle the list in place
    random.shuffle(char_list)
    # Convert the list back to a string
    shuffled_string = ''.join(char_list)
    return shuffled_string

password = shuffle_string(password)

# Display the generated password
print(f'Your generated password is:{password}')

