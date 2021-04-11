from django.test import TestCase
from .models import *
# Create your tests here.

class ProfileTestClass(TestCase):
    '''
    Test case to test instances of the profile class
    '''
    def setUp(self):
        self.samfan = Profile(profile_pic='url',first_name='Samfan',last_name='Douglas',bio='I am a christian')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.samfan,Profile ))
