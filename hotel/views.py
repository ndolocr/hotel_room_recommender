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