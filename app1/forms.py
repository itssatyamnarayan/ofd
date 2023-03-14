from django import forms
from .models import CustomerRegister
# Create your views here.
class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomerRegister
        fields= ['user_name','email','password',]
