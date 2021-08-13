from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ValidationError
#from django.core.checks.messages import Error

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(max_length=50, required=True)
    class Meta:
        model = User
        fields =["username","first_name","last_name","email"]
    def clean_email(self):
        email= self.cleaned_data['email']
        user=None
        try:
            user=User.objects.get(email=email)
        except:
            return email
        if(user is not None):
            raise ValidationError("User already exist")    


