import json
from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from hotel.models import Hotel
# Create your views here.
# ***********************************************************************************
# HOTEL
@csrf_exempt
def addHotel(request):
    if request.method == "POST":
        # json_data = json.loads(request.body)

        try:
            # if json_data:
            #     print("GET JSON data")
            #     hotel = Hotel(
            #         name = json_data["name"],
            #         city = json_data["city"],
            #         address = json_data["address"],
            #         description = json_data["description"],
            #         created_on = datetime.today()
            #     )
            
            print("GET FORM data")
            hotel = Hotel(
                name = request.POST["name"],
                city = request.POST["city"],
                address = request.POST["address"],
                description = request.POST["description"],
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

            # return JsonResponse(response, safe=False)
            return render(request, 'hotel/add_new_hotel.html')
        except Exception as e:
            response = { "Error": "Error adding Hotel information - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'hotel/add_new_hotel.html')

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
    elif request.method == "GET":
        return render(request, 'hotel/update_hotel_information.html')

@csrf_exempt
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

@csrf_exempt
def getSingleHotel(request, uid):
    if request.method == "GET":
        try:
            hotel = Hotel.nodes.get(uid=uid)

            response = {
                "uid" : hotel.uid,
                "Name": hotel.name,
                "City": hotel.city,
                "Address": hotel.address,
                "created_on": hotel.created_on,
                "Description": hotel.description,
            }
            # return JsonResponse(response, safe=False)
            return render(request, 'hotel/view_single_hotel.html', context=response)
        except Exception as e:
            response = { "ERROR": "Error getting hotel record - {}".format(e)}
            return JsonResponse(response, safe=False)

def getAllHotels(request):
    if request.method == "GET":
        try:
            hotels = Hotel.nodes.all()
            response = []
            context = {}

            for hotel in hotels:
                hotel_data = {
                    "uid" : hotel.uid,
                    "Name": hotel.name,
                    "City": hotel.city,
                    "Address": hotel.address,
                    "created_on": hotel.created_on,
                    "Description": hotel.description,
                }

                response.append(hotel_data)

            context = {"data": response}
            # return JsonResponse(response, safe=False)
            return render(request, 'hotel/view_all_hotels.html', context)
        except Exception as e:
            response = { "ERROR": "Error getting all hotel records - {}".format(e)}
            return JsonResponse(response, safe=False)