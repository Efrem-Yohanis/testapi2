from django.urls import path
from .views import (
    PortfolioCreateView,
    PortfolioUpdateView,
    PortfolioListView,
    PortfolioDetailView
)

urlpatterns = [
    path('create/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('update/<str:api_id>/', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('', PortfolioListView.as_view(), name='portfolio-list'),
    path('<str:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]