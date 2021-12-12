@echo off
echo 1-test.pypi
echo 2-pypi
set /p data="-}"
python setup.py bdist_wheel --universal
if %data%==1 (
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
) else (
	twine upload dist/*
)
pause