import json
import requests

class question():
    def __init__(self, text = None, answer = None, guess = None):
        self.text = text
        self.answer = answer
        self.guess = guess
        
    def ask(self):
        """ask for the answer"""
        print(self.text)
        self.guess = str(input("Your answer = "))
        
    def check(self):
        """check if the answer is correct"""
        return self.answer == self.guess
        
class game():
    def __init__(self, questions):
        self.score = 0
        self.questions = questions
        
    def run(self):
        """main engine that run the quiz game"""
        for q in self.questions:
            q.ask()
            if q.check() == 1:
                self.score += 1
                print(f"Correct! Score is {self.score}/{len(self.questions)}\n")
            else:
                print(f"Wrong! The right answer is {q.answer}")
                print(f"Score is {self.score}/{len(self.questions)}\n")


# Request API from Open Trivial Database to get random questions
r = requests.get('https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple')

# Convert JSON payload to python dictionary type
r_json = json.loads(r.text)

# fill the question table with question\answer pairs
questionTable = []
for q in r_json["results"]:
    text    = q["question"]
    answer  = q["correct_answer"]
    questionTable.append(question(text, answer))