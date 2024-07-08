from django.shortcuts import render
from data_upload.models import Tickets

import plotly.graph_objects as go
from plotly.offline import plot

from .utils import count_completed_tickets

# Create your views here.
def home(request):
    data = Tickets.objects.all()
    completed_tickets = count_completed_tickets(data)

    x_data = completed_tickets.values()
    y_data = completed_tickets.keys()
    x_data = list(x_data)
    y_data = list(y_data)

    fig = go.Figure(data=go.Bar(x=x_data, y=y_data, orientation='h'))

    fig.update_layout(title='Completed Tickets by Name')
    fig.to_plotly_json()
    plt_div = plot(fig, output_type='div')
    context = {'plot': plt_div}
    return render(request, 'base/home.html', context)