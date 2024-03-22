QUIET_RUN= > /dev/null 2>&1

PYTHON = python3
TWINE = twine

VERSION = $(shell $(PYTHON) setup.py --version)

all: clean check-branch test build check upload

check-branch:
	@ #TODO:

test:
	@ echo TESTING...
	@ $(PYTHON) tests/test.py
	@ echo
#FIXME: is that build?
build:
	@ echo BUILDING...
	@ $(PYTHON) setup.py sdist bdist_wheel
	@ echo

check:
	@ echo CHECKING...
	@ twine check dist/*
	@ echo

upload:
	@ # Confirm
	@ # FIXME: better confirmation
	@ read -p 'Upload version $(VERSION)? [y/N] ' confirm && [ $${confirm:-N} = 'y' ]
	@ echo

	# Upload
	@ echo UPLOADING...
	@ $(TWINE) upload dist/*

clean:
	@ echo CLEANING...
	@ rm -rf dist
	@ rm -rf build
	@ echo
