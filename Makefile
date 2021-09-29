BACKEND_PORT ?= 5000  # https://stackoverflow.com/questions/24263291/define-a-makefile-variable-using-a-env-variable-or-a-default-value
RUNNER := $(shell pwd)/runner.sh

.PHONY: run-front
run-front:
	cd front; $(RUNNER) npm run dev

.PHONY: run-backend
run-backend:
	$(RUNNER) uvicorn twdouga.main:app --host=0.0.0.0 --port=$(BACKEND_PORT)
