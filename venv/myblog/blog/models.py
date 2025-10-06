from django.db import models
from tinymce.models import HTMLField
# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=HTMLField()
    description=models.CharField(max_length=300)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Comment(models.Model):
    blog=models.ForeignKey(Blog,related_name='comments',on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    body=HTMLField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Comment by {self.name}"
