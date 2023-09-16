import random
import string

def generate_password(length):
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    special_chars = '!@#$%^&*()_+[]{}|;:,.<>?'

    complexity = input("Choose complexity level (easy/medium/hard): ").lower()
    if complexity == 'easy':
        characters = lower_case + upper_case
    elif complexity == 'medium':
        characters = lower_case + upper_case + digits
    elif complexity == 'hard':
        characters = lower_case + upper_case + digits + special_chars
    else:
        print("Invalid complexity level. Using medium complexity.")
        characters = lower_case + upper_case + digits

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))

    if length < 8:
        print("Password length should be at least 8 characters.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
