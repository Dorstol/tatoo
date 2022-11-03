from django.views.generic import ListView
from django.views.generic import TemplateView

from tatoo.models import Pin


class IndexView(TemplateView):
    template_name = 'base/index.html'


class Explore(ListView):
    queryset = Pin.objects.all()
    template_name = "explore.html"
