from django.shortcuts import render
from .serializer import AccountSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import CustomUser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
class AccountsListCreate(generics.ListCreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=AccountSerializer
    permission_classes=[AllowAny]
    def post(self, request):
        serializer = AccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "تم التسجيل بنجاح!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = AccountSerializer(request.user)
        return Response(serializer.data)