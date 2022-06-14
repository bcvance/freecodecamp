from time import strftime
from tkinter import CASCADE
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=140)
    numLikes = models.IntegerField(default=0)

    def post_serialize(self):
        return {
            "poster": self.poster.id,
            "content": self.content,
            "numLikes": self.numLikes
        }

class Like(models.Model):
    liker = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    timestamp = models.DateTimeField(auto_now_add=True)

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")
    followee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed_by")
    timestamp = models.DateTimeField(auto_now_add=True)