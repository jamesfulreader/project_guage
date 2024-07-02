from django.shortcuts import render
from .models import Tickets, File
import pandas as pd

# Create your views here.
def upload(request):
    data_to_display = None
    if request.method == 'POST':
        file = request.FILES['files']
        obj = File.objects.create(file=file)
        path = file.file
        df = pd.read_csv(path)
        data_to_display = df.to_html()
    context = {'data_to_display': data_to_display}
    return render(request, 'data_upload/upload.html', context)