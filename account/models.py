from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime


# Create your models here.

class Userprofile(models.Model):
    name=models.CharField(max_length=100)
    bio=models.CharField(max_length=500)
    image=models.ImageField(upload_to="user_images")
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.name



class Posting(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user =models.CharField(max_length=100)
    image = models.ImageField(upload_to='post_images')
    
    caption = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__ (self):
        return self.user
    

class likes(models.Model):
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    user = models.ForeignKey(Posting, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100, default="liked")

    def number_of_likes(self):
        return self.likes.count()
    

# comment
from django.contrib.auth.models import User  # Assuming User model for authentication

class Comment(models.Model):
  post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')  # Replace 'your_app.Posting' with your posting model
  user = models.ForeignKey(to=User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
