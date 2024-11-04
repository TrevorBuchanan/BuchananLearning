# app/Controller/routes.py
import sys
from flask import Blueprint, render_template
from config import Config
from flask_login import login_user, current_user, logout_user, login_required
from app.decorators import role_required 

bp_routes = Blueprint('routes', __name__, template_folder=Config.TEMPLATE_FOLDER)

@bp_routes.route('/', methods=['GET'])
def index():
    return render_template('index.html', title="Buchanan Learning")

@bp_routes.route('/student_courses', methods=['GET'])
@login_required
@role_required('Student')
def student_courses():
    courses = []
    educators = []
    return render_template('student_courses.html', title="Courses", courses=courses, educators=educators)

@bp_routes.route('/admin_courses', methods=['GET'])
@login_required
@role_required('Admin')
def admin_courses():
    courses = []
    educators = []
    return render_template('admin_courses.html', title="Courses", courses=courses, educators=educators)

@bp_routes.route('/educator_courses', methods=['GET'])
@login_required
@role_required('Educator')
def educator_courses():
    courses = []
    educators = []
    return render_template('educator_courses.html', title="Courses", courses=courses, educators=educators)

@bp_routes.route('/lessons/<course_title>', methods=['GET'])
@login_required
def course_lessons(course_title):
    return render_template('lessons.html', title=f"{course_title} Lessons")

@bp_routes.route('/lesson/<lesson_title>', methods=['GET'])
@login_required
def single_lesson(lesson_title):
    # Lesson details should be structured with the appropriate template and data.
    return render_template('lesson.html', title=lesson_title)

@bp_routes.route('/student_profile', methods=['GET', 'POST'])
@login_required
@role_required('Student')
def student_profile():
    return render_template('student_profile.html')

@bp_routes.route('/admin_profile', methods=['GET', 'POST'])
@login_required
@role_required('Admin')
def admin_profile():
    return render_template('admin_profile.html')

@bp_routes.route('/educator_profile', methods=['GET', 'POST'])
@login_required
@role_required('Educator')
def educator_profile():
    return render_template('educator_profile.html')