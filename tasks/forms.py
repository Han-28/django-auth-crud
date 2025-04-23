from django.forms import ModelForm 
from django import forms
from .models import Task
class TasksForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description','important']
        widgets ={
            'title':forms.TextInput(attrs={'class': 'form-control','placeholder':'Write a title '}), 
            'description':forms.Textarea(attrs={'class': 'form-control','placeholder':'Write description '}), 
            'important':forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}) 
        }

