from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime
from django.contrib.auth.models import User


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
    image = models.ImageField(upload_to='post_images',null=True)
    video = models.FileField(upload_to='post_videos', blank=True)
    
    caption = models.CharField(max_length=300)
    created_at = models.DateField(auto_now_add=True)
    
    
    def __str__ (self):
        return self.user 
    
class Newsfeed(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=100)
    image=models.ImageField(upload_to="news_image")
    
    caption=models.CharField(max_length=150)
    created_at=models.DateField(auto_now_add=True)

    def __str__ (self):
        return self.user
    

class likes(models.Model):
    likes = models.ManyToManyField(User, related_name='blogpost_like')
    user = models.ForeignKey(Posting, on_delete=models.CASCADE,null=True)
    status = models.CharField(max_length=100, default="liked")

    def number_of_likes(self):
        return self.likes.count()
    

# comment
  # Assuming User model for authentication

class Comment(models.Model):
  post = models.ForeignKey(Posting, on_delete=models.CASCADE, related_name='comments')  # Replace 'your_app.Posting' with your posting model
  user = models.ForeignKey(to=User, on_delete=models.CASCADE)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)



# Optional, if using user authentication

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Optional, if using user authentication
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:50]  # Truncate long messages



    # Add other fields as needed (e.g., description, creation date)
