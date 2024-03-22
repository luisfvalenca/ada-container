build:
	echo "Building App"
	docker build -t container-image .

run:
	echo "Running App"
	docker run --rm --name container-name container-image main.py ${ARGS}
