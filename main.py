import random

class TwentyQuestionsGame:
    def __init__(self, objects):
        self.objects = objects
        self.selected_object = random.choice(objects)
        self.questions_asked = 0
        self.max_questions = 20

    def ask_question(self, question):
        self.questions_asked += 1
        if self.questions_asked > self.max_questions:
            return "You've exceeded the maximum number of questions."

        response = input(question + " (yes/no): ").strip().lower()
        if response not in ['yes', 'no']:
            return "Please answer with 'yes' or 'no'."
        return response

    def guess_object(self, guess):
        self.questions_asked += 1
        if self.questions_asked > self.max_questions:
            return "You've exceeded the maximum number of questions."

        if guess.lower() == self.selected_object.lower():
            return "Congratulations! You guessed it!"
        else:
            return "Incorrect guess. Try asking more questions."

    def start(self):
        print("Welcome to the 20 Questions Game!")
        print(f"You have {self.max_questions} questions to guess the object I'm thinking of.")
        
        while self.questions_asked < self.max_questions:
            question = input("Ask a yes/no question or make a guess: ").strip()
            if question.lower().startswith("is it") or question.lower().startswith("does it"):
                response = self.ask_question(question)
            else:
                response = self.guess_object(question)
            print(response)
            if response == "Congratulations! You guessed it!":
                break
        
        if self.questions_asked >= self.max_questions:
            print(f"Sorry, you've used all your questions. The object was: {self.selected_object}")

# List of objects to guess from
objects = ["apple", "banana", "car", "dog", "elephant", "flower", "guitar", "house", "ice cream", "jacket"]

# Start the game
game = TwentyQuestionsGame(objects)
game.start()