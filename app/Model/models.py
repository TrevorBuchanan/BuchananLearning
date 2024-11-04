# app/Model/models.py

from datetime import datetime
from app import db, login

from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return Member.query.get(int(id))

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    lessons = db.Column(db.String(), nullable=True)

class Member(UserMixin, db.Model):
    __tablename__ = 'member'
    id = db.Column(db.Integer, primary_key= True)
    username = db.Column(db.String(64), unique= True, index= True)
    email = db.Column(db.String(120), unique= True)
    password_hash = db.Column(db.String(128))
    user_type = db.Column(db.String(50))
    
    __mapper_args__ = {
        'polymorphic_identity': 'Member',
        'polymorphic_on':user_type
    }
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def get_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def get_user_posts(self):
        return self.reviews
        
    def __repr__(self):
        return '<Member {},{},{},{} >'.format(self.id, self.username, self.email, self.password_hash)
    
class Student(Member):
    __tablename__ = 'student'
    id = db.Column(db.ForeignKey("member.id"), primary_key= True)
    __mapper_args__ = {
        'polymorphic_identity':'Student'
    }

class Admin(Member):
    __tablename__ = 'admin'
    id = db.Column(db.ForeignKey("member.id"), primary_key= True)
    __mapper_args__ = {
        'polymorphic_identity':'Admin'
    }

class Educator(Member):
    __tablename__ = 'educator'
    id = db.Column(db.ForeignKey("member.id"), primary_key= True)
    __mapper_args__ = {
        'polymorphic_identity':'Educator'
    }

