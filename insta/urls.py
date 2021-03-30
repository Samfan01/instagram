from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name = 'home'),
    path('new_post',views.new_post,name = 'new_post'),
    path('profile',views.profile,name = 'profile'),
    path('update_profile',views.update_profile,name = 'update_profile'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)