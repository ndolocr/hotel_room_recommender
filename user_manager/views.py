from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == "GET":
        context = {}
        return render(request, 'user_manager/register.html', context = context)
    else:
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
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
