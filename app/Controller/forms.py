# 
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import  ValidationError, DataRequired, Length
from flask_login import current_user

from app.Model.models import Course, Member

class CourseForm(FlaskForm):
    title = StringField('Course title', 
                        validators=[
                            DataRequired(), 
                            Length(max=150) 
                        ])
    description = StringField('Course description', 
                        validators=[
                            Length(max=500)  
                        ])
    submit = SubmitField('Post')

    def validate_title(self, title): 
        course = Course.query.filter_by(title = title.data).first()
        if course is not None:
            raise ValidationError('A course with this title already exists!')
