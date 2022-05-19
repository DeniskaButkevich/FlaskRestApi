import logging
import os
from pathlib import Path

import uvicorn
from fastapi import FastAPI

from core import CustomizeLogger, main
from core.main.database import Base, engine
from core.routers.api import router as api_router

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")


def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    app.include_router(api_router)

    return app


app = create_app()

Base.metadata.create_all(bind=engine)

setting = main.settings[os.environ.get('APPLICATION_ENV', 'development')]

# Database Migrations Initialization
# migration.init_app(app, db)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
