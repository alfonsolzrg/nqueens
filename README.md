# N queens problem

## Building the project

```
pip install -r requirements.txt

```

## Running docker container

```
docker build . -t nqueens
```

This will start postgres and call main.py, logging solution count for specified board size in docker-compose.yml to stdout.

```
docker-compose up
```

## Inspecting results

You can inspect the running `postgres` container.
