from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/blogs.html', {'blogs':blogs})

def search(request):
    content = {'results': [x for x in range(3)]}
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/search.html', content)

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # blog = Blog.objects.get(id=blog_id)
    return render(request, 'Blogs-Section/blog.html', {'blog':blog})
