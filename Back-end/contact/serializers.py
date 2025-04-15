from rest_framework import serializers
from .models import Contact
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contact
        fields = ['id', 'name', 'email', 'message', 'created_at']
        read_only_fields = ['created_at']
        extra_kwargs = {
            'name': {'required': True},
            'email': {'required': True, 'allow_blank': False},
            'message': {'required': True, 'allow_blank': False}
        }
    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required.")
        if not isinstance(value, str) or '@' not in value:
            raise serializers.ValidationError("Invalid email format.")
        return value
    def validate_message(self, value):
        if not value:
            raise serializers.ValidationError("Message is required.")
      
        return value

    