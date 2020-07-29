THIS_FILE := $(lastword $(MAKEFILE_LIST))

### Tests section
#####

# Run ALL configured tests
.PHONY: tests
tests: build-tests
	@$(MAKE) -f "$(THIS_FILE)" PACKAGE=gammit test-package

.PHONY: build-tests
build-tests:
	docker rmi --force ${USER}/gammit-tests:latest
	docker build -f "${PWD}/Dockerfile.test" -t ${USER}/gammit-tests .

# Base test runner takes $PACKAGE env var
.PHONY: test-package
test-package:
	rm -rf "${PWD}/python-pkg/${PACKAGE}/tests/__pycache__"
	docker run --rm -i -v "${PWD}/python-pkg/${PACKAGE}":/code ${USER}/gammit-tests /bin/sh -c "py.test --cov --cov-report=html:tests/htmlcov -s tests/"
