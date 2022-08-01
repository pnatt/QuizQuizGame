class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    def next_question(self):
        quest = self.question_list(self.question_number["text"])
        user_answer = input(quest + " (True / False)? : ").lower()
        self.question_number += 1
        return user_answer



