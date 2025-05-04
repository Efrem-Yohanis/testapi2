from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
        

class BulkPortfolioSerializer(serializers.Serializer):
    payload = PortfolioSerializer(many=True)

    def create(self, validated_data):
        portfolios = []
        for item in validated_data['payload']:
            portfolio = Portfolio.objects.create(**item)
            portfolios.append(portfolio)
        return {'portfolios': portfolios}

    def update(self, instance, validated_data):
        # Handle bulk update if needed
        pass