web: python aprilandjake/manage.py collectstatic --noinput; bin/gunicorn_django --workers=3 --bind=0.0.0.0:$PORT aprilandjake/settings.py