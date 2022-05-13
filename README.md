# Flask API

---

This is a Flask API CRUD project.

### Dependencies

* [Python](https://www.python.org/) - Programming Language
* [Flask](https://flask.palletsprojects.com/) - The framework used
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
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ python -m flask run
```

This launches a very simple builtin server, which is good enough for testing but probably not what you want to use in
production.

If you enable debug support the server will reload itself on code changes, and it will also provide you with a helpful
debugger if things go wrong.

If you have the debugger disabled or trust the users on your network, you can make the server publicly available simply
by adding --host=0.0.0.0 to the command line:

```
flask run --host=0.0.0.0
```

### Running using Manager

This app can be started using Flask Manager. It provides some useful commands and configurations, also, it can be
customized with more functionalities.

```
python manage.py runserver
```

### Alembic Migrations

Use the following commands to create a new migration file and update the database with the last migrations version:

```
flask db revision --autogenerate -m "description here"
flask db upgrade head
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

[Flask documentation](https://flask.palletsprojects.com/)

[REST APIs with Flask and Python](https://www.udemy.com/rest-api-flask-and-python/) 
