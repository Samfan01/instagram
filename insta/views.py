from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import ImageForm,ProfileForm,CommentForm
from .models import Image,Profile,Comment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.http import HttpResponseRedirect


# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    
    title = 'My Own Instagram'
    users = User.objects.all()
    profiles = Profile.objects.all()
    images = Image.get_images()
    all_comments = Comment.get_comments()
    template_name='home.html'
    return render(request,template_name,{'title':title,'images':images,'all_comments':all_comments,'users':users,'profiles':profiles})

def Comments(request, image_id):
    form = CommentForm
    image = get_object_or_404(Image, id = image_id)
    current_user = request.user
    image_comments = Comment.objects.filter(image=image_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.commenter = current_user
            comment.save()
            return redirect('home')
        else:
            form = CommentForm()
            
    return render(request,'comment.html',{'image':image,'form':form,'image_comments':image_comments})
    
def Likes(request,pk):
    image = get_object_or_404(Image,id=request.POST.get('image_id'))
    image.likes = image.likes + 1
    image.save()
    return HttpResponseRedirect(reverse('home')) 

def new_post(request):
    model = Image
    form = ImageForm
    template_name = 'new_post.html',
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user.profile
            form.save()
        return redirect('home')
    else:
        
    
        return render(request,template_name,{'form':form})

def profile(request):
    template_name = 'profile.html'
    images = request.user.profile.image.all()
    
    
    return render(request,template_name,{'images':images})

def update_profile(request):
    model = Profile
    form = ProfileForm
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            post = form.save(commit=False)      
            post.save()
        return redirect('profile')
    else:
        form = ProfileForm
   
    template_name = 'update_profile.html',
    
    return render(request,template_name,{'form':form})



















 # import pdb;pdb.set_trace()