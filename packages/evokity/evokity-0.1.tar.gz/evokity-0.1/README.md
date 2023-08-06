# Evokity

<p align="center">
Collection of essential <a href=https://github.com/EC-KitY/EC-KitY> Evolutionary Computaion Kit</a> utilities.
</p>

<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/amitkummer/evolutionary-mini-project/integration.yaml?label=Tests%2C%20Linting%20%26%20Formatting&style=for-the-badge">
</p>

## Development

Requires `poetry` installed (tested with `v1.2.2`).

Install the dependencies:

```sh
poetry install
```

Spawn a shell within the project's environment:

```
poetry shell
```


## Unit Tests

To run the unit-tests, use:

```
pytest
pytest -s // To show captured stdout.
```


## Formatting

To run formatting, use:

```
black evokity tests
```

