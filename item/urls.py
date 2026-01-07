from django.urls import path
from .views import item_detail

app_name = "item"

urlpatterns = [
    path('<int:pk>/', item_detail, name='item-detail'),
]
