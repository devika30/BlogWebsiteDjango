from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    blog=models.CharField(max_length=30)

    def __str__(self):
        return self.blog
    
