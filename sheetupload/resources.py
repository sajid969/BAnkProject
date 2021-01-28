from import_export import resources
from .models import BankDetails

class BankDetailsResource(resources.ModelResource):
    class Meta:
        model = BankDetails
