# app/Controller/auth_forms.py

from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from config import Config
from app.Controller.auth_forms import StudentRegistrationForm, AdminRegistrationForm, EducatorRegistrationForm
from app.Model.models import Member, Student, Admin, Educator
from app import db
from flask_login import current_user, login_user, logout_user, login_required
from app.Controller.auth_forms import LoginForm

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 


@bp_auth.route('/student_register', methods=['GET', 'POST'])
def student_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform = StudentRegistrationForm()
    if rform.validate_on_submit():
        student = Student(username=rform.username.data, email=rform.email.data)
        student.set_password(rform.password.data)
        db.session.add(student)
        db.session.commit()
        flash('Congratulations, you are now a registered student!')
        return redirect(url_for('auth.login'))
    return render_template('student_register.html', form=rform)

@bp_auth.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform = AdminRegistrationForm()
    if rform.validate_on_submit():
        admin = Admin(username=rform.username.data, email=rform.email.data)
        admin.set_password(rform.password.data)
        db.session.add(admin)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('auth.login'))
    return render_template('admin_register.html', form=rform)

@bp_auth.route('/educator_register', methods=['GET', 'POST'])
def educator_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    rform = EducatorRegistrationForm()
    if rform.validate_on_submit():
        educator = Educator(username=rform.username.data, email=rform.email.data)
        educator.set_password(rform.password.data)
        db.session.add(educator)
        db.session.commit()
        flash('Congratulations, you are now a registered educator!')
        return redirect(url_for('auth.login'))
    return render_template('educator_register.html', form=rform)

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('routes.index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        member = Member.query.filter_by(username= lform.username.data).first()
        if (member is None) or (member.get_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(member, remember= lform.remember_me.data)
        return redirect(url_for('routes.index'))
    return render_template('login.html', title='Sign In', form = lform)


@bp_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))