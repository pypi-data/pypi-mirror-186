# orderlyweb-api

[![Build Status](https://travis-ci.com/vimc/orderly-web-py.svg?branch=master)](https://travis-ci.com/vimc/orderly-web-py)
[![codecov.io](https://codecov.io/github/vimc/orderly-web-py/coverage.svg?branch=master)](https://codecov.io/github/vimc/orderly-web-py?branch=master)

Python client for [OrderlyWeb](https://github.com/vimc/orderly-web). 

Initial use case is to run a report only. 

## Usage

Instantiate the `OrderlyWebAPI` class, providing base url and bearer token as parameters:

```
api = OrderlyWebAPI('http://localhost:8080', 'H2AAbjvhjbbhbhjlh')
```
The bearer token must be obtained externally to this client. Use the 
[Montagu Python client](https://github.com/vimc/montagu-py) to obtain a token by 
authenticating with Montagu. 

To run a report:
```
api.run_report(report_name, report_paraneters, timeout)
```
where `report_parameters` is a dictionary or JSON string, and `timeout` is an 
integer. `Timeout` sets a timeout for the report run in seconds, after which the 
run will be halted. The default timeout is 600.


## Development

Clone the repo anywhere and install dependencies with (from the repo root):
```
pip3 install --user -r requirements.txt
```

Run dependencies (a local copy of Montagu API and database, and OrderlyWeb) with `scripts/run-dev-dependencies.sh`. This will also
add a test user to Montagu.

## Testing

Run dependencies as described above, then run `pytest`

## Publishing

This repository is published to [PyPI](https://pypi.org/project/orderlyweb-api). 

Building and publishing is done manually, with local sources. 

Publishing configuration can be found in `setup.py`, and any classes, methods etc which should be accessible to users of the package
must be added to `orderlyweb_api/__init__.py`. 
Remember to increment `version` in `setup.py` before publishing a new build.

To publish:
1. Delete the following folders: `.eggs`, `build`, `dist`, `orderlyweb_api.egg-info`. 
1. Build the package with: `python3 setup.py sdist bdist_wheel`
1. Publish with: `python3 -m twine upload dist/*`

To use the OrderlyWebAPI class as a client of the package, include `orderlyweb-api` in your `requirements.txt`. Import with
`import orderlyweb_api`, and instantiate the API class with `orderlyweb_api.OrderlyWebAPI(url, token)`

See general instructions for publishing Python packages [here](https://packaging.python.org/tutorials/packaging-projects/).

Some troubleshooting tips for publishing Python packages can be found in the 
[consellations repo](https://github.com/reside-ic/constellation/blob/master/publish.md).