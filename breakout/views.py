from django.shortcuts import render


# Create your views here.
def homepageview(request):
    return render(request, 'index.html')

def roomview(request):
    room_number = request.POST['room_number']
    user_name = request.POST['user_name']
    return render(request, 'room.html', {'room_number':room_number, 'user_name':user_name})
    