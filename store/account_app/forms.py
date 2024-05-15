from django import forms


class UserRegister(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()

    