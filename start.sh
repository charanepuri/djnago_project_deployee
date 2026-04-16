python manage.py migrate -

python manage.py collectstatic --noinput 

gunicorn jango_project_deployee.wsgi:application