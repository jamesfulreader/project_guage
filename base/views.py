import urllib.parse
from django.shortcuts import render
from data_upload.models import Tickets
import matplotlib.pyplot as plt
import io
import urllib, base64

from .utils import count_completed_tickets

# Create your views here.
def home(request):
    data = Tickets.objects.all()
    completed_tickets = count_completed_tickets(data)
    plt.figure(figsize=(10, 5))
    plt.barh(completed_tickets.keys(), completed_tickets.values())
    plt.ylabel("Names")
    plt.xlabel("Completed Tickets")
    plt.title("Completed Tickets by Name")
    plt.grid(True)
    
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    string = base64.b64encode(buffer.read())
    uri = urllib.parse.quote(string)

    return render(request, 'base/home.html', {
        'data': uri
    })