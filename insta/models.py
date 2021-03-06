from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    profile_pic = models.ImageField(upload_to = 'profile/',null=True,blank=True,default='download.jpeg')
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    bio = models.TextField()
    following = models.ManyToManyField(User,related_name='following',blank=True)
    
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
        return self.user.username
    
    class Meta:
        ordering = ['first_name']
        
    def save_profile(self):
        self.save()
        
    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles





class Image(models.Model):
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='image')
    image_name = models.CharField(max_length = 60)
    image_caption = models.TextField()
    image = models.ImageField(upload_to = 'insta/')
    post_date = models.DateTimeField(auto_now_add = True)
    likes = models.PositiveIntegerField(default=0)
    
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
    
      
    def likes_count(self):
        total_likes = self.likes.count()
        return total_likes
    
class Comment(models.Model):
    comment = models.TextField()
    image = models.ForeignKey(Image,on_delete=models.CASCADE)
    date_posted = models.DateTimeField(auto_now_add=True, null=True)
    commenter = models.ForeignKey(User,on_delete=models.CASCADE)
    
    class Meta:
        ordering = ['comment']
        
    def __str__(self):
        return self.comment
    
    def save_comment(self):
        self.save()
         
        
    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments
