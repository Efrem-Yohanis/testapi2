from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Portfolio
from .serializers import PortfolioSerializer
import logging
from django.shortcuts import get_object_or_404

logger = logging.getLogger(__name__)

class PortfolioCreateView(APIView):
    """Handle POST /create requests from your pipeline"""
    
    def post(self, request):
        serializer = PortfolioSerializer(data=request.data.get('payload', {}))
        if serializer.is_valid():
            portfolio = serializer.save()
            # Generate API ID (fixed typo from 'use' to 'api_id')
            #portfolio.api_id = f"pf-{portfolio.id}-{portfolio.number}"
            portfolio.save()
            logger.info(f"Created portfolio {portfolio.user_id} for user {portfolio.user_id}")
            
            return Response({
                'status': 'success',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        
        logger.error(f"Validation error: {serializer.errors}")
        return Response({
            'status': 'error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PortfolioUpdateView(APIView):
    """Handle PUT /update/{api_id} requests"""
    
    def put(self, request, api_id):
        portfolio = get_object_or_404(Portfolio, api_id=api_id)
        serializer = PortfolioSerializer(portfolio, data=request.data['payload'][0], partial=True)
        
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Updated portfolio {api_id}")
            return Response({
                'status': 'success',
                'api_id': api_id,
                'data': serializer.data
            })
            
        logger.error(f"Update error for {api_id}: {serializer.errors}")
        return Response({
            'status': 'error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PortfolioListView(APIView):
    """Handle GET all portfolios"""
    
    def get(self, request):
        portfolios = Portfolio.objects.all().order_by('-created_at')
        serializer = PortfolioSerializer(portfolios, many=True)
        return Response({
            'status': 'success',
            'count': len(serializer.data),
            'data': serializer.data
        })

class PortfolioDetailView(APIView):
    """Handle GET single, PUT, and DELETE operations"""
    
    def get(self, request, api_id):
        portfolio = get_object_or_404(Portfolio, user_id=user_id)
        serializer = PortfolioSerializer(portfolio)
        return Response({
            'status': 'success',
            'data': serializer.data
        })
    
    def put(self, request, api_id):
        portfolio = get_object_or_404(Portfolio, api_id=api_id)
        serializer = PortfolioSerializer(portfolio, data=request.data['payload'][0], partial=True)
        
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Updated portfolio {api_id}")
            return Response({
                'status': 'success',
                'data': serializer.data
            })
            
        logger.error(f"Update error: {serializer.errors}")
        return Response({
            'status': 'error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, api_id):
        portfolio = get_object_or_404(Portfolio, api_id=api_id)
        portfolio.delete()
        logger.info(f"Deleted portfolio {api_id}")
        return Response({
            'status': 'success',
            'message': 'Portfolio deleted successfully'
        }, status=status.HTTP_204_NO_CONTENT)