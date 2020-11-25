from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('photography', views.photo, name='photo'),
    path('developer', views.developer, name='developer'),
]
