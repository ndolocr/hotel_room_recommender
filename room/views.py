import ast
import json

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from datetime import datetime

from room.models import Room
from hotel.models import Hotel
from room.models import RoomType
from room.models import RoomElement
from room.models import RoomViewPreference

# Create your views here.
# ***********************************************************************************
# ROOM
def getAllRooms(request):
    if request.method == 'GET':
        try:
            rooms  = Room.nodes.all()
            response = []
            context = {}
            for room in rooms:
                room_obj = {
                    'uid': room.uid,
                    'floor' : room.floor,
                    'hotel' : room.hotel_id,                    
                    'created_on' : room.created_on,
                    'availability': room.availability,
                    'room_number': room.room_number,
                    'room_type' : room.room_type_id,
                    'cost_per_night': room.cost_per_night,
                    'room_element' : room.room_element_id,                    
                }
                response.append(room_obj)
            context = {"data": response}
            return render(request, 'room/room_pages/view_all.html', context)
        except Exception as e:
            response = {"Error": "Error occurred while getting room records - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def getSingleRoom(request, uid):
    if request.method == 'GET':
        # Get single room details                
        try:
            room = Room.nodes.get(uid=uid)
            room_response = {
                    'floor' : room.floor,
                    'created_on': room.created_on,        
                    'availability': room.availability,
                    'room_number': room.room_number,                     
                    'cost_per_night': room.cost_per_night,                    
            }
            
            # Get Hotel
            hotel = Hotel.nodes.get(uid=room.hotel_id)
            hotel_response = {
                'hotel_uid': hotel.uid,
                'hotel_name': hotel.name,                
            }
            
            # Get Room Type
            room_type =RoomType.nodes.get(uid=room.room_type_id)
            room_type_response = {
                'room_type_uid': room_type.uid,
                'room_type_name': room_type.name,                
            }
            all_room_element_list = []
            room_element_list = ast.literal_eval(room.room_element_id)
            print("All ELEMENT UDI ==>", room_element_list)
            print("All ELEMENT UDI TYPE ==>", type(room_element_list))
            for room_ele in room_element_list:
                print("Room Ele UID ====>", room_ele)
                room_element_obj = RoomElement.nodes.get(uid=room_ele)
                room_element_response = {
                    'room_element_uid': room_element_obj.uid,
                    'room_element_name': room_element_obj.name,
                }

                all_room_element_list.append(room_element_response)

            context = {
                'room': room_response,
                'hotel': hotel_response,
                'room_type': room_type_response,
                'room_element': all_room_element_list,
            }
            
            return render(request, 'room/room_pages/view_single.html', context)
        except Exception as e:
            response = {"Error": "Error occurred while viewing single room record - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def addRoom(request):
    if request.method == 'POST':
        floor = request.POST['floor']
        availability = request.POST['availability']
        room_number  =request.POST['room_number']
        cost_per_night = float(request.POST['cost_per_night'])

        hotel = request.POST['hotel']
        room_type = request.POST['room_type']
        room_element_list = request.POST.getlist('checks[]')
        
        try:
            room = Room(
                floor=floor,
                hotel_id = hotel,
                availability=availability, 
                room_number=room_number,  
                room_type_id = room_type,
                cost_per_night=cost_per_night,
                created_on = datetime.today(),                            
                room_element_id = room_element_list
            )
            room.save()

            room_type_obj = RoomType.nodes.get(uid = room_type)
            room_type_connection = room.room_type.connect(room_type_obj)

            hotel_obj = Hotel.nodes.get(uid = hotel)
            hotel_room_connection = room.hotel.connect(hotel_obj)

            for data in room_element_list:
                room_element_obj = RoomElement.nodes.get(uid = data)
                room_element_connection = room.room_element.connect(room_element_obj)

            return render(request, 'room/room_pages/add.html')

        except Exception as e:
            response = {"ERROR": "Error occurred while adding room - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        try:
            room_types = RoomType.nodes.all()
            room_type_response = []
            context = {}

            for room_type in room_types:
                room_type_data = {
                    "uid" : room_type.uid,
                    "Name": room_type.name,
                    "Maximum_Capacity": room_type.max_capacity,
                    "created_on": room_type.created_on,
                    "Description": room_type.description,
                }

                room_type_response.append(room_type_data)
            
            room_elements = RoomElement.nodes.all()
            room_element_response = []

            for room_element in room_elements:
                room_element_data = {
                    "uid" : room_element.uid,
                    "Name": room_element.name,
                    "Element_type": room_element.elementType,
                    "created_on": room_element.created_on,
                    "Description": room_element.description,
                }

                room_element_response.append(room_element_data)
            
            hotels = Hotel.nodes.all()
            hotel_response = []

            for hotel in hotels:
                hotel_data = {
                    "uid" : hotel.uid,
                    "Name": hotel.name,
                    "City": hotel.city,
                    "Address": hotel.address,
                    "created_on": hotel.created_on,
                    "Description": hotel.description,
                }

                hotel_response.append(hotel_data)

            context = {
                "hotels": hotel_response,
                "room_types": room_type_response,
                "room_elements" : room_element_response
            }
            return render(request, 'room/room_pages/add.html', context)  
        except Exception as e:
            response = {"ERROR": "Error occurred while fethcing room types - {}".format(e)}
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
            room.availability = json_data['availability']
            room.room_number  =json_data['room_number']
            room.room_element = json_data['room_element']
            room.cost_per_night = int(json_data['cost_per_night'])

            response = {
                        
                        'image': room.image,
                        'floor' : room.floor,
                        'hotel ' : room.hotel,
                        'room_type ' : room.room_type,
                        'availability': room.availability,
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
        # json_data = json.loads(request.body)

        # name = json_data['name']
        # description = json_data['description']
        # elementType = json_data['elementType']
        # created_on = datetime.today()

        name = request.POST['name']
        description = request.POST['description']
        elementType = request.POST['elementType']
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

            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_element/add.html')
        except Exception as e:
            response = {"error": "Error Saving Room Element - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_element/add.html')        

def getAllRoomElements(request):
    if request.method == "GET":
        try:
            room_types = RoomElement.nodes.all()
            response = []
            context = {}

            for room_type in room_types:
                room_type_data = {
                    "uid" : room_type.uid,
                    "Name": room_type.name,
                    "Element_type": room_type.elementType,
                    "created_on": room_type.created_on,
                    "Description": room_type.description,
                }

                response.append(room_type_data)

            context = {"data": response}
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_element/view_all.html', context)
        except Exception as e:
            response = { "ERROR": "Error getting all Room Element records - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def getSingleRoomElement(request, uid):
    if request.method == "GET":
        try:
            record = RoomElement.nodes.get(uid=uid)

            response = {
                "uid" : record.uid,
                "Name": record.name,
                "Element_type": record.elementType,
                "created_on": record.created_on,
                "Description": record.description,
            }
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_element/view_single.html', context=response)
        except Exception as e:
            response = { "ERROR": "Error getting room element record - {}".format(e)}
            return JsonResponse(response, safe=False)

# ***********************************************************************************
# ROOM TYPE

@csrf_exempt
def addRoomType(request):
    if request.method == "POST":
        # json_data = json.loads(request.body)
        try:
            room_type = RoomType(
                name = request.POST['name'],
                description = request.POST['description'],
                max_capacity = request.POST['max_capacity'],
                created_on = datetime.today()
            )

            room_type.save()

            response = {
                "name" : room_type.name,
                "description" : room_type.description,
                "max_capacity" : room_type.max_capacity,
                "created_on" : room_type.created_on
            }

            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_type/add.html')
        except Exception as e:
            response = {"Error": "Error on saving Room Type - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_type/add.html')

def getAllRoomTypes(request):
    if request.method == "GET":
        try:
            room_types = RoomType.nodes.all()
            response = []
            context = {}

            for room_type in room_types:
                room_type_data = {
                    "uid" : room_type.uid,
                    "Name": room_type.name,
                    "Maximum_Capacity": room_type.max_capacity,
                    "created_on": room_type.created_on,
                    "Description": room_type.description,
                }

                response.append(room_type_data)

            context = {"data": response}
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_type/view_all.html', context)
        except Exception as e:
            response = { "ERROR": "Error getting all Room Type records - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def getSingleRoomType(request, uid):
    if request.method == "GET":
        try:
            record = RoomType.nodes.get(uid=uid)

            response = {
                "uid" : record.uid,
                "Name": record.name,
                "Maximum_Capacity": record.max_capacity,
                "created_on": record.created_on,
                "Description": record.description,
            }
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_type/view_single.html', context=response)
        except Exception as e:
            response = { "ERROR": "Error getting room element record - {}".format(e)}
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

# ***********************************************************************************
# ROOM View Preference

@csrf_exempt
def addRoomViewPreference(request):
    if request.method == "POST":
        try:
            query = RoomViewPreference(
                name = request.POST['name'],
                description = request.POST['description'],
                created_on = datetime.today()
            )

            query.save()

            response = {
                "name" : query.name,
                "description" : query.description,
                "created_on" : query.created_on
            }

            # return JsonResponse(response, safe=False)
            # return render(request, 'room/room_type/add.html')
            return redirect(reverse('room-view-preference-all'))
        except Exception as e:
            response = {"Error": "Error on saving Room Type - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_view/add.html')

def getAllRoomTypes(request):
    if request.method == "GET":
        try:
            room_types = RoomType.nodes.all()
            response = []
            context = {}

            for room_type in room_types:
                room_type_data = {
                    "uid" : room_type.uid,
                    "Name": room_type.name,
                    "Maximum_Capacity": room_type.max_capacity,
                    "created_on": room_type.created_on,
                    "Description": room_type.description,
                }

                response.append(room_type_data)

            context = {"data": response}
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_type/view_all.html', context)
        except Exception as e:
            response = { "ERROR": "Error getting all Room Type records - {}".format(e)}
            return JsonResponse(response, safe=False)

@csrf_exempt
def getSingleRoomType(request, uid):
    if request.method == "GET":
        try:
            record = RoomType.nodes.get(uid=uid)

            response = {
                "uid" : record.uid,
                "Name": record.name,
                "Maximum_Capacity": record.max_capacity,
                "created_on": record.created_on,
                "Description": record.description,
            }
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_type/view_single.html', context=response)
        except Exception as e:
            response = { "ERROR": "Error getting room element record - {}".format(e)}
            return JsonResponse(response, safe=False)
