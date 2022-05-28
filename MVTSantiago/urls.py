from django.contrib import admin
from django.urls import path
from Familiares.views import show_data

urlpatterns = [
    path('admin/', admin.site.urls),
]
