from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Channel, Message
from django.contrib.auth.models import User
from django.utils import timezone

def index(request):
    return HttpResponse("Hello World")

def channel_list(request):
    channels = Channel.objects.all()
    return render(request, 'chatroom/channel_list.html', {'channels': channels})

def channel_message(request, channel_id):
    try:
        channel = Channel.objects.get(id=channel_id)
        channel_name = channel.name
    except Channel.DoesNotExist:
        channel_name = "Channel not found"
    messages = Message.objects.filter(channel=channel) # Adjust based on your field name

    if request.method == 'POST':
        message_content = request.POST.get('message_content')
        user = request.user  # Or a specific user if you're not using authentication
        if message_content:  # Make sure the message is not empty
            new_message = Message(content=message_content, user=user, channel=channel, timestamp=timezone.now())
            new_message.save()
            return redirect('chatroom:channel_message', channel_id=channel_id)

    return render(request, 'chatroom/channel_message.html', {
        'current_channel': channel,
        'messages': messages,
        'channels': Channel.objects.all(),  # Assuming you want to list all channels
    })