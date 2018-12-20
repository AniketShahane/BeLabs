from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class Goal(models.Model):
    goal = models.CharField(max_length=40)
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now())
