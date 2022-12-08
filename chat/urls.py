from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from chat import views as chat_views

urlpatterns = [
    path("", chat_views.chatPage, name="chat-page"),

    path("auth/login/", LoginView.as_view(template_name="LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]
