# In app/views.py - add this class
class PortfolioUpdateView(APIView):
    """Handle PUT /update/{id} requests"""
    
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