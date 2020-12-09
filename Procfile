web: gunicorn main.wsgi

web: python manage.py collectstatic --no-input; gunicorn main.wsgi --log-file - --log-level debug
