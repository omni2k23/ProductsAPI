# ProductsAPI

An API to get mock products instead of getting them in realtime

## Install

Before running the service, make sure you have the dependecies to run it. You can run this command:
`pip install djangorestframework markdown django-filter psycopg2 python-environ jsonschema`

Create a `.env` file in `views/` and add the following environment variables
````
GMAP_API=key
````

## Run the app

    python manage.py runserver 0.0.0.0:8000

# REST API

## Get products from a store

### Request
`GET /search/<store>`

### Params
`category` = Only select products that matches category
`lat` = Latitude of caller REQUIRED
`lng` =  Longitutde of caller REQUIRED

### Response
```json
[
  {
    "name": "",
    "description": "",
    "category": "",
    "price": 0,
    "quantity": 0,
    "image": "",
    "travel_distance": 1710,
    "travel_time": "7 mins"
  }
]
```