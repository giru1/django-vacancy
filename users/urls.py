from django.urls import path
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.views import UserListView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, Logout

urlpatterns = [
    path('', UserListView.as_view()),
    path('<int:pk>', UserDetailView.as_view()),
    path('create', UserCreateView.as_view()),
    path('<int:pk>/update', UserUpdateView.as_view()),
    path('<int:pk>/delete', UserDeleteView.as_view()),

    path('login', views.obtain_auth_token),
    path('logout', Logout.as_view()),
    path('token', TokenObtainPairView.as_view()),
    path('token/refresh', TokenRefreshView.as_view()),
]