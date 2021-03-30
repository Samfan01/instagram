from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    image = models.ImageField(upload_to = 'insta/')
    post_date = models.DateTimeField(auto_now_add = True)
    
    
    
    def __str__(self):
        return self.image_name
    class Meta:
        ordering = ['image_name']
        
    def save_image(self):
        self.save()
        
    @classmethod
    def get_images(cls):
        images = cls.objects.all()
        return images
    
class Profile(models.Model):
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    bio = models.TextField()