![version](https://img.shields.io/badge/version-1.1.31-blue.svg)

```shell
pip install wheel twine\
python setup.py sdist bdist_wheel\
twine check *\
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*\
pip install uniphi
```

### To generate thrift files
```shell
thrift --gen py server.thrift
```

