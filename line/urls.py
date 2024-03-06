from django.urls import path
from . import views

urlpatterns = [
    path("user/", views.Line_User.as_view()),
]