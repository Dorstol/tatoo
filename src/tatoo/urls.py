from django.urls import path

from tatoo.views import *

app_name = "tatoo"

urlpatterns = [
    path("bitcoin/", bitcoin, name='bitcoin'),
    path("normalize_email/", normalize_email, name='normalize_email'),
    path("data/", get_data, name='get_data'),
]
