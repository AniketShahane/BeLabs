from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
# Create your models here.


class Profile(models.Model):
    # The user needs to have a bio, profile picture, Interests, Github information and LinkedIn
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(validators=[MaxLengthValidator(140)])
    picture = models.ImageField(
        upload_to="profile-pictures/", default="/defaults/defaul.png")
    interests = models.TextField()
    github = models.CharField(max_length=100)
    linkedIn = models.CharField(max_length=100)
    is_bom = models.BooleanField(default=False)
 