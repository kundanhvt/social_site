from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
from user.models import PostUser

class Post(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length = 100)
    description = models.TextField()
    like = models.ManyToManyField(PostUser, related_name="likes")
    dislike = models.ManyToManyField(PostUser, related_name="dislikes")
    # like = models.IntegerField(default=0)
    # dislike = models.IntegerField(default=0)
    user = models.ForeignKey(PostUser,on_delete = models.CASCADE, related_name='posts')


class Comment(models.Model):
    comment = models.TextField(default='')
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="comments")
    user = models.ManyToManyField(PostUser, related_name="users")

