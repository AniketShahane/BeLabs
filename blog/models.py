from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinLengthValidator
from django.utils import timezone
from time import time
# Create your models here. 

"""
    The blog needs to have: 1. Title, 2. Author Name, 3. Publishing Date, 4. Image, 5. Body, 6. No of likes, 7. No of comments, 8. No. of views, 9. Is published
    Functions: 1. Smaller Body, 2. Pretty Publishing Date, 3. The Number of words in the blog
"""


class Blog(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # This is going to be the user who publishes the blog
    pub_date = models.DateTimeField(default=timezone.now())
    main_image = models.ImageField(
        upload_to='blog-images/', default="/defaults/default_blog_image.jpg")
    body = models.TextField(validators=[MinLengthValidator(30)])
    likes = models.IntegerField(default=1)
    comments = models.IntegerField(default=0)
    views = models.IntegerField(default=1)
    is_published = models.BooleanField(default=True)
    likers = models.TextField(default='', blank=True)
    pre_time = models.FloatField(default=time())

    def words(self):
        return len(self.body.split())

    def pretty_pub(self):
        return self.pub_date.strftime('%b %d, %H:%M')

    def small_body(self):
        if len(self.body) > 80:
            return self.body[:80]+'...'

        else:
            return self.body

    def pretty_date(self):
        return self.pub_date.strftime("%b %d")
