
from data_upload.models import Tickets
import plotly.graph_objects as go

def get_names():
    unique_names = Tickets.objects.values_list('Resolved_By', flat=True).distinct()
    return unique_names

def count_completed_tickets(data):
    names_list = get_names()
        
    name_completed_tickets = {name: 0 for name in names_list}
 
    for item in data:
        if item.Resolved_By in names_list:
            name_completed_tickets[item.Resolved_By] += 1
    
    return name_completed_tickets

def get_complete_tickets():
    names_list = get_names()
    complete_tickets = Tickets.objects.filter(Status='Completed')
    values_dict = {name: 0 for name in names_list}
    for ticket in complete_tickets:
        if ticket.Resolved_By in names_list:
            values_dict[ticket.Resolved_By] += 1
    return values_dict

def get_withdrawn_tickets():
    names_list = get_names()
    withdrawn_tickets = Tickets.objects.filter(Status='Withdrawn')
    values_dict = {name: 0 for name in names_list}
    for ticket in withdrawn_tickets:
        if ticket.Resolved_By in names_list:
            values_dict[ticket.Resolved_By] += 1
    return values_dict