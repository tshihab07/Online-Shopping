from django.contrib import admin
from django.urls import path

from core.views import index, contact, login, register

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', register, name='register'),
    path('admin/', admin.site.urls),
]
