USER_INPUT=list the files
build:
	docker-compose build
command:
	USER_INPUT="${USER_INPUT}" docker-compose up
