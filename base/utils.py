import pandas as pd

def get_names(data):
    names_list = []
    for item in data:
        if item.Resolved_By not in names_list:
            names_list.append(item.Resolved_By)
    return names_list

def count_completed_tickets(data):
    names_list = get_names(data)
        
    name_completed_tickets = {name: 0 for name in names_list}

    for item in data:
        if item.Resolved_By in names_list:
            name_completed_tickets[item.Resolved_By] += 1
    
    return name_completed_tickets