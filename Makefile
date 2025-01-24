.PHONY: test start logs

test:
	pytest -v

start:
	docker compose up --build -d

logs:
	docker compose logs