from django.urls import path
from .views import (
    RegisterView,
    CategoryListCreateView,
    ItemListCreateView,
    ItemDetailView,
    StockLogListView,
    ProfileView,
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('stock-logs/', StockLogListView.as_view(), name='stock-log-list'),
    path('profile/', ProfileView.as_view(), name='profile'),
]