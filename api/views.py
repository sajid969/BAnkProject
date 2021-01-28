from django.shortcuts import render
from rest_framework import generics
from api.serializers import BankDetailsSerializer
from sheetupload.models import BankDetails
from rest_framework.pagination import PageNumberPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class BankDetailsAPIView(generics.ListAPIView):
    queryset=BankDetails.objects.all()
    serializer_class=BankDetailsSerializer
    pagination_class=PageNumberPagination
    authentication_classes=[JWTAuthentication,]
    permission_classes=[IsAuthenticated,]


class bankcityandnameAPIView(generics.ListAPIView):
    serializer_class=BankDetailsSerializer
    def get_queryset(self):
        qs=BankDetails.objects.all()
        bankcity=self.request.GET.get('city')
        bankname=self.request.GET.get('bank_name')
        pagination_class=PageNumberPagination
        if bankcity is not None and bankname is not None:
            qs=qs.filter(city__icontains=bankcity,bank_name__icontains=bankname)

        return qs



class ifscdetailsAPIView(generics.ListAPIView):
    serializer_class=BankDetailsSerializer
    def get_queryset(self):
        qs=BankDetails.objects.all()
        ifsccode=self.request.GET.get('ifsc')
        if ifsccode is not None:
            qs=qs.filter(ifsc__icontains=ifsccode)
        return qs
