# Django task

1. Clone project from GIT repo

```
    git clone git@github.com:andrewast/milo-django-task.git
```

2. Create virtualenv

```
    virtualenv venv --no-site-packages
```

3. Activate environment and install project dependencies
```
    pip install -r requirements.txt
```

4.  Run migrations
```
    ./manage.py migrate
```

5. Add initial data into DB
```
    ./manage.py db
```

6. Run server
```
    ./manage.py runserver
```