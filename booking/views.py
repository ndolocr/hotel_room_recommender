from django.shortcuts import render

# Create your views here.
def booking(request):
    context = {}
    return render(request, 'core/booking.html', context=context)