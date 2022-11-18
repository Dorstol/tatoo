from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "phone", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = UsernameField(label=_("Input your phone"))

    class Meta:
        model = get_user_model()
        fields = ("phone", "password")
