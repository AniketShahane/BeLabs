from django import forms
from django.forms import ModelForm
from .models import Blog
# Create your views here.


class ImageUploadForm(forms.Form):
    image = forms.ImageField()


# class PostForm(ModelForm):
#     class Meta:
#         model = Blog
#         fields = ['body']
