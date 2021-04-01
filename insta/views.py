from django.shortcuts import render
from django.http import HttpResponse
from .forms import ImageForm,ProfileForm
from .models import Image,Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
   
    title = 'My Own Instagram'
    images = Image.get_images()
    template_name='home.html'
    return render(request,template_name,{'title':title,'images':images})

def new_post(request):
    model = Image
    form = ImageForm
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    template_name = 'new_post.html',
    
    return render(request,template_name,{'form':form})

def profile(request):
    template_name = 'profile.html'
    images = Image.objects.filter(id)
    
    return render(request,template_name,{'images':images})

def update_profile(request):
    model = Profile
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            post = form.save(commit=False)      
            post.save()
    else:
        form = ProfileForm
   
    template_name = 'update_profile.html',
    
    return render(request,template_name,{'form':form})



















 # import pdb;pdb.set_trace()