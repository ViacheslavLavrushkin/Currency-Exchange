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
	cd app; celery -A settings worker -l info

beat:
	cd app; celery -A settings beat -l info

