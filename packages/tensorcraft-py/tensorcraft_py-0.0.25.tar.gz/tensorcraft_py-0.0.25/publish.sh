rm -rf dist/
python -m build
twine upload -r pypi dist/*

