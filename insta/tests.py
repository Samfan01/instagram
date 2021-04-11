from django.test import TestCase
from .models import *
from django.contrib.auth.models import User
# Create your tests here.

class ProfileTestClass(TestCase):
    
    from django.contrib.auth.models import User
    '''
    Test case to test instances of the profile class
    '''
    def setUp(self):
        self.user = User(username='samfan')
        self.user.save()
        self.profile = Profile(id=7,user=self.user,profile_pic='url',first_name='Samfan',last_name='Douglas',bio='I am a christian')
        self.profile.save_profile()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.samfan,Profile ))

    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)