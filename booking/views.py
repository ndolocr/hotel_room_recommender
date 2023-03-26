from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime

from user_manager.models import User
from hotel_guest.models import HotelGuest
from user_manager.models import UserManager

from room.models import RoomType
from room.models import RoomLight
from room.models import RoomScent
from room.models import RoomElement
from room.models import RoomHumidity
from room.models import RoomTemprature
from room.models import RoomViewPreference

# Create your views here.
def booking(request):
    context = {}
    return render(request, 'core/booking.html', context=context)

def capture_guest_data(request):
    if request.method == "POST":
        dob = request.POST['dob']+"T00:00:00.000000"
        town = request.POST['town']
        title = request.POST['title']
        gender = request.POST['gender']
        address = request.POST['address']
        religion = request.POST['religion']
        area_code = request.POST['area_code']
        residency = request.POST['residency']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        middle_name = request.POST['middle_name']
        nationality = request.POST['nationality']
        phone_number = request.POST['phone_number']
        email_address = request.POST['email_address']
        marital_status = request.POST['marital_status']
        id_document_type = request.POST['id_document_type']
        id_document_number = request.POST['id_document_number']
        dob = parse_datetime(dob)

        print("Date Of Birt --**-->>", dob)
        try:
            guest = HotelGuest(
                dob = dob,
                town = town,
                title = title,
                gender = gender,
                address = address,
                religion = religion,
                area_code = area_code,
                residency = residency,
                last_name = last_name,
                first_name = first_name,
                middle_name = middle_name,
                nationality = nationality,
                phone_number = phone_number,
                email_address = email_address,
                marital_status = marital_status,
                id_document_type = id_document_type,
                id_document_number = id_document_number,
                created_on = datetime.now(),
            )

            guest.save()

            

            context = {
                "self": "NO",
                "guest_id": guest.uid,
                "guest_email": guest.email,
                "guest_last_name": guest.last_name,
                "guest_first_name": guest.first_name,
            }

            return render(request, 'core/booking_room_information.html', context=context)
        except Exception as e:
            response = {"ERROR": "Error occured while saving guest information- {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return redirect('customer-booking')
    
    
def booking_self(request):
    if request.user.is_authenticated:
        user = request.user
        user_uid = user.uid
        guest = User.nodes.get(uid=user_uid)

        # begin room type
        room_type_response = []
        room_types = RoomType.nodes.all()

        for room_type in room_types:
            room_type_data = {
                "uid" : room_type.uid,
                "name": room_type.name,
                "room_type_uid": room_type.uid,
                "created_on": room_type.created_on,
                "Description": room_type.description,
                "Maximum_Capacity": room_type.max_capacity,
            }

            room_type_response.append(room_type_data)
        # end room type

        # begin room view
        room_view_response = []
        room_views = RoomViewPreference.nodes.all()

        for room_view in room_views:
            room_view_data = {            
                "name": room_view.name,
                "room_view_uid": room_view.uid,
                "description": room_view.description,
            }

            room_view_response.append(room_view_data)
        # end room view

        # begin room elements
        room_elements_response = []
        room_elements = RoomElement.nodes.all()
        
        for room_element in room_elements:
            room_elements_data = {            
                "name": room_element.name,
                "room_element_uid": room_element.uid,
                "description": room_element.description,
                "elementType": room_element.elementType,
            }
            room_elements_response.append(room_elements_data)
        # end room elements

        # begin room temprature range
        room_temprature_response = []
        room_temprature = RoomTemprature.nodes.all()

        for room_temp in room_temprature:
            room_temprature_data = {
                "temp_uid": room_temp.uid,
                "max_temprature": room_temp.max_temprature,
                "min_temprature": room_temp.min_temprature,
            }
            room_temprature_response.append(room_temprature_data)
        # end room temprature range

        # begin room humidity range
        room_humidity_response = []
        room_humidity = RoomHumidity.nodes.all()

        for room_hum in room_humidity:
            room_humidity_data = {
                "temp_uid": room_hum.uid,
                "max_humidity": room_hum.max_humidity,
                "min_humidity": room_hum.min_humidity,
            }
            room_humidity_response.append(room_temprature_data)
        # end room humidity range

        # begin room light range
        room_light_response = []
        room_light = RoomLight.nodes.all()

        for light in room_light:
            room_light_data = {
                "temp_uid": light.uid,
                "max_light": light.max_light,
                "min_light": light.min_light,
            }
            room_light_response.append(room_light_data)
        # end room light range

        # begin room scent range
        room_scent_response = []
        room_scent = RoomScent.nodes.all()

        for scent in room_scent:
            room_scent_data = {
                "scent_uid": scent.uid,
                "scent_name": scent.scent_name,
                "description": scent.description,
            }
            room_scent_response.append(room_scent_data)
        # end room humidity range

        context = {
            "guest": guest,
            "room_view_response": room_view_response,
            "room_type_response": room_type_response,
            "room_light_response": room_light_response,
            "room_scent_response": room_scent_response,
            "room_humidity_response": room_humidity_response,
            "room_elements_response": room_elements_response,
            "room_temprature_response": room_temprature_response,
        }

        return render(request, 'core/booking_room_information.html', context=context) 
    else:
        return redirect('login_user')