from django.db import models
from django.urls import reverse
from accounts.models import CustomUser

from ckeditor.fields import RichTextField

# Create your models here.

class Articles(models.Model):
    title = models.CharField(max_length=150)
    summary = models.CharField(max_length=200, blank=True)
    body = RichTextField()
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
    )

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
class Comment(models.Model):
    article = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    comment = models.CharField(max_length=150, null=True, blank=True)
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
    )

    def __str__(self) -> str:
        return self.comment
    
    def get_absolute_url(self):
        return reverse('article_list')