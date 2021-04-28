build:
	docker build -t alg .

module = ''
test: build
	docker run --rm -it alg pytest -v $(module)