from django.urls import path
from .views import (
    PortfolioCreateView,
    PortfolioUpdateView,  # Now this exists
    PortfolioListView,
    PortfolioDetailView
)

urlpatterns = [
    path('create/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('update/<str:id>/', PortfolioUpdateView.as_view(), name='portfolio-update'),
    path('', PortfolioListView.as_view(), name='portfolio-list'),
    path('<str:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]