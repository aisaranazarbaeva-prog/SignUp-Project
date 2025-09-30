from django.contrib import admin
from django.urls import path
from authentication1.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
]
