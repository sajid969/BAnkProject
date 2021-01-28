"""bankdetails URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from sheetupload import views
from api import views as apiview
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', views.export),
    path('', views.simple_upload),
    path('api/', apiview.BankDetailsAPIView.as_view()),
    path('api/ifscdetails/', apiview.ifscdetailsAPIView.as_view()),
    path('api/bankcityandname/', apiview.bankcityandnameAPIView.as_view()),
    path('api/auth-jwt/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/auth-jwt-refresh/', TokenRefreshView.as_view(),name='token_refresh'),
    path('api/auth-jwt-verify/', TokenVerifyView.as_view(),name='token_verify'),
]
