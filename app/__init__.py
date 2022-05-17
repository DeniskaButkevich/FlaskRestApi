import logging
import os

from flask import Flask

from app import main
from app import model
from app.main.api import api, blueprint as documented_endpoint
from app.main.database import db, migration
from app.main.logging import LOGGING_CONFIG

# Flask App Initialization
app = Flask(__name__)
app.config.from_object(main.settings[os.environ.get('APPLICATION_ENV', 'testing')])

# from app import model
console = logging.getLogger('console')

# Database ORM Initialization
db.init_app(app)

# # Database Migrations Initialization
# migration.init_app(app, db)

# Flask API Initialization
app.register_blueprint(documented_endpoint)

# _____________________________________
# app.app_context().push()
with app.app_context():
    db.create_all()
