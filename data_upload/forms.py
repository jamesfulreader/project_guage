from django import forms
from .models import Tickets

import pandas as pd

def validate_file_extension(value):
    try:
        df = pd.read_csv(value)
        expected_fields = ['Resolved By', 'Status', 'Parent Record Type', 'Resolved DateTime', 'Created Date Time']
        if not all(field in df.columns for field in expected_fields):
            raise forms.ValidationError('CSV header row does not match expected values')
    except Exception as e:
        forms.ValidationError(f'Error processing CSV file: {e}')

class TicketUploadForm(forms.ModelForm):
    csv_file = forms.FileField(required=True, validators=[validate_file_extension])
    class Meta:
        model = Tickets
        fields = ['csv_file']
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def is_valid(self):
        valid = super().is_valid()
        return valid