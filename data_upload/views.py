from django.shortcuts import render
from django.conf import settings
from .models import Tickets, File
import pandas as pd
import os as os

# Create your views here.
def upload(request):
    data_to_display = None
    if request.method == 'POST':
        file = request.FILES['files']
        obj = File.objects.create(file=file)
        path = os.path.join(settings.MEDIA_ROOT, 'uploads', file.name)
        print(f"this is the PATH {path}")
        df = pd.read_csv(path)
        data_to_display = df.to_html()
    context = {'data_to_display': data_to_display}
    return render(request, 'data_upload/upload.html', context)