from django.urls import path
from .views import *
urlpatterns = [
    path('create_photo_form/',create_photo_form, name="create_photo_form"),
    path('add_photo/<int:id>/',create_photos, name="create_photos"),
]
