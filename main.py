import uvicorn
from pathlib import Path
from fastapi import FastAPI

from core import main
from core.main.database import Base, engine
from core.routers.api import router as api_router

config_path = Path(__file__).with_name("logging_config.json")


def create_app() -> FastAPI:

    Base.metadata.create_all(bind=engine)
    application = FastAPI(debug=False)
    log = main.CustomizeLogger.make_logger(config_path)
    application.logger = log
    application.include_router(api_router)

    return application


app = create_app()
if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=5000, log_level="info", reload=False)
