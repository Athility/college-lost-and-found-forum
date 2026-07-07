from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.home, name="home"),
    path("lost/", views.lost, name="Lost Item Registration"),
    path("lost-items/", views.lost_items, name="Lost Items"),
    path("found/", views.found, name="Found Items"),
    path("register/", views.register, name="sign up" ),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("items/<int:item_id>/edit/", views.edit_item, name="edit item"),
    path("items/<int:item_id>/delete/", views.delete_item, name="delete item"),
    path("claimed/", views.claimed, name="Claimed Items"),
    path("items/<int:item_id>/claim/", views.claim_item, name="claim item"),
]