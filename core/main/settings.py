# -*- coding: utf-8 -*-
import os


class Config:
    # project root directory
    BASE_DIR = os.path.join(os.pardir, os.path.dirname(__file__))
    SECRET_KEY = os.environ.get("SECRET_KEY")
    FAB_API_SWAGGER_UI = True

    # FastAPI Configuration
    # --------------------------------------------------------------------
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True

    # sqlalchemy database main
    # --------------------------------------------------------------------
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@localhost/fast_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'executemany_mode': 'batch',
        'client_encoding': 'utf8',
        'case_sensitive': False,
        'echo': True,
        'echo_pool': True
    }


class DevelopmentConfig(Config):
    # ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = True
    ASSETS_DEBUG = True


class TestingConfig(Config):
    # ENV = os.environ.get("FLASK_ENV", "testing")
    DEBUG = True
    TESTING = True
    DATABASE_URL = "postgresql://admin:admin@db:5432/fast_db"
    SQLALCHEMY_DATABASE_URI = "postgresql://admin:admin@db:5432/fast_db"


class ProductionConfig(Config):
    # ENV = os.environ.get("FLASK_ENV", "production")
    DEBUG = False
    USE_RELOADER = False


settings = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
