import random

class GuessGame:
    def __init__(self, min_value=1, max_value=100):
        self.min_value = min_value
        self.max_value = max_value
        self.number_to_guess = random.randint(min_value, max_value)
        self.attempts = 0

    def make_guess(self, guess):
        self.attempts += 1
        if guess < self.number_to_guess:
            return "Příliš nízko!"
        elif guess > self.number_to_guess:
            return "Příliš vysoko!"
        else:
            return f"Správně! Uhodl jsi číslo {self.number_to_guess} za {self.attempts} pokusů."

def play_game():
    print("Vítej ve hře 'Hádej číslo'!")
    print("Hádáš číslo mezi 1 a 100.")
    game = GuessGame()

    while True:
        try:
            user_guess = int(input("Zadej svůj tip: "))
            result = game.make_guess(user_guess)
            print(result)
            if "Správně!" in result:
                break
        except ValueError:
            print("Prosím, zadej platné číslo!")

# Spuštění hry
if __name__ == "__main__":
    play_game()
