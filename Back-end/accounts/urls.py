app_name="accounts"
from django.urls import path
from .views import AccountsListCreate, CurrentUserView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',AccountsListCreate.as_view(),name='accounts'),
    path('user-info/', CurrentUserView.as_view(), name='user-info'),

    # ✅ Add these:
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    
]
