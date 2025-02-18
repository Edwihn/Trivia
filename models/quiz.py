class Question:
    def __init__(self, difficulty, category, question, correct_answer):
        self.difficulty = difficulty
        self.category = category
        self.question = question
        self.correct_answer = correct_answer
        
class Quiz:
    def __init__(self):
        self.array = []
        self.size = 0
    def add_question(self,difficulty, category, question, correct_answer):
        question = Question(difficulty, category, question, correct_answer)
        self.array.append(question)
        self.size+=1
        