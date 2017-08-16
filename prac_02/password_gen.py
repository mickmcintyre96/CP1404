print("Password Generator")

import random
LETTERS = "abcdefghijklmnopqrstuvwyz"
LETTERS_UPPER = "ABCDEFGHIJKLMONPQRSTUVWYXZ"
NUMBERS = "1234567890"
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
password = ""

password_length = int(input('How long should the password be? '))

while password_length < 4:
    print("Error, Password must be atleast 4 characters long")
    password_length = int(input("Please re-enter the length of the password: "))

password += (random.choice(LETTERS_UPPER))
password += (random.choice(LETTERS))
password += (random.choice(NUMBERS))
password += (random.choice(SPECIAL_CHARACTERS))
for i in range (4, password_length):
    x = random.randint(1,4)
    if x == 1:
        password += (random.choice(LETTERS_UPPER))
    elif x == 2:
        password += (random.choice(LETTERS))
    elif x == 3:
        password += (random.choice(NUMBERS))
    else:
        password += (random.choice(SPECIAL_CHARACTERS))

shuffled_password = ''.join(random.sample(password, len(password)))

print(shuffled_password)

