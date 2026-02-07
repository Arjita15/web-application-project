from django.urls import path
from . import views
from . import auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", auth_views.signup, name="signup"),
    path("note/<int:id>/", views.read_one, name="read_one"),
    path("note/<int:id>/edit/", views.update_one, name="update_one"),
    path("note/<int:id>/delete/", views.delete_one, name="delete_one"),
]