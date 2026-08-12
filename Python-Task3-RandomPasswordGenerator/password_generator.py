import random
import string

while True:
    try:
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            print("Password length must be at least 8.")
            continue

        upper = input("Include uppercase letters? (yes/no): ").lower() == "yes"
        lower = input("Include lowercase letters? (yes/no): ").lower() == "yes"
        numbers = input("Include numbers? (yes/no): ").lower() == "yes"
        symbols = input("Include symbols? (yes/no): ").lower() == "yes"

        if sum([upper, lower, numbers, symbols]) < 2:
            print("Please select at least two character types.")
            continue

        characters = ""

        if upper:
            characters += string.ascii_uppercase

        if lower:
            characters += string.ascii_lowercase

        if numbers:
            characters += string.digits

        if symbols:
            characters += string.punctuation

        password = "".join(random.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

        again = input("\nGenerate another password? (yes/no): ").lower()

        if again != "yes":
            print("Thank you for using the Password Generator!")
            break

    except ValueError:
        print("Please enter a valid number.")