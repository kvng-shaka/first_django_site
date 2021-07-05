from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=120)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)
