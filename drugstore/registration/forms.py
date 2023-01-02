from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import CharField, TextInput, PasswordInput, EmailInput, EmailField


class RegisterForm(UserCreationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'input100',
                'name': 'username',
                'placeholder': 'Enter Username',
            }
        )
    )
    email = EmailField(
        widget=EmailInput(
            attrs={
                'class': 'input100',
                'name': 'email',
                'placeholder': 'Enter Email',
            }
        )
    )
    password1 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password1',
                'placeholder': 'Enter Password',
            }
        )
    )
    password2 = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password2',
                'placeholder': 'Repeat Password',
            }
        )
    )

    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = User

class LoginForm(AuthenticationForm):
    username = CharField(
        max_length=150,
        widget=TextInput(
            attrs={
                'class': 'input100',
                'name': 'username',
                'placeholder': 'Enter Username'
            }
        )
    )
    password = CharField(
        min_length=8,
        widget=PasswordInput(
            attrs={
                'class': 'input100',
                'name': 'password',
                'placeholder': 'Enter Password'
            }
        )
    )
