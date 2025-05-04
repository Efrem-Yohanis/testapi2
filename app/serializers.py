from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'
        extra_kwargs = {
            'user_sk': {'required': True},
            'user_id': {'required': True},
            'number': {'required': True},
            'name': {'required': True},
            'last_name': {'required': True},
            'first_name': {'required': True},
            'is_active': {'required': False, 'default': True},
            'broker_dealer_id': {'required': False}
        }

    def validate(self, data):
        """Ensure either user_sk or user_id is provided"""
        if not data.get('user_sk') and not data.get('user_id'):
            raise serializers.ValidationError("Either user_sk or user_id must be provided")
        return data