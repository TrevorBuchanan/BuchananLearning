from app import create_app, db
from app.Model.models import Course, Member, Student, Educator, Admin

app = create_app()

# Users
# - Student 
# - Educator
# - AdminLearners

# Index 
# - Educators
#   - Eductor ratings
# - Courses
#   - Course ratings
#   - Course suggestions
#   - Course comments

# All Courses
# My Courses
# Lessons
# Lesson
# Add course
# Add lesson
# Message educator

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Course': Course, 'Member': Member, 'Student': Student, 'Educator': Educator, 'Admin': Admin}

@app.before_request
def initDB(*args, **kwargs):
    if app.got_first_request:
        db.create_all()

if __name__ == "__main__":
    app.run(debug=True)