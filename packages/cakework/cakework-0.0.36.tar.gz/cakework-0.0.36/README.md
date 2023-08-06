# sdk-python

# TODO add instructions for testing package locally
To install locally: note: this isn't currently working
Q: is setup.py being used by anyone?
`pip install .` (in root of package, where pyproject.toml is located)

Running the example to create a new activity
```
cd test
python cakework.py
```

Python SDK for Cakework

Make sure to bump up the version number in setup.py

Building and publishing to Test PyPi repo: 
Activate virtual env
```
pip3 install -r requirements.txt # Q: is there a way to get around having to install build, twine, etc? 
python3 -m build
python3 -m twine upload --repository testpypi dist/*
````

Installing package:
`python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps cakework`

Note: need to first create a test PyPi account and create an API key and put it in the `$HOME/.pypirc` file as per https://packaging.python.org/en/latest/tutorials/packaging-projects/

Can then view the package on Test PyPi i.e. https://test.pypi.org/project/cakework


Building and publishing to PyPi repo:
# TODO: need to figure out whether we are packaging dependencies correctly. Add instructions to do a pip install -r requirements.txt

```
python3 -m build
python3 -m twine upload --skip-existing dist/*
```

For Docker to have access to the latest repo, run
`pip3 install cakework --upgrade` 

And we can install normally using
`pip3 install cakework`


----------------------
TODOS
Q: if we do pip install update will that be faster? 

Generating the grpc files which we want to copy over to the src/cakework directory:
# TODO automate this part
```
cd src/cakework
source env/bin/activate
pip install grpcio
pip install protobuf
pip install grpcio-tools
python3 -m grpc_tools.protoc -I. --python_out=. --pyi_out=. --grpc_python_out=. cakework.proto
```