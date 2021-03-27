.PHONY: test

deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

test:
	PYTHONPATH=. py.test --verbose -s

lint:
	flake8 hello_world test

run:
	PYTHONPATH=. FLASK_APP=hello_world flask run

test_smoke:
	curl -s -o /dev/null -w "%{http_code}" --fail 127.0.0.1:5000

test_cov:
	PYTHONPATH=. py.test --verbose -s --cov=.

test_xunit:
	PYTHONPATH=. py.test --verbose -s --cov=. --cov-report xml
	PYTHONPATH=. py.test -s --cov=. --cov-report xml --junit-xml=test_results.xml

docker_build:
	docker build -t hello-world-printer .

docker_run: docker_build
	docker run \
		--name hello-world-printer-dev \
		-p 5000:5000 \
		-d hello-world-printer

USERNAME=aniatest1
TAG=$(USERNAME)/hello-world-printer
TAG_VERSION=0.1.0

docker_push: docker_build
	#if [ -z "${TRAVIS_TAG}" ]; then
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag hello-world-printer $(TAG):$(TAG_VERSION); \
	docker push $(TAG):$(TAG_VERSION); \
	docker logout;
	#fi;
