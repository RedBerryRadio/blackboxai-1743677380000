from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db():
    """Create database tables if they do not exist."""
    db.create_all()

def hash_password(password):
    """Generate a hashed password."""
    return generate_password_hash(password)

def verify_password(stored_password, provided_password):
    """Verify a provided password against the stored hashed password."""
    return check_password_hash(stored_password, provided_password)