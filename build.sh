python setup.py sdist bdist_wheel
python -m twine upload dist/*

rm -rf build
rm -rf dist
rm -rf tracardi_regex_match.egg-info
