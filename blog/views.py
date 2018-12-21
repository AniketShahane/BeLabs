from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.models import User
from comment.models import Comment
from .models import Blog
from .forms import ImageUploadForm

def blogs(request):
    blogs_list = Blog.objects.order_by('-pub_date')
    blogs = []
    for blog in blogs_list:
        likers_list = [int(x) for x in blog.likers.split()]
        is_liked = request.user.id in likers_list
        blogs.append({'blog':blog, 'is_liked': is_liked})
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/blogs.html', {'blogs':blogs})

def search(request):
    results = Blog.objects.order_by('-pub_date') # Gets all the objects
    if request.method == "POST":
        # Check to see if title is in the post request that was made
        if 'title' in request.POST:
            title = request.POST['title']
            if title:
                results = results.filter(title__icontains=title)

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
                    for obj in Blog.objects.filter(author_id=d):
                        author_results.append(obj)
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
    list_likers = blog.likers.split()
    likers = [int(x) for x in list_likers]
    is_liked = False
    if request.user.id in likers:
        is_liked = True

    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.order_by('pub_time').filter(blog=blog)
    num_comments = len(comments)

    blog.views += 1 
    blog.save()
    print(blog.views)

    return render(request, 'Blogs-Section/blog.html', {'blog':blog, 'is_liked':is_liked, 'comments':comments, 'num_comments':num_comments})

def liker(request, blog_id):
    if request.user.is_authenticated and request.method=="POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        list_likers = blog.likers.split()
        likers = [int(x) for x in list_likers]
        if request.user.id not in likers:
            blog.likers += str(request.user.id) + ' '
            blog.likes += 1
            blog.save()
        else:
            likers.remove(request.user.id)
            list_likers_intd = [str(x) for x in likers]
            list_likers = " ".join(list_likers_intd)
            blog.likers = list_likers
            blog.likes -= 1
            blog.save()
        return redirect('/blogs/'+str(blog_id))

def liker2(request, blog_id):
    if request.user.is_authenticated and request.method=="POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        list_likers = blog.likers.split()
        likers = [int(x) for x in list_likers]
        if request.user.id not in likers:
            blog.likers += str(request.user.id) + ' '
            blog.likes += 1
            blog.save()
        else:
            likers.remove(request.user.id)
            list_likers_intd = [str(x) for x in likers]
            list_likers = " ".join(list_likers_intd)
            blog.likers = list_likers
            blog.likes -= 1
            blog.save()
        return redirect('blogs')

def addblog(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            blog_title = request.POST['blog_title']
            blog_body = request.POST['blog_body']
            blog_image = form.cleaned_data['image']
            if len(blog_body.split()) > 30:
                new_blog = Blog(title=blog_title, body=blog_body, main_image=blog_image, author=request.user)
                new_blog.save()
            else: 
                print('Minimum 30 words are required')
                return redirect('dashboard')
            return redirect('/blogs/'+str(new_blog.id))
    else: 
        print('Getty')
        return redirect('dashboard')
 
def publishing(request):
     if request.method == "POST":
        checkedboxes = request.POST.getlist('checkboxes')
        print(checkedboxes)
        blogs = Blog.objects.all().filter(author=request.user)
        print(blogs)
        for blog in blogs:
            if str(blog.id) in checkedboxes:
                blog.is_published = True
                blog.save() 
            else: 
                blog.is_published = False 
                blog.save()
        return redirect('dashboard')