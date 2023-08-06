# avi_package
This is a tutorial project for publishing your own python library on PyPi.

## Requirments

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all the requirements.
Just follow the commands below:

Upgrade Setuptoos:
```bash
python -m pip install --upgrade twine setuptools
```

Install Wheel:
```bash
pip install wheel
```

Make a build for your Library/Package:
```bash
python setup.py sdist bdist_wheel
```

Install twine:
```bash
pip install twine
```

Upload Your Library:
```bash
twine upload dist/*
```

If the above command fail to upload:
```bash
python -m twine upload dist/*
```



If you want to upload through Git repo,
Add this code after import statements
```python
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
```
After add this code you have to add an Readme.md file and the just follow the commands above.
