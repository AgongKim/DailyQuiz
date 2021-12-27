from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    answer = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

