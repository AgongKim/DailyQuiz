from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=500)
    body = models.TextField()
    answer = models.CharField(max_length=200)
    category = models.CharField(max_length=200, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
