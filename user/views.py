from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from account.models import Posting,likes
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .chatbot import ChatBot
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache


# Create your views here.

def signin_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.error(request,"please Login first")
            return redirect('log')
    return inner
dec=[signin_required,never_cache]

@method_decorator(dec,name="dispatch")
class HomeView(ListView):
    template_name="home.html"
    queryset=Posting.objects.all().order_by('-created_at')
    context_object_name="Posting"

    def get_context_data(self, **kwargs):
        res = super().get_context_data(**kwargs)
        print(res)
        like = likes.objects.filter()
        res['like'] = like
        return res


# class UploadView(TemplateView):
#     template_name="home.html"
    
@method_decorator(dec,name="dispatch")
class UploadView(TemplateView):
    template_name="upload.html"
    def post(self,request):
        user = request.user
        caption = request.POST.get('caption')
        image = request.FILES.get('post_image')
        Posting.objects.create(user = user,image=image,caption=caption)
        return redirect('home')


    # queryset=Userprofile.objects.all()
    # pk_url_kwarg='pid'
    # context_object_name="Userprofile"
        

def add_like(request,*args,**kwargs):
    pid=kwargs.get('pid')
    pro=Posting.objects.get(id=pid)
    likes.objects.create(user=pro)
    return redirect('home')
    


                    
@method_decorator(dec,name="dispatch")
class ChatcenterView(TemplateView):
    template_name="chatcenter.html"

@method_decorator(dec,name="dispatch")
class LeftsideView(TemplateView):
    template_name="leftside.html"

@method_decorator(dec,name="dispatch")
class Schoolhome(TemplateView):
    template_name="schoolhome.html"

@method_decorator(dec,name="dispatch")
class NewsView(TemplateView):
    template_name="news.html"


def chat(request):
    responses = {
        "hi": "Hello!",
        "how are you?": "I'm doing well, thank you.",
        "what's your name?": "I'm a chatbot.",
        "bye": "Goodbye! Have a great day.",
        
    }
    chatbot = ChatBot(responses)
    context = {
        'chatbot': chatbot
    }
    return render(request, 'upload.html', context)

@method_decorator(dec,name="dispatch")
class Aiview(TemplateView):
    template_name="ai.html"

@method_decorator(dec,name="dispatch")          
class DetailView(TemplateView):
    template_name="details.html"


# class ExploreView(TemplateView):
#     template_name="explore.html"

@method_decorator(dec,name="dispatch")
class ExploreView(ListView):
    template_name="explore.html"
    queryset=Posting.objects.all().order_by('-created_at')
    context_object_name="Posting"

@method_decorator(dec,name="dispatch")  
class ProfileView(ListView):
    template_name="profile.html"
    queryset=Posting.objects.all().order_by('-created_at')
    context_object_name='posting'



# comment
from django.shortcuts import render, get_object_or_404
from account.models import Posting, Comment
from account.forms import CommentForm

def post_detail(request, pk):
  post = get_object_or_404(Posting, pk=pk)
  comments = post.comments.all().order_by('-created_at')  # Order comments by creation date (descending)
  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      comment = form.save(commit=False)  # Don't save right away
      comment.post = post  # Assign the comment to the current post
      comment.user = request.user  # Assign the comment to the current logged-in user
      comment.save()
  else:
    form = CommentForm()
  context = {
      'post': post,
      'comments': comments,
      'form': form,
  }
  return render(request, 'template/upload.html', context)
