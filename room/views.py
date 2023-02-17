import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

from room.models import Room
from hotel.models import Hotel
from room.models import RoomType
from room.models import RoomElement

# Create your views here.
# ***********************************************************************************
# ROOM
def getAllRooms(request):
    if request.method == 'GET':
        try:
            rooms  = Room.nodes.all()
            response = []
            for room in rooms:
                room_obj = {
                    
                    'image': room.image,
                    'floor' : room.floor,
                    'hotel ' : room.hotel,
                    'room_type ' : room.room_type,
                    'availabilty': room.availabilty,
                    'room_number': room.room_number,
                    'room_element ' : room.room_element,
                    'cost_per_night': room.cost_per_night,
                }

                response.append(room_obj)
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def getRoomDetails(request):
    if request.method == 'GET':
        # Get single room details
        hotel = request.GET.get('hotel')
        room_number = request.GET.get('room_number')
        
        try:
            room = Room.nodes.get(room_number = room_number, hotel = hotel)
            response = {
                    
                    'image': room.image,
                    'floor' : room.floor,
                    'hotel ' : room.hotel,
                    'room_type ' : room.room_type,
                    'availabilty': room.availabilty,
                    'room_number': room.room_number,
                    'room_element ' : room.room_element,
                    'cost_per_night': room.cost_per_night,
                }
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def addRoom(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)

        floor = json_data['floor']
        image = json_data['image']
        hotel = json_data['hotel']
        room_type = json_data['room_type']
        availabilty = json_data['availabilty']
        room_number  =json_data['room_number']
        room_element = json_data['room_element']
        cost_per_night = int(json_data['cost_per_night'])
        
        try:
            room = Room(
                floor=floor, 
                image=image, 
                hotel=hotel, 
                room_type=room_type,
                availabilty=availabilty, 
                room_number=room_number, 
                room_element=room_element, 
                cost_per_night=cost_per_night
            )

            room.save()

            response = {
                    
                    'image': room.image,
                    'floor' : room.floor,
                    'hotel ' : room.hotel,
                    'room_type ' : room.room_type,
                    'availabilty': room.availabilty,
                    'room_number': room.room_number,
                    'room_element ' : room.room_element,
                    'cost_per_night': room.cost_per_night,
                }
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

@csrf_exempt
def editRoom(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        hotel  =json_data['hotel']
        room_number  =json_data['room_number']
        try:
            room = Room.nodes.get(room_number=room_number, hotel=hotel)
            room.floor = json_data['floor']
            room.image = json_data['image']
            room.hotel = json_data['hotel']
            room.room_type = json_data['room_type']
            room.availabilty = json_data['availabilty']
            room.room_number  =json_data['room_number']
            room.room_element = json_data['room_element']
            room.cost_per_night = int(json_data['cost_per_night'])

            response = {
                        
                        'image': room.image,
                        'floor' : room.floor,
                        'hotel ' : room.hotel,
                        'room_type ' : room.room_type,
                        'availabilty': room.availabilty,
                        'room_number': room.room_number,
                        'room_element ' : room.room_element,
                        'cost_per_night': room.cost_per_night,
                    }
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)
        
    if request.method == 'DELETE':
        json_data = json.load(request.body)

        hotel  =json_data['hotel']
        room_number  =json_data['room_number']

        try:
            room = Room.nodes.get(room_number=room_number,hotel=hotel)
            room.delete()
            response = {"success": "Room successfully deleted"}
            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error occurred"}
            return JsonResponse(response, safe=False)

# ***********************************************************************************
# ROOM ELEMENT

@csrf_exempt
def addRoomElement(request):
    if request.method =="POST":
        json_data = json.loads(request.body)

        name = json_data['name']
        description = json_data['description']
        elementType = json_data['elementType']
        created_on = datetime.today()

        try:
            room_element = RoomElement(
                name=name, 
                description=description,
                elementType=elementType,
                created_on=created_on
            )

            room_element.save()

            response = {
                'name': room_element.name, 
                'description': room_element.description,
                'elementType': room_element.elementType,
                'created_on': room_element.created_on
            }

            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"error": "Error Saving Room Element - {}".format(e)}
            return JsonResponse(response, safe=False)

# ***********************************************************************************
# ROOM TYPE

@csrf_exempt
def addRoomType(request):
    json_data = json.loads(request.body)
    try:
        room_type = RoomType(
            name = json_data['name'],
            description = json_data['description'],
            max_capacity = json_data['max_capacity'],
            created_on = datetime.today()
        )

        room_type.save()

        response = {
            "name" : room_type.name,
            "description" : room_type.description,
            "max_capacity" : room_type.max_capacity,
            "created_on" : room_type.created_on
        }

        return JsonResponse(response, safe=False)
    except Exception as e:
        response = {"Error": "Error on saving Room Type - {}".format(e)}
        return JsonResponse(response, safe=False)

# ***********************************************************************************
# HOTEL
@csrf_exempt
def addHotel(request):
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

# ***********************************************************************************
# CONNECTORS
@csrf_exempt
def connectHotelToRoom(request):
    if request.method == 'PUT':
        json_data = json.loads(request.body)
        
        room_number = json_data["room_number"]
        hotel_name = json_data['hotel_name']
        
        try:
            hotel = Hotel.nodes.get(name=hotel_name)
            room = Room.nodes.get(room_number=room_number)

            response_data = room.hotel.connect(hotel)

            response = {
                "result": response_data,
                "room": room.room_number,
                "hotel": hotel.name
            }

            return JsonResponse(response, safe=False)
        except Exception as e:
            response = {"Error": "Error connecting room to hotel - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectRoomTypeToRoom(request):
    if request.method == "PUT":
        json_data = json.loads(request.body)
        room_number = json_data["room_number"]
        room_type_name = json_data["room_type_name"]

        try:
            room = Room.nodes.get(room_number = room_number)
            room_type = RoomType.nodes.get(name = room_type_name)
            
            response_data = room.room_type.connect(room_type)

            response = {
                "result": response_data,
                "room": room.room_number,
                "room_type": room_type.name
            }

            return JsonResponse(response, safe=False)
        except Exception as e:
            response = { "ERROR": "Error connecting Room type to Room - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def connectRoomElelemntToRoom(request):
    if request.method == "PUT":
        json_data = json.loads(request.body)

        room_number = json_data["room_number"]
        room_element_name = json_data["room_element_name"]

        try:
            room = Room.nodes.get(room_number=room_number)
            room_element = RoomElement.nodes.get(name=room_element_name)
            response_data = room.room_element.connect(room_element)

            response = {
                "result": response_data,
                "room": room.room_number,
                "room_element": room_element.name
            }

            return JsonResponse(response, safe=False)
            
        except Exception as e:
            response = {"ERROR": "Error on conecting room to Room Element - {}".format(e)}
            return JsonResponse(response, safe=False)

            