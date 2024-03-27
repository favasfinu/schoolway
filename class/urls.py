from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('python',PythonView.as_view(),name="python"),
    path('kg1',kg1View.as_view(),name="kg1"),
    path('learn_alphabet', views.learn_alphabet, name='learn_alphabet'),
    path('one',oneView.as_view(),name="one"),
    path('two',twoView.as_view(),name="two"), 
    path('three',ThreeView.as_view(),name="three"),
    path('four',FourView.as_view(),name="four"),
    path('five',FiveView.as_view(),name="five"),

]
