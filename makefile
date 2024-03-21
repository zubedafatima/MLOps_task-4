.PHONY: all build run

all: build run
build:
    @docker build -t modelimage .
run:
    @docker run -d -p 5000:5000 --name modelcontainer modelimage
