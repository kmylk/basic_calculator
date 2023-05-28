"""
URL configuration for calculator project.
"""
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path("count", include("calculations.urls")),
    path('admin/', admin.site.urls),

]
