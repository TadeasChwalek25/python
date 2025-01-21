class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "Jaký je hlavní město Česka?", "options": ["Praha", "Brno", "Ostrava"], "answer": "Praha"},
            {"question": "Kolik je 87 * 36?", "options": ["3 135", "4 568", "2846"], "answer": "3 135"},
            {"question": "Datum narození Karla IV. Lucemburského?", "options": ["15.06.1548", "30.05.1325", "14.05.1316"], "answer": "14.05.1316"}
        ]
        self.score = 0

    def ask_question(self, question_data):
        print(f"\nOtázka: {question_data['question']}")
        for i, option in enumerate(question_data['options'], 1):
            print(f"{i}. {option}")
        while True:
            try:
                choice = int(input("Vyber číslo správné odpovědi: "))
                if 1 <= choice <= len(question_data["options"]):
                    return question_data["options"][choice - 1] == question_data["answer"]
                else:
                    print("Zadej číslo v rozsahu možností!")
            except ValueError:
                print("Zadej platné číslo!")

    def play(self):
        print("Vítej ve hře Kvíz! Odpověz správně na otázky a získej body.")
        for question_data in self.questions:
            if self.ask_question(question_data):
                print("Správně!")
                self.score += 1
            else:
                print(f"Špatně! Správná odpověď byla: {question_data['answer']}")
        print(f"\nHra skončila! Tvé konečné skóre: {self.score}/{len(self.questions)}")

# Spuštění hry
if __name__ == "__main__":
    game = QuizGame()
    game.play()
