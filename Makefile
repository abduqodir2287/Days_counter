run:
	uvicorn src.main:app --reload --port 8000

test:
	python -m pytest

compose:
	docker-compose up --build

git:
	git status

add-all:
	git add *
