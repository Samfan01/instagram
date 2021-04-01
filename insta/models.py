from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist 

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
    
    @classmethod
    def get_user_images(cls,id):
        images = cls.objects.filter(id)
        return images
    
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile',null=True)
    profile_pic = models.ImageField(upload_to = 'profile/',null=True,blank=True,default='download.jpeg')
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    bio = models.TextField()
    
    @receiver(post_save, sender=User)
    def user_profile(sender,instance,created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)
            
    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        instance.profile.save()
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ['first_name']
        
    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles