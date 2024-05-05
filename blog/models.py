from django.db import models



class Blog(models.Model):
    title = models.CharField(max_length=400, unique=True)
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    body = models.TextField(unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
    
