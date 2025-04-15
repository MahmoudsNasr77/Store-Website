from django.shortcuts import render
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
class ContactView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    #throttle_classes = [UserRateThrottle, AnonRateThrottle]
    #throttle_scope = 'contact'
    
    
