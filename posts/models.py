from django.db import models
import datetime
from django.utils import timezone

class Post(models.Model):
    def __str__(self):
        return self.post_title
    poster = models.IntegerField(default=0)
    post_text = models.CharField(max_length=500)
    post_title = models.CharField(max_length=20)
    post_sub = models.CharField(max_length=20)
    pub_date = models.DateTimeField('Date published')
    votes = models.IntegerField(default=0)
    to_show = models.BooleanField(default=True)
    happy = models.BooleanField(default=False)
    angry = models.BooleanField(default=False)
    stressy = models.BooleanField(default=False)
    energy = models.BooleanField(default=False)
    worry = models.BooleanField(default=False)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Account(models.Model):
    def __str__(self):
        return self.uname
    uname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    pword = models.CharField(max_length=64)
    signup_date = models.DateTimeField('Date signed up')
