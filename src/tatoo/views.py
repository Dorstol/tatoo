from django.views.generic import ListView, TemplateView, DetailView

from tatoo.models import Pin


class IndexView(TemplateView):
    template_name = "base/base.html"


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


