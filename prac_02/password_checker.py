"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"
MIN_NUMBER_CHARACTERS = 1


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {0} and {1} characters, and contain at least {2} each of the following: \n "
          "\t- Uppercase character\n \t- Lowercase character\n \t- Number".format(MIN_LENGTH, MAX_LENGTH,
                                                                                  MIN_NUMBER_CHARACTERS))

    # print("\t1 or more uppercase characters")
    # print("\t1 or more lowercase characters")
    # print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\t- Special character {}: ".format(SPECIAL_CHARACTERS))
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password! Please try again")
        password = input("> ")
    print("Your " + str(
        len(password)) + " character password is valid: {}".format(password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # TODO: if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False
    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        # TODO: count each kind of character (use str methods like isdigit)
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isnumeric():
            count_digit += 1
        elif char in SPECIAL_CHARACTERS:
            count_special += 1


    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower < MIN_NUMBER_CHARACTERS or count_upper < MIN_NUMBER_CHARACTERS or count_digit < MIN_NUMBER_CHARACTERS:
        return False
        # TODO: if special characters are required, then check the count of those
        # and return False if it's zero
    if SPECIAL_CHARS_REQUIRED and count_special == 0:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
