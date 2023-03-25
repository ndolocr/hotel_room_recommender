from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime

from user_manager.models import User
from hotel_guest.models import HotelGuest
from user_manager.models import UserManager

from room.models import RoomType
from room.models import RoomElement

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
    user = request.user
    user_uid = user.uid
    guest = User.nodes.get(uid=user_uid)

    # begin room type
    room_type_response = []
    room_types = RoomType.nodes.all()

    for room_type in room_types:
        room_type_data = {
            "uid" : room_type.uid,
            "Name": room_type.name,
            "Maximum_Capacity": room_type.max_capacity,
            "created_on": room_type.created_on,
            "Description": room_type.description,
        }

        room_type_response.append(room_type_data)
    # end room type

    # begin room elements
    room_elements_response = []
    room_elements = RoomElement.nodes.all()
    
    for room_element in room_elements:
        room_elements_data = {
            "name": room_element.name,
            "description": room_element.description,
            "elementType": room_element.elementType,
        }
        room_elements_response.append(room_elements_data)
    # end room elements

    context = {
        "guest_id": guest.uid,
        "guest_email": guest.email,
        "guest_last_name": guest.last_name,        
        "guest_first_name": guest.first_name,
        "room_type_response": room_type_response,
        "room_elements_response": room_elements_response,
    }

    return render(request, 'core/booking_room_information.html', context=context)