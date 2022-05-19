# Fast API

---

This is a Fast API CRUD project.

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

Install all project dependencies using:

```
$ sudo apt-get install python-virtualenv
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
```

### Running

```
 uvicorn main:app --port 5008 --access-log
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in
production.

If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful
debugger if things go wrong.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply
by adding --host=0.0.0.0 to the command line:

```
 uvicorn main:app --port 5008 --access-log
```

```
python manage.py runserver
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

### Swagger UI

Swagger UI url

```
http://127.0.0.1:5000/api/doc
```

### Alembic Migrations

Use the following commands to create a new migration file and update the database with the last migrations version:

```
db revision --autogenerate -m "description here"
db upgrade head
```

This project also uses the customized manager command to perform migrations.

```
python manage.py db revision --autogenerate -m "description here"
python manage.py db upgrade head
```

To upgrade the database with the newest migrations version, use:

```
python manage.py db upgrade head
```

For more information, access [Auto generating migrations](https://alembic.sqlalchemy.org/en/latest/autogenerate.html).

## Materials

This API was developed based on:

[FastApi documentation](https://fastapi.tiangolo.com/)