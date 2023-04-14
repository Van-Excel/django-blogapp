from django.db import models
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    author = models.ForeignKey(
        'auth.User',  # learn more about User model django provides for authentication
        on_delete=models.CASCADE  # revise to understand
    )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
