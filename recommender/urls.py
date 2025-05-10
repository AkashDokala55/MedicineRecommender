# your_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('recommend/', views.recommend_medicine, name='recommend_medicine'),  # ✅ this line is required
]
