from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.Line_User.as_view()),
    path("bot/", views.Send_Message.as_view())
]