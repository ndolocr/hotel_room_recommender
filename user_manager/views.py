from django.shortcuts import render

# Create your views here.
def register(request):
    if request.method == "GET":
        context = {}
        return render(request, 'user_manager/register.html', context = context)
    else:
        pass
