from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'core/index.html', context=context)

def dashboard(request):
    context = {}
    return render(request, 'core/dashboard.html', context=context)
