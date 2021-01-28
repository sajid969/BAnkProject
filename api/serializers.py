from sheetupload.models import BankDetails
from rest_framework import serializers

class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model=BankDetails
        fields='__all__'
