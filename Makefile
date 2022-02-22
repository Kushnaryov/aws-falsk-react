run-back:
	FLASK_APP=app.py	\
	FLASK_ENV=development	\
	cd backend
	flask db init
	flask run


run-back2:
	set -e	\
	flask db upgrade	\
	gunicorn -c gunicorn.config.py wsgi:app	

run-front:
	cd frontend && npm start

run:
	make run-front & make run-back

freeze:
	pip freeze > backend/requirements.txt

kill:
	fuser -k 5000/tcp & fuser -k 3000/tcp

audit:
	fuser 5000/tcp & fuser 3000/tcp

build:
	docker-compose up -d --build