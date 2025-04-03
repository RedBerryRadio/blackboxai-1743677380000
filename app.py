from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from config import DevelopmentConfig, StagingConfig, ProductionConfig

app = Flask(__name__)

# Load configuration based on the environment
env = os.getenv('ENV', 'development')
if env == 'production':
    app.config.from_object(ProductionConfig)
elif env == 'staging':
    app.config.from_object(StagingConfig)
else:
    app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
login_manager = LoginManager(app)

# Define routes here (to be implemented later)

if __name__ == '__main__':
    app.run()