from django.urls import path

from core.views import normalize_email, get_data

app_name = "core"

urlpatterns = [
    path("normalize_email/", normalize_email, name="normalize_email"),
    path("data/", get_data, name="get_data"),
]