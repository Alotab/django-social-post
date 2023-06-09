from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100, blank=None)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title
    
    # redirect user to the post detail after a new post is made
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})