# lnhub-rest: Cross-instance management

Note: For more extensive documentation, see [docs/content](docs/content.md).

## Installation

1. Clone this repository
2. Navigate to the repository and run:

   ```
   pip install .
   ```

## Start the server

Start the server by running:

```
python3 ./lnhub_rest/main.py
```

or

```
./devops/run.sh
```

## Run in a docker container

Run the server in a docker container:

```
./devops/docker-run.sh
```

## Deployment

Push on the `main` branch to deploy in production.
End point url:

```
https://lnhub-rest-cloud-run-main-xv4y7p4gqa-uc.a.run.app
```

## Usage

Access API documentation from these endpoints.

Locally:

```
http://localhost:8000/docs
```

On production server:

```
https://lnhub-rest-cloud-run-main-xv4y7p4gqa-uc.a.run.app/docs
```
