import string

COMMAN_PASSWORDS = [
    "password", "123456", "12345678",
    "qwerty", "abc123", "letmein", "monkey",
    "dragon", "111111", "iloveyou"
]

SYMBOLS = string.punctuation

def check_strength(password):
    strength = 0
    notes = []

    length = (len(password))

    if length >= 12: 
        strength += 2
    elif length >= 8:
        strength += 1
    else:
        notes.append("password is too short (less than 8 characters). ")

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in SYMBOLS for c in password)

    count_type = sum([has_lower, has_upper, has_digit, has_symbol])
    if count_type == 4:
        strength += 2
    elif count_type == 3:
        strength += 1
    else:
        notes.append("Use a mix of uppercase, lowercase, digits, ans symbols.")


    if password.islower() in COMMAN_PASSWORDS:
        note.append("This is a very comon password. Avoid it!")
        strength = 0
    
    if password.isdigit():
        notes.append("All digits is esay to guess!")
        strength = min(strength, 1)

    if len(set(password)) <= 2:
        notes.append("Too few unique characters - easy to guess! ")
        strengh = min (strength , 1)

    if strength >= 4:
        rating = "Very Strong!"
    elif strength >= 3:
        rating = "Strong"
    elif strength == 2:
        rating = "Medium"
    else:
        rating = "Weak"

    return rating, notes


def main():
    print("=== Password Strength Check ===")
    print("Enter 'quit' to exit.\n")
    while True:
        pwd = input("Enter password to check: ").strip()
        if pwd.lower() == 'quit':
            print("By")
            break
        rating, notes = check_strength(pwd)
        print(f"\nPassword strength {rating}")
        if notes: 
            print("Notes:")
            for n in notes:
                print(" -",n)
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()

        