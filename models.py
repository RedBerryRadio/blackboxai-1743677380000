from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

class ScheduledStream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stream_url = db.Column(db.String(255), nullable=False)
    schedule_time = db.Column(db.DateTime, nullable=False)
    action = db.Column(db.String(50), nullable=False)  # "playback" or "download"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(50), default='pending')

    def __repr__(self):
        return f'<ScheduledStream {self.stream_url}>'