build:
	docker-compose build

start:
	docker-compose up

stop:
	docker-compose down

migrate:
	docker-compose exec web python manage.py migrate

makemigrations:
	docker-compose exec web python manage.py makemigrations

install_deps:
	docker-compose run web pip install -r requirements.txt

run_command:
	docker-compose exec web $(cmd)

reset_db:
	docker-compose down
	docker volume rm your_project_name_dbdata
	docker-compose up -d
	make migrate
