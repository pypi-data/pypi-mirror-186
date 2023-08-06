# smart_energy.green_energy_api

A python library to access the Awattar Api. Refer also to the [Awattar Energy Price API](https://www.awattar.de/). This repo provides functionality for:

- Getting Energy Price forecast forecast information.

## Installing the library locally

Python 3 is recommended for this project.

```bash
python -m pip install -e .
```

> **This is needed for the first time when working with the library/examples/tests.**

## Example usage

```bash
ENERGY_DATA_API_URL="https://api.awattar.de" python3 examples/simple.py
```

or

```python
from green_energy_api.green_energy_api import GreenEnergyApi

green_energy_api = GreenEnergyApi('provide_api_url')
# or you can define additional optional parameters
# green_energy_api = GreenEnergyApi('provide_api_url', timeout=10)

print(green_energy_api.get_electricity_price())
```

## Development

### Installing required pip packages

```bash
python pip install -r requirements.txt
pre-commit install -t pre-push
```

### Linting

```bash
pylint green_energy_api/*.py tests/*.py examples/*.py
```

### Unit testing

```bash
pytest tests/*.py

# show logs
pytest -o log_cli=true

# code coverage
pytest --durations=10 --cov-report term-missing --cov=green_energy_api tests
```
