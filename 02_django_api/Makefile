.PHONY: run pre-commit all files
pre-commit:
	pre-commit run --all-files

.PHONY: interactive build services
build:
	docker compose up --build

.PHONY: interactive run services
run:
	docker compose up

.PHONY: daemon build services
buildd:
	docker compose up -d --build

.PHONY: daemon run services
rund:
	docker compose up -d

.PHONY: backend cli
cli:
	docker exec -it backend bash

.PHONY: clean-pyc
clean-pyc:
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

.PHONY: clean all docker images
clean-all:
	T=$$(docker ps -q); docker stop $$T; docker rm $$T; docker container prune -f

.PHONY: clean docker images
clean:
	T="backend db swagger"; docker stop $$T; docker rm $$T; docker container prune -f