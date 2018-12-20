from django.db import models
from django.contrib.auth.models import User
from blog.models import Blog
from datetime import datetime
# Create your models here.

class Comment(models.Model):
    comment_text = models.TextField()
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(default=datetime.now())

    def pub_pretty(self):
        return self.pub_time.strftime("%b %e, %Y")
