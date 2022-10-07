from django.urls import include, path
from rest_framework import routers

from api.views import *

app_name = "api"
routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("rest_framework.urls")),
    path("pinner/<int:pk>/", PinnerAPIView.as_view(), name="pinner_detail"),
    path("pinner/update/<int:pk>/", PinnerUpdateAPIView.as_view(), name="pinner_update"),
    path("pinner/delete/<int:pk>/", PinnerDestroyAPIView.as_view(), name="pinner_delete"),
    path("boards/", BoardListAPIView.as_view(), name="boards_list"),
    path("board/<int:pk>/", BoardDetailAPIView.as_view(), name="board_detail"),
    path("board/update/<int:pk>/", BoardUpdateAPIView.as_view(), name="board_update"),
    path("board/delete/<int:pk>/", BoardDestroyAPIView.as_view(), name="board_delete"),
    path("pins/", PinListAPIView.as_view(), name="pins_list"),
    path("pin/<int:pk>/", PinDetailAPIView.as_view(), name="pin_detail"),
    path("pin/update/<int:pk>/", PinUpdateAPIView.as_view(), name="pin_update"),
    path("pin/delete/<int:pk>/", PinDestroyAPIView.as_view(), name="pin_delete"),
    path("images/", ImageListAPIView.as_view(), name="images_list"),
    path("image/<int:pk>/", ImageDetailAPIView.as_view(), name="image_detail"),
    path("image/update/<int:pk>/", ImageUpdateAPIView.as_view(), name="image_update"),
    path("image/delete/<int:pk>/", ImageDestroyAPIView.as_view(), name="image_delete"),
    path("comments/", CommentListAPIView.as_view(), name="comments_list"),
    path("comment/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail"),
    path("comment/update/<int:pk>/", CommentUpdateAPIView.as_view(), name="comment_update"),
    path("comment/delete/<int:pk>/", CommentDestroyAPIView.as_view(), name="comment_delete"),
]
