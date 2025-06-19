from flask import Blueprint, render_template, url_for, redirect, request
from models import get_db_connection, Quiz
from utils import get_random_number

main_bp = Blueprint("main", __name__)

quiz = Quiz()

@main_bp.route("/")
def index():
    return render_template('main_page.html')

@main_bp.route('/questions/<category>', methods=['GET'])
def questions_video_games(category):
    match category:
        case 'videogames':        
            quiz.create_ten_questions(10,1,50)
            return redirect(url_for('main.render_quiz_page', category='Videogames'))
        case 'geography':
            quiz.create_ten_questions(10,51,90)
            return redirect(url_for('main.render_quiz_page', category='Geography'))
        case 'general':
            quiz.create_ten_questions(10,91,140)
            return redirect(url_for('main.render_quiz_page', category='General Knowledge'))
        case 'film':
            quiz.create_ten_questions(10,141,170)
            return redirect(url_for('main.render_quiz_page', category='Film movies'))
        case 'music':
            quiz.create_ten_questions(10,171,200)
            return redirect(url_for('main.render_quiz_page', category='Music'))
        case _:
            return 'You must choose a category'

@main_bp.route('/quiz/<category>')
def render_quiz_page(category):
    questions = quiz.get_questions()
    if category and questions:
        return render_template('test.html', category=category, questions=questions)
    return 'there are not questions or category'

@main_bp.route('/answers', methods=['POST'])
def answer():
    if request.method == 'POST':
        questions_answers = []
        for i in range(1,11):
            questions_answers.append(request.form.get(f'questions{i}'))
        
        print('ANSWERS ', questions_answers) 
        quiz.update_user_answers(questions_answers)
        return redirect(url_for('main.render_answers'))
    else:
        return 'METHOD NOT ALLOWED'
        
@main_bp.route('/correct_incorrect_answers', methods=['GET'])
def render_answers():
    answers = quiz.get_user_answers()
   
    questions = quiz.get_questions()
   
    questions_and_answers = []
    for i in range(0,10):
        questions_and_answers.append([questions[i][2], questions[i][3], answers[i]])
    print('QUESTIONS AND ANSWERS ', questions_and_answers)
    return render_template('answers.html', questions=questions_and_answers)