from accounts.models import Newusers
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm



class Baseuser(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','email','username','password')


class Newuserform(ModelForm):
    
    class Meta():
        model = Newusers
        fields = ('user_pic',)