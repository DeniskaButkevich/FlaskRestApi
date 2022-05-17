import logging
import os

from fastapi import FastAPI

from core import main
# from core import model
# from core.routers.api import api, blueprint as documented_endpoint
from core.main.database import db, migration
from core.main.logging import LOGGING_CONFIG

# Flask App Initialization
app = FastAPI()
setting = main.settings[os.environ.get('APPLICATION_ENV', 'development')]
# from core import model
console = logging.getLogger('console')

# Database ORM Initialization
db.init_app(app)

# Database Migrations Initialization
# migration.init_app(app, db)

# Flask API Initialization

# _____________________________________
# core.app_context().push()
db.create_all()
