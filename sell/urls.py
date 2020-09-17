from django.urls import path
from .views import (SellListView, 
					SellDetailView,
					SellCreateView,
					SellUpdateView,
					SellDeleteView,)
from . import views

urlpatterns = [
    path('', SellListView.as_view(), name='sell-home'),
    path('sell/<int:pk>/', SellDetailView.as_view(), name='sell-detail'),
    path('sell/<int:pk>/update/', SellUpdateView.as_view(), name='sell-update'),
    path('sell/<int:pk>/delete/', SellDeleteView.as_view(), name='sell-delete'),
    path('sell/new/', SellCreateView.as_view(), name='sell-create'),
]
