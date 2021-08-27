from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/kakao/", views.kakao_login, name="kakao-login"),
    path("login/kakao/callback/", views.kakao_callback, name="kakao-callback"),
]
