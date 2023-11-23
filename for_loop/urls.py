from django.urls import path
from .views import loop_view

urlpatterns = [
    path('loop/', loop_view, name='loop'),
]
