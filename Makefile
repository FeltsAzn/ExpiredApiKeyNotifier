# Makefile commands to fast run
.PHONY: start run rerun build stop down local-run local-down logs

help | h:
	@printf "[HELP]\n"
	@printf "Commands:\n"
	@printf "start: start assembled containers and show logs.\n"
	@printf "run: build containers and run.\n"
	@printf "rerun: stop, rebuild containers to set changes and run again.\n"
	@printf "build: assemble project to run.\n"
	@printf "clear cache: clear redis cache.\n"
	@printf "down: stop and remove docker containers.\n"
	@printf "stop: stop docker containers.\n"
	@printf "logs (t=(handler | fabric)): show docker compose logs or if set a target shows logs from target container.\n"

start:
	@docker compose up -d
	@docker compose logs -f

run:
	@docker compose build
	@docker compose up -d

rerun:
	@docker compose down
	@docker compose build
	@docker compose up -d

build:
	@docker compose build

down:
	@docker compose down

stop:
	@docker compose stop

logs:
	@docker compose logs -f

local-run:
	@if [ -z $$(docker volume ls -q -f name=mock-mongodb-data) ]; then \
        docker volume create --name=mock-mongodb-data; \
        echo "Docker volume 'mock-mongodb-data' created."; \
    else \
        echo "Docker volume 'mock-mongodb-data' already exists. Skipping creation."; \
    fi

	@docker compose -f local/docker-compose.local.yaml --env-file local/.env up -d

local-down:
	@docker compose -f local/docker-compose.local.yaml --env-file local/.env down

local-logs:
	@docker compose -f local/docker-compose.local.yaml --env-file local/.env logs -f

ls:
	@docker ps

exec:
	@docker exec -it expired_key_notifier_worker bash