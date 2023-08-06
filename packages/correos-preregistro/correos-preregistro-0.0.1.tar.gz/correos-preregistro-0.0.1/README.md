[![pipeline status](https://git.coopdevs.org/coopdevs/som-connexio/correos/correos-preregistro/badges/main/pipeline.svg)](https://git.coopdevs.org/coopdevs/som-connexio/correos/correos-preregistro/commits/master)
[![coverage report](https://git.coopdevs.org/coopdevs/som-connexio/correos/correos-preregistro/badges/main/coverage.svg)](https://git.coopdevs.org/coopdevs/som-connexio/correos/correos-preregistro/commits/master)

:warning: WORK IN PROGRESS :warning:

This library is a Python wrapper for accessing PreregistroEnvio Correos SOAP API.

You can find the complete documentation of the API [here](https://preregistroenvios.correos.es/interfacepreregistroenvios/).

## Operations

* PreRegistroEnvio - Customers will provide all the necessary data for pre-registering a shipment and will receive in return the pre-registered shipment code and label with which to label the shipment in the format that they requested (XML or base64 encoded PDF format)

## Installation

```commandline
$ pip install correos-preregistro
```

## Configuration Environment


## Usage

#### Create PreRegistroEnvio shipment

Create a preregistroenvio annd save a file with the shipment number in the name and the PDF label as content:

```python
>>> from correos_preregistro.services.shipment import PreRegistrationShipment
>>> user = "utest"
>>> password = "ptest"
>>> client = RawClient(user, password)
>>> receiver = Receiver(
...     name="Emilio Jose",
...     surname="Marti Gomez",
...     address="Cami del corrar, 51, Baix B",
...     city="Moralla",
...     state="Valencia",
...     zip="03015",
...     phone="666555444",
...     email="emilio.jose@marti.com",
...     lang="CA",
... )
>>> sender = Sender(
...     name="SomConnexio",
...     nif="F66380676",
...     address="C/ de les Moreres, 119",
...     city="El Prat de Llobregat",
...     state="Barcelona",
...     zip="08820",
...     phone="931311728",
...     email="serveis@somconnexio.coop",
...     lang="CA",
... )
>>> package = Package(
...     weight=1,
...     postage_type="FP",
...     product_code="S0132",
...     delivery_modality="ST",
...     weight_type="R",
        )
>>> shipment = PreRegistrationShipment.create(
...     client=client,
...     code="XXX1",
...     receiver=receiver,
...     sender=sender,
...     package=package,
... )
>>> shipment.shipment_code
"PQXXX10721392610108021C"
>>> label_file_name = "shipment_label_{}.pdf".format(shipment.shipment_code)
>>> f = open(shipment.get_pdf_label(), "wb")
>>> f.write(pdf_label)
>>> f.close()
```

## Development

### Setup environment

1. Install `pyenv`
```sh
curl https://pyenv.run | bash
```
2. Build the Python version
```sh
pyenv install  3.7.13
```
3. Create a virtualenv
```sh
pyenv virtualenv 3.7.13 correos-preregistro
```
4. Install dependencies
```sh
pyenv exec pip install -r requirements.txt
```
5. Install pre-commit hooks
```sh
pyenv exec pre-commit install
```

### Install the package locally in development mode

When we are using this package in other projects, we need to install it to use as import in the other files. Install the package in development mode helps us to modify the package and use the new version in live in the other project.

```sh
pip install -e .
```

### Test the HTTP request

We are using the HTTP recording plugin of Pytest: [pytest-recording](https://pytest-vcr.readthedocs.io/).

With VRC we can catch the HTTP responses and then, execute the tests using them.

To add a new test:

* Expose the needed envvars. Look for them at the [Configuration Environment section](#configuration-environment)
* Execute the tests using `pytest` command:
* If you are writing a new test that is making requests, you should run:

```
$ pytest --record-mode=once path/to/your/test
```

* You might need to record requests for an specific tests. In that case make sure to only run the tests affected and run

```
$ pytest --record-mode=rewrite path/to/your/test
```

* Add the new `cassetes` to the commit and push them.
* The CI uses the cassetes to emulate the HTTP response in the test.

### Run test suite

```commandline
$ tox
```

### Formatting

We use [Black](https://github.com/psf/black) as formatter.
First to commit, tun the `black` command:

```commandline
$ black .
All done! ✨ 🍰 ✨
29 files left unchanged.
```

#### Darker

Black is a great formatter, but to mantain your code without execute the `black` command avery time, you can configure your IDE to use [darker](https://pypi.org/project/darker/) to format only the changed or added code when you save the file.

### Release process

Update CHANGELOG.md following this steps:

1. Add any entries missing from merged merge requests.
1. Duplicate the `[Unreleased]` header.
1. Replace the second `Unreleased` with a version number followed by the current date. Copy the exact format from previous releases.

Then, you can release and publish the package to PyPi:

1. Update the `__version__` var in `__init__.py` matching the version you specified in the CHANGELOG.
1. Open a merge request with these changes for the team to approve
1. Merge it, add a git tag on that merge commit and push it.
1. Once the pipeline has successfully passed, your package had been published.
