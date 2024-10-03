from django.urls import path, re_path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('set-language/', views.set_language, name='set_language'),
    path('set-theme/', views.set_theme, name='set_theme'),
]