from django.urls import path

from .views import home_view, create_view, edit_view, delete_view


app_name = "pictures"


urlpatterns = [
    path("", home_view, name="home"),
    path("create/", create_view, name="create"),
    path("edit/<pk>/", edit_view, name="edit"),
    path("delete/<pk>/", delete_view, name="delete"),
]
