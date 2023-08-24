from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    post_body = models.CharField(max_length=800)
    date = models.DateField(auto_now=True)
    username = models.ForeignKey(User,related_name="poster",on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title

class Comment(models.Model):
    username = models.ForeignKey(User,related_name="commentor",on_delete=models.CASCADE,default=None)
    comment = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='c_post',default=None)
    
    def __str__(self):
        return self.comment