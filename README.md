# Beckstrand Recipe App

This is a recipe app built entirely in Django. 

# Getting Started

To launch this application, first clone this repository. From the root directory, install the necessary packages using pipenv:

```
pipenv install
```

Next, use switch to the newly created venv:

```
pipenv shell
```

Before the project can be started, it is necessary to add the Django secret key. To do so, create a `.env` file in the recipes project directory. 

```
cd recipes
touch .env
```

If you are creating this as a new project and need a new secret key, you can generate one using the following command: 

```
python3 -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

After acquring your applications secret key, add the following entry to your .env file:

```
SECRET_KEY = "<Add your secret key here>"
```

Next, run initial migrations and populate the database:

```python manage.py migrate```

Create a super user to perform administrative operations:

```
python manage.py createsuperuser
```

Finally, we are now ready to run the web server:

```
python manage.py runserver
```