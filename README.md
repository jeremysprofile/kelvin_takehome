# Overview
This is a take-home project provided by Kelvin Inc.

## Requirements
See [`requirements.md`](./requirements.md).

## Initial State
See [`coding_challenge.py`](./coding_challenge.py).

## Running
```bash
docker build . -t challenge
docker run --rm challenge
```

## Future Improvements
Use poetry to create a python package and manage installs of requirements.
Make an entrypoint to call the script.
Use a slimmer python image.
Don't find the highest average temperature if we're not going to do anything with it.
Use a cache in front of the API since the calls are slow?
