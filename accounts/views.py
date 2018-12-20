from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from blog.models import Blog
from comment.models import Comment
# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
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
        first_name = request.POST['FirstName']
        last_name = request.POST['LastName']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if cpassword == password:
            #This means the passwords match now we check if the username is available
            user = User.objects.all().filter(username=username)
            if not user:
                user = User.objects.all().filter(email=email)
                if not user:
                    #We have a perfect registeration scenario
                    u = User.objects.create_user(email=email, username=username, password=password,first_name=first_name, last_name=last_name)
                    u.save()
                    return redirect('dashboard')
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
    blogs = Blog.objects.order_by('-pub_date').filter(author_id=request.user.id)
    likes = 0
    comments = 0
    no_blogs = len(blogs)
    # views = 0
    words = 0
    # messages = 0
    for blog in blogs:
        likes += blog.likes
        words += len(blog.body.split())
        comments += len(Comment.objects.all().filter(blog=blog))
    content = {
        'likes':likes,
        'words':words,
        'comments':comments,
        'no_blogs':no_blogs,
        'blogs':blogs
    }
    return render(request, 'Dashboard/dashboard.html', content)


def logout(request):
    if request.method == "POST":
        auth.logout(request)
        return redirect('main')
