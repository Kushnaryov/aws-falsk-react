# Flask-React-Boilerplate

Template for building a Flask-React-Postgres app served with nginx with using docker-compose

## Running application

To run the application on your machine:

Clone repo:

`git clone https://github.com/Kushnaryov/falsk-react-boilerplate.git`

Run development mode:

`docker-compose up -d build && docker-compose up`

Run production mode:

`docker-compose up -d build -f docker-compose.prod.yml && docker-compose up -f docker-compose.prod.yml`

## Application usage description
to create db run `docker-compose exec backend python3 manage.py create_db`

to test app open `localhost:1337/send`

to add instance to db open `localhost:1337/create`

to show instances in db open `localhost:1337/show`
