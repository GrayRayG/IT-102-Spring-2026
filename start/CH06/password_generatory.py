"""
Password Generator

A secure password generator that has a minimum lenght of 8
"""
#Libraries utilized
import random
import string 


#Define character pools
UPPERCASE = string.ascii_uppercase
LOWERCASE = string.ascii_lowercase
DIGITS = string.digits
SPECIAL = r"!@$%&*()_-|\;<>"

# Minimum password length
MIN_LENGTH = 8

#Helper function

def get_yes_or_no(prompt: str) -> bool:
    """Ask the user for a yes or no question"""
    while True:
        answer = input(prompt).strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print(" Please enter yes or no: ")

def get_password_length() -> int:
    while True:
        try:
            length = int(input("How long do you want password?"))
            if length >= MIN_LENGTH:
                return length
            print("Please enter a valid length try again")
        except ValueError:
            print("Please enter a whole number")

def get_criteria() -> dict:
    """Take length, uppercase, lowercase, digits, special input from user"""
    length = get_password_length()

    criteria = {
        "length": length,
        "uppercase": get_yes_or_no(" Do you want uppercase letters?"),
        "lowercase": get_yes_or_no(" Do you wanter lowercase letters?"),
        "digits": get_yes_or_no(" Numbers (0-9)"),
        "special": get_yes_or_no(" Do you want special characters?"),
    }
    
    #Validator of criteria
    if not any([criteria["uppercase"], ["lowercase"],
                criteria["digits"], criteria["special"]]):
        print(" You must select one character type")
        return get_criteria()
    return criteria

def build_pool(criteria: dict) -> tuple[str, list[str]]:
    """This is a character pool"""
    pool = ""
    required = []

    if criteria["uppercase"]:
        pool += UPPERCASE
        required.append(random.choice(UPPERCASE))

    if criteria["lowercase"]:
        pool += LOWERCASE
        required.append(random.choice(LOWERCASE))

    if criteria["digits"]:
        pool += DIGITS
        required.append(random.choice(DIGITS))

    if criteria["special"]:
        pool += SPECIAL
        required.append(random.choice(SPECIAL))
    return pool, required

def generate_password(criteria: dict) -> str:
    """Generation of password creator"""
    pool, required = build_pool(criteria)
    length = criteria["length"]

    #Fill any remainingh slot with random characters
    remaining_count = length - len(required)
    remaining = [random.choice(pool) for _ in range(remaining_count)]

    password_chars = required + remaining
    random.shuffle(password_chars)


    return"".join(password_chars)


def main():

    while True:
        criteria = get_criteria()
        password = generate_password(criteria)
        print("This is your generated password")
        print(f"{password}")

        if not get_yes_or_no("Generate another password(y/n)"):
            print("Stay secure")
            break
        print()

if __name__ == "__main__":
    main()