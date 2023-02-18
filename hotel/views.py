import json
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from hotel.models import Hotel
# Create your views here.
# ***********************************************************************************
# HOTEL
@csrf_exempt
def addHotel(request):
    if request.method == "POST":
        json_data = json.loads(request.body)

        try:
            hotel = Hotel(
                name = json_data["name"],
                city = json_data["city"],
                address = json_data["address"],
                description = json_data["description"],
                created_on = datetime.today()
            )

            hotel.save()
            response = {
                "uid" : hotel.uid,
                "name" : hotel.name,
                "city" : hotel.city,
                "address" : hotel.address,
                "description" : hotel.description,
                "created_on" : hotel.created_on
            }

            return JsonResponse(response, safe=False)
        except Exception as e:
            response = { "Error": "Error adding Hotel information - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def updateHotel(request, uid):
    if request.method == "PUT":
        json_data = json.loads(request.body)

        name = json_data["name"]
        city = json_data["city"]
        address = json_data["address"]
        description = json_data["description"]

        try:
            hotel = Hotel.nodes.get(uid=uid)

            hotel.name = name
            hotel.city = city
            hotel.address = address
            hotel.descrption = description

            hotel.save()

            response = {
                "Success" : "Hotel Successfully Updates",
                "Name": hotel.name,
                "City": hotel.city,
                "Address": hotel.address,
                "Description": hotel.description
            }

            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"ERROR": "Error on updating hotel information - {}".format(e)}
            return JsonResponse(response, safe=False)

def deleteHotel(request, uid):
    if request.method == "DELETE":
        try:
            hotel = Hotel.nodes.get(uid=uid)
            hotel.delete()
            response = {"success": "Hotel successfully deleted"}
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = { "ERROR": "Error on deleting hotel record - {}".format(e)}
            return JsonResponse(response, safe=False)



