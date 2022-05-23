# FastAPI CRUD example

---

This is a Fast API CRUD example.

### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [FastApi](https://fastapi.tiangolo.com/) - The framework used
* [SQLAlchemy](https://docs.sqlalchemy.org/) - ORM
* [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation
* [Alembic](https://alembic.sqlalchemy.org/) - Database Migrations
* [Loguru](https://loguru.readthedocs.io/) - Logging
* [PyTest](https://docs.pytest.org/) - Testing
* [Pip](https://pypi.org/project/pip/) - Dependency Management
* [RESTful](https://restfulapi.net/) - REST docs

### Virtual environments

Install venv if u need
```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
```
Install all project dependencies using:
```
$ pip install fastapi
$ pip install -r requirements.txt
```
### Database
This application uses postgres db.   
Set your database settings in a `core.main.config.Dev` class

### Running

```
 uvicorn main:app --port 5008 --access-log
```
### Swagger UI

```
http://127.0.0.1:5008/doc
```

### Testing

```
python -m pytest tests/unit/
python -m pytest tests/functional/
```

To really get a sense of when the `test_client()` fixture is run,
pytest can provide a call structure of the fixtures and tests with the `--setup-show` argument:

```
(venv)$ python -m pytest --setup-show tests/functional/test_recipes.py
====================================== test session starts =====================================

tests/functional/test_recipes.py
  ...
  SETUP    M test_client
      functional/test_recipes.py::test_home_page_with_fixture (fixtures used: test_client).
      functional/test_recipes.py::test_home_page_post_with_fixture (fixtures used: test_client).
  TEARDOWN M test_client
======================================= 4 passed in 0.18s ======================================
```

### Alembic Migrations

Use the following commands to create a new migration file and update the database with the last migrations version:

```
db revision --autogenerate -m "description here"
db upgrade head
```

For more information, access [Auto generating migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html).

## Materials

This API was developed based on:

[FastApi documentation](https://fastapi.tiangolo.com/)