from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title=models.CharField(max_length=100)
    text=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.title
class PostPhotos(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, related_name='photos')
    image=models.ImageField(upload_to='socialpost/postPhotos')
