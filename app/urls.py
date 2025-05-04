from django.urls import path
from .views import (
    PortfolioCreateView,
    PortfolioListView,
    PortfolioDetailView
)

urlpatterns = [
    path('', PortfolioListView.as_view(), name='portfolio-list'),
    path('create/', PortfolioCreateView.as_view(), name='portfolio-create'),
    path('<int:id>/', PortfolioDetailView.as_view(), name='portfolio-detail'),
]