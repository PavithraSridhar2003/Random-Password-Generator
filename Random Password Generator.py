#Create a Random Password Generator using Python

import random
import string

# Prompt the user to specify the desired length of the password
password_length = int(input("Enter the desired length of the password: "))

# Define character sets for the password
lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

# Combine character sets based on desired complexity
character_sets = [lowercase_letters, uppercase_letters, digits, special_characters]

# Ensure the password length is at least 4 characters (one from each character set)
if password_length < 4:
    print("Password length must be at least 4 characters.")
else:
    # Generate the password
    password = []
    for i in range(4):
        password.append(random.choice(character_sets[i]))
    
    # Fill the rest of the password with random characters
    for i in range(4, password_length):
        charset = random.choice(character_sets)
        password.append(random.choice(charset))

    # Shuffle the characters to make the password random
    random.shuffle(password)

    # Convert the list of characters to a string
    generated_password = ''.join(password)

    # Display the generated password
    print("Generated Password: " + generated_password)