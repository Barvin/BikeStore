web: gunicorn varnhems_cyklar.wsgi --log-file -
web: python varnhems_cyklar/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT varnhems_cyklar/settings.py
