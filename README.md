## pixshare

<div align="center">

  [![Status](https://img.shields.io/badge/status-active-success.svg)]()
  [![GitHub Issues](https://img.shields.io/github/issues/kevinbowen777/pixshare.svg)](https://github.com/kevinbowen777/pixshare/issues)
  [![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)
  [![Coverage](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/kevinbowen777/261b3eac2838cf0bc3b365335c8323df/raw/covbadge.json)](https://kevinbowen777.github.io/pixshare/)

</div>

- pixshare - A Django web application for users to bookmark and share images


##### Table of Contents
 - [Features](#features)
 - [Installation](#installation)
 - [Testing](#testing)
 - [Application Demo](#application-demo)
 - [Screenshots](#screenshots)
 - [Reporting Bugs](#reporting-bugs)

---

### Features
 - Application
     - TBD
 - Dev/testing
     - Basic module testing templates
     - [Coverage](https://kevinbowen777.github.io/) reports on web
     - [Debug-toolbar](https://pypi.org/project/django-debug-toolbar/) available. See notes in `config/settings.py` for enabling.
     - [shell_plus](https://django-extensions.readthedocs.io/en/latest/shell_plus.html) with [IPython](https://pypi.org/project/ipython/) via [django-extensions](https://pypi.python.org/pypi/django-extensions/) package
     - [Pre-commit](https://github.com/pre-commit/pre-commit)
     - [Nox](https://pypi.org/project/nox/) testing sessions for latest Python 3.10, 3.11, 3.12, 3.13 
         - [coverage](https://pypi.org/project/coverage/) (`nox -s coverage`)
         - [Sphinx](https://pypi.org/project/Sphinx/) documentaion generation (`nox -s lint`)
         - linting (`nox -s lint`)
             - [ruff](https://pypi.org/project/ruff/)
             - [djlint](https://pypi.org/project/djlint/)
         - [safety](https://pypi.org/project/safety/)(python package vulnerability testing) (`nox -s safety`)
         - [pytest](https://docs.pytest.org/en/latest/) sessions with
           [pytest-cov](https://pypi.org/project/pytest-cov/)
           [pytest-django](https://pypi.org/project/pytest-django/) (`coverage run -m pytest`)
  - `run` command menu

    (adapted from Nick Janetakis' helpful [docker-django-example](https://github.com/nickjj/docker-django-example))

    You can run `./run` to get a list of commands and each command has documentation in the run file itself. This comes in handy to run various Docker commands because sometimes these commands can be a bit long to type.

    *If you get tired of typing `./run` you can always create a shell alias with `alias run=./run` in your `~/.bash_aliases` or equivalent file. Then you'll be able to run `run` instead of `./run`.*

---

### Installation
 - `git clone https://github.com/kevinbowen777/pixshare.git`
 - `cd django_start`
 - Local installation:
     - `poetry shell`
     - `poetry install`
     - `python manage.py migrate`
     - `python manage.py createsuperuser`
     - `python manage.py runserver`
 - Docker installation:
     - `docker compose up --build`
     - `docker compose build --build-arg "ENV=DEV"` (include testing/dev dependencies)
     - `docker compose build --build-arg "ENV=PROD"`
     - `docker compose exec web python manage.py migrate`
     - `docker compose exec web python manage.py createsuperuser`
     Additional commands:
       - `docker compose exec web python manage.py shell_plus`
         (loads Django shell autoloading project models & classes)
       - `docker run -it django-start-web bash`
         (CLI access to container)
 - Browse to http://127.0.0.1:8000 or http://127.0.0.1:8000/resources/
 - Pre-commit:
     - To add the hook, run the following command in the poetry shell:
         - `pre-commit install`

---

### Testing
 - `docker compose exec web python manage.py test`
 - `coverage run -m pytest`
 - Nox (includes sessions for black, lint, safety, tests)
     - testing supported for Python 3.10, 3.11, 3.12, 3.13
     - e.g. `nox`, `nox -rs lint-3.13`, `nox -s tests`
       - `nox`
       - `nox -s black-3.12`
       - `nox -s docs-3.13`
       - `nox -rs lint-3.10` (Use the 'r' flag to reuse existing session)
       - `nox -s pyright-3.11`
       - `nox -s safety` (will run tests against all Python versions)
       - `nox -s tests`

---

### Application Demo

 - TBD

---

### Screenshots

TBD

---

### Reporting Bugs

   Visit the [Issues page](https://github.com/kevinbowen777/pixshare/issues)
      to view currently open bug reports or open a new issue.
