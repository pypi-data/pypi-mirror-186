# pagex-stocks-data
The data access layer module

# local python upgrade

1. brew install python@3.10
2. add python_version = "3.10.0" to pipfile
3. pipenv --rm
4. pipenv --python /usr/local/opt/python@3.10/bin/python3.10
5. pipenv update --python 3.10
6. pipenv install

add interpreter setting to pycharm

# build wheel
maintain setup.py
python -m pip install -U wheel setuptools
python setup.py bdist_wheel --universal

# pip - https://pip.pypa.io/en/latest/cli/
pip install --upgrade pagex-stocks-data # upgrade module version
pip check
python -m pip freeze # list dependencies from pip
python -m pip freeze > requirements.txt # list dependencies from pip and export it to requirements.txt
