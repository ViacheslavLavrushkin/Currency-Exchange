SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

show_urls:
	$(manage_py) show_urls

shell:
	$(manage_py) shell_plus --print-sql

createsuperuser:
	$(manage_py) createsuperuser

worker:
	cd app && celery -A settings worker -l info

beat:
	cd app; celery -A settings beat -l info

pytest:
	pytest app/tests --cov=app --cov-report html && coverage report --fail-under=59

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

gunicorn:
	cd app && gunicorn -w 4 settings.wsgi:application -b 0.0.0.0:8000 --log-level=DEBUG

gunicorn1:
	cd app && gunicorn -w 4 settings.wsgi:application -b 0.0.0.0:8001 --log-level=DEBUG

