from flask import Blueprint, render_template
from models import get_db_connection, Quiz
from utils import get_random_number

main_bp = Blueprint("main", __name__)

quiz = Quiz()

@main_bp.route("/")
def index():
    numbers = get_random_number(10,0,50)
    
    return f'Si jalo prro, los siguientes son los numeros: {numbers}'

@main_bp.route('/get_a_question')
def get_question():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = 'SELECT * FROM trivia WHERE id_trivia = 7'
    cursor.execute(query)
    question = cursor.fetchone()
    cursor.close()
    
    return f'Esta es la pregunta perrillo {question}'

@main_bp.route('/questions_video_games')
def questions_video_games():
    quiz.create_ten_questions(10,0,50)
    questions = quiz.get_questions