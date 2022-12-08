from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView

from tatoo.forms import RegisterForm, CreateBoardForm
from tatoo.models import Pin, Pinner, Board


# common views
class IndexView(TemplateView):
    template_name = "base/base.html"


class Explore(ListView):
    model = Pin
    template_name = "base/explore.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pins'] = Pin.objects.all()
        return context


# views linked to user account
class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = reverse_lazy("tatoo:login")


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = reverse_lazy("tatoo:explore")


class UserLogoutView(LogoutView):
    template_name = "accounts/login.html"


class UserProfileView(TemplateView, LoginRequiredMixin):
    template_name = "accounts/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_board_form'] = CreateBoardForm()
        return context


class UserEditProfileView(UpdateView):
    model = Pinner
    template_name = "accounts/edit_profile.html"
    fields = ["first_name", "last_name", "birthdate", "avatar", "username", "about"]
    success_url = reverse_lazy("tatoo:profile")


# views linked to pins

class Pin_detail(DetailView):
    model = Pin
    template_name = "pins/pin_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pin_data = Pin.objects.filter(pk=self.kwargs['pk']).first()
        context["pin_data"] = pin_data
        return context


# views linked to boards

class CreateBoardView(CreateView):
    success_url = reverse_lazy("tatoo:explore")
    model = Board
    fields = ["name"]
