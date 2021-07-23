from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import CharField, EmailField
from django.forms.widgets import EmailInput, PasswordInput


class RegisterForm(forms.Form):
    
    choos_h =(
    ("1", "Slytherin"),
    ("2", "Gryffindor"),
    ("3", "Hufflepuff"),
    ("4", "Ravenclaw"),
    
)
    

    name = CharField(max_length=30, label="Ad:")
    last_name =CharField(max_length=30,label="Soyad:")
    """house = forms.ChoiceField(choices=choos_h,label="Hogwarts eviniz?")"""
    username = CharField(max_length=25, label="İstifadəçi adı:")
    email = CharField(max_length=100,label="Elektron poçtunuzu daxil edin:",widget=EmailInput)
    password= CharField(max_length=50, label="Şifrə:",widget=PasswordInput)
    confirm = CharField(max_length=50, label="Şifrənin təsdiqi:",widget=PasswordInput)
    

    def clean(self):

        name = self.cleaned_data.get("name")
        surname = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password =self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")
    

        if confirm and password and password != confirm:
            raise ValidationError("Şifrələr eyni deyil")

class LoginForm(forms.Form):
    
    username = CharField(max_length=40,label="İstifadəçi adı:")
    password = CharField(max_length=40,label="Şifrə:", widget=PasswordInput)
