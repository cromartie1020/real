from django.db import models
from datetime import date,datetime
from django.contrib.auth.models import User
class Page(models.Model):
    title=models.CharField(max_length=30,unique=True)
    slug=models.SlugField(max_length=30)
    pub_date=models.DateTimeField(auto_now_add=datetime.now())
    image=models.ImageField(upload_to ='media')

    def __str__(self):
        return self.title