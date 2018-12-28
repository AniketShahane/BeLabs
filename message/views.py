from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Message
from accounts.models import Profile
from django.contrib import messages
# Create your views here.


def message(request, receiver_id):
    content = {}
    try:
        # Profile Information
        profile = Profile.objects.get(user=request.user)
        pinterests = ''
        interest = profile.interests.strip().split(';')
        interest = list(filter(lambda a: a != '', interest))
        for word in interest:
            if interest.index(word) < len(interest) - 2:
                pinterests += word + ', '
            elif interest.index(word) == len(interest) - 2:
                pinterests += word + ' '
            elif interest.index(word) == len(interest) - 1:
                pinterests += 'and ' + word
        profile_content1 = {'profile': profile, 'pinterests': pinterests}
        content.update(profile_content1)
    except:
        pass

    try:
        chatter = User.objects.get(id=receiver_id)
        cprofile = Profile.objects.get(user=chatter)
        cpinterests = ''
        cinterest = cprofile.interests.strip().split(';')
        cinterest = list(filter(lambda a: a != '', cinterest))
        for word in cinterest:
            if cinterest.index(word) < len(cinterest) - 2:
                cpinterests += word + ', '
            elif cinterest.index(word) == len(cinterest) - 2:
                cpinterests += word + ' '
            elif cinterest.index(word) == len(cinterest) - 1:
                cpinterests += 'and ' + word

        profile_content2 = {'cprofile': cprofile, 'cinterest': cpinterests}
        content.update(profile_content2)
    except:
        pass

    receiver = User.objects.get(id=receiver_id)
    sent_messages = Message.objects.order_by('time').filter(
        sender=request.user.username, receiver=receiver)
    sender = User.objects.get(id=receiver_id)
    received_messages = Message.objects.order_by('time').filter(
        sender=sender.username, receiver=request.user)

    s = 0
    r = 0

    messages = []

    while s < len(sent_messages) and r < len(received_messages):
        if sent_messages[s].time < received_messages[r].time:
            messages.append({'message': sent_messages[s], 'is_sent': True})
            s += 1
        else:
            received_messages[r].is_read = True
            received_messages[r].save()
            messages.append(
                {'message': received_messages[r], 'is_sent': False})
            r += 1
    while s < len(sent_messages):
        messages.append({'message': sent_messages[s], 'is_sent': True})
        s += 1
    while r < len(received_messages):
        received_messages[r].is_read = True
        received_messages[r].save()
        messages.append({'message': received_messages[r], 'is_sent': False, })
        r += 1
    messages_content = {'messages': messages, 'receiver': receiver}
    content.update(messages_content)

    return render(request, 'Dashboard/messages.html', content)


def sendmsg(request):
    if request.method == 'POST':
        receiver_username = request.POST['username']
        message_text = request.POST['text_message']
        try:
            user = User.objects.get(username=receiver_username)
            new_message = Message(
                receiver=user, sender=request.user.username, message_text=message_text)
            new_message.save()
            return redirect('/messages/' + str(user.id))
            # Make some changes so that the user is redirected to messages page
        except:
            messages.error(request, 'No user with that username exists...')
            return redirect('dashboard')


def sendmsg2(request, receiver_id):
    if request.method == 'POST':
        message_text = request.POST['text_message']
        user = User.objects.get(id=receiver_id)
        if user is not None:
            new_message = Message(
                receiver=user, sender=request.user.username, message_text=message_text)
            new_message.save()
            return redirect('/messages/' + str(user.id))
            # Make some changes so that the user is redirected to messages page
