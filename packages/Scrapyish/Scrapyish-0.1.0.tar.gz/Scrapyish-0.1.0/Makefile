
build: test clean # build wheel and sdist
	python -m build --sdist --wheel


release: build # upload to twine
	twine upload dist/*

clean: # clean directory
	rm -rfv build
	rm -rfv dist
	rm -rfv *.egg-info
	rm -rfv .tox/
	rm -fvr -- *'/__pycache__'
	rm -rfv .eggs/
	rm -rfv .pytest_cache
	rm -rfv htmlcov/
	rm -rfv .coverage

push: test clean # push to repo
	git add .
	git commit -m "$m pushing"
	git push

test: clean # run unit tests
	tox
