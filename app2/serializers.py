from rest_framework import serializers
from .models import User, Profile

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'login_entity_id', 'entity', 'entity_id', 'advisor_name', 
                  'entity_name', 'role_id', 'is_user_default', 'al_client_id', 'role_name']

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    profiles = ProfileSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'user_id', 'first_name', 'last_name', 'email', 'is_active', 
                  'contact_type', 'entity_name', 'profiles']

    def create(self, validated_data):
        profiles_data = validated_data.pop('profiles')
        user = User.objects.create(**validated_data)
        for profile_data in profiles_data:
            profile = Profile.objects.create(**profile_data)
            user.profiles.add(profile)
        return user

    def update(self, instance, validated_data):
        profiles_data = validated_data.pop('profiles')
        # Update basic user fields
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        instance.contact_type = validated_data.get('contact_type', instance.contact_type)
        instance.entity_name = validated_data.get('entity_name', instance.entity_name)
        instance.save()

        # Clear existing profiles and update
        instance.profiles.clear()
        for profile_data in profiles_data:
            profile = Profile.objects.create(**profile_data)
            instance.profiles.add(profile)
        return instance
