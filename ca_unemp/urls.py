from django.urls import path
from .views import county_stats

urlpatterns = [
    path('unemployment', county_stats),
]