.PHONY: docs
docs:
	@tox -e docs

.PHONY: publish
publish:
	rm -rf build dist
	python3 setup.py sdist bdist_wheel
	twine upload dist/*.tar.gz
