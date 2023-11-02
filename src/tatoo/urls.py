from django.urls import path

from tatoo.views import Explore, IndexView, Pin_detail, RegisterView, UserLoginView, UserLogoutView, UserProfileView, \
    UserEditProfileView, CreateBoardView

app_name = "tatoo"

urlpatterns = [
    path("", IndexView.as_view(), name="index_page"),
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("profile/", UserProfileView.as_view(), name="profile"),
    path("profile/edit/<int:pk>", UserEditProfileView.as_view(), name="edit_profile"),
    path("explore/", Explore.as_view(), name="explore"),
    path("pin/<int:pk>", Pin_detail.as_view(), name="pin_detail"),
    path("board/create/", CreateBoardView.as_view(), name="create_board")
]
