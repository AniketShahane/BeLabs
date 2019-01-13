from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
import time as tm
# Create your models here.


class Message(models.Model):
    message_text = models.TextField()
    sender = models.CharField(max_length=30)
    # Sender variable stores the username of the user
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)
    # Receiver variable also stores the username of the user
    time = models.DateTimeField(default=timezone.now())
    is_read = models.BooleanField(default=False)

    def small_message(self):
        if len(self.message_text) > 22:
            return self.message_text[:22] + '...'
        else:
            return self.message_text

    def pretty_time(self):
        return self.time.strftime("%b %d, %H:%M")
