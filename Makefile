ARGS=cart
SHELL=/bin/sh
SAFE_LINT=true
ROOT=/app
MAXLINELENGTH=120
DEV=true

ifeq ($(DEV), true)
	CART=docker-compose -f docker-compose.yml -f docker-compose.dev.yml
else
	CART=docker-compose -f docker-compose.yml
endif

stop:
	docker stop $$(docker ps -q) || true

stop-containers:
	$(CART) stop $$ARGS

remove-containers: stop-containers
	$(CART) rm -f $$ARGS

build:
	$(CART) build

up:
	$(CART) up -d $$ARGS

restart:
	$(CART) restart $(ARGS)

watch:
	$(CART) logs -f --tail=100 $(ARGS)

shell:
	$(CART) exec $(ARGS) $(SHELL)

fix:
	$(CART) exec cart pipenv run autopep8 --in-place -a --max-line-length $(MAXLINELENGTH) -r $(ROOT)

lint:
	$(CART) exec cart touch __init__.py
	$(CART) exec cart pipenv run pylint -j 4 $(ROOT) --rcfile=.pylintrc --output-format=colorized || \
		$(CART) exec cart pipenv run pylint-exit --error-fail $$? || $(SAFE_LINT)
	$(CART) exec cart rm -f ./__init__.py

coverage:
	$(CART) exec cart pipenv run pytest --cov-report html:cov_html --cov=./

test-unit:
	$(CART) exec cart pipenv run pytest tests/unit

test-integration:
	$(CART) exec cart pipenv run pytest tests/integration

test: test-unit test-integration