import sys
from flask import Blueprint, render_template
from config import Config

bp_routes = Blueprint('routes', __name__, template_folder=Config.TEMPLATE_FOLDER)

@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/courses', methods=['GET'])
def courses():
    return render_template('courses.html', title="Courses")

@bp_routes.route('/lessons/<course_title>', methods=['GET'])
def course_lessons(course_title):
    return render_template('lessons.html', title=f"{course_title} Lessons")

@bp_routes.route('/lesson/<lesson_title>', methods=['GET'])
def single_lesson(lesson_title):
    # Lesson details should be structured with the appropriate template and data.
    return render_template('lesson.html', title=lesson_title)
