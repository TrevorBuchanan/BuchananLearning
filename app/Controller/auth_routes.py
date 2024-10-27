from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for
from config import Config
from app.Controller.auth_forms import NormalRegistrationForm, adminRegistrationForm
from app.Model.models import Member, Normal, admin
from app import db
from flask_login import current_user, login_user, logout_user, login_required
from app.Controller.auth_forms import LoginForm

bp_auth = Blueprint('auth', __name__)
bp_auth.template_folder = Config.TEMPLATE_FOLDER 

@bp_auth.route('/admin_register', methods=['GET', 'POST'])
def admin_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.admin_index'))
    rform = adminRegistrationForm()
    if rform.validate_on_submit():
        admin = admin(username=rform.username.data, email=rform.email.data, user_type= "admin")
        admin.set_password(rform.password.data)
        db.session.add(admin)
        db.session.commit()
        flash('Congratulations, you are now a registered admin!')
        return redirect(url_for('auth.login'))
    return render_template('admin_register.html', form=rform)

@bp_auth.route('/normal_register', methods=['GET', 'POST'])
def normal_register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.normal_index'))
    rform = NormalRegistrationForm()
    if rform.validate_on_submit():
        normal = Normal(username=rform.username.data, email=rform.email.data)
        normal.set_password(rform.password.data)
        db.session.add(normal)
        db.session.commit()
        flash('Congratulations, you are now a registered member!')
        return redirect(url_for('auth.login'))
    return render_template('normal_register.html', form=rform)


@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.user_type == "Normal":
            return redirect(url_for('routes.normal_index'))
        else:
            return redirect(url_for('routes.admin_index'))
    lform = LoginForm()
    if lform.validate_on_submit():
        member = Member.query.filter_by(username= lform.username.data).first()
        if (member is None) or (member.get_password(lform.password.data) == False):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(member, remember= lform.remember_me.data)
        if current_user.user_type == "Normal":
            return redirect(url_for('routes.normal_index'))
        else:
            return redirect(url_for('routes.admin_index'))
    return render_template('login.html', title='Sign In', form = lform)


@bp_auth.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('auth.login'))