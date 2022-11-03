from django.urls import path

from core.views import IndexView, Explore

app_name = "core"

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('explore/', Explore.as_view(), name='explore'),
]
