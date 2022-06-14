
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpost", views.new_post, name="newpost"),
    path("following", views.following, name="following"),
    path("edit/<int:post_id>", views.edit, name="edit"),
    path("getpost/<int:post_id>", views.get_post, name="get_post"),
    path("like/<int:post_id>", views.like, name="like"),
    path("user/<int:user_id>", views.profile, name="profile"),
    path("follow/<int:user_id>", views.follow, name="follow")
]
