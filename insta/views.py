from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    template_name='home.html',
    title = 'My Own Instagram'
    
    return render(request,template_name,{'title':title})

def add_post(request):
    template_name = 'add_post.html',
    
    return render = (request,template_name)