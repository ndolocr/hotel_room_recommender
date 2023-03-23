from datetime import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime

from hotel_guest.models import HotelGuest

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
                "guest_id": guest.uid,
                "guest_last_name": guest.last_name,
                "guest_email": guest.email_address,
                "guest_first_name": guest.first_name,
            }

            return render(request, 'core/booking_room_information.html', context=context)
        except Exception as e:
            response = {"ERROR": "Error occured while saving guest information- {}".format(e)}
            return JsonResponse(response, safe=False)
    else:
        return redirect('customer-booking')
        
        