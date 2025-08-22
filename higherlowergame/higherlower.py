import random

def play_game():
    print("Welcome to the Higher-Lower Game!!")
    print("I'm thinking of a number between 1 and 50.")

    computer_number = random.randint(1, 50)

    difficulty = input("Enter 'easy' (10 lives) or 'hard' (5 lives): ").lower()
    lives = 10 if difficulty == "easy" else 5 if difficulty == "hard" else None

    if lives is None:
        print("Invalid input. Starting again...")
        return play_game()

    while lives > 0:
        try:
            user_guess = int(input("Make a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_guess > computer_number:
            print("Your guess is too high.")
            lives -= 1
        elif user_guess < computer_number:
            print("Your guess is too low.")
            lives -= 1
        else:
            print(f"🎉 Correct! The number was {computer_number}.")
            break

        print(f"Lives left: {lives}")

    if lives == 0:
        print(f"😢 Out of lives! The number was {computer_number}.")

def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("Goodbye 👋")
            break
main()
