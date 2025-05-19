from django.db import models

# Create your models here.
class Articles(models.Model):
    title=models.TextField(max_length=25)
    body=models.CharField()
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField()