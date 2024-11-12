# app/decorators.py

from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if current_user.is_authenticated:
                if current_user.user_type == role:
                    return f(*args, **kwargs)
                else:
                    abort(403)  # Forbidden access if user role does not match
            else:
                abort(401)  # Unauthorized access if not logged in
        return decorated_function
    return wrapper
