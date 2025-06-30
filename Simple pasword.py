# password_generator_cli.py

import random
import string

def generate_password(length, use_letters, use_digits, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Error: No character set selected.")
        return ""

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")
    
    try:
        length = int(input("Enter password length: "))
        use_letters = input("Include letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        if length <= 0:
            print("Password length must be positive.")
            return

        password = generate_password(length, use_letters, use_digits, use_symbols)
        if password:
            print(f"\nGenerated Password: {password}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

if _name_ == "_main_":
    main()