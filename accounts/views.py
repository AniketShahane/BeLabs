from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from blog.models import Blog
from comment.models import Comment
from goal.models import Goal
from message.models import Message
from accounts.models import Profile
from .forms import ImageUploadForm
from django.contrib import messages
from django.core.mail import send_mail
from validate_email import validate_email
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
            messages.error(request, 'Invalid Credentials')
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
            try:
                is_valid = validate_email(email, verify=True)
                if is_valid is None:
                    messages.error(request,'Enter an email that really exists')
                    return redirect('register')
            except: 
                messages.error(request, 'Enter a Valid Email Address')
                return redirect('register')
            user = User.objects.all().filter(username=username)
            if not user:
                user = User.objects.all().filter(email=email)
                if not user:
                    # We have a perfect registeration scenario
                    u = User.objects.create_user(email=email, username=username, password=password, first_name=first_name, last_name=last_name)
                    u.save()

                    # Simultaneously also creating a profile for the person so that we don't get any errors
                    profile_newUser = Profile(user=u)
                    profile_newUser.save()

                    # Send and email to the person 
                    send_mail(
                        subject='Successful Registration',
                        message=f"Thankyou {first_name} for registering with us here at BeLabs. Your username is {username}. We hope to see some great content that you put out...Have a great day!!",
                        from_email='belabs.help.00@gmail.com',
                        recipient_list=[email, 'theflash.299792458@gmail.com']
                    )

                    messages.success(request, 'You\'ve been successfully registered. Login to continue...')
                    return redirect('login')
                else:
                    messages.error(
                        request, 'Email Id already used for registration')
                    return redirect('register')
            else:
                messages.error(request, 'Username already taken')
                return redirect('register')
        else:
            messages.error(request, 'Passwords don\'t match')
            return redirect('register')
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'Accounts/register.html')


def dashboard(request):
    # Get all the blogs written by the user
    content = {}
    try:
        profile = Profile.objects.get(user=request.user)
        pinterests = ''
        interest = profile.interests.strip().split(';')
        # print(interest)
        interest = list(filter(lambda a: a != '', interest))
        # print(interest)
        for word in interest:
            if interest.index(word) < len(interest) - 2:
                pinterests += word + ', '
            elif interest[-2] == word:
                pinterests += word + ' '
            elif interest[-1] == word:
                pinterests += 'and ' + word
        profile_content = {'profile': profile, 'pinterests': pinterests}
        content.update(profile_content)
    except:
        pass

    blogs = Blog.objects.order_by('-pub_date').filter(author_id=request.user.id)
    sent_messages = Message.objects.order_by('-time').filter(sender=request.user.username)
    received_messages = Message.objects.order_by('-time').filter(receiver=request.user)
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
        if sent_messages[s].time > received_messages[r].time:
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
    person_content = {
        'likes': likes,
        'words': words,
        'comments': comments,
        'no_blogs': no_blogs,
        'num_messages': messages,
        'blogs': blogs,
        'goals': goals,
        'views': views,
        'final_messages': final_messages,
    }
    content.update(person_content)
    return render(request, 'Dashboard/dashboard.html', content)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('main')


def update_profile(request):
    if request.method == "POST":
        user = User.objects.get(id=request.user.id)
        try:
            profile_user = Profile.objects.get(user=request.user)
        except:
            profile_user = Profile()
        bio = request.POST['edit_bio']
        interest = request.POST['edit_interests']
        email = request.POST['edit_email']
        github = request.POST['edit_github']
        linkedin = request.POST['edit_linkedin']
        if 'picture' in request.FILES:
            if request.FILES['picture']:
                profile_picture = request.FILES['picture']
                profile_user.picture = profile_picture
            else:
                pass
        profile_user.bio = bio
        if len(bio) > 140:
            messages.error(request, 'Your bio cant contain more than 140 characters')
            return redirect('dashboard')
        profile_user.interests = interest
        profile_user.github = github
        profile_user.linkedIn = linkedin
        user.email = email
        user.save()
        profile_user.user = user
        profile_user.save()
        return redirect('dashboard')
