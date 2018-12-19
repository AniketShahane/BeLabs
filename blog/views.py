from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.models import User
# Create your views here.


def blogs(request):
    blogs = Blog.objects.all()
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/blogs.html', {'blogs':blogs})

def search(request):
    results = Blog.objects.all() # Gets all the objects
    if request.method == "POST":
        # Check to see if title is in the post request that was made
        if 'title' in request.POST:
            title = request.POST['title']
            if title:
                results = results.filter(title__iexact=title)

        if 'keywords' in request.POST:
            keywords = request.POST['keywords']
            if keywords:
                results = results.filter(body__icontains=keywords)
        #
        if 'author-name' in request.POST:
            author = request.POST['author-name']
            if author:
                first_name = User.objects.all().filter(first_name__iexact=author)
                last_name = User.objects.all().filter(last_name__iexact=author)
                id = []
                for obj in first_name:
                    if obj.id not in id:
                        id.append(obj.id)
                for obj in last_name:
                    if obj.id not in id:
                        id.append(obj.id)
                author_results = []
                for d in id:
                    author_results.append(Blog.objects.get(author_id=d))
                results_temp = []
                for result in author_results:
                    if result in results:
                        results_temp.append(result)
                results = results_temp

        return render(request, 'Blogs-Section/search.html', {'results': results})
    else:
        return render(request, 'Blogs-Section/search.html', {'results': results})

def blog(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    # blog = Blog.objects.get(id=blog_id)
    return render(request, 'Blogs-Section/blog.html', {'blog':blog})
