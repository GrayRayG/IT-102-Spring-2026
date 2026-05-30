"""
This is to check passwords based on length and complexity
"""

#libraries utilized are
import re
import sys

#List of commonly used weak passwords
COMMON_PASSWORDS = [
    "password", "123456", "password123", "Password1", "admin", "letmein",
    "qwerty", "abc123", "welcome1", "1234567890"
]

def check_password_strength(password):
    """
    Check the password strength freturn feedback and score
    +1 for length of >= 8
    +2 for length of >=12
    +1 for uppercase and lowercase
    +1 for a digit
    +1 for a special character
    Deduction:
    -2 Password is in common password list
    """

    score = 0
    feedback = []

    #Check minimum length minimum
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("To short of password we need 8 characters")
    
    #check normal length
    if len(password) >= 12:
        score += 1
        feedback.append("good length of 12+ characters")
    else:
        feedback.append("Consider using 12+ characters for better security")


    #Check the case
    if re.search(r'[A-Z]', password) and re.search('[a-z]', password):
        score += 1
        feedback.append("Contains both an uppercase and lowercase")
    else:
        feedback.append("Please mix uppercase and lowercase")

    #check if there is a digit
    if re.search(r'\d', password):
        score += 1
        feedback.append("Contains a digit or number")
    else:
        feedback.append("Suggested to add a number")

    #check special character
    if re.search(r'[!@#$%^&*(),.?":{}|<>_\-]', password):
        score += 1
        feedback.append("Contains one special character")

    else:
        feedback.append("Add at least one special character")

    #check password list
    if password.lower() in COMMON_PASSWORDS:
        score -= 2
        feedback.append("This is a common password")

    #Determine the strength of the password
    score = max(score, 0)
    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Moderate"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"
    
    return score, strength, feedback

def main():
    print("Password Strength Check")

        #Accept a password from command line
    if len(sys.argv) > 1:
        password = sys.argv[1]
    else:
        password = input("Enter your password to check: ")

    score, strength, feedback = check_password_strength(password)

    print(f" Score : {score}")
    print(f" Strength: {strength}")
    print("\n Feedback:")
    for line in feedback:
        print(f" {line}")

if __name__ == "__main__":
    main()