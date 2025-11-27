# Who wants to be a millionare game

import sys

class Question:
    def __init__(self, prompt, options, answer, prize):
        self.prompt = prompt
        self.options = options
        self.answer = answer
        self.prize = prize


class MillionaireGame:
    def __init__(self):
        self.questions = self.load_questions()
        self.current_prize = 0

    def load_questions(self):
        return [
            Question(
                "What is the capital of France?",
                ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"],
                "B", 1000
            ),
            Question(
                "Which language is used for web apps?",
                ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
                "C", 2000
            ),
            Question(
                "Who wrote 'Hamlet'?",
                ["A) Shakespeare", "B) Dickens", "C) Orwell", "D) Tolstoy"],
                "A", 5000
            ),
            Question(
                "Which planet is known as the Red Planet?",
                ["A) Venus", "B) Earth", "C) Mars", "D) Jupiter"],
                "C", 10000
            ),
            Question(
                "What is the largest ocean?",
                ["A) Atlantic", "B) Pacific", "C) Indian", "D) Arctic"],
                "B", 20000
            )
        ]

    def start(self):
        print("\n===== WHO WANTS TO BE A MILLIONAIRE =====")
        print("Answer correctly to keep moving. One mistake = game over.\n")

        for q in self.questions:
            print(f"\nPrize: Rs {q.prize}")
            print(q.prompt)
            for opt in q.options:
                print(opt)

            user_ans = input("\nYour answer (A/B/C/D): ").upper()

            if user_ans == q.answer:
                self.current_prize = q.prize
                print(f"✔ Correct! You now have Rs {self.current_prize}.")
            else:
                print(f"\n✘ Wrong answer! Correct answer was: {q.answer}")
                print(f"You leave with Rs {self.current_prize}.")
                sys.exit()

        print("\n🎉 Congratulations! You answered all questions!")
        print(f"You won a total of Rs {self.current_prize}.")


# ---- RUN GAME ----
if __name__ == "__main__":
    game = MillionaireGame()
    game.start()
