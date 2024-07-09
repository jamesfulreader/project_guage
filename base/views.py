from django.shortcuts import render
from data_upload.models import Tickets

import plotly.graph_objects as go
from plotly.offline import plot

from .utils import count_completed_tickets, get_complete_tickets, get_withdrawn_tickets

# Create your views here.
def home(request):
    data = Tickets.objects.all()
    all_tickets = count_completed_tickets(data)

    x_data = all_tickets.values()
    y_data = all_tickets.keys()
    x_data = list(x_data)
    y_data = list(y_data)

    fig = go.Figure(data=go.Bar(x=x_data, y=y_data, orientation='h'))
    fig.update_layout(title='Completed Tickets by Name')
    fig.to_plotly_json()
    plt_div = plot(fig, output_type='div')

    completed_tickets = get_complete_tickets()
    withdrawn_tickets = get_withdrawn_tickets()
    
    completed_names = list(completed_tickets.keys())
    completed_counts = list(completed_tickets.values())
    withdrawn_names = list(withdrawn_tickets.keys())
    withdrawn_counts = list(withdrawn_tickets.values())

    completed_trace = go.Bar(
    x=completed_counts,  # Reversed order for horizontal bars
    y=completed_names,  # Reversed order for horizontal bars
    orientation='h',  # Set orientation to horizontal
    name='Completed Tickets',
    marker=dict(color='blue')  # Set marker color for completed tickets
    )

    withdrawn_trace = go.Bar(
        x=withdrawn_counts,  # Reversed order for horizontal bars
        y=withdrawn_names,  # Reversed order for horizontal bars
        orientation='h',  # Set orientation to horizontal
        name='Withdrawn Tickets',
        marker=dict(color='red')  # Set marker color for withdrawn tickets
    )

    # Combine traces into a figure
    fig2 = go.Figure(data=[completed_trace, withdrawn_trace])

    # Optional layout customization
    fig2.update_layout(title='Ticket Status Distribution (Completed vs Withdrawn)', barmode='group')  # Stack bars visually
    fig2.to_plotly_json()
    plt2_div = plot(fig2, output_type='div')
    context = {'plot': plt_div, 'plot2': plt2_div}
    return render(request, 'base/home.html', context)