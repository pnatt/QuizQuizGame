from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

questions = []
for quest in question_data:
    question_text = quest["text"]
    question_answer = quest["answer"]
    new_question = Question(question_text, question_answer)
    questions.append(new_question)

quiz = QuizBrain(questions)
quiz.next_question()