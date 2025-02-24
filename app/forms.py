from django import forms
from django.forms.widgets import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    password=forms.CharField(required=True, widget=PasswordInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))

    class Meta:
        model = User
        fields = ["username", "password"]

class RegisterForm(UserCreationForm):
    username=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    email=forms.EmailField(required=True, widget=EmailInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    password1=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))
    password2=forms.CharField(required=True, widget=TextInput(attrs={"class":"w-full p-3 mt-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"}))

    class Meta:
        model = User
        fields = ["username", "email", "password1","password2"]