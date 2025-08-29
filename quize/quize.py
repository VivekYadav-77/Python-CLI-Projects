import os

print("*" * 8)
print(" QUIZ GAME ")
print("*" * 8)


questions = {
    "q1": "The ability of one class to acquire methods and attributes of another class is called __",
    "q2": "Which of the following is a type of inheritance?",
    "q3": "What type of inheritance has multiple subclasses to a single superclass?",
    "q4": "What is the depth of multilevel inheritance in Python?",
    "q5": "Which of the following is not an OOP concept in Python?",
    "q6": "Which keyword is used to define a function in Python?"
}

# Options
options = [
    {
        "A": "Inheritance",
        "B": "Abstraction",
        "C": "Polymorphism",
        "D": "Objects"
    },
    {
        "A": "Single",
        "B": "Double",
        "C": "Multiple",
        "D": "Both A and C"
    },
    {
        "A": "Multilevel",
        "B": "Multiplelevel",
        "C": "Hierarchical",
        "D": "None of these"
    },
    {
        "A": "8",
        "B": "9",
        "C": "10",
        "D": "Not defined"
    },
    {
        "A": "Encapsulation",
        "B": "Compilation",
        "C": "Polymorphism",
        "D": "Inheritance"
    },
    {
        "A": "function",
        "B": "def",
        "C": "fun",
        "D": "define"
    }
]


answers = ["A", "D", "C", "D", "B", "B"]


def play_quiz(max_rounds=1):
    """Run the quiz. max_rounds = how many times replay is allowed."""
    round_count = 0
    while round_count < max_rounds:
        score = 0
        for i, q in enumerate(questions.values()):
            print("\n" + q)  
            for key, val in options[i].items():
                print(f"{key}. {val}")  

            user_answer = input("Enter your option (A/B/C/D): ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                if user_answer == answers[i]:
                    print("✅ Correct answer!")
                    score += 1
                else:
                    print("❌ Wrong answer!")
                    score = max(0, score - 1)  
            else:
                print("⚠️ Invalid input! Restarting quiz...")
                os.system("cls")
                return play_quiz(max_rounds)

            print(f"Your current score: {score}/{len(questions)}")

     
        print("\n🎯 Quiz Finished!")
        print(f"Final Score: {score}/{len(questions)}")
        print(f"You answered {score} correctly.")
        print(f"Percentage: {(score / len(questions)) * 100:.2f}%")

        round_count += 1
        if round_count >= max_rounds:
            print("\nGame Over ❌ (Max rounds reached)")
            break

        
        again = input("\nDo you want to play again? (yes/no): ").lower()
        if again == "yes":
            os.system("cls")
            continue
        else:
            print("Thanks for playing!")
            break


play_quiz(max_rounds=3)
