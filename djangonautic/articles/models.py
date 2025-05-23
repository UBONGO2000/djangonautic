from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    date=models.DateField(auto_now_add=True)
    slug=models.SlugField()
    
    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.body[:50]+'...'