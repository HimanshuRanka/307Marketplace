from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def chat_index(request):
    return render(request, 'chat/index.html', {})

@login_required
def chat_room(request, room_name=None):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })
