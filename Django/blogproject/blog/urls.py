
from . import views
from django.urls import path

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:pk>/", views.detail, name="detail")
]
