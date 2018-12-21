from django import forms
# Create your views here.

class ImageUploadForm(forms.Form):
    image = forms.ImageField()