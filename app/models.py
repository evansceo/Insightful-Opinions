from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.orm import backref


    def __repr__(self):
        return f'Comments: {self.comment}'
