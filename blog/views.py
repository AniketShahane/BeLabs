from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.contrib.auth.models import User
from comment.models import Comment
from .models import Blog
from .forms import ImageUploadForm
from accounts.models import Profile
from django.contrib import messages


def blogs(request):
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
        profile_content = {'pinterests': pinterests, 'profile': profile}
        content.update(profile_content)
    except:
        pass
    blogs_list = Blog.objects.order_by('-pub_date')
    blogs = []
    for blog in blogs_list:
        likers_list = [int(x) for x in blog.likers.split()]
        is_liked = request.user.id in likers_list
        blogs.append({'blog': blog, 'is_liked': is_liked})
    blog_content_dict = {'blogs': blogs}
    content.update(blog_content_dict)
    # This is a temporary fix for the blogs section. Later use database
    return render(request, 'Blogs-Section/blogs.html', content)


def search(request):
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
        profile_content = {'profile': profile, 'pinterests': pinterests}
        content.update(profile_content)
    except:
        pass

    results = Blog.objects.order_by('-pub_date')  # Gets all the objects
    if request.method == "GET":
        # Check to see if title is in the post request that was made
        if 'title' in request.GET:
            title = request.GET['title'].rstrip()
            if title:
                results = results.filter(title__icontains=title)
        else:
            title = None

        if 'keywords' in request.GET:
            keywords = request.GET['keywords'].rstrip()
            if keywords:
                results = results.filter(body__icontains=keywords)
        else:
            keywords = None
        #
        if 'authorname' in request.GET:
            author = request.GET['authorname'].rstrip()
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
        else:
            author = None

        results_content = {'results': results, 'keywords': keywords,
                           'authorname': author, 'title': title, 'values': request.GET.values}
        content.update(results_content)
        return render(request, 'Blogs-Section/search.html', content)
    # else:
    #     return render(request, 'Blogs-Section/search.html', {'results': results, 'pinterests': pinterests, 'profile': profile})


def blog(request, blog_id):
    content = {}
    blog = get_object_or_404(Blog, pk=blog_id)
    list_likers = blog.likers.split()
    likers = [int(x) for x in list_likers]
    is_liked = False
    if request.user.id in likers:
        is_liked = True
    blogger = blog.author
    try:
        # Profile Information
        profile = Profile.objects.get(user=blogger)
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
        profile_content = {'profile': profile, 'pinterests': pinterests}
        content.update(profile_content)
    except:
        pass

    blog = Blog.objects.get(id=blog_id)
    comments = Comment.objects.order_by('pub_time').filter(blog=blog)
    comments_and_poster = []
    for comment in comments:
        has_profile = False
        try:
            profile_user = Profile.objects.get(user=comment.writer)
            has_profile = True
            comments_and_poster.append(
                {'comment': comment, 'profile': profile_user, 'has_profile': has_profile})
        except:
            comments_and_poster.append(
                {'comment': comment, 'poster': comment.writer, 'has_profile': has_profile})
    num_comments = len(comments)
    num_views = blog.views

    blog.views += 1
    blog.save()
    blog_content_dict = {'blog': blog, 'is_liked': is_liked,
                         'comments': comments_and_poster, 'num_comments': num_comments, 'num_views': num_views}
    content.update(blog_content_dict)
    return render(request, 'Blogs-Section/blog.html', content)


def liker(request, blog_id):
    if request.user.is_authenticated and request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        list_likers = blog.likers.split()
        likers = [int(x) for x in list_likers]
        if request.user.id not in likers:
            blog.likers += ' ' + str(request.user.id) + ' '
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
    if request.user.is_authenticated and request.method == "POST":
        blog = get_object_or_404(Blog, pk=blog_id)
        list_likers = blog.likers.split()
        likers = [int(x) for x in list_likers]
        if request.user.id not in likers:
            blog.likers += ' ' + str(request.user.id) + ' '
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
        # form = ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        blog_title = request.POST['blog_title'].rstrip()
        blog_body = request.POST['blog_body'].rstrip()
        if 'image' in request.FILES:
            blog_image = request.FILES['image']
        if len(blog_body.split()) > 30:
            new_blog = Blog(title=blog_title, body=blog_body,
                            main_image=blog_image, author=request.user)
            new_blog.save()
            return redirect('/blogs/'+str(new_blog.id))
        else:
            messages.error(
                request, 'Minimum 30 words are required to post a blog...')
            return redirect('dashboard')


def publishing(request):
    if request.method == "POST":
        checkedboxes = request.POST.getlist('checkboxes')
        blogs = Blog.objects.all().filter(author=request.user)
        for blog in blogs:
            if str(blog.id) in checkedboxes:
                blog.is_published = True
                blog.save()
            else:
                blog.is_published = False
                blog.save()
        return redirect('dashboard')


def redirectBlog(request, blogWriter):
    return redirect('/blogs/search/?authorname=' + blogWriter)
