from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Blog
from .models import Comment
# Create your views here.
def comment(request, blog_id):
    if request.method == "POST":
        comment = request.POST['comment']
        user = User.objects.get(id=request.user.id)
        blog = Blog.objects.get(id=blog_id)
        new_comment = Comment(comment_text=comment, writer=user, blog=blog)
        new_comment.save()
        return redirect('/blogs/' + str(blog_id))
