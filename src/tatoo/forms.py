from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from tatoo.models import Board


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "phone", "password1", "password2")


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password")


class CreateBoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['name']