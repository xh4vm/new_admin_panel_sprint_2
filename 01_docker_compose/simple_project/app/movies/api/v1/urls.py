from django.urls import path

from .views import MoviesListApi

urlpatterns = [
    path('movies/', MoviesListApi.as_view()),
]
