from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView
from django.views import View
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

class LandingView(TemplateView):
    template_name="landing.html"

class LoginView(View):
    def get(self,request,*args,**kwargs):
        form=LogForm()
        return render(request,"login.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form_data=LogForm(data=request.POST)
        if form_data.is_valid():
                user=form_data.cleaned_data.get('username')
                pswd=form_data.cleaned_data.get('password')
                user=authenticate(request,username=user,password=pswd)
                if user:
                    login(request,user)
                    messages.success(request,"sign in success!!")
                    return redirect('home')
                else:
                    messages.error(request,"invalid username or password")
                    return redirect('log')
        else:
            return render(request,"login.html",{"form":form_data})
        

class RegView(View):
    def get(self,request,*args,**kwargs ):
        form=RegForm()
        return render(request,"reg.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"sign up success!!")
            return redirect('log')
        else:
            return redirect(request,"reg.html",{"form":form_data})


class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')


