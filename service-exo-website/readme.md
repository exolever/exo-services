# service-exo-website

This service handles microsites for events promotion 

service-exo-website is powered by [django](https://github.com/django/django).

 
## Set-up
Install all the dependencies:
```
$ pipenv install
$ pip install -r local_requirements.txt
```

Create the database structure:
```
$ python manage.py migrate
```

Check everything is ok
```
$ python manage.py check
```

## Testing
```
$ python manage.py test
```

## External dependencies
- Celery
- Redis
- Postgres

_See a full dependency list on_ `Pipfile`.
