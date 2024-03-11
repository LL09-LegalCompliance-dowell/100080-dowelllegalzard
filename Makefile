.PHONY: migrate run-server superuser coverage pytest

migrate:
	python3 manage.py makemigrations; python3 manage.py migrate

run-server:
	python3 manage.py runserver

superuser:
	python3 manage.py createsuperuser

coverage:
	cd project && coverage run -m pytest; coverage html
pytest:
	cd project && pytest -s ; pytest -s --cov