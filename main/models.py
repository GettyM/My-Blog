from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from datetime import datetime, date
from django.template.defaultfilters import slugify

# remember to register your models on admin.py file


class Post(models.Model):
    title = models.CharField(max_length=300)
    title_label = models.CharField(max_length=300, default="Getty's Blog")
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.CharField(
        max_length=280, default='My Tech Journey')
    content = models.TextField()
    article_date = models.DateField(auto_now_add=True)
    # article_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.writer)

    def get_absolute_url(self):
        return reverse('postdetails', args=(str(self.id)))
        # return reverse('home')


class Categories(models.Model):
    name = models.CharField(max_length=280)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse('postdetails', args=(str(self.id)))
        return reverse('home')
