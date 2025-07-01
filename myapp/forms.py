from django import forms
from .models import Tasks

class task_form(forms.ModelForm):
    
    class Meta:
        model = Tasks
        fields = ("title", "complete")
        
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter task title...'
            }),
            'complete': forms.CheckboxInput(attrs={
                'class': 'btn-check',
                'id': 'btn-check-outlined',
                'autocomplete': 'off'
            })
        }
        