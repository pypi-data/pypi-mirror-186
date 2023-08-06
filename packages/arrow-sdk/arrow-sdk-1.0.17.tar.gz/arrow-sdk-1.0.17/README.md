### Getting Started

1. Install the package from PyPi `pip install arrow-sdk`.
2. To import the package in a Python file, run `import arrow_sdk`.
3. You could then access the SDK functions, for example `arrow_sdk.estimateOptionPrice(...)`.

### Setting it up locally
1. Create a virtual environment `python -m venv venv`. 
2. Activate the virtual environment `source venv/bin/activate`. 
3. Install required dependencies `pip install -r requirements.txt`. 

### To deploy to Pypi
1. Run `python setup.py sdist bdist_wheel` to set up the `dist` folder.
2. To upload to Pypi, run `twine upload dist/*`.

### To run the tests

1. Make sure the virtual environment is activated. 
2. Run `pytest`. 


