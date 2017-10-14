freeze:
	pip freeze > requirements.txt

test:
	FLASK_CONFIG=testing python manage.py tests
