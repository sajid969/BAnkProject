from django.shortcuts import render
from django.http import HttpResponse
from sheetupload.resources import BankDetailsResource
from tablib import Dataset
from .models import BankDetails

def export(request):
    BankDetails_Resource = BankDetailsResource()
    dataset = BankDetails_Resource.export()
    response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="BankDetails.xlsx"'
    return response

def simple_upload(request):
    if request.method == 'POST':
        BankDetails_Resource = BankDetailsResource()
        dataset = Dataset()
        new_bankdetails = request.FILES['myfile']

        imported_data = dataset.load(new_bankdetails.read(),format='xlsx')
        #print(imported_data)
        for data in imported_data:
        	print(data[1])
        	value = BankDetails(
        		data[0],
        		data[1],
        		 data[2],
        		 data[3],
                 data[4],
        		 data[5],
                 data[6],
                 data[7],
                 data[8]
        		)
        	value.save()

        #result = person_resource.import_data(dataset, dry_run=True)  # Test the data import

        #if not result.has_errors():
        #    person_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'input.html')
