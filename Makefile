all: fmt test

fmt:
	poetry run black lg.py

test:
	poetry run mypy lg.py

# Build the docker image
build:
	docker build -t nickpegg/looking-glass .

# Run the development server
run: build
	docker run -p 8000:8000 -it nickpegg/looking-glass flask run -h 0.0.0.0 -p 8000

push:
	docker push nickpegg/looking-glass:latest
