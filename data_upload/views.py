from django.shortcuts import render

# Create your views here.
def upload_csv(request):
    return render(request, 'data_upload/csv_upload.html')