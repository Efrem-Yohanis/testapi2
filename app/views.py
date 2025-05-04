from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Portfolio
from .serializers import PortfolioSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class PortfolioCreateView(APIView):
    def post(self, request):
        # Check if payload exists
        if 'payload' not in request.data:
            return Response({
                'status': 'error',
                'message': 'Missing payload in request'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = PortfolioSerializer(data=request.data['payload'])
        if serializer.is_valid():
            portfolio = serializer.save()
            return Response({
                'status': 'success',
                'data': PortfolioSerializer(portfolio).data
            }, status=status.HTTP_201_CREATED)
            
        return Response({
            'status': 'error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class PortfolioDetailView(APIView):
    def get(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)
        serializer = PortfolioSerializer(portfolio)
        return Response({
            'status': 'success',
            'data': serializer.data
        })
    
    def put(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)
        
        # Check if payload exists
        if 'payload' not in request.data or not request.data['payload']:
            return Response({
                'status': 'error',
                'message': 'Missing or empty payload'
            }, status=status.HTTP_400_BAD_REQUEST)
            
        serializer = PortfolioSerializer(
            portfolio, 
            data=request.data['payload'][0], 
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'success',
                'data': serializer.data
            })
            
        return Response({
            'status': 'error',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)