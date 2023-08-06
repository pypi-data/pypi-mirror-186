# myb-lofty-api
An unofficial API client for the unofficial Lofty API

Lofti AI: https://lofty.ai/

API: https://api.lofty.ai/prod

## Installation

The package is availble via PyPi and can be installed with the following command:
```
pip3 install myb-lofty-api
```

To install it from the repo, clone the repo and cd into the directory:

```
git clone https://github.com/mine-your-business/myb-lofty-python-api.git
cd myb-lofty-python-api
```

You can install this library with `pip`:

```
pip3 install .
```

## Examples

There is an example available: [`LoftyAiApi`](example.py)

## Testing

This project leverages `wiremock` to test the code to some extent. Note this will not protect the project from changes that Lofty AI makes to their API, but instead verifies that the existing code functions consistently as written.

### Local Testing 

Note that the tests setup leverages the [`local_env_vars.py`](tests/local_env_vars.py) file. The values for those environment variables need to be set based on the following:

* `LOFTY_USERNAME`: `example@email.com` - This must have parity with the `email` in the `body` specified in [`tests/wiremock/mappings/jwt_request.json`](tests/wiremock/mappings/jwt_request.json)
* `LOFTY_PASSWORD`: `lofty_password` - This must have parity with the `password` in the `body` specified in [`tests/wiremock/mappings/jwt_request.json`](tests/wiremock/mappings/jwt_request.json)
* `API_HOST_OVERRIDE`: `http://127.0.0.1:9090` - This URL is simply `http://127.0.0.1` but the url port must have parity with the [`docker-compose.yaml`](docker-compose.yaml) wiremock service's exposed http `port`. 

To run tests, you will first need to start the wiremock service by running:

```
docker-compose up -d
```

Then, you can run the actual tests with the following command:

```
pytest --verbose
```

### GitHub Testing

This project leverages GitHub Actions and has a [workflow](.github/workflows/python-package.yml) that will run these tests. The environment configuration for the tests must have parity with the [`local_env_vars.py`](tests/local_env_vars.py) file from the [local testing](#local-testing).


## Releases

Releases should follow a [Semantic Versioning](https://semver.org/) scheme. 

When changes have been made that warrant a new release that should be published, modify the `__version__` in [`setup.py`](setup.py) 

After the change is merged to the `main` branch, go to [releases](https://github.com/mine-your-business/myb-lofty-python-api/releases) and `Draft a new release`. The `Tag version` should follow the pattern `v1.0.0` and should `Target` the `main` branch. 

The `Release title` should not include the `v` from the tag and should have a reasonably detailed description of the new release's changes. 

Once the release has been published, the [`.github/workflows/python-publish.yml`](.github/workflows/python-publish.yml) GitHub Actions Workflow should trigger and automatically upload the new version to [PyPi](https://pypi.org/) using GitHub secrets credentials.

## Not-so-secret Keys

Certain values found in [constants.py](./lofty/constants.py) are copied from the [Lofty AI Website](https://lofty.ai/) where they conveniently left their source maps. Those values are in fact ***not*** tied to a personal account with Lofty AI, but are instead specific to their deployments.
