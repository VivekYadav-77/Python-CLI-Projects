import hanggamelogo
import random
words = ["orange", "mango", "tiger", "lion"]
print(hanggamelogo.logo)
stages = [
    """
  +----+
  |    |
  0    |
 /|\\   |
 / \\   |
--------""",
    """
  +----+
  |    |
  0    |
 /|\\   |
 /     |
--------""",
    """
  +----+
  |    |
  0    |
 /|\\   |
       |
--------""",
    """
  +----+
  |    |
  0    |
 /|    |
       |
--------""",
    """
  +----+
  |    |
  0    |
  |    |
       |
-------- """,
    """
  +----+
  |    |
  0    |
       |
       |
-------"""
]

play_again = True

while play_again:
    chosen_word = random.choice(words)
    display = ["_" for _ in chosen_word]
    print(" ".join(display))

    lives = 6
    game_over = False

    while not game_over:
        guess = input("\nguess a letter: ").lower()

        if guess in chosen_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    display[i] = guess
            print("right guess")
        else:
            lives -= 1
            print("wrong guess")
            print(stages[6 - lives - 1])
            print(f"lives left: {lives}")

            if guess > chosen_word[0]:
                print("your guess is too big")
            elif guess < chosen_word[0]:
                print("your guess is too low")
        print(" ".join(display))
        if "_" not in display:
            game_over = True
            print("\n🎉 You won!")
        if lives == 0:
            game_over = True
            print("\n💀 You lost! The word was:", chosen_word)
    again = input("\nDo you want to play again 😇? (y/n): ").lower()
    if again != "y":
        play_again = False
        print("thanks for playing!")


