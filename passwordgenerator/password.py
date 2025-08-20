import passheading
import random

letters = list("abcdefghijklmnopqrstuvwxyz")
symbols = ['(', ')', '%', '@', '!', '&', '+', '$', '[', ']', '{', '}']
numbers = list("123456789")

print(passheading.logo)

def easy_mode():
    password_chars = []

    letter_count = int(input("How many letters do you want in your password? "))
    for _ in range(letter_count):
        password_chars.append(random.choice(letters))

    number_count = int(input("How many numbers do you want in your password? "))
    for _ in range(number_count):
        password_chars.append(random.choice(numbers))

    random.shuffle(password_chars)
    generated_password = "".join(password_chars)
    print(f"\nYour EASY password is:\n{generated_password}\n")


def hard_mode():
    password_chars = []

    letter_count = int(input("How many letters do you want in your password? "))
    for _ in range(letter_count):
        password_chars.append(random.choice(letters))

    symbol_count = int(input("How many symbols do you want in your password? "))
    for _ in range(symbol_count):
        password_chars.append(random.choice(symbols))

    number_count = int(input("How many numbers do you want in your password? "))
    for _ in range(number_count):
        password_chars.append(random.choice(numbers))

    random.shuffle(password_chars)
    generated_password = "".join(password_chars)
    print(f"\nYour HARD password is:\n{generated_password}\n")


# Difficulty selection
difficulty = input("Choose difficulty level (easy / hard): ").lower()

if difficulty == "easy":
    easy_mode()
elif difficulty == "hard":
    hard_mode()
else:
    print("Invalid input. Please restart and choose 'easy' or 'hard'.")
