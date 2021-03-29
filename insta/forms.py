from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image_name','image_caption','image')
        
        widgets = {
            'image_name': forms.TextInput(attrs = {'class': 'form-control'}),
            'image_caption': forms.Textarea(attrs = {'class': 'form-control'}),
            
        }
        