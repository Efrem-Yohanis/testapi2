from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from .models import Portfolio
from .serializers import PortfolioSerializer
from django.shortcuts import get_object_or_404
import logging

logger = logging.getLogger(__name__)

class PortfolioCreateView(APIView):
    """
    Create a new portfolio
    POST /api/portfolios/
    """
    def post(self, request):
        # Validate payload exists
        if 'payload' not in request.data:
            return Response(
                {"status": "error", "message": "Payload is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PortfolioSerializer(data=request.data['payload'])
        if serializer.is_valid():
            portfolio = serializer.save()
            logger.info(f"Created portfolio {portfolio.id} for user {portfolio.user_id}")
            return Response(
                {"status": "success", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        logger.error(f"Validation error: {serializer.errors}")
        return Response(
            {"status": "error", "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class PortfolioListView(ListAPIView):
    """
    List all portfolios
    GET /api/portfolios/
    """
    queryset = Portfolio.objects.all().order_by('-created_at')
    serializer_class = PortfolioSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response({
            "status": "success",
            "count": len(response.data),
            "data": response.data
        })

class PortfolioDetailView(APIView):
    """
    Retrieve, update or delete a portfolio
    GET/PUT/DELETE /api/portfolios/<id>/
    """
    def get(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)
        serializer = PortfolioSerializer(portfolio)
        return Response({
            "status": "success",
            "data": serializer.data
        })

    def put(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)
        
        # Validate payload exists
        if 'payload' not in request.data:
            return Response(
                {"status": "error", "message": "Payload is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = PortfolioSerializer(
            portfolio, 
            data=request.data['payload'],
            partial=True
        )
        
        if serializer.is_valid():
            serializer.save()
            logger.info(f"Updated portfolio {id}")
            return Response({
                "status": "success",
                "data": serializer.data
            })
            
        logger.error(f"Update error: {serializer.errors}")
        return Response({
            "status": "error",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        portfolio = get_object_or_404(Portfolio, id=id)
        portfolio.delete()
        logger.info(f"Deleted portfolio {id}")
        return Response(
            {"status": "success", "message": "Portfolio deleted"},
            status=status.HTTP_204_NO_CONTENT
        )