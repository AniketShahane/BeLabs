from django.shortcuts import render

# Create your views here.


def blogs(request):
    content = {'blogs': [x for x in range(6)]}
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/blogs.html', content)

def search(request):
    content = {'results': [x for x in range(3)]}
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/search.html', content)
