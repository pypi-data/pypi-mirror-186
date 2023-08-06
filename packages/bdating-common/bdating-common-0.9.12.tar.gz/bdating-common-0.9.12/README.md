# README #

Standard python library for Bdating

# build

### install tools
```
python -m pip install build twine tox
```

### build and upload
```
# given ~/.pypirc has been set.
rm -rf dist/*; tox -e build && tox -e upload 

```