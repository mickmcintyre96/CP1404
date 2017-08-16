print("Password Generator")

import random
LETTERS = "abcdefghijklmnopqrstuvwyz"
LETTERS_UPPER = "ABCDEFGHIJKLMONPQRSTUVWYXZ"
NUMBERS = "1234567890"
password = ""

password_length = int(input('How long should the password be? '))
# upper_case_characters = int(input("How many upper case characters are required? "))
# lower_case_characters = int(input("How many lower case characters are required? "))
# numbers_required = int(input("How many numbers are required? "))

# while upper_case_characters + lower_case_characters + numbers_required != password_length:
    print("error, make sure length and numbers is equal")
    password_length = int(input('How long should the password be? '))
    # upper_case_characters = int(input("How many upper case characters are required? "))
    # lower_case_characters = int(input("How many lower case characters are required? "))
    # numbers_required = int(input("How many numbers are required? "))

# for i in range (upper_case_characters):
#     password += (random.choice(LETTERS_UPPER))
#
# for c in range (lower_case_characters):
#     password += (random.choice(LETTERS))
#
# for d in range (numbers_required):
#     password += (random.choice(NUMBERS))


shuffled = ''.join(random.sample(password, len(password)))

print (shuffled)