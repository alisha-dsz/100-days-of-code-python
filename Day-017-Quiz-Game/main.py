from data import question_data
from question_model import Question
from quiz_brain import QuizBrain


question_bank = []
for q_and_a in question_data:
    question_text = q_and_a["text"]
    question_answer = q_and_a["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.next_question()

quiz_brain.ending()