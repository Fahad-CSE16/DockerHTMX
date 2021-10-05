from django import forms
from django.db.models import fields
from .models import *

# class PostPhotosForm(forms.ModelForm):
#     class Meta:
#         model = PostPhotos
#         # fields = (
#         #     'image',
#         # )
#         # exclude=['post']
#         fields=['image',]
class PostPhotosForm(forms.ModelForm):
    class Meta:
        model = PostPhotos
        fields = ['image']