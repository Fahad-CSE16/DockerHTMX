from django.urls import path
from .views import *
urlpatterns = [
    path('create_photo_form/',create_photo_form, name="create_photo_form"),
    path('add_photo/<int:id>/',create_photos, name="create_photos"),
    path('detail_photo/<int:id>/',detail_photo, name="detail_photo"),
    path('delete_photo/<int:id>/',delete_photo, name="delete_photo"),
    path('update_photo/<int:id>/',update_photo, name="update_photo"),
]
