from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from .models import Tickets, File
from .forms import TicketUploadForm
import pandas as pd
import os as os

# Create your views here.
def upload(request):
    data_to_display = None
    if request.method == 'POST':
        form = TicketUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['csv_file']
            obj = File.objects.create(file=file)
            path = obj.file.path
            file_extension = file.name.split('.')[-1].lower()
            if file_extension == 'csv':
                df = pd.read_csv(path)
                data_to_display = df.head().to_html()
                for index, row in df.iterrows():
                    _, created = Tickets.objects.update_or_create(
                    Resolved_By = row['Resolved By'],
                    Status = row['Status'],
                    Parent_Record_Type = row['Parent Record Type'],
                    Resolved_DateTime = row['Resolved DateTime'],
                    Created_Date_Time = row['Created Date Time'],
                )
                context = messages.success(request, 'Uploading your data now')
            else:
                context = messages.error(request, f'Error unsupported file extension: {file_extension}') 
        else:
            context = messages.error(request, 'Error Processing the form please verify it matches the format')
            print(form.errors.as_text())
        return render(request, 'data_upload/upload.html')
    else:
        form = TicketUploadForm()
    context = {'data_to_display': data_to_display}
    return render(request, 'data_upload/upload.html', context)