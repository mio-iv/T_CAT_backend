# Django

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8080

.PHONY: runserver
runserver:
	python manage.py runserver 0.0.0.0:8080

.PHONY: createsuperuser
createsuperuser:
	python manage.py createsuperuser

.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: showmigrations
showmigrations:
	python manage.py showmigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: admin
migrate:
	open http://localhost:8080/admin/
