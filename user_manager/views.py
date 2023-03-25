from datetime import datetime
from django.contrib import messages
from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import redirect
from django.utils.dateparse import parse_datetime
from django.contrib.auth import authenticate, login, logout

from user_manager.models import User
from user_manager.models import UserManager


# Create your views here.
def register(request):
    if request.method == "GET":
        context = {}
        return render(request, 'user_manager/register.html', context = context)
    else:
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:

            try:
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

                user = User(
                    dob = dob,
                    town = town,
                    title = title,
                    gender = gender,
                    address = address,
                    password = password,
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

                user.save()

                user_manager = UserManager.objects.create(
                    dob = dob,
                    town = town,
                    title = title,
                    uid = user.uid,
                    gender = gender,
                    address = address,
                    password = password,
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
                    is_active = True                    
                )

                context = {
                    "message": "User successfully Registered",
                }

                return redirect('home-page')
            except Exception as e:
                response = {"ERROR": "Error while registering new user - {}".format(e)}
                return JsonResponse(response)
    
def login_user(request):
    if request.method == "GET":
        return render(request, 'user_manager/login.html')
    elif request.method == "POST":
        password = request.POST["password"]
        email = request.POST["email_address"]
        user = authenticate(request, email = email, password = password)
        
        if user is not None:
            print("User found->", user)
            login(request, user)
            return redirect('home-page')
        else:
            messages.success(request, ("Invalid Email address or Password. Please try again!"))
            return redirect('login_user')

def logout_user(request):
    logout(request)
    messages.success(request, ("User successfully logged out!"))
    return redirect('home-page')