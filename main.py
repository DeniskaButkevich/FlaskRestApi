import logging
import os
import uvicorn
from dotenv import load_dotenv
from pathlib import Path
from fastapi import FastAPI
from core import CustomizeLogger
from core.main import config
from core.main.database import Base, engine
from core.routers.api import router as api_router
os.environ["ENV_STATE"] = "test"

load_dotenv()

logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")

Base.metadata.create_all(bind=engine)


def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger(config_path)
    app.logger = logger
    app.include_router(api_router)

    return app


app = create_app()

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8005, log_level="info", reload=True)
