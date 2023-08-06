# Pyramid-Helpers

Pyramid-Helpers is a set of helpers to develop applications using Pyramid framework.

It includes authentication, forms, i18n and pagination helpers.


## Prerequisites
The project is managed using [Poetry](https://poetry.eustace.io/docs/#installation)

### PostgreSQL adapter (Optional)
In order to use a PostgreSQL database, it is recommended to install the [psycopg](https://www.psycopg.org/) adapter. You should check the [build prerequisites](https://www.psycopg.org/docs/install.html#build-prerequisites) in order to install this package (source only).

### LDAP client (Optional)
LDAP client relies on the [python-ldap](https://www.python-ldap.org/en/latest/) client. You should check the [build prerequisites](https://www.python-ldap.org/en/latest/installing.html#build-prerequisites) in order to install this package.


## Development
```
# Create virtualenv
mkdir .venv
python3 -m venv .venv

# Activate virtualenv
source .venv/bin/activate

# Update virtualenv
pip install -U pip setuptools

# Install Poetry
pip install wheel
pip install poetry

# Install application in development mode
poetry install --extras "[api-doc] [auth-ldap] [auth-radius]"
poetry run invoke i18n.generate

# Copy and adapt conf/ directory
cp -a conf .conf

# Initialize database
phelpers-init-db .conf/application.ini

# Run web server in development mode
poetry run invoke service.httpd --config-uri=.conf/application.ini --env=.conf/environment

# Run static and functional tests:
poetry run invoke test
```

## Tests
### Static code validation
```
# ESLint
poetry run invoke test.eslint

# flake8
poetry run invoke test.flake8

# pylint
poetry run invoke test.pylint

# All
poetry run invoke test.static
```

### Functional tests
```
# Validators
poetry run invoke test.functional --test='tests/test_01_validators.py'

# Forms
poetry run invoke test.functional --test='tests/test_02_forms.py'

# Authentication client
poetry run invoke test.functional --test='tests/test_10_auth_client.py'

# LDAP client
poetry run invoke test.functional --test='tests/test_11_ldap_client.py'

# RADIUS client
poetry run invoke test.functional --test='tests/test_12_radius_client.py'

# Common views
poetry run invoke test.functional --test='tests/test_50_common_views.py'

# API views
poetry run invoke test.functional --test='tests/test_51_api_views.py'

# Articles views
poetry run invoke test.functional --test='tests/test_52_articles_views.py'

# All
poetry run invoke test.functional
```


## I18n
Extract messages
```
poetry run invoke i18n.extract i18n.update
```

Compile catalogs and update JSON files
```
poetry run invoke i18n.generate
```

Create new language
```
poetry run invoke i18n.init {locale_name}
```


## Installation

```
pip install pyramid-helpers

# And optionally:
phelpers-init-db conf/application.ini
```


## Files list

```
.
├── .coveragerc                         Coverage configuration file
├── .eslintrc.json                      ESLint configuration file
├── babel.cfg                           Babel configuration file (i18n)
├── CHANGES.md
├── pylintrc                            Pylint configuration file
├── pyproject.toml                      Poetry configuration file
├── README.md                           This file
├── setup.cfg
├── conf
│   ├── application.ini                 main configuration file
│   ├── auth.ini                        authentication configuration
│   ├── ldap.ini                        LDAP configuration file (auth)
│   └── radius.ini                      RADIUS configuration file (auth)
├── pyramid_helpers
│   ├── __init__.py                     initialization
│   ├── api_doc.py                      API documentation helper
│   ├── auth.py                         authentication helper
│   ├── ldap.py                         LDAP client
│   ├── models.py                       SQLAlchemy model for demo app
│   ├── paginate.py                     pagination class, decorator and setup
│   ├── predicates.py                   custom route predicates (Enum, Numeric)
│   ├── radius.py                       RADIUS client
│   ├── resources.py                    basic resource file for demo app
│   ├── forms
│   │   ├── __init__.py                 form class, decorator and setup, largely inspired from formhelpers[1]
│   │   ├── articles.py                 formencode schemas for articles for demo app
│   │   ├── auth.py                     formencode schema for authentication for demo app
│   │   └── validators.py               various formencode validators
│   ├── funcs
│   │   └── articles.py                 functions for articles management
│   ├── i18n.py                         i18n setup and helpers
│   ├── locale
│   │   ├── fr
│   │   │   └── LC_MESSAGES
│   │   │       └── pyramid-helpers.po
│   │   └── pyramid-helpers.pot
│   ├── scripts
│   │   └── initializedb.py             script for database initialization
│   ├── static
│   │   ├── css
│   │   │   ├── api-doc-bs3.css         javascript code for API documentation (Bootstrap 3)
│   │   │   ├── api-doc-bs4.css         javascript code for API documentation (Bootstrap 4)
│   │   │   ├── api-doc-bs5.css         javascript code for API documentation (Bootstrap 5)
│   │   │   └── pyramid-helpers.css     stylesheet for demo app
│   │   └── js
│   │       ├── api-doc.js              javascript code for API documentation
│   │       └── pyramid-helpers.js      javascript code for demo app
│   ├── templates                       Mako templates
│   │   ├── articles                    Mako templates for demo app
│   │   │   ├── edit.mako
│   │   │   ├── index.mako
│   │   │   └── view.mako
│   │   ├── confirm.mako
│   │   ├── errors.mako
│   │   ├── form-tags.mako              Mako template for forms rendering - derivates from formhelpers[1]
│   │   ├── login.mako
│   │   ├── paginate.mako               Mako template for pagination rendering
│   │   ├── site.mako                   Main template for demo app
│   │   └── validators.mako             Mako template to test validators
│   └── views                           views for demo app
│       ├── api
│       │   └── articles.py
│       └── articles.py
├── tasks                               Invoke tasks
│   ├── __init__.py                     initialization
│   ├── common.py                       common file
│   ├── i18n.py                         i18n tasks
│   ├── service.py                      service tasks
│   └── test.py                         test tasks
└── tests                               functional tests (pytest)
    ├── conftest.py                     configuration file for pytest
    ├── test_01_validators.py           test functions for forms validators
    ├── test_02_forms.py                test functions for forms
    ├── test_03_utils.py                test functions for utilities
    ├── test_10_auth_client.py          test functions for authentication
    ├── test_11_ldap_client.py          test functions for LDAP client
    ├── test_12_radius_client.py        test functions for radius client
    ├── test_50_common_views.py         test functions for common views
    ├── test_51_api_views.py            test functions for articles API
    └── test_52_articles_views.py       test functions for articles views
```


## Useful documentation

* https://docs.pylonsproject.org/projects/pyramid/en/latest/
* https://docs.pylonsproject.org/projects/pyramid/en/latest/#api-documentation
* https://techspot.zzzeek.org/2008/07/01/better-form-generation-with-mako-and-pylons/
