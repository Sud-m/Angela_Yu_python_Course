from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(question["text"], question["answer"]) for question in question_data]
Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print(f"You've completed the quiz. \nYour final score was: {Quiz.score}/{len(question_bank)}.")
