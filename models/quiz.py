from models import get_db_connection
from utils import get_random_number

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
        self.user_answers = []
        
    def add_question(self,difficulty, category, question, correct_answer):
        question = Question(difficulty, category, question, correct_answer)
        self.array.append(question)
        self.size+=1
        
    def clear_array(self):
        if self.size <= 0:
            return 'There is nothing here'
        for i in range(len(self.array)):
            self.array[i] = None
        self.array.clear()
        self.size = 0
        
    def get_questions(self):
        if self.size <= 0:
            return None
        
        question_list = list()
        
        for i in range(len(self.array)):
            question_list.append((self.array[i].difficulty, self.array[i].category, self.array[i].question, self.array[i].correct_answer))
        
        return question_list
    
    def create_ten_questions(self, count, min_value, max_value):
        if self.size > 0:
            self.clear_array()
        if min_value < 0:
            return 'Type a valid number'
        if max_value > 200:
            return 'Max number out of index'
        if min_value >= max_value:
            return 'Incorrect sintaxis (The min value is bigger than the max value or equals)'
    
        numbers = get_random_number(count, min_value, max_value)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        
        for i in numbers:
            print('Here is the NUMBER', i)
            query = 'SELECT * FROM trivia WHERE id_trivia = %s'
            cursor.execute(query, (i,))
            question = cursor.fetchone()
            self.add_question(question[1],question[2], question[3],question[4])
            
        cursor.close()
        
    def update_user_answers(self, answers_array):
        if not answers_array:
            return print('Insert a valid array')
        if self.size <= 0:
            return print('There is not a question to add an answer')
        
        self.user_answers = answers_array
        
    def get_user_answers(self):
        if len(self.user_answers) <= 0:
            return print('There is not answers registered')
        
        return self.user_answers    
        
    def __str__(self):
        return '\n'.join([f"Difficulty: {question.difficulty}, Category: {question.category}, Question: {question.question}, Correct answer: {question.correct_answer}" for question in self.array])