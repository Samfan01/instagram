from django import forms
from .models import Image,Profile

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_name','image_caption','image')
        
        widgets = {
            'image_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'image_caption': forms.Textarea(attrs = {'class': 'form-control'}),
           
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name','last_name','bio','profile_pic')
        
        widgets = {
            'first_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'last_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'bio': forms.Textarea(attrs = {'class': 'form-control'}),
        }