from django.urls import path     
from . import views

urlpatterns = [
    path('', views.main),
    path('home', views.main),
    path('result', views.result),
    path('success', views.success)
]