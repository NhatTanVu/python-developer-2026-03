"""
URL configuration for blog pages.
"""

from django.urls import path

from . import views

urlpatterns = [
    path("posts/", views.index, name="index"),
    path("post/<uuid:pk>/", views.post_detail, name="post_detail"),
    path("", views.welcome, name="welcome"),
]
