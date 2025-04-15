from .models import CustomUser
from rest_framework.serializers import ModelSerializer
from django_countries import countries
from rest_framework import serializers
class AccountSerializer(ModelSerializer):
    class Meta:
        model=CustomUser
        exclude = ['groups', 'is_staff', 'is_active', 'date_joined', 'last_login', 'user_permissions',]
        is_superuser = serializers.BooleanField(read_only=True)



    def validate_username(self, value):
        if CustomUser.objects.filter(username=value).exists():
            raise serializers.ValidationError("اسم المستخدم هذا موجود بالفعل. من فضلك اختر اسمًا آخر.")
        if len(value) < 3:
            raise serializers.ValidationError("اسم المستخدم يجب أن يكون على الأقل 3 أحرف.")
        if len(value) > 150:
            raise serializers.ValidationError("اسم المستخدم يجب أن يكون أقل من 150 حرفًا.")
    
        if not value.isalnum():
            raise serializers.ValidationError("اسم المستخدم يجب أن يكون حروف وأرقام.")
        if not value[0].isalpha():
            raise serializers.ValidationError("اسم المستخدم يجب أن يبدأ بحرف.")
            
        return value

    def validate_email(self, value):
        if CustomUser.objects.filter(email=value).exists():
            raise serializers.ValidationError("البريد الإلكتروني هذا مستخدم بالفعل. من فضلك استخدم بريدًا آخر.")
        return value
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("يجب أن تكون كلمة المرور على الأقل 8 أحرف.")
        return value
