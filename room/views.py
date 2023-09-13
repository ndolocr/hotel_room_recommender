import ast
import json

from django.urls import reverse
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import datetime

from neomodel import db

from room.models import Room
from hotel.models import Hotel
from room.models import RoomType
from room.models import RoomScent
from room.models import RoomLight
from room.models import RoomElement
from room.models import RoomHumidity
from room.models import RoomTemprature
from room.models import RoomViewPreference
from room.models import RoomAccessibility

from booking.models import Reservation

from user_manager.models import Pet
from user_manager.models import UserNode

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

        availability = 'available'
        floor = request.POST['floor']                        
        hotel = request.POST['hotel']
        pet_room = request.POST.get('pet_room')
        room_type = request.POST['room_type']        
        room_view = request.POST['room_view']
        room_scent = request.POST['room_scent']
        room_light = request.POST['room_light']
        room_number  =request.POST['room_number']        
        room_humidity = request.POST['room_humidity']
        room_temprature = request.POST['room_temprature']
        room_element_list = request.POST.getlist('checks[]')
        cost_per_night = float(request.POST['cost_per_night'])
        disability_features = request.POST['disability_features']
        room_accessibility_list = request.POST.getlist('acess_checks[]')
        
        
        try:
            room = Room(
                floor=floor,
                hotel_id = hotel,
                pet_room = pet_room,
                room_number=room_number,  
                room_type_id = room_type,                                                                                            
                room_view_id  =room_view,
                availability=availability,
                room_light_id = room_light,
                room_scent_id = room_scent,
                created_on = datetime.today(),
                cost_per_night=cost_per_night,
                room_humidity_id = room_humidity,                
                room_element_id = room_element_list,
                room_temprature_id = room_temprature,
                disability_features = disability_features,
                # room_accessibility_id = room_accessibility,
            )
            room.save()

            room_type_obj = RoomType.nodes.get(uid = room_type)
            room_type_connection = room.room_type.connect(room_type_obj)

            hotel_obj = Hotel.nodes.get(uid = hotel)
            hotel_room_connection = room.hotel.connect(hotel_obj)

            
            room_scent_obj = RoomScent.nodes.get(uid = room_scent)
            room_light_obj = RoomLight.nodes.get(uid = room_light)
            room_view_obj = RoomViewPreference.nodes.get(uid = room_view)
            room_humidity_obj = RoomHumidity.nodes.get(uid = room_humidity)
            room_temprature_obj = RoomTemprature.nodes.get(uid = room_temprature)
            # room_accessibility_obj = RoomAccessibility.nodes.get(uid=room_accessibility)

            room_scent_connection = room.room_scent.connect(room_scent_obj)
            room_light_connection = room.room_light.connect(room_light_obj)
            room_view_connection = room.room_view.connect(room_view_obj)
            room_humidity_connection = room.room_humidity.connect(room_humidity_obj)
            room_temprature_connection = room.room_temprature.connect(room_temprature_obj)
            # room_accessibility_connection = room.room_accessibility.connect(room_accessibility_obj)


            for data in room_element_list:
                room_element_obj = RoomElement.nodes.get(uid = data)
                room_element_connection = room.room_element.connect(room_element_obj)
            
            for data in room_accessibility_list:
                obj = RoomAccessibility.nodes.get(uid = data)
                room_connection = room.room_accessibility.connect(obj)

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

            room_view_query = RoomViewPreference.nodes.all()
            room_view_response = []

            for room_view_record in room_view_query:
                room_view_dictionary = {
                    "uid": room_view_record.uid,
                    "name": room_view_record.name,
                    "created_on": room_view_record.created_on,
                    "description": room_view_record.description,                    
                }

                room_view_response.append(room_view_dictionary)

            room_temprature_query = RoomTemprature.nodes.all()
            room_temprature_response = []

            for room_temprature_record in room_temprature_query:
                room_temprature_dictionary = {
                    "uid": room_temprature_record.uid,
                    "created_on": room_temprature_record.created_on,
                    "max_temprature": room_temprature_record.max_temprature,
                    "min_temprature": room_temprature_record.min_temprature,
                }

                room_temprature_response.append(room_temprature_dictionary)

            room_humidity_query = RoomHumidity.nodes.all()
            room_humidity_response = []

            for room_humidity_record in room_humidity_query:
                room_humidity_dictionary = {
                    "uid": room_humidity_record.uid,
                    "created_on": room_humidity_record.created_on,
                    "max_humidity": room_humidity_record.max_humidity,
                    "min_humidity": room_humidity_record.min_humidity,
                }

                room_humidity_response.append(room_humidity_dictionary)

            room_light_query = RoomLight.nodes.all()
            room_light_response = []

            for room_light_record in room_light_query:
                room_light_dictionary = {
                    "uid": room_light_record.uid,
                    "created_on": room_light_record.created_on,
                    "max_light": room_light_record.max_light,
                    "min_light": room_light_record.min_light,
                }

                room_light_response.append(room_light_dictionary)

            room_scent_query = RoomScent.nodes.all()
            room_scent_response = []

            for room_scent_record in room_scent_query:
                room_scent_dictionary = {
                    "uid": room_scent_record.uid,
                    "created_on": room_scent_record.created_on,
                    "scent_name": room_scent_record.scent_name,
                    "description": room_scent_record.description,
                }

                room_scent_response.append(room_scent_dictionary)

            room_accessibility_query = RoomAccessibility.nodes.all()
            room_accessibility_response = []

            for room_accessibility_record in room_accessibility_query:
                room_accessibility_dictionary = {
                    "uid": room_accessibility_record.uid,
                    "created_on": room_accessibility_record.created_on,
                    "name": room_accessibility_record.accessibility_name,
                    "description": room_accessibility_record.description,
                }

                room_accessibility_response.append(room_accessibility_dictionary)


            context = {
                "hotels": hotel_response,
                "room_views": room_view_response,                
                "room_types": room_type_response,
                "room_lights": room_light_response,
                "room_scents": room_scent_response,
                "room_elements": room_element_response,
                "room_humidities": room_humidity_response,
                "room_tempratures": room_temprature_response, 
                "room_accessibility": room_accessibility_response,
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
        name = request.POST['name']
        score = request.POST['score'] 
        description = request.POST['description']
        elementType = request.POST['elementType']
        created_on = datetime.today()

        try:
            room_element = RoomElement(
                name=name, 
                score=score,
                description=description,
                elementType=elementType,
                created_on=created_on
            )

            room_element.save()

            response = {
                'name': room_element.name,
                'score': score,
                'description': room_element.description,
                'elementType': room_element.elementType,
                'created_on': room_element.created_on
            }

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
                    "Score": room_type.score,
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
                "Score": record.score,
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
                score = request.POST['score'],
                description = request.POST['description'],
                max_capacity = request.POST['max_capacity'],
                created_on = datetime.today()
            )

            room_type.save()

            response = {
                "name" : room_type.name,
                "score": room_type.score,
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
                    "Score": room_type.score,
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
                "Score": record.score,
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
                score = request.POST['score'],
                description = request.POST['description'],
                created_on = datetime.today()
            )

            query.save()

            response = {
                "name" : query.name,
                "score" : query.score,
                "description" : query.description,
                "created_on" : query.created_on
            }

            # return JsonResponse(response, safe=False)
            # return render(request, 'room/room_type/add.html')
            return redirect(reverse('room-view-preference-all'))
        except Exception as e:
            response = {"Error": "Error on saving Room View - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_view/add.html')

@csrf_exempt
def getSingleRoomViewPreference(request, uid):
    if request.method == "GET":
        try:
            record = RoomViewPreference.nodes.get(uid=uid)

            response = {
                "uid" : record.uid,
                "Name": record.name,
                "created_on": record.created_on,
                "Description": record.description,
            }
            # return JsonResponse(response, safe=False)
            return render(request, 'room/room_view/view_single.html', context=response)
        except Exception as e:
            response = { "ERROR": "Error getting room view record - {}".format(e)}
            return JsonResponse(response, safe=False)

def viewAllRoomViewPreferences(request):
    try:
        context = {}
        response = []
        query = RoomViewPreference.nodes.all()

        for record in query:
            record_dictionary = {
                "uid": record.uid,
                "name": record.name,
                "score": record.score,
                "created_on": record.created_on
            }

            response.append(record_dictionary)
        context = {
            "data": response
        }

        return render(request, 'room/room_view/view_all.html', context=context)
    except Exception as e:
        response = {"ERROR": "Error getting all room view preferences - {}".format(e)}


# ***************************************************************************************************** #
# Room Temprature Range
@csrf_exempt
def addRoomTemprature(request):
    if request.method == 'POST':
        try:
            maximum_temprature = request.POST['maximum_temprature']
            minimum_temprature = request.POST['minimum_temprature']

            print('Maximum Temp --> ', maximum_temprature)
            print('Minimum Temp ==>', minimum_temprature)

            query = RoomTemprature(
                max_temprature = maximum_temprature,
                min_temprature = minimum_temprature,
                created_on = datetime.today()
            )

            print('Query : --->', query)
            query.save()
            return render(request, 'room/room_temprature/add.html')
        except Exception as e:
            response = { "ERROR": "Error while creating new room temprature range - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_temprature/add.html')

def getAllRoomTemprature(request):
    try:
        context = {}
        response_data = []        
        query = RoomTemprature.nodes.all()
        
        for record in query:
            record_dict = {
                'created_on': record.created_on,
                'min_temprature': record.min_temprature,
                'max_temprature': record.max_temprature,
            }

            response_data.append(record_dict)

            context = {
                'data':response_data,
            }

            return render(request, 'room/room_temprature/view_all.html', context=context)
    except Exception as e:
        response = { "ERROR": "Error while getting all room temprature records - {}".format(e)}
        return JsonResponse(response, safe=False)

# ***************************************************************************************************** #
# Room Humidity Range

def addRoomHumidity(request):
    if request.method == "POST":
        try:
            maximum_humidity = request.POST["maximum"]
            minimum_humidity = request.POST["minimum"]

            query = RoomHumidity(
                max_humidity = maximum_humidity,
                min_humidity = minimum_humidity,
                created_on = datetime.today()
            )

            query.save()
        except Exception as e:
            response = {"ERROR": "Error while saving Room Humidity information - {}".format(e)}
            return JsonResponse(response, safe=False)
        return render(request, 'room/room_humidity/add.html')
    else:
        return render(request, 'room/room_humidity/add.html')
    
def viewAllRoomHumidity(request):
    try:
        contex = {}
        response_data = []
        query  =RoomHumidity.nodes.all()

        for record in query:
            record_dictionary = {
                'created_on': record.created_on,
                'min_humidity': record.min_humidity,
                'max_humidity': record.max_humidity,
            }

            response_data.append(record_dictionary)

        context = {"data": response_data}
        return render(request, 'room/room_humidity/view_all.html', context=context)
    except Exception as e:
        response = { "ERROR": "Error while getting all room humidity records - {}".format(e)}
        return JsonResponse(response, safe=False)

# ***************************************************************************************************** #
# Room Lighting Range

def addRooLight(request):
    if request.method == "POST":
        try:
            score = request.POST["score"]
            maximum_humidity = request.POST["maximum"]
            minimum_humidity = request.POST["minimum"]

            query = RoomLight(
                score = score,
                max_light = maximum_humidity,
                min_light = minimum_humidity,
                created_on = datetime.now()
            )

            query.save()
            return render(request, 'room/room_light/add.html')
        except Exception as e:
            response = { "ERROR": "Error while saving room lighting information - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_light/add.html')
    
def viewAllRoomLight(request):
    try:
        context = {}
        response_data = []
        query = RoomLight.nodes.all()

        for record in query:
            record_dictionary = {
                'score': record.score,
                'min_light': record.min_light,
                'max_light': record.max_light,
                'created_on': record.created_on,
            }

            response_data.append(record_dictionary)
        context = {"data": response_data}
        return render(request, 'room/room_light/view_all.html', context=context)
    except Exception as e:
        response = {
            "ERROR": "Error while fetching records for room lighting -> {}".format(e)
        }
        return JsonResponse(response)
    
# ***************************************************************************************************** #
# Room Accessibility Features

def addAccessibilityFeature(request):
    if request.method == "POST":
        try:
            accessibility_name = request.POST["name"]
            description = request.POST["description"]

            query = RoomAccessibility(                
                description = description,
                created_on = datetime.now(),
                accessibility_name = accessibility_name
            )

            query.save()
            return render(request, 'room/room_accessibility/add.html')
        except Exception as e:
            response = { "ERROR": "Error while saving room accessibility features - {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return render(request, 'room/room_accessibility/add.html')

def getAllAccessibilityFeatures(request):
    try:
        context = {}
        response_data = []
        query = RoomAccessibility.nodes.all()

        for record in query:
            record_dictionary = {
                'created_on': record.created_on,
                'description': record.description,
                'accessibility_name': record.accessibility_name,                
            }

            response_data.append(record_dictionary)
        context = {"data": response_data}
        return render(request, 'room/room_accessibility/view_all.html', context=context)
    except Exception as e:
        response = {
            "ERROR": "Error while fetching records for room accessibility features -> {}.".format(e)
        }
        return JsonResponse(response)

# ***************************************************************************************************** #
# Room Scent

def addRoomScent(request):
    if request.method == 'POST':
        try:
            scent_name = request.POST["name"]
            description = request.POST["description"]
            
            query = RoomScent(
                scent_name = scent_name,
                description = description,
                created_on = datetime.now()
            )

            query.save()
            return render(request, 'room/room_scent/add.html')
        except Exception as e:
            response = {"ERROR": "Error while saving room scent information"}
            return JsonResponse(response)
    else:
        return render(request, 'room/room_scent/add.html')

def viewAllRoomScent(request):
    try:
        context = {}
        response = []

        query = RoomScent.nodes.all()

        for record in query:
            record_dictionary = {
                "uid": record.uid,
                "scent_name": record.scent_name,
                "created_on": record.created_on,
                "description": record.description,                
            }

            response.append(record_dictionary)
        context = {"data": response}
        return render(request, 'room/room_scent/view_all.html', context=context)
    except Exception as e:
        response = {"ERROR": "Error while fetching records for room scent information"}
        return JsonResponse(response)
    
@api_view(["POST"])
def filterRooms(request):
    if request.method == "POST":
        
        room_response = []
        date_to_value = request.POST["date_to_value"]
        pet_room_value = request.POST.get("pet_room_value", None)
        date_from_value = request.POST["date_from_value"]
        max_light_value = request.POST["max_light_value"]
        min_light_value = request.POST["min_light_value"]
        room_type_value = request.POST["room_type_value"]
        room_view_value = request.POST["room_view_value"]
        room_scent_value = request.POST["room_scent_value"]
        # room_access_value = request.POST["room_access_value"]
        min_humidity_value = request.POST["min_humidity_value"]
        max_humidity_value = request.POST["max_humidity_value"]
        min_temprature_value = request.POST["min_temprature_value"]
        max_temprature_value = request.POST["max_temprature_value"]
        disability_features_value = request.POST["disability_features_value"]
        
        print("PET ROOM- >", pet_room_value)
        query = "MATCH (room:Room)WHERE room.availability = 'available' "

        if room_type_value:
            new_query = "MATCH(room)-[:`Room Type`]->(roomType:RoomType {uid: '%s'}) " %room_type_value
            query = query + new_query

        if disability_features_value:
            new_query = "MATCH(room) WHERE room.disability_features = '%s' " %disability_features_value
            query = query + new_query

        if pet_room_value:
            new_query = "MATCH(room) WHERE room.pet_room = '%s' " %pet_room_value
            query = query + new_query

        if room_view_value:
            new_query = "MATCH(room)-[:`View visible while in room`]->(roomView:RoomViewPreference {uid: '%s'}) " %room_view_value
            query = query + new_query
        
        if room_scent_value:
            new_query = "MATCH(room)-[:`Scent in a Room`]->(roomScent:RoomScent {uid: '%s'}) " %room_scent_value
            query = query + new_query

        print("Min Light ->", min_light_value)

        if min_light_value:
            min_light_value = float(min_light_value)
            new_query = "MATCH(room)-[:`Lighting Range in a Room`]->(roomLight:RoomLight WHERE roomLight.min_light >= %f) " %min_light_value
            query = query + new_query
        
        if max_light_value:
            max_light_value = float(max_light_value)
            new_query = "MATCH(room)-[:`Lighting Range in a Room`]->(roomLight:RoomLight WHERE roomLight.max_light <= %f) " %max_light_value
            query = query + new_query

        if min_humidity_value:
            min_humidity_value = float(min_humidity_value)
            new_query = "MATCH(room)-[:`Humidity Range in a Room`]->(roomHumidity:RoomHumidity WHERE roomHumidity.min_humidity >= %f) " %min_humidity_value
            query = query + new_query
        
        if max_humidity_value:
            max_humidity_value = float(max_humidity_value)
            new_query = "MATCH(room)-[:`Humidity Range in a Room`]->(roomHumidity:RoomHumidity WHERE roomHumidity.max_humidity <= %f) " %max_humidity_value
            query = query + new_query

        if min_temprature_value:
            min_temprature_value = float(min_temprature_value)
            new_query = "MATCH(room)-[:`Temprature Range in a Room`]->(roomTemprature:RoomTemprature WHERE roomTemprature.min_temprature >= %f) " %min_temprature_value
            query = query + new_query
        
        if max_temprature_value:
            max_temprature_value = float(max_temprature_value)
            new_query = "MATCH(room)-[:`Temprature Range in a Room`]->(roomTemprature:RoomTemprature WHERE roomTemprature.max_temprature <= %f) " %max_temprature_value
            query = query + new_query

        query = query + " RETURN room"
        
        print("QUERY --> ", query)

        results, meta = db.cypher_query(query)
        
        for row in results:
            room_row = Room.inflate(row[0])
            room_obj = {
                'uid': room_row.uid,
                'room_number': room_row.room_number,                   
            }
            print("ROOM OBJ -> ", room_obj)
            room_response.append(room_obj)

        context = {
            "room_response": room_response
        }
        return Response(context)

def bookRoom(request):
    if request.method == "POST":
        print("Booking a room")
        
        total_cost = 0
        pet_name = request.POST["pet_name"]        
        pet_type = request.POST["pet_type"]        
        guest_uid = request.POST["guest_uid_value"] 
        pet_room_value = request.POST.get("pet_room_value", None)
        max_light_value = request.POST["max_light_value"]
        min_light_value = request.POST["min_light_value"]
        room_type_value = request.POST["room_type_value"]
        room_view_value = request.POST["room_view_value"]
        room_scent_value = request.POST["room_scent_value"]
        # room_access_value = request.POST["room_access_value"]
        min_humidity_value = request.POST["min_humidity_value"]
        max_humidity_value = request.POST["max_humidity_value"]
        min_temprature_value = request.POST["min_temprature_value"]
        max_temprature_value = request.POST["max_temprature_value"]                
        room_reservation_list = request.POST.getlist('selectedRoomValues[]')
        disability_features_value = request.POST.get("disability_features_value", None)
        room_element_list = request.POST.getlist('checkedRoomElementsValues[]')

        date_to_val =None
        date_to_value = str(request.POST["date_to_value"])
        
        if date_to_value:            
            date_to_obj = datetime.strptime(date_to_value, "%Y-%m-%d").date()
            date_to_val = date_to_obj
            
        else: 
            date_to_val=None
        
        date_from_val=None
        date_from_value = str(request.POST["date_from_value"])
        if date_from_value:
            # from_datetime_obj = datetime.strptime(date_from_value, "%Y-%m-%dT%H:%M:%S.%f")
            date_from_obj = datetime.strptime(date_from_value, "%Y-%m-%d").date()
            date_from_val = date_from_obj
        else: 
            date_from_val=None

        print("Date To ->", date_to_val)
        print("Date From ->", date_from_val)
        num_days = (date_to_val - date_from_val).days if date_to_val and date_from_val else None
        print("Num of Days- >", num_days)
        
        # Get guest Information to get religion        
        guest_obj = UserNode.nodes.get(uid=guest_uid)
        religion = guest_obj.religion
        
        religious_book = getReligiousBook(religion)
        
        # Save Pet Information
        if pet_name:
            pet_obj = Pet(
                name = pet_name,
                pet_type = pet_type             
            )

            pet_obj.save()
            pet_guest_connection = pet_obj.guest.connect(guest_obj)

        # format = '%b %d %Y %I:%M%p'
        # date_to_value = datetime.strptime(date_to_value, format)
        # datedate_to_value_from= datetime.strptime(date_to_value, format)

        reservation = Reservation(               
            date_to = date_to_val,
            date_from = date_from_val,            
            religious_book = religious_book,
            min_light = min_light_value,
            max_light = max_light_value,
            min_humidity = min_humidity_value,
            max_humidity = max_humidity_value,
            min_temprature = min_temprature_value,
            max_temprature = max_temprature_value
        )
        reservation.save()

        if pet_name:
            pet_reservation_connection = reservation.pet.connect(pet_obj)

        # Room Details
        for room_id in room_reservation_list:
            room_obj = Room.nodes.get(uid = room_id)
            
            room_connection = reservation.room.connect(room_obj)
            cost_per_night = room_obj.cost_per_night
            total_cost = total_cost+cost_per_night

        # Save Room amount paid in total
        reservation.amount_paid = (total_cost*num_days)
        reservation.save()

        # Room Elements 
        for room_element_id in room_element_list:
            obj = RoomElement.nodes.get(uid = room_element_id)
            room_element_connection = reservation.room_element.connect(obj)
        
        # Room Type
        room_type_obj = RoomType.nodes.get(uid=room_type_value)
        room_type_connection = reservation.room_type.connect(room_type_obj)

        # Guest
        guest_reservation = reservation.guest.connect(guest_obj)

        # Room Scent
        room_scent_obj = RoomScent.nodes.get(uid=room_scent_value)
        room_scent_connection = reservation.room_scent.connect(room_scent_obj)

        # Room View
        room_view_obj = RoomViewPreference.nodes.get(uid=room_view_value)
        room_view_connection = reservation.room_view.connect(room_view_obj)
        
        # Room Access
        # room_access_obj = RoomAccessibility.nodes.get(uid=room_access_value)
        # room_view_connection = reservation.room_access.connect(room_access_obj)        

        print("Saved!")
        context = {
            "response": "Saved Successfully!"
        }

        return JsonResponse(context)
        # url = "/view/guest/bookings/{}".format(guest_uid)
        
        # return redirect(url)
        
def getReligiousBook(religion):
    if str(religion) == "Christian":
        return "BIBLE"
    elif str(religion) == "Islma":
        return "QURAN"
    elif str(religion) == "Hindu":
        return "GUITAR"
    else:
        return "None"

from django.core import serializers
def createGraph(request):
    all_rooms = Room.nodes.all()
    room_response = []
    for room in all_rooms:
        room_obj = {
            'uid': room.uid,
            'floor' : room.floor,
            'hotel' : room.hotel_id,                    
            'availability': room.availability,
            'room_number': room.room_number,
            'room_type' : room.room_type_id,
            'cost_per_night': room.cost_per_night,
            'room_element' : room.room_element_id,                    
        }
        room_response.append(room_obj)
    return render(request, 'room/room_pages/graph_template.html', {'rooms': json.dumps(room_response)})