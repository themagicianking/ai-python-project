import random


class Mastermind:
    # generates code and sets max attempts as well as attempts made
    def __init__(self):
        self.code = self.generate_code()
        self.max_attempts = 10
        self.attempts = 0

    def generate_code(self):
        # Generate a random 4-digit code with digits from 1 to 6
        return [random.randint(1, 6) for _ in range(4)]

    # runs every turn after the player has guessed and returns the number of correct digits in correct positions and correct digits in incorrect positions
    def get_feedback(self, guess):
        black_pegs = 0
        white_pegs = 0
        code_copy = self.code[:]
        guess_copy = guess[:]

        # First pass: count black pegs
        for i in range(4):
            if guess_copy[i] == code_copy[i]:
                black_pegs += 1
                code_copy[i] = guess_copy[i] = None

        # Second pass: count white pegs
        for i in range(4):
            if guess_copy[i] is not None and guess_copy[i] in code_copy:
                white_pegs += 1
                code_copy[code_copy.index(guess_copy[i])] = None

        return black_pegs, white_pegs

    def start(self):
        print("Welcome to Mastermind!")
        print("Try to guess the 4-digit code. Each digit is between 1 and 6.")
        print(f"You have {self.max_attempts} attempts to guess the code.")
        # initiates turn if player has not run out of attempts
        while self.attempts < self.max_attempts:
            guess = input("Enter your guess (4 digits, each between 1 and 6): ")
            # ensure guesses are all digits
            try:
                int(guess)
            except:
                print("Invalid guess. Please enter 4 digits, each between 1 and 6.")
                continue
            guess = [int(digit) for digit in guess]
            # ensure guesses are the correct length and not more than 6
            if len(guess) != 4 or not all(1 <= digit <= 6 for digit in guess):
                print("Invalid guess. Please enter 4 digits, each between 1 and 6.")
                continue

            self.attempts += 1
            black_pegs, white_pegs = self.get_feedback(guess)
            # prints feedback to console
            print(f"Black pegs (correct digit and position): {black_pegs}")
            print(f"White pegs (correct digit but wrong position): {white_pegs}")
            # checks to see if player has guessed code correctly
            if black_pegs == 4:
                print(
                    f"Congratulations! You guessed the code in {self.attempts} attempts!"
                )
                break
        else:
            print(
                f"Sorry, you've used all your attempts. The code was: {''.join(map(str, self.code))}"
            )


# Start the game
game = Mastermind()
game.start()
