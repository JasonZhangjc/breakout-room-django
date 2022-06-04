from django.shortcuts import render
from .models import BreakoutModel

# Create your views here.
def homepageview(request):
    return render(request, 'index.html')

def roomview(request):
    room_number = request.POST['room_number']
    user_name = request.POST['user_name']
    messages = []
    for eachobj in BreakoutModel.objects.filter(room_number = room_number):
        messages.append(eachobj.message)

    return render(request, 'room.html', {'room_number':room_number, 'user_name':user_name, 'messages': messages})
