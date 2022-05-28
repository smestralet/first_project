from django.contrib import admin
from django.urls import path
from Familiares.views import show_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('show_data/', show_data , name='show_data')
]
