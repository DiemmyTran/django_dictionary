from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('word/', views.search_word, name='word'),
    path('word/', views.audio, name='word')
]
