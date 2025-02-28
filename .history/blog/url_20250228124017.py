from . import views
from django.urls import path

urlpattern = [
    path('', views.PostList.as_view(), name=
]