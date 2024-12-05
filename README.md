# Fullstack App Backend

## Description

This is a simple python app using flask to server data.

## How to use

This app is best run using the included Dockerfile

### Build the Docker image
```
docker build -t flask-app .
```

## Run the container
```
docker run -p 5000:5000 flask-app
```

## Test

Request  
```
curl --location 'localhost:5000/tasks'
```

Response
```
[
    {
        "id": 1,
        "task": "Buy groceries"
    },
    {
        "id": 2,
        "task": "Walk the dog"
    },
    {
        "id": 3,
        "task": "Prepare dinner"
    }
]
```
