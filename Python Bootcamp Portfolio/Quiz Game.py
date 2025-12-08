#-------QUIZ GAME (Object Oriented Programming)-------#

question_data = [
    {"question": "Approximately one quarter of human bones are in the feet.", "correct_answer": "True"},
    {"question": "The total surface area of a human lungs is the size of a football pitch.", "correct_answer": "True"},
    {"type": "boolean", "difficulty": "hard", "category": "Science &amp; Nature",
     "question": "It was once believed that injecting shark cartilage into people would prevent them from contracting cancer.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science &amp; Nature",
     "question": "An average human can go two weeks without water.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "'Tachycardia' or 'Tachyarrhythmia' refers to a resting heart-rate near or over 100 BPM.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Centripedal force is an apparent force that acts outward on a body moving around a center, arising from the body's inertia.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science &amp; Nature",
     "question": "An exothermic reaction is a chemical reaction that releases energy by radiating electricity.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "The Neanderthals were a direct ancestor of modern humans.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "Sugar contains fat.", "correct_answer": "False",
     "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science &amp; Nature",
     "question": "A plant that has a life cycle for more than a year is known as an annual.",
     "correct_answer": "False", "incorrect_answers": ["True"]},
    {"type": "boolean", "difficulty": "medium", "category": "Science &amp; Nature",
     "question": "In the periodic table, Potassium's symbol is the letter K.",
     "correct_answer": "True", "incorrect_answers": ["False"]},
    {"type": "boolean", "difficulty": "easy", "category": "Science &amp; Nature",
     "question": "Celiac Disease is a disease that effects the heart, causing those effected to be unable to eat meat.",
     "correct_answer": "False", "incorrect_answers": ["True"]}
]

class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.question} (True/False): ")
        self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Congrats, you are correct!")
        else:
            print("Sorry, you are incorrect.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")

question_bank = []

for question in question_data:
    question_question = question["question"]
    question_correct_answer = question["correct_answer"]
    new_question = Question(question_question, question_correct_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score: {quiz.score}/{quiz.question_number}")

