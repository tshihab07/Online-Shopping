from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core.views import index, contact, login, register

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', register, name='signup'),           # refactor: name = register -> name = signup
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
