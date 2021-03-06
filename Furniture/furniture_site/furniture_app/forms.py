from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms


class ResisterUserForm(UserCreationForm):
    username = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ("username", 'email', "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control'}
        )
    )

    last_name = forms.CharField(
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя', 'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email', 'class': 'form-control'}
        )
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
