from django.urls import path

from tatoo.views import Explore, IndexView, Pin_detail

app_name = "tatoo"

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("explore/", Explore.as_view(), name="explore"),
    path("pin/<int:pk>", Pin_detail.as_view(), name="pin_detail")
]
