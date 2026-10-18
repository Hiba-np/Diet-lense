from rest_framework import serializers
from diet_app.models import *

class USerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = "__all__"
        read_only_fields = ["id", "bmr", "owner"]


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "email", "password", "phone", "profile"]
        read_only_fields = ["id"]
        
    

    def get_profile(self, obj):
        profile = UserProfile.objects.get(owner=obj)
        return USerProfileSerializer(profile).data
        

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class FoodLogSerializer(serializers.ModelSerializer):
    class Meta:
        model=FoodLog
        fields="__all__"
        read_only_fields=["id","owner","created_at"]
