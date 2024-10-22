# test python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulamos la base de datos con diccionarios para cursos y lecciones
courses = {}
lessons = {}

@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)  # Listar todos los cursos disponibles

@app.route('/courses', methods=['POST'])
def create_course():
    course_id = len(courses) + 1
    courses[course_id] = request.json  # Crear curso (sólo profesores)
    return jsonify({'course_id': course_id})

@app.route('/courses/<int:course_id>/lessons', methods=['GET'])
def get_lessons(course_id):
    return jsonify(lessons.get(course_id, {}))  # Obtener lecciones del curso

@app.route('/lessons/<int:lesson_id>', methods=['POST'])
def take_lesson(lesson_id):
    answers = request.json.get('answers', [])  # Enviar respuestas de la lección
    return jsonify({"result": "Aprobado" if sum(answers) > 70 else "Reprobado"})
