from django.urls import path, include
from .views import *

urlpatterns = [
    path('', pg_index),
    path('add_form', pg_index),
    path('edit_form', pg_index),
    path('auth', pg_index),
    path('api/points', pg_api_points),
]