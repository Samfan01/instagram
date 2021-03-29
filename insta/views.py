from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm
from .models import Image

# Create your views here.
def home(request):
    template_name='home.html',
    title = 'My Own Instagram'
    images = Image.get_images()
    return render(request,template_name,{'title':title},{'images':images})

def new_post(request):
    model = Image
    form = ImageForm
    template_name = 'new_post.html',
    
    return render(request,template_name,{'form':form})