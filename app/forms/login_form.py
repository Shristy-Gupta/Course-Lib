from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django import forms
from django.forms import ValidationError
#from django.core.checks.messages import Error


class LoginForm(AuthenticationForm):
    username=forms.CharField( required=True)
    def clean(self):
        user=None
        username= self.cleaned_data['username']
        password=self.cleaned_data['password']
        try:
            user=User.objects.get(username=username)
            result=authenticate(username=username,password=password)
            if(result is not None):
                login(self.request,result)
                return result
            else:
                raise ValidationError("Username or Password is Invalid!")
        except:
            raise ValidationError("Username or Password is Invalid!")
            

        
    


