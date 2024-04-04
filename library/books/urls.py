from django.urls import path
from . import views

urlpatterns = [
    path("", views.main),
    path("books/", views.books),
    path("description/<int:id>", views.description),
]