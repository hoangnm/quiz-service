# Quiz API

## Run app in development with docker compose
```
docker-compose up
```

## Run test
```
poetry run pytest
```

## Init data
```
python run init_data.py
```

## API Document
http://localhost:8000/docs

## Technology
- Python
- FastAPI with uvicorn
- MongoDB with motor
- Poetry for dependency management

## Folder structure
Main code is put into `app` folder
We follow 3 layers architecture:
- `api/routes` layer: manage exposed rest api to client, each route is put into a separate file
- `db` layer: manage access to database
- `service` layer: business logic

Later on, once the service is more complex, we can add uplift 3 layers architecture to "clean architecture" with domain driven design.

## TODO
- [x] setup unit test
- [x] add middleware to get user id
- [ ] create participant api