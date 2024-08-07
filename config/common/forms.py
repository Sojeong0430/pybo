from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    #email 속성 추가

    class Meta:
        model = User
        fields = ("username","password1","password2","email")
#UserCreationForm 클래스를 상속해서 UserForm 만들기
