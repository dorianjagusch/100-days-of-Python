class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("Your answer is correct!")
            self.score += 1
        else:
            print("Your answer is false.")
        print(f"The answer is: {correct_ans}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: "
                            f"{current_question.text} Type True/False: ")
        self.check_answer(user_answer, current_question.answer)

