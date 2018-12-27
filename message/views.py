from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message
from accounts.models import Profile
# Create your views here.


def message(request, receiver_id):
    # Profile Information
    profile = Profile.objects.get(user=request.user)
    pinterests = ''
    interest = profile.interests.strip().split(';')
    print(interest)
    interest = list(filter(lambda a: a != '', interest))
    print(interest)
    for word in interest:
        if interest.index(word) < len(interest) - 2:
            pinterests += word + ', '
        elif interest.index(word) == len(interest) - 2:
            pinterests += word + ' '
        elif interest.index(word) == len(interest) - 1:
            pinterests += 'and ' + word

    chatter = User.objects.get(id=receiver_id)
    cprofile = Profile.objects.get(user=chatter)
    cpinterests = ''
    cinterest = cprofile.interests.strip().split(';')
    print(interest)
    cinterest = list(filter(lambda a: a != '', cinterest))
    print(interest)
    for word in cinterest:
        if cinterest.index(word) < len(cinterest) - 2:
            cpinterests += word + ', '
        elif cinterest.index(word) == len(cinterest) - 2:
            cpinterests += word + ' '
        elif cinterest.index(word) == len(cinterest) - 1:
            cpinterests += 'and ' + word

    receiver = User.objects.get(id=receiver_id)
    print(receiver)
    sent_messages = Message.objects.order_by('time').filter(
        sender=request.user.username, receiver=receiver)
    sender = User.objects.get(id=receiver_id)
    print(sender)
    received_messages = Message.objects.order_by('time').filter(
        sender=sender.username, receiver=request.user)

    print(sent_messages)
    print(received_messages)
    print(Message.objects.all())

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

    print(messages)
    return render(request, 'Dashboard/messages.html', {'messages': messages, 'receiver': receiver, 'pinterests': pinterests, 'profile': profile, 'cprofile': cprofile, 'cinterest': cpinterests})


def sendmsg(request):
    if request.method == 'POST':
        receiver_username = request.POST['username']
        message_text = request.POST['text_message']
        user = User.objects.get(username=receiver_username)
        if user is not None:
            new_message = Message(
                receiver=user, sender=request.user.username, message_text=message_text)
            new_message.save()
            return redirect('/messages/' + str(user.id))
            # Make some changes so that the user is redirected to messages page
        else:
            print('Something went wrong')
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
