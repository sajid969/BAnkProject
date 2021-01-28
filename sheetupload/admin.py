from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import BankDetails

# Register your models here.

@admin.register(BankDetails)
class BankDetailsAdmin(ImportExportModelAdmin):
    list_display = ('ifsc', 'city', 'bank_name')
