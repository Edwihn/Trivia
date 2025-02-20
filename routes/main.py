from flask import Blueprint, render_template, url_for, redirect, request
from models import get_db_connection, Quiz
from utils import get_random_number

main_bp = Blueprint("main", __name__)

quiz = Quiz()

@main_bp.route("/")
def index():
    
    return render_template('main_page.html')

@main_bp.route('/get_a_question')
def get_question():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM trivia WHERE id_trivia = 7'
    cursor.execute(query)
    question = cursor.fetchone()
    cursor.close()
    
    return f'Esta es la pregunta perrillo {question}'

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
    print(questions)
    if category and questions:
        return render_template('test.html', category=category, questions=questions)
    return 'there are not questions or category'