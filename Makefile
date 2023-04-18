build:
	docker-compose  build

up:
	docker-compose  up

down:
	docker-compose  down

stop:
	docker-compose  stop

apply-migrations:
	docker-compose  run --rm base_service alembic upgrade head

migrate:
	docker-compose  run --rm base_service alembic revision --autogenerate -m "create table"

black:
	docker-compose  run --rm base_service black --config=pyproject.toml --skip-string-normalization .

arm-build:
	docker-compose -f docker-compose-arm.yml build

arm-up:
	docker-compose -f docker-compose-arm.yml up

arm-down:
	docker-compose -f docker-compose-arm.yml down

arm-stop:
	docker-compose -f docker-compose-arm.yml stop

arm-apply-migrations:
	docker-compose -f docker-compose-arm.yml run --rm base_service alembic upgrade head

arm-migrate:
	docker-compose -f docker-compose-arm.yml run --rm base_service alembic revision --autogenerate -m "create table"

arm-black:
	docker-compose -f docker-compose-arm.yml run --rm base_service black --config=pyproject.toml --skip-string-normalization .
