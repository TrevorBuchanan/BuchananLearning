# app/Controller/auth_forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import  ValidationError, DataRequired, EqualTo, Length, Email
from app.Model.models import Member

class StudentRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        member = Member.query.filter_by(username=username.data).first()
        if member is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self, email):
        member = Member.query.filter_by(email= email.data).first()
        if member is not None:
            raise ValidationError('The email already exists! Please use a different email address')
        
class AdminRegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        member = Member.query.filter_by(username=username.data).first()
        if member is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self, email):
        member = Member.query.filter_by(email= email.data).first()
        if member is not None:
            raise ValidationError('The email already exists! Please use a different email address')
        
class EducatorRegistrationForm(FlaskForm):
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    bio = StringField('Bio', validators=[Length(max=500)], render_kw={"rows": 5, "cols": 30})
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        member = Member.query.filter_by(username=username.data).first()
        if member is not None:
            raise ValidationError('The username already exists! Please use a different username.')
        
    def validate_email(self, email):
        member = Member.query.filter_by(email= email.data).first()
        if member is not None:
            raise ValidationError('The email already exists! Please use a different email address')

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    