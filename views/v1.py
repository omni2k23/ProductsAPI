import json
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_http_methods
import environ
import requests


@require_http_methods(["GET"])
def get_store_products(request: HttpRequest, store: str):
    env = environ.Env()
    environ.Env.read_env()

    # Get data from JSON
    with open("stores/stores.json") as fp:
        data = json.load(fp)

    selected_store = data[store]
    category = request.GET.get("category")

    products = []
    lat = request.GET.get("lat")
    lng = request.GET.get("lng")
    for product in selected_store["products"]:
        # Check if lat/longtitude is given in params
        if not lat or not lng:
            response_body = {"Error": "Missing either lat or long"}
            response = JsonResponse(
                response_body, json_dumps_params={"indent": 2}, safe=False
            )
            response.status_code = 400
            return response

        # Call to Google Maps API to calculate travel time between user and the store
        url = "https://maps.googleapis.com/maps/api/directions/json?origin={},{}&destination={},{}&mode=bicycling&key={}".format(
            float(lat), float(lng),selected_store["lat"],selected_store["lng"] , env("GMAP_API")
        )
        req = requests.get(url)
        results = req.json()
        product["travel_time"] = results['routes'][0]['legs'][0]['duration']['text']
        if category:
            if category == product[category]:
                products.append(product)
        else:
            products.append(product)
    return JsonResponse(products, json_dumps_params={"indent": 2}, safe=False)
