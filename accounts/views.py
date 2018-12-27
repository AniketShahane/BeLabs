from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from blog.models import Blog
from comment.models import Comment
from goal.models import Goal
from message.models import Message
from accounts.models import Profile
# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST['username'].rstrip()
        password = request.POST['password'].rstrip()
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            print('Something is not right')
            return redirect('login')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'Accounts/login.html')


def register(request):
    if request.method == "POST":
        first_name = request.POST['FirstName'].rstrip()
        last_name = request.POST['LastName'].rstrip()
        username = request.POST['username'].rstrip()
        email = request.POST['email'].rstrip()
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if cpassword == password:
            # This means the passwords match now we check if the username is available
            user = User.objects.all().filter(username=username)
            if not user:
                user = User.objects.all().filter(email=email)
                if not user:
                    # We have a perfect registeration scenario
                    u = User.objects.create_user(
                        email=email, username=username, password=password, first_name=first_name, last_name=last_name)
                    u.save()
                    return redirect('login')
                else:
                    print('The email is already registered')
                    return redirect('register')
            else:
                print('The username is not availble')
                return redirect('register')
        else:
            print('passwords dont match')
            return redirect('register')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'Accounts/register.html')


def dashboard(request):
    # Get all the blogs written by the user
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

    blogs = Blog.objects.order_by(
        '-pub_date').filter(author_id=request.user.id)
    sent_messages = Message.objects.order_by(
        '-pre_time').filter(sender=request.user.username)
    received_messages = Message.objects.order_by(
        '-pre_time').filter(receiver=request.user)
    messages = len(sent_messages) + len(received_messages)
    sent_messages_temp = []
    sent_to_id = []

    received_messages_temp = []
    received_from_id = []

    for message in sent_messages:
        if message.receiver.id not in sent_to_id:
            sent_messages_temp.append(message)
            sent_to_id.append(message.receiver.id)
        elif message.receiver.id in sent_to_id and sent_messages_temp[sent_to_id.index(message.receiver.id)].time == message.time:
            index = sent_to_id.index(message.receiver.id)
            sent_messages_temp[index] = message

    for message in received_messages:
        user = User.objects.get(username=message.sender)
        if user.id not in received_from_id:
            received_messages_temp.append(message)
            received_from_id.append(user.id)
        elif user.id in received_from_id and received_messages_temp[received_from_id.index(user.id)].time == message.time:
            index = received_from_id.index(user.id)
            received_messages_temp[index] = message

    received_messages = received_messages_temp
    sent_messages = sent_messages_temp

    s = 0
    r = 0

    final_messages = []

    while s < len(sent_messages) and r < len(received_messages):
        if sent_messages[s].pre_time > received_messages[r].pre_time:
            final_messages.append(
                {'message': sent_messages[s], 'is_sent': True})
            s += 1
        else:
            sender = User.objects.get(username=received_messages[r].sender)
            sender_ID = sender.id
            final_messages.append(
                {'message': received_messages[r], 'is_sent': False, 'sender_ID': sender_ID})
            r += 1
    while s < len(sent_messages):
        final_messages.append({'message': sent_messages[s], 'is_sent': True})
        s += 1
    while r < len(received_messages):
        sender = User.objects.get(username=received_messages[r].sender)
        sender_ID = sender.id
        final_messages.append(
            {'message': received_messages[r], 'is_sent': False, 'sender_ID': sender_ID})
        r += 1

    likes = 0
    comments = 0
    no_blogs = len(blogs)
    views = 0
    words = 0
    for blog in blogs:
        likes += blog.likes
        words += len(blog.body.split())
        comments += len(Comment.objects.all().filter(blog=blog))
        views += blog.views

    goals = Goal.objects.order_by('-time').filter(writer=request.user)
    content = {
        'likes': likes,
        'words': words,
        'comments': comments,
        'no_blogs': no_blogs,
        'messages': messages,
        'blogs': blogs,
        'goals': goals,
        'views': views,
        'final_messages': final_messages,
        'profile': profile,
        'pinterests': pinterests
    }
    return render(request, 'Dashboard/dashboard.html', content)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('main')
