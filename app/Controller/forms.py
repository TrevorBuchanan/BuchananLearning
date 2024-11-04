# 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  ValidationError, DataRequired
from flask_login import current_user

from app.Model.models import Course, Member

class CourseForm(FlaskForm):
    title = StringField('Course title', validators=[DataRequired()])
    submit = SubmitField('Post')

    def validate_title(self, title): 
        course = Course.query.filter_by(title = title.data).first()
        if course is not None:
            raise ValidationError('A course with this title already exists!')
