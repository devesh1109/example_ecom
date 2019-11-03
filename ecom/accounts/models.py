from django.db import models
from django.forms import forms
from django.contrib.auth.models import User


# Create your models here.


class Newusers(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    # additional and optional fields here
    user_pic = models.ImageField(upload_to='user_pics',blank=True)
    class Meta():
        db_table = 'accounts_newusers'
    def __str__(self):
        return self.user.username