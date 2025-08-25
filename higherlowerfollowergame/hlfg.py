import random
import os


data = [
    {"name": "Rohit Sharma", "follower": 5000, "description": "cricketer", "country": "India"},
    {"name": "Messi", "follower": 6000, "description": "footballer", "country": "Argentina"},
    {"name": "The Rock", "follower": 3000, "description": "wrestler and actor", "country": "USA"},
    {"name": "Ruhez", "follower": 60000, "description": "YouTuber", "country": "Ukraine"},
    {"name": "Marvel", "follower": 46578, "description": "studio", "country": "USA"},
    {"name": "DC", "follower": 3421, "description": "studio", "country": "UK"}
]


def format_account(account):
    """Return a printable string from account dictionary"""
    return f"{account['name']}, a {account['description']} from {account['country']}"

def compare_followers(choice, f1, f2):
    """Return True if user guessed correctly"""
    return (choice == 1 and f1 > f2) or (choice == 2 and f2 > f1)

def clear_screen():
    """Clear the terminal (cross-platform)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    score = 0
    game_should_continue = True
    account2 = random.choice(data)

    while game_should_continue:
        account1 = account2
        account2 = random.choice(data)
        while account1 == account2:
            account2 = random.choice(data)

        print("\n Higher-Lower Followers Game ")
        print(f"Compare 1: {format_account(account1)}")
        print("   VS")
        print(f"Compare 2: {format_account(account2)}")

        try:
            choice = int(input("Who has more followers? Type 1 or 2: "))
        except ValueError:
            print("❌ Invalid input. Please type 1 or 2.")
            continue

        f1, f2 = account1["follower"], account2["follower"]
        is_correct = compare_followers(choice, f1, f2)

        clear_screen()
        if is_correct:
            score += 1
            print(f"✅ Correct! Current Score: {score}")
        else:
            print(f"❌ Wrong! Final Score: {score}")
            game_should_continue = False

def main():
    while True:
        play_game()
        again = input("Play again? (yes/no): ").lower()
        if again != "yes":
            print("👋 Thanks for playing! Goodbye.")
            break


main()
