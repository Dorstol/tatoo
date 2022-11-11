from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions, routers

from api.views import *

app_name = "api"
routes = routers.DefaultRouter()
routes.register("customers", UserViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Tatoo API",
        default_version="v1",
        description="Chose and get tatoo what you like",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[
        permissions.AllowAny,
    ],
)

urlpatterns = [
    path("", include(routes.urls)),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger_docs"),
    path("pinner/<int:pk>/", PinnerAPIView.as_view(), name="pinner_detail"),
    path("pinner/update/<int:pk>/", PinnerUpdateAPIView.as_view(), name="pinner_update"),
    path("pinner/delete/<int:pk>/", PinnerDestroyAPIView.as_view(), name="pinner_delete"),
    path("boards/", BoardListAPIView.as_view(), name="boards_list"),
    path("board/<int:pk>/", BoardDetailAPIView.as_view(), name="board_detail"),
    path("board/update/<int:pk>/", BoardUpdateAPIView.as_view(), name="board_update"),
    path("board/delete/<int:pk>/", BoardDestroyAPIView.as_view(), name="board_delete"),
    path("pins/", PinListAPIView.as_view(), name="pins_list"),
    path("pins/<int:pk>/", PinDetailAPIView.as_view(), name="pin_detail"),
    path("pins/update/<int:pk>/", PinUpdateAPIView.as_view(), name="pin_update"),
    path("pins/delete/<int:pk>/", PinDestroyAPIView.as_view(), name="pin_delete"),
    path("images/", ImageListAPIView.as_view(), name="images_list"),
    path("image/<int:pk>/", ImageDetailAPIView.as_view(), name="image_detail"),
    path("image/update/<int:pk>/", ImageUpdateAPIView.as_view(), name="image_update"),
    path("image/delete/<int:pk>/", ImageDestroyAPIView.as_view(), name="image_delete"),
    path("comments/", CommentListAPIView.as_view(), name="comments_list"),
    path("comment/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail"),
    path("comment/update/<int:pk>/", CommentUpdateAPIView.as_view(), name="comment_update"),
    path("comment/delete/<int:pk>/", CommentDestroyAPIView.as_view(), name="comment_delete"),
]
