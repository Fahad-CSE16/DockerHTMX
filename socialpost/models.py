from django.db import models
from django.contrib.auth.models import User
from PIL import Image
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
    def save( self, *args, **kwargs):
        super(PostPhotos, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size =(300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)