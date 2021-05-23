from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# class inherited from models model
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # if user is deleted posts are also deleted
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # dunder(double underscore) str method to print what we want
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
    