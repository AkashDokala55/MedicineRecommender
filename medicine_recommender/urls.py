# medicine_recommender/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recommender.urls')),  # ✅ Replace 'your_app' with the actual app name
]
