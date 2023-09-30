from django.db import models
from django.contrib.auth.models import User

#importações locais


# Create your models here.
class Autor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idade = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
