from django.urls import path
from .views import *
from . import views



urlpatterns = [
    path('home',HomeView.as_view(),name="home"),
    path('upload',UploadView.as_view(),name="upload"),
    path('profile',ProfileView.as_view(),name='profile'),
    path('like<pid>',add_like,name="likes"),
    path('chatcenter',ChatcenterView.as_view(),name="chatcenter"),
    path('leftside',LeftsideView.as_view(),name="leftside"),
    path('schoolhome',Schoolhome.as_view(),name='schoolhome'),
    path('news',NewsView.as_view(),name="news"),
    # path('upload', views.chat, name='chat'),
    path('ai',Aiview.as_view(),name="ai"),
    path('details',DetailView.as_view(),name="details"),
    path('explore',ExploreView.as_view(),name="explore")
 
]