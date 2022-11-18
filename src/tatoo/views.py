from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, DetailView, CreateView

from tatoo.forms import RegisterForm, LoginForm
from tatoo.models import Pin, Pinner


class IndexView(TemplateView):
    template_name = "base/base.html"


class RegisterView(CreateView):
    template_name = "accounts/register.html"
    form_class = RegisterForm
    success_url = "tatoo:index_page"


class UserLoginView(LoginView):
    template_name = "accounts/login.html"
    success_url = "tatoo:index_page"
    form_class = LoginForm


class Explore(ListView):
    model = Pin
    template_name = "base/explore.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pins'] = Pin.objects.all()
        return context


class Pin_detail(DetailView):
    model = Pin
    template_name = "pins/pin_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pin_data = Pin.objects.filter(pk=self.kwargs['pk']).first()
        context["pin_data"] = pin_data
        return context
